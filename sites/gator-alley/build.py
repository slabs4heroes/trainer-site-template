#!/usr/bin/env python3
"""Gator Alley Dog Training — static site generator. Output: ./site"""
import os, html, json
from PIL import Image

OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://gatoralleyk9.com"
PHONE = "(941) 842-0849"
TEL = "+19418420849"
EMAIL_FORM = "gatoralleyk9@gmail.com"
IG = "https://www.instagram.com/gatoralleyk9"
FB = "https://www.facebook.com/share/1HG7KeMFk3/?mibextid=wwXIfr"
ADDR = "10328 Charlotte Dr, Parrish, FL 34219"


def img(name, alt, cls="", lazy=True, eager=False):
    w, h = Image.open(f"{OUT}/assets/{name}").size
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="/assets/{name}" alt="{html.escape(alt)}" width="{w}" height="{h}" {load} class="{cls}">'


def frame(name, alt, cap="", cls=""):
    w, h = Image.open(f"{OUT}/assets/{name}").size
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return (f'<figure class="frame reveal {cls}" style="--ar:{w}/{h}">{img(name, alt)}{c}</figure>')


PROGRAMS = [
    dict(slug="puppy-head-start-parrish-fl", track="01", tag="2 WEEKS", name="Puppy Head Start",
         it="Program", blurb="A focused 2-week program for puppies covering basic obedience, potty training and exposure training — the best possible start before habits set in.",
         img="img13.jpg", alt="Young puppy practicing leash skills in Parrish, Florida",
         h1="Puppy Head Start in Parrish, FL", lead="Two weeks of focused work on the three things that shape a young dog fastest: basic obedience, potty training and real-world exposure.",
         who=["New puppy owners who want clear foundations before habits set in", "Households that need a reliable potty routine and calmer manners", "Families who want a personal handover so everyone can carry the work forward"]),
    dict(slug="basic-obedience-parrish-fl", track="02", tag="BOARD & TRAIN", name="Basic Obedience",
         it="Program", blurb="A focused program for clearer communication, better manners, reliable routines and practical obedience matched to your household.",
         img="img10.jpg", alt="Dogs practicing loose-leash walking during basic obedience training in Parrish, Florida",
         h1="Basic Obedience Board & Train in Parrish, FL", lead="Clearer communication, better manners and routines that hold up at home — built around your dog and your household, not a script.",
         who=["Dogs who pull, jump, bark or struggle to settle", "Owners who want practical obedience that works in everyday life", "Anyone who wants direct, personal guidance from the trainer doing the work"]),
    dict(slug="advanced-obedience-behavior-parrish-fl", track="03", tag="ADVANCED", name="Advanced Obedience, Off-Leash & Behavior Modification",
         it="", blurb="For owners navigating reactivity, anxiety, difficult behavior, or a higher standard of advanced obedience, calmness, communication and off-leash reliability.",
         img="img09.jpg", alt="Dogs practicing calm impulse control during behavior training in Parrish, Florida",
         h1="Advanced Obedience & Behavior Modification in Parrish, FL", lead="For the harder cases and the higher standard: reactivity, anxiety, difficult behavior, calm communication and off-leash reliability.",
         who=["Dogs with reactivity, fear, anxiety or a behavior history", "Owners who want advanced obedience and off-leash reliability", "Households ready to be candid about what has happened so the plan can be responsible"]),
    dict(slug="puppy-raise-and-train-parrish-fl", track="04", tag="12 WEEKS", name="Puppy Raise & Train",
         it="", blurb="A longer foundation-focused program personally led by Jacob during the key early stages of development, with structured routines, socialization, real-world exposure and advanced foundations.",
         img="img11.jpg", alt="Dogs holding a down-stay during puppy foundations training in Parrish, Florida",
         h1="Puppy Raise & Train in Parrish, FL", lead="Twelve weeks of structured routines, socialization and real-world exposure during the stages of development that matter most.",
         who=["Puppy owners who want a deeper foundation than a short program", "Families who want Jacob personally leading the key early stages", "Owners planning for advanced foundations from the start"]),
]
VIRTUAL = dict(slug="virtual-dog-training-coaching", track="+", tag="ZOOM", name="Virtual Coaching Sessions",
               blurb="Live one-on-one coaching with Jacob over Zoom — leash manners, puppy foundations, or behavior and consistency. Every session is recorded for you to keep.",
               img="img12.jpg", alt="Jacob Soos holding a dog during virtual coaching preparation",
               h1="Virtual Dog Training Coaching with Jacob Soos", lead="Can't make it to Parrish? Train one-on-one with Jacob over Zoom on the topic you need most — and keep the recording.",
               who=["Owners outside the Parrish area", "Dog owners who want help with one specific topic", "Anyone who wants a recording to practice from between sessions"])

FAQ = [
    ("Where does training happen?", "Dogs live and learn in Jacob’s real home environment in Parrish rather than a kennel facility, with exposure to household routines and real-world distractions."),
    ("Who trains my dog?", "Jacob personally trains and cares for every dog throughout the program."),
    ("What happens when my dog comes home?", "The program includes a detailed handover and ongoing support so you can continue the training consistently at home."),
    ("What ages and breeds are a fit?", "Every dog is different. Share your dog’s age, breed, history and goals so Jacob can discuss the appropriate next step."),
    ("Can puppy owners start the conversation?", "Yes, puppy owners can include their socialization, household-manners and foundation goals in the consultation request. Jacob can then discuss whether the current programs are appropriate."),
    ("Can you help with reactivity or aggression?", "Behavior history matters. Be candid about fear, aggression, reactivity or bite history during the consultation so the situation can be discussed responsibly."),
    ("What does training cost?", "Program fit and scope are discussed during the consultation. Contact Jacob for current availability and program details rather than relying on an assumed price."),
]

AREAS = ["Parrish", "Palmetto", "Ellenton", "Bradenton", "Lakewood Ranch", "Sarasota"]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">')

ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW = '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg>'
PHONE_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/></svg>'
IG_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 3v6c0 5-3.4 9.3-8 11-4.6-1.7-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>'
HOME_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.7 7-6.3-3.8-6.3 3.8 1.7-7L2 9.2l7.1-.6z"/></svg>'


def ar(name):
    w, h = Image.open(f"{OUT}/assets/{name}").size
    return w, h


def btn(href, label, cls=""):
    return f'<a class="btn {cls}" href="{href}">{label}{ARROW}</a>'


def head(title, desc, path, extra=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{DOMAIN}{path}"><meta name="theme-color" content="#f6f1ea">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:image" content="{DOMAIN}/assets/img05.jpg">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>document.documentElement.classList.add('js')</script>
{FONTS}<link rel="stylesheet" href="/styles.css">{extra}</head><body>'''


def header(cur=""):
    def a(h, t, k=None):
        return f'<a href="{h}"{" aria-current=page" if k == cur else ""}>{t}</a>'
    links = a("/#programs", "Programs") + a("/about-jacob-soos", "About Jacob", "about") + a("/#faq", "FAQ") + a("/#consult", "Contact")
    drawer = "".join(f'<a href="{h}">{t}</a>' for h, t in [("/#programs", "Programs"), ("/virtual-dog-training-coaching", "Virtual coaching"), ("/about-jacob-soos", "About Jacob"), ("/#faq", "FAQ"), ("/#consult", "Contact")])
    return f'''<a class="skip" href="#main">Skip to content</a><div class="progress" aria-hidden="true"><i></i></div>
<header class="header" id="top"><div class="pill"><a href="/" class="brand" aria-label="Gator Alley Dog Training home"><img src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356"></a>
<nav class="nav" aria-label="Main">{links}</nav>{btn("/#consult", "Free consultation", "sm")}
<button class="menu-btn" aria-label="Menu" aria-expanded="false"><i></i></button></div></header>
<div class="drawer">{drawer}{btn("/#consult", "Free consultation")}</div>'''


def footer():
    ar_ = "".join(f"<li>{a}</li>" for a in AREAS)
    plinks = "".join(f'<li><a href="/{p["slug"]}">{"Advanced Obedience &amp; Behavior" if "Advanced" in p["name"] else p["name"]}</a></li>' for p in PROGRAMS) + f'<li><a href="/{VIRTUAL["slug"]}">Virtual Coaching</a></li>'
    return f'''<footer class="foot"><div class="wrap"><div class="foot-grid">
<div><img src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356" loading="lazy"><p>Dog training in Parrish, Florida. Serving board-and-train clients nationwide.</p><p style="margin-top:12px">Gator Alley Dog Training Academy, LLC<br>{ADDR}</p></div>
<div><h4>Explore</h4><ul><li><a href="/">Home</a></li>{plinks}<li><a href="/about-jacob-soos">About Jacob</a></li></ul></div>
<div><h4>Serving</h4><ul>{ar_}</ul></div>
<div><h4>Get in touch</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li>Wed–Sun, 9 AM–8 PM</li><li><a href="{IG}" rel="noopener">Instagram</a></li><li><a href="{FB}" rel="noopener">Facebook</a></li><li><a href="/#consult">Request a consultation</a></li></ul></div>
</div><div class="legal"><span>© Gator Alley Dog Training Academy, LLC</span><a href="#top">Back to top</a></div></div></footer>
<div class="mbar"><a href="tel:{TEL}">Call</a><a href="/#consult" class="go">Book consultation</a></div>
<div class="peek" aria-hidden="true"><img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></div>
<script src="/script.js" defer></script></body></html>'''


def form_compact():
    return f'''<form class="form compact" data-form action="https://formsubmit.co/ajax/{EMAIL_FORM}" method="post">
<input type="hidden" name="_subject" value="New consultation request — Gator Alley website"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
<label>First name<input name="name" required autocomplete="given-name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label class="wide">Email<input name="email" type="email" required autocomplete="email"></label>
<button class="btn" type="submit">Book phone consultation{ARROW}</button><p class="form-msg" role="status" aria-live="polite"></p></form>'''


def form():
    opts = "".join(f"<option>{o}</option>" for o in ["Puppy Head Start (2 weeks)", "Basic Obedience", "Advanced Obedience, Off-Leash & Behavior", "Puppy Raise & Train (12 weeks)", "Virtual Coaching (Zoom)", "Not sure yet — help me choose"])
    return f'''<form class="form" data-form action="https://formsubmit.co/ajax/{EMAIL_FORM}" method="post">
<input type="hidden" name="_subject" value="New consultation request — Gator Alley website"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
<label>Your name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label class="wide">Email<input name="email" type="email" required autocomplete="email"></label>
<label class="wide">Interested in<select name="program">{opts}</select></label>
<label class="wide">Tell Jacob about your dog (age, breed, what’s going on)<textarea name="message" rows="4"></textarea></label>
<button class="btn" type="submit">Request my consultation{ARROW}</button><p class="form-msg" role="status" aria-live="polite"></p>
<small>Jacob will follow up personally. Available Wednesday–Sunday, 9 AM–7 PM Eastern.</small></form>'''


def contact(extra=""):
    return f'''<section class="section contact" id="consult"><div class="wrap contact-grid"><div class="rv"><h2>Book your free consultation</h2><p class="lede">Tell Jacob about you and your dog. He follows up personally, Wednesday through Sunday. {extra}</p>
<div class="ways"><a href="tel:{TEL}">{PHONE_IC}{PHONE}</a><a href="{IG}" rel="noopener">{IG_IC}@gatoralleyk9</a><span style="display:inline-flex;gap:12px;align-items:center">{PIN}{ADDR}</span></div></div><div class="rv" data-d="120">{form()}</div></div></section>'''


def schema(extra=""):
    return f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","@id":"{DOMAIN}/#business","name":"Gator Alley Dog Training","legalName":"Gator Alley Dog Training Academy, LLC","url":"{DOMAIN}/","telephone":"{TEL}","image":"{DOMAIN}/assets/img05.jpg","address":{{"@type":"PostalAddress","streetAddress":"10328 Charlotte Dr","addressLocality":"Parrish","addressRegion":"FL","postalCode":"34219","addressCountry":"US"}},"areaServed":{json.dumps(AREAS)},"sameAs":["{IG}","{FB}"],"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"16"}}}}</script>{extra}'''


def proof_strip():
    items = ["Puppy Head Start", "Basic Obedience", "Advanced &amp; Off-Leash", "Behavior Modification", "Puppy Raise &amp; Train", "Virtual Coaching", "Real home, not a kennel", "Personally led by Jacob"]
    r = "".join(f"<span>{i}</span>" for i in items)
    return f'<div class="proof" aria-hidden="true"><div class="row">{r}{r}</div></div>'


def display_name(n):
    return "Advanced Obedience, Off-Leash &amp; Behavior" if "Advanced" in n else n.replace("&", "&amp;")


def home():
    cards = ""
    for p in PROGRAMS:
        w, h = ar(p["img"])
        cards += f'''<a class="pcard rv" href="/{p["slug"]}"><div class="pph"><img src="/assets/{p["img"]}" alt="{html.escape(p["alt"])}" width="{w}" height="{h}" loading="lazy"></div><div class="pbody"><span class="meta">{p["tag"].title()}</span><h3>{display_name(p["name"])}</h3><p>{p["blurb"]}</p><span class="more-l">Explore program {ARROW_SVG}</span></div></a>'''
    faq = "".join(f'<details class="rv"><summary>{q}<span class="pm"></span></summary><div class="ans"><p>{a}</p></div></details>' for q, a in FAQ)
    faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}) + "</script>"
    cap = [("img03.jpg", "Jacob Soos giving a hand-signal cue to a German Shepherd during training", "Hand signals and verbal cues layered together during an obedience session."),
           ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator", "Jacob and Chloe with Gator, the same balanced approach used with client dogs."),
           ("img05.jpg", "German Shepherd walking a path in Parrish, Florida", "Real-world reliability, practiced outside the training space.")]
    media = "".join(f'<figure class="mfig rv" data-d="{i*100}"><div class="photo" style="aspect-ratio:{"/".join(map(str, ar(n)))}">{img(n, a)}</div><figcaption>{c}</figcaption></figure>' for i, (n, a, c) in enumerate(cap))
    w01, h01 = ar("img01.jpg")
    w06, h06 = ar("img06.jpg")
    return head("Dog Trainer in Parrish, FL | Gator Alley Dog Training",
                "Personally led board-and-train dog training in Parrish, FL. Puppy head start, basic and advanced obedience, behavior modification and virtual coaching with Jacob Soos.", "/",
                schema(faq_ld)) + header() + f'''
<main id="main">
<section class="hero hero-photo"><div class="hphoto" style="aspect-ratio:{w01}/{h01}"><img src="/assets/img01.jpg" alt="Jacob Soos and Chloe walking their dogs in Parrish, Florida" width="{w01}" height="{h01}" fetchpriority="high"></div>
<div class="fx" aria-hidden="true"><div class="rays" data-speed=".03"></div><div class="sunglow"></div>
<img class="palm p1" src="/assets/palm.svg" alt="" width="760" height="560" data-speed=".08"><img class="palm p2" src="/assets/palm.svg" alt="" width="760" height="560" data-speed=".14">
<svg class="gull g1" viewBox="0 0 48 20"><path d="M2 14 Q12 0 24 12 Q36 0 46 14" fill="none" stroke="#0b2e3a" stroke-width="2.2" stroke-linecap="round"/></svg><svg class="gull g2" viewBox="0 0 48 20"><path d="M2 14 Q12 0 24 12 Q36 0 46 14" fill="none" stroke="#0b2e3a" stroke-width="2.2" stroke-linecap="round"/></svg><svg class="gull g3" viewBox="0 0 48 20"><path d="M2 14 Q12 0 24 12 Q36 0 46 14" fill="none" stroke="#0b2e3a" stroke-width="2.2" stroke-linecap="round"/></svg>
<div class="waves"><i class="wa"></i><i class="wb"></i><i class="wc"></i></div></div>
<div class="sticker" data-speed="-.04"><svg viewBox="0 0 200 200"><defs><path id="circ" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs><text><textPath href="#circ">PERSONALLY LED • BOARD &amp; TRAIN • PARRISH, FL • </textPath></text></svg><b>5.0<small>★★★★★</small></b></div>
<div class="wrap hero-copy"><div class="status fade"><i></i>Dog training in Parrish, Florida</div>
<h1><span class="ln"><span>Reliable obedience</span></span><span class="ln"><span>built for <span class="swash">real life<svg viewBox="0 0 300 6" preserveAspectRatio="none" aria-hidden="true"><path d="M0 3 H300"/></svg></span>.</span></span></h1>
<p class="lede fade">Gator Alley Dog Training offers personally led board-and-train programs for owners who want calm, trustworthy and obedient dogs.</p>
<div class="rating fade"><span class="g">G</span><div><b>5.0</b> <span class="stars">★★★★★</span><br><small>Google reviews · 16 reviews</small></div></div>
<div class="hero-card fade"><h2>Free consultation</h2><p>Tell us about you and your dog. We’ll follow up shortly.</p>{form_compact()}</div></div></section>
{proof_strip()}
<section class="section" id="programs"><div class="wrap"><div class="sec-head"><h2 class="rv">Gator Alley board &amp; train</h2><p class="rv" data-d="100">Every program is built around your dog’s history, home life and training goals. Jacob leads the work in a real home environment, with practical routines and a clear owner handoff so progress carries into everyday life.</p></div>
<div class="pgrid">{cards}</div>
<a class="virtual rv" href="/{VIRTUAL["slug"]}"><div><h3>New: train with Jacob over Zoom</h3><p>Live one-on-one virtual coaching for leash manners, puppy foundations, or behavior and consistency. Every session is recorded for you to keep.</p></div><span class="btn">See virtual coaching{ARROW}</span></a></div></section>
<section class="section local"><div class="wrap"><div class="sec-head"><h2 class="rv">What Parrish dog owners come to us for</h2><p class="rv" data-d="100">These are topics we discuss during a consultation, not guaranteed fixes. Every dog and household is different.</p></div>
<div class="worries local3"><blockquote class="rv"><q>Puppy foundations</q><span>Basic obedience, potty training and real-world exposure while habits are still forming.</span></blockquote>
<blockquote class="rv" data-d="100"><q>Everyday obedience challenges</q><span>Pulling, jumping, barking or trouble settling, and routines that hold up at home.</span></blockquote>
<blockquote class="rv" data-d="200"><q>Behavior history</q><span>Reactivity, fear or anxiety, discussed candidly so the plan can be responsible.</span></blockquote></div></div></section>
<section class="section statement"><div class="wrap"><p class="big rv">Is this you? When everyday dog life feels harder than it should, you want <em>a clear plan and support that fits your household</em>.</p>
<div class="worries"><blockquote class="rv"><q>I love my dog, but I feel overwhelmed.</q><span>Training should make daily life more manageable, not leave you guessing what to do next.</span></blockquote>
<blockquote class="rv" data-d="100"><q>The behavior changes depending on the situation.</q><span>Real-world routines and distractions matter. The goal is usable communication beyond a quiet training space.</span></blockquote>
<blockquote class="rv" data-d="200"><q>I want my family to feel confident.</q><span>Clear handover guidance helps owners continue the work consistently once their dog returns home.</span></blockquote></div></div></section>
<section class="section method"><div class="wrap method-grid"><div class="sticky"><h2 class="rv">A simple path forward: Book. Train. Thrive.</h2><p class="rv" data-d="100">Every conversation begins with your dog’s needs, your goals and the right fit, never a one-size-fits-all promise.</p></div>
<div class="steps"><div class="step"><span class="n">1</span><h3>Book</h3><p>Share what is happening at home and speak directly with Jacob about your goals.</p></div>
<div class="step"><span class="n">2</span><h3>Train</h3><p>Your dog receives personally led work, structure and real-world exposure in the appropriate program.</p></div>
<div class="step"><span class="n">3</span><h3>Thrive</h3><p>Use the handover and ongoing support to carry clearer communication into everyday life.</p></div></div></div></section>
<section class="section"><div class="wrap"><h2 class="rv" style="margin-bottom:40px">More from the program</h2><div class="media3">{media}</div></div></section>
<section class="section difference"><div class="wrap jacob-grid"><div class="photo rv" style="aspect-ratio:{w06}/{h06};max-width:560px">{img("img06.jpg", "Jacob Soos working obedience with his German Shepherd")}</div>
<div class="rv" data-d="100"><h2>The Gator Alley difference</h2>
<p>Dogs live and learn in a real home environment, not a facility. Jacob personally trains and cares for every dog, working through the routines, people and distractions that make reliable behavior matter.</p>
<p>Born and raised in Palmetto, Florida, Jacob spent five years in the U.S. Coast Guard before bringing that same structure, calm and follow-through to dog training, with his wife Chloe, their German Shepherd Gator, and a couple of cats.</p>
<p style="margin-top:28px">{btn("/about-jacob-soos", "Meet Jacob")}</p></div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="google rv"><div class="score">5.0</div><div><span class="stars">★★★★★</span><h3>Proof from the program</h3><p class="muted">Sixteen Google reviews, every one five stars. See what Parrish dog owners say about training with Jacob.</p></div>{btn("https://www.google.com/search?q=Gator+Alley+Dog+Training+Parrish+FL", "Read the reviews")}</div></div></section>
<section class="section" id="faq" style="padding-top:0"><div class="wrap faq-grid"><div class="rv"><h2>Frequently asked questions</h2></div><div>{faq}</div></div></section>
<section class="section" id="area" style="padding-top:0"><div class="wrap area-grid"><div class="rv"><h2>Serving Parrish &amp; nearby areas</h2><p class="lede" style="margin-top:20px">Gator Alley is based in Parrish and serves owners in {", ".join(AREAS[1:-1])} and {AREAS[-1]}, while also welcoming board-and-train clients from around the country.</p>
<ul class="towns">{"".join(f"<li>{a}</li>" for a in AREAS)}<li>Nationwide board &amp; train</li></ul></div>
<div class="mapcard rv" data-d="100"><iframe title="Map of Parrish, Florida" loading="lazy" referrerpolicy="no-referrer" src="https://www.openstreetmap.org/export/embed.html?bbox=-82.645%2C27.426%2C-82.205%2C27.746&amp;layer=mapnik"></iframe>
<div class="mpin" aria-hidden="true"><i></i><i></i><i></i><b>{PIN}</b><span>Gator Alley<br><small>Parrish, FL</small></span></div>
<a class="mlink" href="https://www.google.com/maps/search/?api=1&amp;query=10328+Charlotte+Dr+Parrish+FL+34219" rel="noopener">Get directions</a></div></div></section>
{contact("Wednesday–Sunday, 9 AM–7 PM Eastern.")}
</main>''' + footer()


def program_page(p, v=False):
    others = [x for x in PROGRAMS if x["slug"] != p["slug"]] + ([VIRTUAL] if not v else [])
    if v: others = list(PROGRAMS)
    who = "".join(f"<li>{CHECK}<span>{w}</span></li>" for w in p["who"])
    oth = "".join(f'<a href="/{o["slug"]}"><small>{o["tag"].title()}</small>{display_name(o["name"])}</a>' for o in others)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Service", "name": p["name"], "provider": {"@id": f"{DOMAIN}/#business"}, "areaServed": AREAS, "description": p["blurb"]}) + "</script>"
    w, h = ar(p["img"])
    h1 = p["h1"]
    step2 = "Live one-on-one Zoom coaching, recorded so you can keep it." if v else "Personally led work, structure and real-world exposure in a real home, not a kennel."
    step3 = "Practice from your recording and carry the work into everyday life." if v else "A detailed handover and ongoing support so progress carries into everyday life."
    return head(f'{h1} | Gator Alley Dog Training', p["lead"], f'/{p["slug"]}', schema(ld)) + header() + f'''
<main id="main"><section class="phero"><div class="wrap hero-grid"><div><div class="status fade"><i></i>{"One-on-one over Zoom" if v else p["tag"].title()}</div>
<h1><span class="ln"><span>{h1}</span></span></h1><p class="lede fade" style="margin:26px 0 32px">{p["lead"]}</p>
<div class="cta-row fade">{btn("#consult", "Free consultation")}<a class="btn ghost" href="tel:{TEL}">{PHONE}</a></div></div>
<div class="arch-solo"><div class="sun"><div class="sun-in"></div></div><div class="topo" data-speed=".05"></div><div class="arch" style="aspect-ratio:{w}/{h}">{img(p["img"], p["alt"], eager=True).replace('loading="lazy" decoding="async"', '')}</div></div></div></section>
{proof_strip()}
<section class="section"><div class="wrap split"><div class="rv"><h2>{display_name(p["name"])}</h2><p class="lede" style="margin-top:22px">{p["blurb"]}</p></div>
<div class="rv" data-d="100"><h3>A good fit for</h3><ul class="fit">{who}</ul><p class="note">Program fit and scope are discussed during your consultation. Contact Jacob for current availability and details rather than relying on an assumed price.</p></div></div></section>
<section class="section method" style="padding-block:90px"><div class="wrap method-grid"><div class="sticky"><h2 class="rv">How it works</h2></div>
<div class="steps"><div class="step"><span class="n">1</span><h3>Book</h3><p>Share what is happening at home and speak directly with Jacob.</p></div><div class="step"><span class="n">2</span><h3>Train</h3><p>{step2}</p></div><div class="step"><span class="n">3</span><h3>Thrive</h3><p>{step3}</p></div></div></div></section>
<section class="section" style="padding-bottom:0"><div class="wrap"><h2 class="rv" style="font-size:clamp(28px,3vw,42px)">Explore more</h2><div class="more rv">{oth}</div></div></section>
{contact()}
</main>''' + footer()


def about():
    w14, h14 = ar("img14.jpg")
    w06, h06 = ar("img06.jpg")
    w16, h16 = ar("img16.jpg")
    return head("About Jacob Soos | Gator Alley Dog Training, Parrish FL", "Meet Jacob Soos, Coast Guard veteran, Parrish native and the trainer who personally works with every dog at Gator Alley.", "/about-jacob-soos", schema()) + header("about") + f'''
<main id="main"><section class="phero"><div class="wrap hero-grid"><div><div class="status fade"><i></i>Meet your trainer</div>
<h1><span class="ln"><span>Jacob Soos,</span></span><span class="ln"><span>dog trainer in Parrish, FL</span></span></h1><p class="lede fade" style="margin:26px 0 32px">Gator Alley Dog Training is built around patient, consistent work and clearer communication between dogs and their families.</p>
<div class="cta-row fade">{btn("#consult", "Talk with Jacob")}</div></div>
<div class="arch-solo"><div class="sun"><div class="sun-in"></div></div><div class="topo" data-speed=".05"></div><div class="arch" style="aspect-ratio:{w14}/{h14}">{img("img14.jpg", "Jacob Soos serving in the United States Coast Guard", eager=True).replace('loading="lazy" decoding="async"', '')}</div></div></div></section>
{proof_strip()}
<section class="section"><div class="wrap story-grid"><div class="rv"><h2>A lifelong respect for dogs, and the work behind their behavior</h2></div><div class="rv" data-d="100"><p>Born and raised in Palmetto, Florida, Jacob grew up around dogs, including dogs with challenging behaviors. His training approach was shaped by years of learning how patience, consistency and clear communication change a dog’s relationship with its owner.</p><p>While serving in the U.S. Coast Guard along the Mississippi Gulf Coast, Jacob began training dogs to build experience and deepen that knowledge. Today he lives in Parrish with his wife and high-school sweetheart, Chloe, their German Shepherd Gator, and their cats Guru and Goose.</p></div></div></section>
<section class="section" style="padding-top:0"><div class="wrap story-grid"><div class="photo rv" style="aspect-ratio:{w06}/{h06}">{img("img06.jpg", "Jacob Soos working obedience with his German Shepherd")}</div><div class="rv" data-d="100"><h2>Your family becomes part of ours</h2><p>During Board &amp; Train, dogs live and learn in a real home environment, not a kennel. Daily structure, socialization and individualized work prepare them for the household routines and distractions that matter after they go home.</p><p>Every program ends with a detailed handover session and ongoing support so owners can confidently continue their dog’s progress.</p></div></div></section>
<section class="section method"><div class="wrap story-grid rev"><div class="rv"><h2>Discipline learned on the water, applied on the leash</h2><p>Jacob served five years in the U.S. Coast Guard as a Boatswain’s Mate Second Class, including search-and-rescue, law-enforcement missions and hurricane response along the Mississippi Gulf Coast. The same structure, calm and follow-through carries directly into his training.</p></div><div class="photo rv" style="aspect-ratio:{w16}/{h16}">{img("img16.jpg", "Jacob Soos in U.S. Coast Guard uniform holding service paperwork")}</div></div></section>
{contact()}
</main>''' + footer()


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


if __name__ == "__main__":
    pages = {"index.html": ("/", home())}
    for p in PROGRAMS:
        pages[f'{p["slug"]}.html'] = (f'/{p["slug"]}', program_page(p))
    pages[f'{VIRTUAL["slug"]}.html'] = (f'/{VIRTUAL["slug"]}', program_page(VIRTUAL, v=True))
    pages["about-jacob-soos.html"] = ("/about-jacob-soos", about())
    for f, (_, c) in pages.items():
        write(f, c)
    urls = "".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u, _ in pages.values())
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    write("vercel.json", '{"cleanUrls":true,"trailingSlash":false,"headers":[{"source":"/assets/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]}]}')
    print("built", len(pages), "pages")
