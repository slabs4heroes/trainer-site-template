"""
Step 1 of the K9PN scrape -> ChatGPT content-pack -> render -> Vercel pipeline.

Crawls a client's *current* website (every page reachable from its sitemap or nav,
capped) and writes one raw-facts JSON: real body copy per page, contact info, socials,
and a manifest of real photo URLs — everything CONTENT_PACK_PROMPT.md's ChatGPT step
needs, and nothing invented. Also downloads + compresses a capped set of the largest
photos to <out_dir>/images/ so they're ready to drop straight into a content pack's
images.json (see trainer-snapshot-spec.md; real full-resolution photo originals only,
never a Wix/Squarespace URL-transform crop like `/v1/fill/`).

Usage:
    uv run python scrape_client_site.py https://clientsite.com out_dir [--max-pages 8] [--max-images 12]
"""
import argparse
import json
import re
import sys
from io import BytesIO
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PIL import Image

UA = {"User-Agent": "Mozilla/5.0 (compatible; K9PN-site-build/1.0)"}
SKIP_SLUG_HINTS = (
    "store", "shop", "cart", "checkout", "video", "event", "blog", "wp-json",
    "cdn-cgi", "privacy-policy", "terms",
)


def fetch(url, timeout=25):
    try:
        r = requests.get(url, timeout=timeout, headers=UA)
        return r if r.status_code == 200 else None
    except requests.RequestException:
        return None


def discover_pages(base_url, max_pages):
    parsed = urlparse(base_url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    urls = {base_url}
    r = fetch(urljoin(root, "/sitemap.xml"))
    if r is not None:
        for m in re.finditer(r"<loc>([^<]+)</loc>", r.text):
            u = m.group(1)
            if urlparse(u).netloc != parsed.netloc:
                continue
            slug = urlparse(u).path.lower()
            if any(h in slug for h in SKIP_SLUG_HINTS):
                continue
            urls.add(u)
    else:
        home = fetch(base_url)
        if home is not None:
            soup = BeautifulSoup(home.text, "html.parser")
            for a in soup.select("nav a[href], header a[href]"):
                u = urljoin(base_url, a["href"])
                if urlparse(u).netloc == parsed.netloc:
                    urls.add(u.split("#")[0])
    return list(urls)[:max_pages]


def page_facts(url):
    r = fetch(url)
    if r is None:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    headings = [h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2", "h3"]) if h.get_text(strip=True)]
    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True)) > 25]
    tels = sorted({a["href"].replace("tel:", "") for a in soup.select('a[href^="tel:"]')})
    emails = sorted({a["href"].replace("mailto:", "") for a in soup.select('a[href^="mailto:"]')})
    socials = sorted({
        a["href"] for a in soup.select("a[href]")
        if any(s in a["href"] for s in ("instagram.com", "facebook.com", "tiktok.com", "youtube.com"))
    })
    img_tags = soup.find_all("img")
    images = []
    for img in img_tags:
        src = img.get("src") or img.get("data-src") or ""
        if not src or src.startswith("data:"):
            continue
        images.append({"url": urljoin(url, src), "alt": img.get("alt", "")})
    return {
        "url": url, "title": title, "headings": headings[:20],
        "paragraphs": paragraphs[:15], "tel_links": tels, "mailto_links": emails,
        "social_links": socials, "images": images,
    }


def download_and_compress(images, out_dir: Path, max_images):
    out_dir.mkdir(parents=True, exist_ok=True)
    seen = set()
    saved = []
    for i, img in enumerate(images):
        if len(saved) >= max_images:
            break
        url = img["url"].split("?")[0]
        if url in seen:
            continue
        seen.add(url)
        r = fetch(url)
        if r is None:
            continue
        try:
            im = Image.open(BytesIO(r.content))
            im = im.convert("RGB") if im.mode not in ("RGB", "RGBA") else im
        except Exception:
            continue
        w, h = im.size
        if w < 400 and h < 400:
            continue  # skip icons/logos-as-decoration; logo should be picked manually
        if w > 1800:
            im = im.resize((1800, int(h * 1800 / w)), Image.LANCZOS)
        key = f"img{i:02d}"
        path = out_dir / f"{key}.jpg"
        im.save(path, "JPEG", quality=82, optimize=True)
        saved.append({"key": key, "source_url": img["url"], "alt": img.get("alt", ""), "local_path": str(path)})
    return saved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start_url")
    ap.add_argument("out_dir")
    ap.add_argument("--max-pages", type=int, default=8)
    ap.add_argument("--max-images", type=int, default=14)
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pages_to_crawl = discover_pages(args.start_url, args.max_pages)
    print(f"crawling {len(pages_to_crawl)} pages")
    pages = []
    all_images = []
    for u in pages_to_crawl:
        facts = page_facts(u)
        if facts:
            pages.append(facts)
            all_images.extend(facts["images"])
        print(f"  {'ok' if facts else 'FAILED'}: {u}")

    all_images.sort(key=lambda x: 0)  # keep discovery order; dedup happens in download step
    saved_images = download_and_compress(all_images, out_dir / "images", args.max_images)

    raw = {
        "source_url": args.start_url,
        "pages": pages,
        "downloaded_images": saved_images,
    }
    (out_dir / "raw_facts.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False))
    print(f"wrote {out_dir / 'raw_facts.json'} — {len(pages)} pages, {len(saved_images)} images")
    print("Next: paste raw_facts.json into the CONTENT_PACK_PROMPT.md prompt with ChatGPT to get a content_pack.json.")


if __name__ == "__main__":
    main()
