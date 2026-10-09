# K9PN Trainer Site Template

Reusable site-generation pipeline for K9PN client websites (dog trainers, etc).
Each client gets a Jinja2-rendered static site (6 pages: home, programs, about,
contact, privacy, terms) built from one JSON "content pack" plus an images
manifest, deployed to its own Vercel project.

## Standard (as of 2026-09-27)
- Real, verified facts only — no invented reviews/awards/pricing/certifications.
- No image cropping, ever — every photo uses `object-fit: contain` inside a frame
  matching its own native aspect ratio. Download and host real client photos
  locally (`images/` folder) instead of hotlinking a CDN.
- Preserve the client's real brand colors/logo — sample from their live site/logo
  and set as a `theme` override in the content pack (see `content_packs/lm-k9.json`
  for the pattern), never invent a palette.
- Full "K9PN standard motion pack" is applied automatically via the shared base
  template (`templates/base.html.j2` + `templates/design_system.css`): scroll-reveal,
  Ken Burns hero zoom, sticky header shrink, card hover-lift, animated stat counter
  (on-load timer, not scroll-gated), mobile sticky Call/Book bar. No per-client work
  needed — it's on every page by default.
- Uniform fixed-height card/gallery grids (not mixed-size blocks) — works cleanly
  with real client photo sets that are mostly portrait-orientation.

## Structure
- `templates/` — shared Jinja2 templates + `design_system.css` (edit here to change
  every client site at once).
- `content_packs/*.json` — one JSON file per client with all copy/facts/theme.
- `content_packs/*-images-local.json` — maps `IMG:<key>` placeholders to local
  `/images/<key>.<ext>` paths.
- `render.py content_packs/<client>.json content_packs/<client>-images-local.json <out_dir>` —
  renders the 6 HTML pages + copies images into `<out_dir>`.
- `deploy_vercel.py` — deploys a rendered `<out_dir>` to a Vercel project (inline,
  no git push required).
- `scrape_client_site.py` — crawls a client's existing site to pull real copy/photos
  before rebuilding.

## Service-area pages (built 2026-10-09)
Add a `service_areas` list to the content pack (one entry per town: `slug`, `town`, `content` —
see `content_packs/k9su.json` for a worked example with 6 Knoxville-metro towns) plus a matching
`seo.<slug>` entry each. `render.py` loops over it automatically and renders each with
`templates/service_area.html.j2`; `deploy_vercel.py` auto-adds a pretty route for every
`dog-training-*.html` file in the output dir. Every page also gets a shared "Service areas" footer
column and the homepage's `home.service_area.area_links` cross-links to all of them. `render.py` also
now writes `sitemap.xml` + `robots.txt`. Don't invent per-town facts the client/market-intel data
doesn't have — differentiate each town's page by assigning a different one of the client's real
programs + real metro-level demand data instead of swapping the city name over identical copy.

## Known gaps / open items
- GitHub repo was previously blocked from auto-creation by the connected GitHub App's
  permissions (`Resource not accessible by integration`) — this repo was created
  manually by Mike; code push works fine once the repo exists.
- Vercel deploys are currently inline/API-based (`deploy_vercel.py`), not linked to
  this GitHub repo for auto-deploy-on-push — pushing here is for version control/backup,
  not yet the deploy trigger.
