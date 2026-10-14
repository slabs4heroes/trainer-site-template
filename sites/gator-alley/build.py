#!/usr/bin/env python3
"""Gator Alley Dog Training — static site generator. Output: ./site"""
import os, html
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
         img="img07.jpg", alt="Jacob Soos training a dog in Parrish, Florida",
         h1="Basic Obedience Board & Train in Parrish, FL", lead="Clearer communication, better manners and routines that hold up at home — built around your dog and your household, not a script.",
         who=["Dogs who pull, jump, bark or struggle to settle", "Owners who want practical obedience that works in everyday life", "Anyone who wants direct, personal guidance from the trainer doing the work"]),
    dict(slug="advanced-obedience-behavior-parrish-fl", track="03", tag="ADVANCED", name="Advanced Obedience, Off-Leash & Behavior Modification",
         it="", blurb="For owners navigating reactivity, anxiety, difficult behavior, or a higher standard of advanced obedience, calmness, communication and off-leash reliability.",
         img="img10.jpg", alt="Dogs practicing socialization and impulse control outdoors in Parrish, Florida",
         h1="Advanced Obedience & Behavior Modification in Parrish, FL", lead="For the harder cases and the higher standard: reactivity, anxiety, difficult behavior, calm communication and off-leash reliability.",
         who=["Dogs with reactivity, fear, anxiety or a behavior history", "Owners who want advanced obedience and off-leash reliability", "Households ready to be candid about what has happened so the plan can be responsible"]),
    dict(slug="puppy-raise-and-train-parrish-fl", track="04", tag="12 WEEKS", name="Puppy Raise & Train",
         it="", blurb="A longer foundation-focused program personally led by Jacob during the key early stages of development, with structured routines, socialization, real-world exposure and advanced foundations.",
         img="img12.jpg", alt="Jacob Soos with a young dog during puppy training in Parrish, Florida",
         h1="Puppy Raise & Train in Parrish, FL", lead="Twelve weeks of structured routines, socialization and real-world exposure during the stages of development that matter most.",
         who=["Puppy owners who want a deeper foundation than a short program", "Families who want Jacob personally leading the key early stages", "Owners planning for advanced foundations from the start"]),
]
VIRTUAL = dict(slug="virtual-dog-training-coaching", track="+", tag="ZOOM", name="Virtual Coaching Sessions",
               blurb="Live one-on-one coaching with Jacob over Zoom — leash manners, puppy foundations, or behavior and consistency. Every session is recorded for you to keep.",
               img="img11.jpg", alt="Dogs holding a down command during neighborhood obedience training",
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
         '<link href="https://fonts.googleapis.com/css2?family=DM+Mono&family=DM+Sans:wght@400;500;600;700&family=Oswald:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">')


def head(title, desc, path, extra=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{DOMAIN}{path}"><meta name="theme-color" content="#14301f">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:image" content="{DOMAIN}/assets/img05.jpg">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
{FONTS}<link rel="stylesheet" href="/styles.css">{extra}</head><body>'''


def header():
    return f'''<div class="notice"><span>◆</span> PARRISH, FLORIDA <span>◆</span> PERSONALLY LED BOARD &amp; TRAIN <span>◆</span> REAL HOME. REAL WORLD. <span>◆</span></div>
<header class="header" id="top"><div class="wrap bar"><a href="/" class="brand" aria-label="Gator Alley Dog Training home"><img src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356"></a>
<nav aria-label="Main"><a href="/#programs">Programs</a><a href="/about-jacob-soos">About Jacob</a><a href="/#faq">FAQ</a><a href="/#consult">Contact</a></nav>
<a class="small-cta" href="/#consult">Free consultation <b>→</b></a></div></header>'''


def footer():
    ar = "".join(f"<li>{a}</li>" for a in AREAS)
    plinks = "".join(f'<li><a href="/{p["slug"]}">{p["name"].split(",")[0] if "Advanced" not in p["name"] else "Advanced Obedience &amp; Behavior"}</a></li>' for p in PROGRAMS) + f'<li><a href="/{VIRTUAL["slug"]}">Virtual Coaching</a></li>'
    return f'''<footer class="foot"><div class="wrap foot-grid">
<div><img class="foot-logo" src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356" loading="lazy"><p>Dog training in Parrish, Florida · Serving board-and-train clients nationwide</p><p class="mono">Gator Alley Dog Training Academy, LLC<br>{ADDR}</p></div>
<div><h4>Explore</h4><ul><li><a href="/">Home</a></li>{plinks}<li><a href="/about-jacob-soos">About Jacob</a></li></ul></div>
<div><h4>Serving</h4><ul class="areas">{ar}</ul></div>
<div><h4>Get in touch</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li>Wed–Sun, 9 AM–8 PM</li><li><a href="{IG}" rel="noopener">Instagram</a> · <a href="{FB}" rel="noopener">Facebook</a></li><li><a href="/#consult">Request a consultation</a></li></ul></div>
</div><div class="wrap legal"><span>© Gator Alley Dog Training Academy, LLC</span><a href="#top">Back to top ↑</a></div></footer>
<div class="mobile-bar"><a href="tel:{TEL}">Call</a><a href="/#consult" class="go">Book consultation</a></div>
<script src="/script.js" defer></script></body></html>'''


def form(idn="consult", dark=True):
    opts = "".join(f"<option>{o}</option>" for o in ["Puppy Head Start (2 weeks)", "Basic Obedience", "Advanced Obedience, Off-Leash & Behavior", "Puppy Raise & Train (12 weeks)", "Virtual Coaching (Zoom)", "Not sure yet — help me choose"])
    return f'''<form class="lead-form" data-form action="https://formsubmit.co/ajax/{EMAIL_FORM}" method="post">
<input type="hidden" name="_subject" value="New consultation request — Gator Alley website"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
<label>Your name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label class="wide">Email<input name="email" type="email" required autocomplete="email"></label>
<label class="wide">Interested in<select name="program">{opts}</select></label>
<label class="wide">Tell Jacob about your dog (age, breed, what’s going on)<textarea name="message" rows="4"></textarea></label>
<button class="primary" type="submit">Request my consultation <b>→</b></button><p class="form-msg" role="status" aria-live="polite"></p>
<small>Jacob will follow up personally. Available Wednesday–Sunday, 9 AM–7 PM Eastern.</small></form>'''


def schema(extra=""):
    return f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","@id":"{DOMAIN}/#business","name":"Gator Alley Dog Training","legalName":"Gator Alley Dog Training Academy, LLC","url":"{DOMAIN}/","telephone":"{TEL}","image":"{DOMAIN}/assets/img05.jpg","address":{{"@type":"PostalAddress","streetAddress":"10328 Charlotte Dr","addressLocality":"Parrish","addressRegion":"FL","postalCode":"34219","addressCountry":"US"}},"areaServed":{[__import__("json").dumps(a) for a in []] or __import__("json").dumps(AREAS)},"sameAs":["{IG}","{FB}"],"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"16"}}}}</script>{extra}'''


def marquee():
    items = ["PUPPY HEAD START", "BASIC OBEDIENCE", "ADVANCED &amp; OFF-LEASH", "BEHAVIOR MODIFICATION", "PUPPY RAISE &amp; TRAIN", "VIRTUAL COACHING"]
    row = "".join(f"<span>{i}</span><b>◆</b>" for i in items)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{row}{row}</div></div>'


def home():
    cards = ""
    for p in PROGRAMS:
        nm = p["name"]
        nm_html = "Advanced Obedience, <i>Off-Leash</i> &amp; Behavior" if "Advanced" in nm else nm.replace(" Start", " <i>Start</i>").replace("Basic ", "Basic <i>").replace("Obedience", "Obedience</i>", 1) if nm == "Basic Obedience" else nm
        if nm == "Basic Obedience": nm_html = "Basic <i>Obedience</i>"
        if nm == "Puppy Raise & Train": nm_html = "Puppy Raise <i>&amp; Train</i>"
        if nm == "Puppy Head Start": nm_html = "Puppy Head <i>Start</i>"
        cards += f'''<a class="pcard reveal" href="/{p["slug"]}"><div class="pimg" style="--ar:{'/'.join(map(str, Image.open(f"{OUT}/assets/{p['img']}").size))}">{img(p["img"], p["alt"])}</div>
<div class="pbody"><p class="mono">TRACK {p["track"]} · {p["tag"]}</p><h3>{nm_html}</h3><p>{p["blurb"]}</p><span class="more">Explore <b>→</b></span></div></a>'''
    faq = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    faq_ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}) + "</script>"
    gallery = [("img06.jpg", "Jacob Soos and his German Shepherd on the waterfront"), ("img09.jpg", "Dogs practicing calm impulse control inside a home"),
               ("img11.jpg", "Dogs holding a down command during neighborhood obedience training"), ("img19.jpg", "Two German Shepherds resting near a boat"),
               ("img03.jpg", "Jacob kneeling with his German Shepherd Gator"), ("img13.jpg", "Puppy practicing leash skills")]
    gal = "".join(frame(n, a) for n, a in gallery)
    return head("Dog Trainer in Parrish, FL | Gator Alley Dog Training",
                "Personally led board-and-train dog training in Parrish, FL. Puppy head start, basic and advanced obedience, behavior modification and virtual coaching with Jacob Soos.", "/",
                schema(faq_ld)) + header() + f'''
<main>
<section class="hero wrap"><div class="hero-copy"><p class="kicker">DOG TRAINING IN PARRISH, FLORIDA</p>
<h1>Reliable obedience <i>built for</i> real life.</h1>
<p class="lede">Gator Alley Dog Training offers personally led board-and-train programs for owners who want calm, trustworthy and obedient dogs.</p>
<div class="hero-buttons"><a class="primary" href="#consult">Free consultation <b>→</b></a><a class="play-link" href="#programs"><span>↓</span>See the programs</a></div>
<div class="hero-details"><span>5.0 ★ GOOGLE · 16 REVIEWS</span><span>HOME ENVIRONMENT, NOT A KENNEL</span><span>TRAINED BY JACOB, PERSONALLY</span></div></div>
<div class="hero-art"><div class="blob"></div><figure class="hero-photo" style="--ar:1150/762"><img src="/assets/img05.jpg" alt="German Shepherd Gator walking a sandy path in Parrish, Florida" width="1150" height="762" fetchpriority="high"></figure>
<figure class="hero-photo sm" style="--ar:1150/762"><img src="/assets/img03.jpg" alt="Jacob Soos kneeling with his German Shepherd" width="1150" height="762" loading="lazy"></figure>
<div class="badge"><b>5.0</b><span>★★★★★<br>GOOGLE REVIEWS</span></div></div></section>
{marquee()}
<section class="problem wrap"><p class="big-number reveal">01</p><div class="reveal"><p class="kicker">IS THIS YOU?</p><h2>When everyday dog life feels <i>harder than it should.</i></h2></div>
<p class="reveal">Maybe walks are stressful, guests bring out jumping or barking, recall feels unreliable, or you’re not sure how to help a puppy build good foundations. You’re not looking for a gimmick — you want a clearer plan and support that fits your household.</p></section>
<section class="quotes wrap"><blockquote class="reveal"><p>“I love my dog, but I feel overwhelmed.”</p><span>Training should make daily life more manageable, not leave you guessing what to do next.</span></blockquote>
<blockquote class="reveal"><p>“The behavior changes depending on the situation.”</p><span>Real-world routines and distractions matter. The goal is usable communication beyond a quiet training space.</span></blockquote>
<blockquote class="reveal"><p>“I want my family to feel confident.”</p><span>Clear handover guidance helps owners continue the work consistently once their dog returns home.</span></blockquote></section>
<section class="programs" id="programs"><div class="wrap"><div class="section-head reveal"><div><p class="kicker">GATOR ALLEY BOARD &amp; TRAIN</p><h2>Four paths.<br>One goal: <i>a better life with your dog.</i></h2></div>
<p>Every Gator Alley program is structured around your dog’s history, home life and training goals. The work is personally led by Jacob in a real home environment, with focused training, practical routines and a clear owner handoff so progress carries into everyday life.</p></div>
<div class="pgrid">{cards}</div>
<a class="virtual reveal" href="/{VIRTUAL["slug"]}"><span class="mono">NEW — ONE-ON-ONE, FROM ANYWHERE</span><h3>Can’t make it to Parrish? <i>Train with Jacob over Zoom.</i></h3><p>Live virtual coaching for leash manners, puppy foundations, or behavior and consistency. Every session is recorded for you to keep.</p><b>See virtual coaching →</b></a></div></section>
<section class="path wrap"><div class="reveal"><p class="kicker">A SIMPLE PATH FORWARD</p><h2>Book. Train. <i>Thrive.</i></h2><p class="sub">Every conversation begins with your dog’s needs, your goals and the right fit — not a one-size-fits-all promise.</p></div>
<ol><li class="reveal"><b>01</b><h3>Book</h3><p>Share what is happening at home and speak directly with Jacob about your goals.</p></li><li class="reveal"><b>02</b><h3>Train</h3><p>Your dog receives personally led work, structure and real-world exposure in the appropriate program.</p></li><li class="reveal"><b>03</b><h3>Thrive</h3><p>Use the handover and ongoing support to carry clearer communication into everyday life.</p></li></ol></section>
<section class="meet" id="meet"><div class="wrap meet-grid"><figure class="frame reveal tall" style="--ar:1150/762">{img("img17.jpg", "Portrait of Jacob Soos outdoors in Parrish, Florida")}<figcaption>JACOB SOOS · FOUNDER &amp; LEAD TRAINER</figcaption></figure>
<div class="reveal"><p class="kicker">MEET JACOB</p><h2>Built around the dog. <i>Led by one trainer.</i></h2>
<p>Born and raised in Palmetto, Florida, Jacob grew up around dogs, including dogs with challenging behaviors. After five years in the U.S. Coast Guard, he brings that same structure, calm and follow-through to every dog in his care — in a real home, with his wife Chloe, their German Shepherd Gator, and a couple of cats.</p>
<p>Dogs live and learn in a real home environment, not a facility. Jacob personally works with each dog through the routines, people and distractions that make reliable behavior matter.</p>
<a class="primary" href="/about-jacob-soos">Meet Jacob <b>→</b></a></div></div></section>
<section class="gallery"><div class="wrap"><div class="section-head reveal"><div><p class="kicker">REAL SESSIONS, REAL DOGS</p><h2>Out in <i>the work.</i></h2></div><p>Real photos from Gator Alley training in and around Parrish — hand signals, calm impulse control, and reliability practiced outside the training space.</p></div>
<div class="gal">{gal}</div></div></section>
<section class="proof wrap"><div class="reveal"><p class="kicker">PROOF FROM THE PROGRAM</p><h2>5.0 <i>on Google.</i></h2><p>Sixteen Google reviews, every one five stars. See what Parrish dog owners say about training with Jacob.</p>
<a class="primary light" href="https://www.google.com/search?q=Gator+Alley+Dog+Training+Parrish+FL" rel="noopener">Read the reviews <b>→</b></a></div></section>
<section class="area wrap" id="area"><div class="reveal"><p class="kicker">SERVING PARRISH &amp; NEARBY AREAS</p><h2>Dog training that starts in Parrish and <i>travels home with you.</i></h2></div>
<div class="reveal"><p>Gator Alley is based in Parrish and serves owners in {", ".join(AREAS[1:-1])} and {AREAS[-1]}, while also welcoming board-and-train clients from around the country. The conversation starts with your dog’s actual routines, behavior history and household goals.</p><ul class="chips">{"".join(f"<li>{a}</li>" for a in AREAS)}<li>Nationwide board &amp; train</li></ul></div></section>
<section class="faq wrap" id="faq"><div class="reveal"><p class="kicker">FREQUENTLY ASKED QUESTIONS</p><h2>What to know <i>before you call.</i></h2></div><div class="faq-list">{faq}</div></section>
<section class="lead" id="consult"><div class="wrap lead-grid"><div class="reveal"><p class="kicker">TALK WITH JACOB</p><h2>Book your <i>free consultation.</i></h2><p>Tell us about you and your dog — Jacob will follow up personally. Available Wednesday through Sunday, 9 AM–7 PM Eastern. Prefer to talk first? Call <a href="tel:{TEL}">{PHONE}</a>.</p></div>
<div class="reveal">{form()}</div></div></section>
</main>''' + footer()


def program_page(p, v=False):
    others = [x for x in PROGRAMS if x["slug"] != p["slug"]]
    who = "".join(f"<li>{w}</li>" for w in p["who"])
    oth = "".join(f'<a href="/{o["slug"]}"><span class="mono">TRACK {o["track"]}</span><b>{o["name"]}</b></a>' for o in others)
    if not v:
        oth += f'<a href="/{VIRTUAL["slug"]}"><span class="mono">ZOOM</span><b>{VIRTUAL["name"]}</b></a>'
    else:
        oth = "".join(f'<a href="/{o["slug"]}"><span class="mono">TRACK {o["track"]}</span><b>{o["name"]}</b></a>' for o in PROGRAMS)
    desc = p["lead"]
    ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "Service", "name": p["name"], "provider": {"@id": f"{DOMAIN}/#business"}, "areaServed": AREAS, "description": p["blurb"]}) + "</script>"
    return head(f'{p["h1"]} | Gator Alley Dog Training', desc, f'/{p["slug"]}', schema(ld)) + header() + f'''
<main><section class="phero wrap"><div class="reveal"><p class="kicker">{"TRACK " + p["track"] + " · " if not v else "ONE-ON-ONE · "}{p["tag"]}</p><h1>{p["h1"].replace(" in Parrish, FL", "<br><i>in Parrish, FL</i>") if " in Parrish, FL" in p["h1"] else p["h1"]}</h1><p class="lede">{p["lead"]}</p>
<div class="hero-buttons"><a class="primary" href="#consult">Free consultation <b>→</b></a><a class="play-link" href="tel:{TEL}"><span>☎</span>{PHONE}</a></div></div>
{frame(p["img"], p["alt"], cls="phero-img")}</section>{marquee()}
<section class="pdetail wrap"><div class="reveal"><p class="kicker">THE PROGRAM</p><h2>{p["name"]}</h2><p class="big">{p["blurb"]}</p></div>
<div class="reveal"><p class="kicker">A GOOD FIT FOR</p><ul class="fit">{who}</ul><p class="note">Program fit and scope are discussed during your consultation — contact Jacob for current availability and details rather than relying on an assumed price.</p></div></section>
<section class="path wrap"><div class="reveal"><p class="kicker">HOW IT WORKS</p><h2>Book. Train. <i>Thrive.</i></h2></div>
<ol><li class="reveal"><b>01</b><h3>Book</h3><p>Share what is happening at home and speak directly with Jacob.</p></li><li class="reveal"><b>02</b><h3>Train</h3><p>{"Live one-on-one Zoom coaching, recorded so you can keep it." if v else "Personally led work, structure and real-world exposure in a real home — not a kennel."}</p></li><li class="reveal"><b>03</b><h3>Thrive</h3><p>{"Practice from your recording and carry the work into everyday life." if v else "A detailed handover and ongoing support so progress carries into everyday life."}</p></li></ol></section>
<section class="more-programs wrap"><p class="kicker reveal">EXPLORE MORE</p><div class="mp-grid reveal">{oth}</div></section>
<section class="lead" id="consult"><div class="wrap lead-grid"><div class="reveal"><p class="kicker">TALK WITH JACOB</p><h2>Book your <i>free consultation.</i></h2><p>Tell us about you and your dog — Jacob will follow up personally. Prefer to talk first? Call <a href="tel:{TEL}">{PHONE}</a>.</p></div><div class="reveal">{form()}</div></div></section></main>''' + footer()


def about():
    return head("About Jacob Soos | Gator Alley Dog Training, Parrish FL", "Meet Jacob Soos — Coast Guard veteran, Parrish native and the trainer who personally works with every dog at Gator Alley.", "/about-jacob-soos", schema()) + header() + f'''
<main><section class="phero wrap"><div class="reveal"><p class="kicker">MEET YOUR TRAINER</p><h1>Jacob Soos,<br><i>dog trainer in Parrish, FL.</i></h1><p class="lede">Gator Alley Dog Training is built around patient, consistent work and clearer communication between dogs and their families.</p>
<div class="hero-buttons"><a class="primary" href="#consult">Talk with Jacob <b>→</b></a></div></div>{frame("img14.jpg", "Jacob Soos serving in the United States Coast Guard", "U.S. COAST GUARD · BOATSWAIN’S MATE SECOND CLASS", "phero-img portrait")}</section>{marquee()}
<section class="story wrap"><div class="reveal"><p class="kicker">FROM PALMETTO TO PARRISH</p><h2>A lifelong respect for dogs — <i>and the work behind their behavior.</i></h2></div>
<div class="reveal"><p>Born and raised in Palmetto, Florida, Jacob grew up around dogs, including dogs with challenging behaviors. His training approach was shaped by years of learning how patience, consistency and clear communication change a dog’s relationship with its owner.</p>
<p>While serving in the U.S. Coast Guard along the Mississippi Gulf Coast, Jacob began training dogs to build experience and deepen that knowledge. Today he lives in Parrish with his wife and high-school sweetheart, Chloe, their German Shepherd Gator, and their cats Guru and Goose.</p></div></section>
<section class="duo wrap">{frame("img06.jpg", "Jacob Soos working obedience with his German Shepherd")}<div class="reveal"><p class="kicker">A HOME ENVIRONMENT</p><h2>Your family becomes <i>part of ours.</i></h2><p>During Board &amp; Train, dogs live and learn in a real home environment — not a kennel. Daily structure, socialization and individualized work prepare them for the household routines and distractions that matter after they go home.</p><p>Every program ends with a detailed handover session and ongoing support so owners can confidently continue their dog’s progress.</p></div></section>
<section class="duo wrap rev"><div class="reveal"><p class="kicker">FIVE YEARS IN THE U.S. COAST GUARD</p><h2>Discipline learned on the water, <i>applied on the leash.</i></h2><p>Jacob served five years in the U.S. Coast Guard as a Boatswain’s Mate Second Class, including search-and-rescue, law-enforcement missions and hurricane response along the Mississippi Gulf Coast. The same structure, calm and follow-through carries directly into his training.</p></div>{frame("img16.jpg", "Jacob Soos in U.S. Coast Guard uniform holding service paperwork")}</section>
<section class="lead" id="consult"><div class="wrap lead-grid"><div class="reveal"><p class="kicker">TALK WITH JACOB</p><h2>Book your <i>free consultation.</i></h2><p>Tell us about you and your dog — Jacob will follow up personally. Prefer to talk first? Call <a href="tel:{TEL}">{PHONE}</a>.</p></div><div class="reveal">{form()}</div></div></section></main>''' + footer()


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
