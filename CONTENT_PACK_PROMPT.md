# Content-pack fill prompt (ChatGPT step)

Use this to turn a scraped client site + real facts into a `content_pack.json` that
`render.py` can build straight away. This is the "ChatGPT" step in the K9PN
scrape -> content-pack -> template -> Vercel pipeline
(`skills/k9pn_ghl_ops/references/trainer-snapshot-spec.md`).

## When to use it

After `scrape_client_site.py <url>` has produced a raw-facts JSON (real business info,
page copy, and a list of real photo URLs) for a new or existing K9PN client, paste the
prompt below into ChatGPT together with that raw-facts JSON. Mike does this today in
`#k9pn-ai-consultations`, same as the existing site_generator cost model — ChatGPT writes,
Viktor/the script only merges data into markup (cheap, deterministic).

## The prompt

```
You are writing the content pack for a dog-training business's new website, to be
rendered by K9PN's `trainer-site-template` generator. Follow these rules exactly:

1. Use ONLY the facts given to you below (scraped from the client's current site, their
   Google Business Profile, or supplied directly). Never invent pricing, review counts,
   certifications, testimonials, staff, or years in business. If a fact is missing, leave
   the field out or write an honest placeholder and flag it in a top-level "_needs_review"
   array — do not guess.
2. Tone: calm, expert, empathetic to an anxious/overwhelmed dog owner. No hype, no fake
   urgency, no guaranteed-result language ("100% off-leash", "guaranteed calm dog").
3. Structure every page around K9PN's standard sections (all required unless the business
   genuinely doesn't offer that program — then omit the section, don't invent content
   for it): hero + Google-review trust strip, Is-This-You friction section, Book -> Train
   -> Thrive process, services/programs, trainer/about story, FAQ (age, breed,
   aggression/reactivity, format, pricing expectations), service-area/contact.
4. Output valid JSON matching this exact schema (copy every key, keep types, fill values):
   <paste the current content_packs/lm-k9.json here as the schema/shape reference —
   business/nav/seo/home/programs/about/contact, same key names and nesting>
5. Image slots: every image_url must be either a real photo URL from the client's own
   site/socials (use exactly the URL provided in the raw facts) or "IMG:<short-key>" if
   Viktor still needs to source/compress it — never a stock photo, never invented.
6. SEO: title <=70 chars, description <=155 chars, one factual H1 per page using real
   search phrasing ("Dog Training in {city}"), not a slogan.
7. Write real alt text for every image (what's actually in the photo).

Raw facts (scraped, verified):
<paste raw-facts JSON here>
```

## After ChatGPT returns JSON

1. Save it as `content_packs/<client-slug>.json`.
2. Build/confirm the matching `content_packs/<client-slug>-images.json` (IMG: key -> local
   `/images/<key>.jpg` path or real hosted URL) — see `scrape_client_site.py` for how to
   pull and compress real photos.
3. `uv run python render.py content_packs/<client-slug>.json content_packs/<client-slug>-images.json <out_dir>`
   — fails closed with a specific error if anything required is missing (see
   `validate_pack` in `render.py`).
4. QA at desktop/tablet/390px (`website-build-standard.md`), then deploy with
   `deploy_vercel.py <out_dir> <client-slug>` (see that script's docstring).
5. Once the client's real HighLevel webhook (or n8n endpoint) is live and tested, set
   `business.lead_webhook_url` in the pack and re-render before using `--publish` /
   deploying with `--prod`.
