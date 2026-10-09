"""
Deploy a rendered static site (output of render.py) directly to Vercel via the
REST Deployments API — no GitHub repo needed (our GitHub App connection can't
create new repos: 403 "Resource not accessible by integration", confirmed
2026-09-27). Vercel auto-creates the project from `name` on first deploy.

Usage:
    uv run python deploy_vercel.py <site_dir> <project_name> [--prod]

site_dir must contain the rendered *.html files (from render.py) plus any
images/ subfolder referenced by them. This uploads everything under site_dir.

Files are uploaded individually to Vercel's content-addressed file store
(POST /v2/files, one call per file — the deployment-create call itself must
stay under the tool gateway's 1MB *inline* payload limit, so we reference
each file by its sha1 digest instead of inlining base64 data for all of them
in one request).
"""
import asyncio
import base64
import hashlib
import json
import sys
from pathlib import Path

from sdk.tools.pd_vercel_token_auth import pd_vercel_token_auth_proxy_post

TEAM = "team_KmLKiQHSqlwQjmpKtAyrI74v"  # K9PN (poke-grade)


async def upload_file(path: Path) -> dict:
    data = path.read_bytes()
    digest = hashlib.sha1(data).hexdigest()
    resp = await pd_vercel_token_auth_proxy_post(
        url="https://api.vercel.com/v2/files",
        query_params={"teamId": TEAM},
        headers={"Content-Type": "application/octet-stream", "x-vercel-digest": digest},
        body_base64=base64.b64encode(data).decode("ascii"),
        timeout_ms=60000,
    )
    return {"file": None, "sha": digest, "size": len(data)}, resp


async def deploy(site_dir: str, project_name: str, prod: bool = False, inline: bool = False):
    site_path = Path(site_dir)
    files = []
    if inline:
        # Small sites (hosted image URLs, no local /images) fit under the tool gateway's
        # 1MB inline-argument limit in one shot — skip the per-file /v2/files upload dance.
        for p in sorted(site_path.rglob("*")):
            if not p.is_file():
                continue
            rel = str(p.relative_to(site_path))
            if p.suffix.lower() in {".html", ".json", ".txt", ".xml", ".css", ".js", ".svg"}:
                files.append({"file": rel, "data": p.read_text(encoding="utf-8")})
            else:
                files.append({"file": rel, "data": base64.b64encode(p.read_bytes()).decode("ascii"), "encoding": "base64"})
    else:
        for p in sorted(site_path.rglob("*")):
            if not p.is_file():
                continue
            rel = str(p.relative_to(site_path))
            meta, resp = await upload_file(p)
            if resp.get("error"):
                print(f"upload FAILED for {rel}: {resp}")
                raise SystemExit(1)
            meta["file"] = rel
            files.append(meta)
            print(f"uploaded {rel} ({meta['size']} bytes, sha {meta['sha'][:10]}…)")

    routes = [
        {"handle": "filesystem"},
        {"src": "/", "dest": "/home.html"},
        {"src": "/privacy", "dest": "/privacy.html"},
        {"src": "/terms", "dest": "/terms.html"},
        {"src": "/programs", "dest": "/programs.html"},
        {"src": "/about", "dest": "/about.html"},
        {"src": "/contact", "dest": "/contact.html"},
    ]
    # Service-area pages (one per town) — any file named "dog-training-*.html" in
    # site_dir gets its own pretty route automatically, so new towns need no edit here.
    for p in sorted(site_path.glob("dog-training-*.html")):
        slug = p.stem
        routes.append({"src": f"/{slug}", "dest": f"/{slug}.html"})
    body = {
        "name": project_name,
        "target": "production" if prod else "staging",
        "files": files,
        "projectSettings": {"framework": None},
        "routes": routes,
    }
    resp = await pd_vercel_token_auth_proxy_post(
        url="https://api.vercel.com/v13/deployments",
        query_params={"teamId": TEAM},
        headers={"Content-Type": "application/json"},
        json_body=body,
        timeout_ms=120000,
    )
    return resp


def main():
    args = sys.argv[1:]
    prod = "--prod" in args
    inline = "--inline" in args
    args = [a for a in args if a not in ("--prod", "--inline")]
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    site_dir, project_name = args
    resp = asyncio.run(deploy(site_dir, project_name, prod, inline))
    print(json.dumps(resp, indent=2)[:4000])


if __name__ == "__main__":
    main()
