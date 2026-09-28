"""
K9PN multipage site generator (Path A prototype).

Takes a "content pack" JSON (business facts + per-page copy/photo slots,
supplied by Mike or drafted by ChatGPT from a lead's real audit/scrape data)
and mechanically renders it against the approved Book->Train->Thrive design
system (extracted from the hand-built gatoralleyk9.com pages) into full,
SEO-tagged multi-page HTML. No creative writing happens in this script --
it only merges data into markup, which is what keeps this step cheap.

Usage:
    uv run python render.py <content_pack.json> <images.json> <out_dir>

images.json maps "IMG:<key>" placeholders used in the content pack to real
image sources (data URIs today; swap for hosted https:// URLs once photos
are stored centrally e.g. in Supabase storage).
"""
import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

HERE = Path(__file__).parent


def resolve_images(node, images):
    """Recursively replace 'IMG:<key>' strings with real image sources."""
    if isinstance(node, dict):
        return {k: resolve_images(v, images) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve_images(v, images) for v in node]
    if isinstance(node, str) and node.startswith("IMG:"):
        key = node[4:]
        if key not in images:
            raise KeyError(f"content pack references unknown image key: {key!r}")
        return images[key]
    return node


def build_schema(pack, page_key):
    biz = pack["business"]
    seo = pack["seo"][page_key]
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": seo["title"],
        "description": seo["description"],
        "url": seo["canonical_url"],
        "about": {
            "@type": "LocalBusiness",
            "name": biz["name"],
            "telephone": biz["phone_e164"],
            "address": {
                "@type": "PostalAddress",
                "streetAddress": biz["street_address"],
                "addressLocality": biz["city"],
                "addressRegion": biz["state"],
                "postalCode": biz["postal_code"],
                "addressCountry": "US",
            },
            "areaServed": biz["area_served"],
        },
    }


PAGES = {
    "home": "home.html.j2",
    "programs": "programs.html.j2",
    "about": "about.html.j2",
    "contact": "contact.html.j2",
}

# Fixed legal pages: same boilerplate (A2P/SMS consent language) every client needs,
# filled only from business.* fields — never authored per-client, never in content_pack
# validation below (see trainer-snapshot-spec.md section 1).
STATIC_PAGES = {
    "privacy": "privacy.html.j2",
    "terms": "terms.html.j2",
}

def validate_pack(pack, images, publish=False):
    """Reject incomplete or inconsistent packs before any HTML is written."""
    errors = []
    if not isinstance(pack, dict):
        return ["content pack must be an object"]
    biz = pack.get("business") or {}
    seo = pack.get("seo") or {}
    nav = pack.get("nav") or {}
    for key in ("name", "phone_e164", "email", "city", "state"):
        if not isinstance(biz.get(key), str) or not biz[key].strip():
            errors.append(f"business.{key} is required")
    if not isinstance(biz.get("area_served"), list) or not biz["area_served"]:
        errors.append("business.area_served must contain at least one verified area")
    links = nav.get("links") or []
    for page in PAGES:
        value = seo.get(page) or {}
        if not value.get("title") or len(value["title"]) > 70:
            errors.append(f"seo.{page}.title must be 1–70 characters")
        if not value.get("description") or len(value["description"]) > 155:
            errors.append(f"seo.{page}.description must be 1–155 characters")
        if not str(value.get("canonical_url", "")).startswith("https://"):
            errors.append(f"seo.{page}.canonical_url must be HTTPS")
        if not pack.get(page) or not (pack[page].get("hero") or {}).get("headline"):
            errors.append(f"{page}.hero.headline is required")
    if len(links) != len(PAGES) or len({x.get("url") for x in links if isinstance(x, dict)}) != len(PAGES):
        errors.append("nav.links must contain four distinct page URLs")

    def walk(node, label="pack"):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{label}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{label}[{i}]")
        elif isinstance(node, str):
            if node.startswith("IMG:") and node[4:] not in images:
                errors.append(f"{label}: image key not in asset manifest")
            if "image_alt" in label and not node.strip():
                errors.append(f"{label}: missing alt text")
            if publish and ("gen-test" in node or "viktor.page" in node or "Private preview" in node):
                errors.append(f"{label}: preview-only content cannot publish")
    walk(pack)
    if publish:
        # Real forms exist since 2026-09-27 (base.html.j2's k9pn-lead-form handler), but they only
        # go live once business.lead_webhook_url is a real, tested CRM endpoint — not blank/placeholder.
        webhook = biz.get("lead_webhook_url")
        if not webhook or not str(webhook).startswith("https://"):
            errors.append("business.lead_webhook_url must be a tested live webhook URL before --publish (see trainer-snapshot-spec.md 'Lead contract')")
    return errors


def main():
    publish = "--publish" in sys.argv
    args = [arg for arg in sys.argv[1:] if arg != "--publish"]
    if len(args) != 3:
        print(__doc__)
        sys.exit(1)
    pack_path, images_path, out_dir = args[0], args[1], Path(args[2])

    pack = json.loads(Path(pack_path).read_text())
    images = json.loads(Path(images_path).read_text())
    errors = validate_pack(pack, images, publish)
    if errors:
        raise ValueError("Invalid content pack:\n- " + "\n- ".join(errors))
    pack = resolve_images(pack, images)
    out_dir.mkdir(parents=True, exist_ok=True)

    design_css = (HERE / "templates" / "design_system.css").read_text()
    # Optional per-client theme override — CSS custom-property overrides so a client's real
    # brand colors/fonts win without forking design_system.css. See trainer-snapshot-spec.md.
    theme = pack.get("theme") or {}
    theme_css = " ".join(f"--{k.replace('_', '-')}:{v};" for k, v in theme.items())

    env = Environment(loader=FileSystemLoader(str(HERE / "templates")), autoescape=False, undefined=StrictUndefined)

    sms_consent_text = (
        f"By checking this box, I agree to receive text messages from {pack['business']['name']} "
        "about my inquiry and appointments. Message frequency varies. Msg and data rates may apply. "
        "Reply STOP to opt out, HELP for help. Consent is not a condition of purchase."
    )

    for page_key, template_name in PAGES.items():
        tpl = env.get_template(template_name)
        ctx = dict(pack)
        ctx["design_css"] = design_css
        ctx["theme_css"] = theme_css
        ctx["sms_consent_text"] = sms_consent_text
        ctx["seo"] = pack["seo"][page_key]
        ctx["local_business_schema"] = build_schema(pack, page_key)
        # mark the current-page nav link so the header highlights it correctly per page
        nav = dict(pack["nav"])
        nav["links"] = [
            {**link, "current": link["url"].rstrip("/").endswith(page_key) if page_key != "home" else link["url"] == pack["nav"]["home_url"]}
            for link in pack["nav"]["links"]
        ]
        ctx["nav"] = nav
        html = tpl.render(**ctx)
        out_path = out_dir / f"{page_key}.html"
        out_path.write_text(html)
        print(f"wrote {out_path} ({len(html)} bytes)")

    # Fixed legal pages — same context shape, no page-specific content-pack section required.
    from datetime import date
    legal_updated = date.today().strftime("%B %-d, %Y")
    for page_key, template_name in STATIC_PAGES.items():
        tpl = env.get_template(template_name)
        ctx = dict(pack)
        ctx["design_css"] = design_css
        ctx["theme_css"] = theme_css
        ctx["sms_consent_text"] = sms_consent_text
        ctx["legal_updated"] = legal_updated
        legal_seo = {
            "title": f"{page_key.capitalize()} | {pack['business']['name']}",
            "description": f"{pack['business']['name']} {page_key} page.",
            "canonical_url": pack["seo"]["home"]["canonical_url"].rsplit("/", 1)[0] + f"/{page_key}",
            "robots": "noindex,follow",
        }
        ctx["seo"] = legal_seo
        ctx["local_business_schema"] = build_schema({**pack, "seo": {**pack["seo"], page_key: legal_seo}}, page_key)
        nav = dict(pack["nav"])
        nav["links"] = [{**link, "current": False} for link in pack["nav"]["links"]]
        ctx["nav"] = nav
        html = tpl.render(**ctx)
        out_path = out_dir / f"{page_key}.html"
        out_path.write_text(html)
        print(f"wrote {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
