#!/usr/bin/env python3
"""Gator Alley Dog Training — static site generator (sleek K9PN design).
Copy, page structure, photos, consultation form and booking calendar mirror https://gatoralleyk9.com exactly."""
import os, html, json
from PIL import Image
from seo_data import AREA_ORDER, AREAS_LOCAL, LANDINGS, PROBLEMS, PROB_PROGRAM, PROBLEM_LABELS

OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://gatoralleyk9.com"
PHONE = "(941) 842-0849"
TEL = "+19418420849"
EMAIL = "gatoralleyk9@gmail.com"
IG = "https://www.instagram.com/gatoralleyk9"
FB = "https://www.facebook.com/share/1HG7KeMFk3/?mibextid=wwXIfr"
ADDR = "10328 Charlotte Dr, Parrish, FL 34219"
GOOGLE = "https://www.google.com/search?q=Gator+Alley+Dog+Training+Parrish+FL"
FORM_ID = "omIJGkHDTkJ2ZCKIWgPn"
BOOK_ID = "fItaqpy8rCCNlzdk7IhM"
AREAS = ["Parrish", "Palmetto", "Ellenton", "Bradenton", "Lakewood Ranch", "Sarasota", "Ruskin", "Apollo Beach", "Sun City Center", "Riverview", "Brandon", "Tampa", "St. Petersburg", "Venice", "North Port"]


def E(s):
    return html.escape(s, quote=False)


def A(s):
    return html.escape(s, quote=True)


def ar(name):
    return Image.open(f"{OUT}/assets/{name}").size


def img(name, alt, eager=False):
    w, h = ar(name)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="/assets/{name}" alt="{A(alt)}" width="{w}" height="{h}" {load}>'


def photo(name, alt, cap="", cls="", d=0):
    w, h = ar(name)
    c = f"<figcaption>{E(cap)}</figcaption>" if cap else ""
    return f'<figure class="mfig rv {cls}" data-d="{d}"><div class="photo" style="aspect-ratio:{w}/{h}">{img(name, alt)}</div>{c}</figure>'


ARROW = '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'
ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PHONE_IC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Big+Shoulders+Display:wght@700;800;900&display=swap" rel="stylesheet">')

# ---------------------------------------------------------------- program data (live copy)
PROGRAMS = [
    dict(slug="puppy-head-start", track="Track 01", tag="2 weeks", name="Puppy Head Start Program", short="Puppy Head Start",
         nav="Puppy Head Start", cta="Explore Puppy Head Start",
         blurb="A focused 2-week program for puppies covering basic obedience, potty training and exposure training — the best possible start before habits set in.",
         card=("prog-pomsky.jpg", "A Pomsky puppy practicing loose-leash walking during basic obedience training in Parrish, Florida"),
         title="Puppy Head Start Program in Parrish, FL | Gator Alley K9",
         desc="The Puppy Head Start Program gives Parrish, FL puppy owners an early advantage on obedience, socialization, and confidence before issues start.",
         h1="Puppy Head Start Program in Parrish, FL",
         lede="A two-week puppy-training program that establishes early routines and communication for home and everyday life.",
         intro=["Designed to give your puppy the best possible start during the earliest stages of development. This two-week program focuses on establishing healthy routines, crate training, potty training, confidence building, proper socialization, household manners, leash introduction, and the beginning stages of obedience.",
                "The goal is to get ahead of common puppy problems before they become lifelong habits while giving owners a clear foundation to continue building on at home."],
         focus=["Healthy routines, crate training and potty training", "Confidence building and proper socialization", "Household manners and leash introduction", "Beginning stages of obedience"],
         local=["For Parrish puppy owners, early routine work can support consistent crate time, potty training, introductions, household expectations and leash practice.",
                "Gator Alley Dog Training serves nearby dog owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and surrounding Manatee County communities."],
         diff="Puppy Head Start is led personally by Jacob in a real home environment during your puppy’s most important early weeks — not a group puppy class, so routines and habits are built the way your household actually lives.",
         how="How the Puppy Head Start Program Works",
         steps=[("Personalized planning", "Jacob discusses your puppy’s age, temperament and your household routines before the two weeks begin."),
                ("Daily routines", "Crate time, potty training, feeding and socialization are built around consistent daily structure from day one."),
                ("Focused training", "Leash introduction, confidence-building and the beginning stages of obedience are practiced every day."),
                ("Real-world exposure", "Your puppy is introduced to new people, places and situations appropriate for their age and stage."),
                ("Owner handoff", "You get a full walkthrough of routines and commands so you can keep building on the foundation at home."),
                ("Consultation first", "Every program starts with a conversation about your puppy’s needs and your family’s goals.")],
         imgs=[("img13.jpg", "Young puppy practicing leash skills during puppy training in Parrish, Florida")],
         faq=[("Where does training happen?", "Your puppy lives and learns in Jacob’s real home environment in Parrish, with exposure to normal household routines rather than a kennel facility."),
              ("Can puppy owners start the conversation before choosing a program?", "Yes — share your puppy’s age, socialization needs and household-manners goals during the consultation, and Jacob can discuss whether Puppy Head Start is the right fit."),
              ("What happens when my puppy comes home after the two weeks?", "You get a full walkthrough of routines and commands, plus ongoing support so you can keep building on the foundation consistently at home.")]),
    dict(slug="basic-obedience", track="Track 02", tag="Board & Train", name="Basic Obedience", short="Basic Obedience",
         nav="Basic Obedience", cta="Explore Basic Obedience",
         blurb="A focused program for clearer communication, better manners, reliable routines and practical obedience matched to your household.",
         card=("prog-frenchie-wait.webp", "An adult French Bulldog practicing a wait command during behavioral training in Parrish, Florida"),
         title="Basic Obedience Training in Parrish, FL | Gator Alley K9",
         desc="Basic obedience training in Parrish, FL builds sit, stay, place, and loose-leash manners for real-world reliability. Book a free consultation today.",
         h1="Basic Obedience Training in Parrish, FL",
         lede="Build clearer communication, better manners and reliable everyday obedience around your dog’s needs.",
         intro=["Designed for owners who want to address specific individual behaviors or begin building a strong foundation of basic obedience. This program focuses on the areas that matter most to you and your dog, developing better manners, clearer communication, and reliable everyday obedience without adding advanced training that may not fit your lifestyle."],
         focus=["Specific individual behaviors", "Basic-obedience foundations", "Better everyday manners", "Clearer communication", "Reliable obedience that fits your lifestyle"],
         local=["For dog owners in Parrish, FL, basic obedience can focus on daily routines where communication matters: walks, greetings, settling indoors, recall, distractions and consistency between family members.",
                "Gator Alley Dog Training serves nearby dog owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and surrounding Manatee County communities."],
         diff="Basic Obedience is built and led personally by Jacob in his own home environment, not a kennel or group class — so the manners and communication you build actually carry over into your daily routine.",
         how="How Basic Obedience Works",
         steps=[("Personalized planning", "Jacob talks through the specific behaviors and goals you want to address before training starts, so the program fits your dog and your household."),
                ("Focused daily training", "Jacob works one-on-one with your dog inside his own home, building manners, clearer communication and everyday obedience day by day."),
                ("Real-world practice", "Skills are practiced around the distractions of daily life — walks, greetings, guests — not just inside a quiet training space."),
                ("Owner handoff", "Before your dog comes home, you get a full walkthrough of the commands and routines so the training holds up at home."),
                ("Consultation first", "Every program starts with a conversation about your dog’s history and goals — not a one-size-fits-all sign-up.")],
         imgs=[("img06.jpg", "Jacob Soos working obedience with his German Shepherd"), ("img03.jpg", "Jacob Soos giving a hand-signal cue to a German Shepherd during obedience training")],
         faq=[("Where does training happen?", "Training happens in Jacob’s real home environment in Parrish rather than a kennel facility, with exposure to normal household routines and real-world distractions."),
              ("Who trains my dog?", "Jacob personally trains and cares for your dog throughout the program — no rotating staff."),
              ("What ages and breeds are a fit for Basic Obedience?", "Every dog is different. Share your dog’s age, breed, history and goals during the consultation so Jacob can discuss whether this program is the right fit.")]),
    dict(slug="behavioral-issues-reactivity", track="Track 03", tag="Advanced", name="Advanced Obedience, Off-Leash & Behavior Modification", short="Advanced Obedience & Behavior",
         nav="Advanced Obedience & Behavior", cta="Explore Advanced Obedience",
         blurb="For owners navigating reactivity, anxiety, difficult behavior, or a higher standard of advanced obedience, calmness, communication and off-leash reliability.",
         card=("prog-gsd-down.webp", "A black German Shepherd holding a down-stay during puppy foundations training in Parrish, Florida"),
         title="Reactivity & Behavior Training in Parrish, FL | Gator Alley",
         desc="Behavior modification for reactivity, anxiety, and unwanted behaviors in Parrish, FL. Structured, one-on-one training with Jacob Soos rebuilds reliability.",
         h1="Advanced Obedience, Off-Leash & Behavior Modification in Parrish, FL",
         lede="Advanced dog training for owners working through serious behavior challenges—or seeking a highly advanced level of obedience.",
         intro=["Designed for owners struggling with serious behavioral challenges—or those who simply want a highly advanced level of obedience. Jacob works hands-on with reactive, aggressive, anxious, or difficult-to-manage dogs to address unwanted behaviors while developing exceptional obedience, calmness, confidence, and control.",
                "Your dog will develop full-spectrum communication, advanced positioning, and off-leash reliability, creating a dog capable of performing reliably at home, in public, and around real-world distractions."],
         focus=["Advanced obedience and real-world reliability", "Off-leash communication and positioning", "Reactivity, anxiety or difficult-to-manage behavior", "Calmness and control around everyday distractions"],
         local=["For Parrish dog owners, this program begins with an honest conversation about the behavior you are seeing and the environments where it occurs. Clear history around reactivity, fear, anxiety, aggression or bite history helps determine the appropriate training plan and next step.",
                "Gator Alley Dog Training serves nearby dog owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and surrounding Manatee County communities."],
         diff="This program is led personally by Jacob in a real home environment, not a kennel or group setting — every case starts with an honest look at your dog’s specific history before any plan is built.",
         how="How Advanced Obedience & Behavior Modification Works",
         steps=[("Personalized planning", "Jacob discusses your dog’s specific behavior history — reactivity, anxiety or a bite history — before building a plan."),
                ("Focused, hands-on training", "Jacob works directly with your dog every day to address the behavior while building advanced obedience and control."),
                ("Daily structure", "Calm, consistent routines help your dog build confidence day after day, not just during a single session."),
                ("Real-world practice", "Training moves into public settings and everyday distractions to build genuine off-leash reliability."),
                ("Owner handoff", "You receive a full walkthrough of the tools, commands and structure your dog needs once home."),
                ("Consultation first", "Every case starts with an honest conversation about your dog’s history — this is a personalized plan, not a guaranteed outcome, especially for aggression or reactivity cases.")],
         imgs=[("img10.jpg", "Dogs practicing socialization and impulse control outdoors in Parrish, Florida"), ("img05.jpg", "German Shepherd walking a path off-leash in Parrish, Florida")],
         faq=[("Can you help with reactivity or aggression?", "Behavior history matters. Be candid about fear, aggression, reactivity or a bite history during the consultation so the situation can be discussed responsibly — this is a personalized plan, not a guaranteed outcome, especially for aggression or reactivity cases."),
              ("Who trains my dog?", "Jacob personally works with your dog throughout the program — no rotating staff or group classes."),
              ("What happens when my dog comes home?", "The program includes a detailed handover and ongoing support so you can continue the training consistently and safely at home.")]),
    dict(slug="puppy-foundations", track="Track 04", tag="12 weeks", name="Puppy Raise & Train", short="Puppy Raise & Train",
         nav="Puppy Raise & Train", cta="Explore Puppy Raise & Train",
         blurb="A longer foundation-focused program personally led by Jacob during the key early stages of development, with structured routines, socialization, real-world exposure and advanced foundations.",
         card=("prog-frenchie-puppy.jpg", "A French Bulldog puppy practicing leash walking during the Puppy Head Start Program in Parrish, Florida"),
         title="Puppy Foundations Training in Parrish, FL | Gator Alley K9",
         desc="Puppy Foundations builds leash manners, socialization, and obedience basics for young dogs in Parrish, FL. Start your puppy off right with Gator Alley.",
         h1="Puppy Raise & Train in Parrish, FL",
         lede="A twelve-week puppy raise-and-train program personally led by Jacob.",
         intro=["During their most important early stages of development, your puppy is raised and trained personally by Jacob, developing exceptional obedience, calm confidence, proper socialization, and real-world exposure while building a strong foundation designed to support them for a lifetime.",
                "Your puppy will graduate with service-dog-level obedience, full-spectrum communication, advanced positioning, and off-leash reliability—creating a highly trained dog capable of performing reliably at home, in public, and around real-world distractions."],
         focus=["Early obedience and household routines", "Calm confidence and appropriate socialization", "Real-world exposure during foundational development", "Full-spectrum communication and off-leash reliability"],
         local=["For Parrish-area families bringing home a young puppy, this twelve-week format creates time to establish routines, early obedience, socialization and real-world exposure during a foundational stage of development.",
                "Gator Alley Dog Training serves nearby dog owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and surrounding Manatee County communities."],
         diff="Puppy Raise & Train is led personally by Jacob in a real home environment throughout the full twelve weeks — not a kennel or rotating-staff facility — so your puppy grows up around real routines and real-world exposure.",
         how="How Puppy Raise & Train Works",
         steps=[("Personalized planning", "Jacob discusses your puppy’s early weeks, breed and your family’s goals before the twelve-week program begins."),
                ("Daily routines", "Consistent structure across feeding, crate time, socialization and rest builds good habits early."),
                ("Focused training", "Jacob personally works with your puppy every day, building obedience, calm confidence and real-world exposure."),
                ("Real-world practice", "As your puppy grows, training extends into public places and everyday situations."),
                ("Owner handoff", "You get a full walkthrough of commands, routines and expectations so you can continue the training at home."),
                ("Consultation first", "Every program begins with a conversation about your puppy’s needs and your family’s goals.")],
         imgs=[("img12.jpg", "Jacob Soos with a young dog during puppy training in Parrish, Florida"), ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator, raised using the same training approach")],
         faq=[("Where does training happen?", "Your puppy is raised and trained in Jacob’s real home environment in Parrish, with exposure to normal household routines and real-world distractions throughout the twelve weeks."),
              ("What ages and breeds are a fit for Puppy Raise & Train?", "Every puppy is different. Share your puppy’s age, breed and your family’s goals during the consultation so Jacob can discuss whether this program is the right fit."),
              ("What happens when my puppy comes home after twelve weeks?", "You get a full walkthrough of commands, routines and expectations, plus ongoing support so you can continue the training consistently at home.")]),
]

HOME_FAQ = [
    ("Where does training happen?", "Dogs live and learn in Jacob’s real home environment in Parrish rather than a kennel facility, with exposure to household routines and real-world distractions."),
    ("Who trains my dog?", "Jacob personally trains and cares for every dog throughout the program."),
    ("What happens when my dog comes home?", "The program includes a detailed handover and ongoing support so you can continue the training consistently at home."),
    ("What ages and breeds are a fit?", "Every dog is different. Share your dog’s age, breed, history and goals so Jacob can discuss the appropriate next step."),
    ("Can puppy owners start the conversation?", "Yes, puppy owners can include their socialization, household-manners and foundation goals in the consultation request. Jacob can then discuss whether the current programs are appropriate."),
    ("Can you help with reactivity or aggression?", "Behavior history matters. Be candid about fear, aggression, reactivity or bite history during the consultation so the situation can be discussed responsibly."),
    ("What does training cost?", "Program fit and scope are discussed during the consultation. Contact Jacob for current availability and program details rather than relying on an assumed price."),
]

PROG_FAQ = [
    ("Which program is right for my dog?", "The right fit depends on your dog’s current behavior, training history and goals. Start with a consultation so Jacob can walk through the options together: the Custom Board & Train program, tailored around Basic Obedience, Behavioral Issues & Reactivity, or Puppy Foundations, with length of stay matched to the outcome you want — or, for puppies just starting out, the 2-week Puppy Head Start Program covering basic obedience, potty training and exposure training."),
    ("Do you offer virtual sessions?", "Yes — Jacob offers live virtual coaching over Zoom for owners who want one-on-one help with a specific topic, wherever they're located. The session is recorded and given to you afterward, plus follow-up support. See the Virtual Coaching Sessions section above for how it works."),
    ("Is virtual coaching a fit for every dog?", "Not necessarily. For serious safety concerns or complex behavior histories, Jacob will first discuss the situation and confirm whether a virtual session is appropriate before booking."),
    ("Where will my dog stay?", "Dogs live and learn in Jacob’s real home environment in Parrish rather than a kennel facility."),
    ("Who works with my dog?", "Jacob personally trains and cares for every dog throughout the board-and-train program."),
    ("Do age and breed matter?", "They are part of the fit conversation, along with training history, health, behavior and household goals. Include those details when you reach out."),
    ("What about reactivity, anxiety or aggression?", "Behavior history should be discussed candidly, including fear, aggression, reactivity or bite history. Jacob can explain what information is needed before recommending a next step."),
    ("Do you use e-collars or balanced training methods?", "Yes—Jacob’s approach combines voice, leash cues, hand signals and properly conditioned e-collar work as part of a balanced training method. This is discussed and agreed to as part of the program terms before training begins."),
    ("What should I expect on format and pricing?", "These are immersive board-and-train programs in a real home environment, with handover and ongoing support. Current fit, availability and program details are discussed during a consultation."),
]

# ---------------------------------------------------------------- shared chrome
def btn(href, label, cls=""):
    return f'<a class="btn {cls}" href="{href}">{E(label)}{ARROW}</a>'


def head(title, desc, path, extra="", embed=False):
    sc = '<script src="https://link.msgsndr.com/js/form_embed.js" defer></script>' if embed else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{A(desc)}">
<link rel="canonical" href="{DOMAIN}{path}"><meta name="theme-color" content="#f6f3ec">
<meta property="og:title" content="{A(title)}"><meta property="og:description" content="{A(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:image" content="{DOMAIN}/assets/img05.jpg">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>document.documentElement.classList.add('js')</script>
{FONTS}<link rel="stylesheet" href="/styles.css">{extra}{sc}</head><body>'''


def header(cur=""):
    def a(h, t, k=None):
        return f'<a href="{h}"{" aria-current=page" if k == cur else ""}>{t}</a>'
    sub = "".join(f'<a href="/{p["slug"]}">{E(p["nav"])}</a>' for p in PROGRAMS)
    links = (a("/", "Home", "home") +
             f'<span class="dd"><a href="/programs"{" aria-current=page" if cur in ("programs",) else ""}>Programs</a><span class="sub">{sub}</span></span>' +
             a("/service-areas", "Service Areas", "areas") + a("/about-jacob", "About Jacob", "about") + a("/contact", "Contact", "contact"))
    drawer = "".join(f'<a href="{h}">{t}</a>' for h, t in [("/", "Home"), ("/programs", "Programs")]) + \
             "".join(f'<a class="s" href="/{p["slug"]}">{E(p["nav"])}</a>' for p in PROGRAMS) + \
             "".join(f'<a href="{h}">{t}</a>' for h, t in [("/service-areas", "Service Areas"), ("/about-jacob", "About Jacob"), ("/contact", "Contact")])
    return f'''<a class="skip" href="#main">Skip to content</a><div class="progress" aria-hidden="true"><i></i></div>
<header class="header" id="top"><div class="pill"><a href="/" class="brand" aria-label="Gator Alley Dog Training home"><img src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356"></a>
<nav class="nav" aria-label="Main">{links}</nav>{btn("/contact", "Request a consultation", "sm")}
<button class="menu-btn" aria-label="Menu" aria-expanded="false"><i></i></button></div></header>
<div class="drawer">{drawer}{btn("/contact", "Request a consultation")}</div>'''


def footer_links():
    towns = "".join(f'<li><a href="/{AREAS_LOCAL[k]["slug"]}">{E(AREAS_LOCAL[k]["town"])}</a></li>' for k in AREA_ORDER)
    helps = "".join(f'<li><a href="/{p["slug"]}">{E(PROBLEM_LABELS[p["slug"]])}</a></li>' for p in PROBLEMS)
    specs = "".join(f'<li><a href="/{l["slug"]}">{E(LANDING_LABEL[l["slug"]])}</a></li>' for l in LANDINGS)
    return (f'<div class="foot-areas"><div><h4>Dog training near you</h4><ul class="cols">{towns}<li><a href="/service-areas">All service areas</a></li></ul></div>'
            f'<div><h4>Help with common problems</h4><ul class="cols">{helps}</ul></div>'
            f'<div><h4>Programs by need and location</h4><ul class="cols">{specs}</ul></div></div>')


def footer():
    return f'''<footer class="foot"><div class="wrap"><div class="foot-grid">
<div><img src="/assets/logo.png" alt="Gator Alley Dog Training Academy" width="739" height="356" loading="lazy"><p>Dog training in Parrish, Florida · Serving board-and-train clients nationwide</p><p style="margin-top:12px">Gator Alley Dog Training Academy, LLC · {ADDR}</p></div>
<div><h4>Explore</h4><ul><li><a href="/">Home</a></li><li><a href="/programs">Programs</a></li><li><a href="/about-jacob">About Jacob</a></li><li><a href="/contact">Contact</a></li></ul></div>
<div><h4>Programs</h4><ul>{"".join(f'<li><a href="/{p["slug"]}">{E(p["nav"])}</a></li>' for p in PROGRAMS)}</ul></div>
<div><h4>Get in touch</h4><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li>Wed–Sun, 9 AM–8 PM</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{IG}" rel="noopener">Instagram</a> · <a href="{FB}" rel="noopener">Facebook</a></li><li><a href="/contact">Request a consultation</a></li></ul></div>
</div>{footer_links()}<div class="legal"><span>© Gator Alley Dog Training Academy, LLC · <a href="https://k9pn.com" title="Dog trainer websites, CRM and SEO by K9PN">Dog Trainer Websites by K9PN</a></span><a href="#top">Back to top ↑</a></div></div></footer>
<div class="mbar"><a href="tel:{TEL}">Call</a><a href="/contact" class="go">Request a consultation</a></div>
<script src="/script.js" defer></script></body></html>'''


def form_embed():
    return (f'<div class="embed"><iframe src="https://api.leadconnectorhq.com/widget/form/{FORM_ID}" id="inline-{FORM_ID}" title="Request a consultation with Gator Alley Dog Training" '
            f'style="width:100%;height:240px;border:none;border-radius:6px" data-layout="{{\'id\':\'INLINE\'}}" data-trigger-type="alwaysShow" data-activation-type="alwaysActivated" '
            f'data-form-name="Gator Alley consultation form" data-form-id="{FORM_ID}"></iframe></div>')


def booking_embed():
    return (f'<div class="embed"><iframe src="https://api.leadconnectorhq.com/widget/booking/{BOOK_ID}" id="{BOOK_ID}_booking" scrolling="no" '
            f'title="Book a consultation with Gator Alley Dog Training" style="width:100%;min-height:760px;border:none;overflow:hidden;border-radius:6px"></iframe></div>')


def schema(extra=""):
    return f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","@id":"{DOMAIN}/#business","name":"Gator Alley Dog Training","legalName":"Gator Alley Dog Training Academy, LLC","url":"{DOMAIN}/","telephone":"{TEL}","email":"{EMAIL}","image":"{DOMAIN}/assets/img05.jpg","address":{{"@type":"PostalAddress","streetAddress":"10328 Charlotte Dr","addressLocality":"Parrish","addressRegion":"FL","postalCode":"34219","addressCountry":"US"}},"areaServed":{json.dumps(AREAS)},"sameAs":["{IG}","{FB}"],"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"16"}}}}</script>{extra}'''


def faq_ld(items):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}) + "</script>"


def proof_strip():
    items = ["Puppy Head Start", "Basic Obedience", "Advanced &amp; Off-Leash", "Behavior Modification", "Puppy Raise &amp; Train", "Virtual Coaching", "Real home, not a kennel", "Personally led by Jacob"]
    r = "".join(f"<span>{i}</span>" for i in items)
    return f'<div class="proof" aria-hidden="true"><div class="row">{r}{r}</div></div>'


def eyebrow(t):
    return f'<div class="status">{E(t)}</div>'


def faq_html(items):
    return "".join(f'<details class="rv"><summary>{E(q)}<span class="pm"></span></summary><div class="ans"><p>{E(a)}</p></div></details>' for q, a in items)


def trio(items, cls=""):
    return f'<div class="trio {cls}">' + "".join(f'<div class="rv" data-d="{i*100}"><h3>{E(t)}</h3><p>{E(p)}</p></div>' for i, (t, p) in enumerate(items)) + "</div>"


def steps_html(items, tight=True, num=True):
    s = "".join(f'<div class="step"><span class="n">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(p)}</p></div>' for i, (t, p) in enumerate(items))
    return f'<div class="steps{" tight" if tight else ""}">{s}</div>'


def section_head(eb, h2, p="", tag="h2"):
    pp = f'<p class="rv" data-d="100">{E(p)}</p>' if p else ""
    return f'<div class="sec-head"><div class="rv">{eyebrow(eb)}<h2>{E(h2)}</h2></div>{pp}</div>'


def pfig(name, alt, wide=False):
    w, h = ar(name)
    return f'<figure class="pf{" wide" if wide else ""}" style="aspect-ratio:{w}/{h}">{img(name, alt, eager=True).replace("loading=\"lazy\" decoding=\"async\"", "")}</figure>'


def hero_block(eb, h1, lede, ctas, fig):
    return (f'<section class="phero"><div class="wrap hero-grid"><div><div class="status fade">{E(eb)}</div>'
            f'<h1><span class="ln"><span>{E(h1)}</span></span></h1><p class="lede fade" style="margin:26px 0 32px">{E(lede)}</p>'
            f'<div class="cta-row fade">{ctas}</div></div>{fig}</div></section>')


def split_photo(eb, h2, paras, name, alt, rev=False, cls=""):
    ps = "".join(f"<p>{E(p)}</p>" for p in paras)
    return (f'<section class="section {cls}"><div class="wrap story-grid{" rev" if rev else ""}"><div class="rv">{eyebrow(eb)}<h2>{E(h2)}</h2>{ps}</div>'
            f'<div class="photo rv" data-d="100" style="aspect-ratio:{"/".join(map(str, ar(name)))}">{img(name, alt)}</div></div></section>')


# ---------------------------------------------------------------- pages
def home():
    cards = ""
    for p in PROGRAMS:
        n, alt = p["card"]
        w, h = ar(n)
        cards += (f'<a class="pcard rv" href="/{p["slug"]}"><div class="pph" style="aspect-ratio:{w}/{h}"><img src="/assets/{n}" alt="{A(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
                  f'<div class="pbody"><span class="meta">{E(p["track"])} · {E(p["tag"])}</span><h3>{E(p["name"])}</h3><p>{E(p["blurb"])}</p><span class="more-l">{E(p["cta"])} {ARROW_SVG}</span></div></a>')
    cap = [("img03.jpg", "Jacob Soos giving a hand-signal cue to a German Shepherd during training", "Hand signals and verbal cues layered together during an obedience session."),
           ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator", "Jacob and Chloe with Gator — the same balanced approach used with client dogs."),
           ("img05.jpg", "German Shepherd walking a path in Parrish, Florida", "Real-world reliability, practiced outside the training space.")]
    media = "".join(photo(n, a, c, d=i * 100) for i, (n, a, c) in enumerate(cap))
    w01, h01 = ar("img01.jpg")
    return head("Dog Trainer in Parrish, FL | Gator Alley Dog Training",
                "Obedience, board-and-train, and behavior programs in Parrish, FL from Gator Alley Dog Training. Serving Bradenton & Sarasota. Free consultations available.",
                "/", schema(faq_ld(HOME_FAQ)), embed=True) + header("home") + f'''
<main id="main">
<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><div class="status fade">Dog training in Parrish, Florida</div>
<h1><span class="ln"><span>Reliable</span></span><span class="ln"><span>obedience built</span></span><span class="ln"><span>for <em>real life.</em></span></span></h1>
<p class="lede fade">Gator Alley Dog Training offers personally led board-and-train programs for owners who want calm, trustworthy and obedient dogs.</p>
<div class="cta-row fade"><a class="btn" href="#consult">Free Consultation{ARROW}</a><a class="btn ghost" href="#book-consultation">Book Phone Consultation</a></div>
<a class="rating fade" href="{GOOGLE}" rel="noopener"><span class="g">G</span><div><b>5.0</b> <span class="stars">★★★★★</span><br><small>Google reviews · 16 reviews</small></div></a></div>
<figure class="pf" style="aspect-ratio:{w01}/{h01}"><img src="/assets/img01.jpg" alt="Jacob Soos and Chloe walking their dogs in Parrish, Florida" width="{w01}" height="{h01}" fetchpriority="high"></figure></div></section>
{proof_strip()}
<section class="section consult" id="consult"><div class="wrap contact-grid"><div class="rv">{eyebrow("Free consultation")}<h2>Free Consultation</h2><p class="lede">Tell us about you and your dog — we’ll follow up shortly.</p>
<div class="ways"><a href="tel:{TEL}">{PHONE_IC}{PHONE}</a></div></div><div class="rv" data-d="120">{form_embed()}</div></div></section>
<section class="section" id="programs"><div class="wrap">{section_head("Gator Alley board & train", "Four clear paths. One goal: a better life with your dog.", "Every Gator Alley program is structured around your dog’s history, home life, and training goals. The work is personally led by Jacob in a real home environment, with focused training, practical routines, and a clear owner handoff so progress can carry into everyday life.")}
<div class="pgrid">{cards}</div>
<a class="virtual rv" href="/programs#virtual-coaching"><div><div class="status inv">New — one-on-one, from anywhere</div><h3>Can't make it to Parrish? Train with Jacob over Zoom.</h3><p>Live virtual coaching sessions for dog owners who want one-on-one help with a specific topic — leash manners, puppy foundations, or behavior and consistency. Each session is held over Zoom and recorded for you to keep.</p></div><span class="btn">See Virtual Coaching Sessions{ARROW}</span></a></div></section>
<section class="section local"><div class="wrap">{section_head("Parrish dog training for real-life goals", "From puppy foundations to more complicated behavior histories.", "Owners in Parrish and nearby communities often start with a practical question: how do we make everyday life with our dog feel calmer, clearer and more manageable? Bring the full picture to the consultation so Jacob can discuss the right next step.")}
{trio([("Puppy foundations", "If you are raising a puppy, share your goals around socialization, household manners, leash skills, recall and building good habits early. Jacob can discuss whether one of the current programs fits your dog and your timeline."), ("Common obedience challenges", "Leash pulling, jumping, barking, inconsistent recall and difficulty settling can make normal routines feel exhausting. Clear communication and real-world practice are part of the conversation."), ("Behavior-history cases", "Reactivity, anxiety, fear, aggression or a bite history need honest context and careful planning. Share what has happened, where it happens and what safety considerations matter at home.")])}
<p class="note rv">These are common goals owners bring to a consultation, not a promise of an instant fix or a separate service menu.</p></div></section>
<section class="section statement"><div class="wrap"><div class="rv">{eyebrow("Is this you?")}</div><h2 class="big rv">When everyday dog life feels harder than it should.</h2><p class="lede rv" style="margin:-20px 0 52px">Maybe walks are stressful, guests bring out jumping or barking, recall feels unreliable, or you’re not sure how to help a puppy build good foundations. You’re not looking for a gimmick—you want a clearer plan and support that fits your household.</p>
<div class="worries"><blockquote class="rv"><q>“I love my dog, but I feel overwhelmed.”</q><span>Training should make daily life more manageable, not leave you guessing what to do next.</span></blockquote>
<blockquote class="rv" data-d="100"><q>“The behavior changes depending on the situation.”</q><span>Real-world routines and distractions matter. The goal is usable communication beyond a quiet training space.</span></blockquote>
<blockquote class="rv" data-d="200"><q>“I want my family to feel confident.”</q><span>Clear handover guidance helps owners continue the work consistently once their dog returns home.</span></blockquote></div></div></section>
<section class="section method"><div class="wrap method-grid"><div class="sticky"><div class="rv">{eyebrow("A simple path forward")}</div><h2 class="rv">Book. Train. Thrive.</h2><p class="rv" data-d="100">Every conversation begins with your dog’s needs, your goals and the right fit—not a one-size-fits-all promise.</p></div>
{steps_html([("Book", "Share what is happening at home and speak directly with Jacob about your goals."), ("Train", "Your dog receives personally led work, structure and real-world exposure in the appropriate program."), ("Thrive", "Use the handover and ongoing support to carry clearer communication into everyday life.")], tight=False)}</div></section>
<section class="section"><div class="wrap">{section_head("More from the program", "Real sessions, real dogs, real Parrish backyards.")}<div class="media3">{media}</div></div></section>
<section class="section difference"><div class="wrap jacob-grid"><div class="photo rv" style="aspect-ratio:{"/".join(map(str, ar("img06.jpg")))};max-width:560px">{img("img06.jpg", "Jacob Soos working obedience with his German Shepherd")}</div>
<div class="rv" data-d="100">{eyebrow("The Gator Alley difference")}<h2>Real-world exposure. Personal care. Clear standards.</h2>
<p>Dogs live and learn in a real home environment, not a facility. Jacob personally works with each dog through the routines, people and distractions that make reliable behavior matter.</p>
<p style="margin-top:28px">{btn("/about-jacob", "Meet Jacob")}</p></div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="google rv"><div class="score">5.0</div><div>{eyebrow("Proof from the program")}<h3>Real work deserves real stories.</h3><p class="muted" style="margin-top:10px">Client success stories coming after approval</p></div><a class="btn ghost" href="{GOOGLE}" rel="noopener">Google reviews · 16 reviews{ARROW}</a></div></div></section>
<section class="section" id="faq" style="padding-top:0"><div class="wrap faq-grid"><div class="rv">{eyebrow("Frequently asked questions")}<h2>What to know before you call.</h2></div><div>{faq_html(HOME_FAQ)}</div></div></section>
<section class="section area" id="area" style="padding-top:0"><div class="wrap story-grid"><div class="rv">{eyebrow("Serving Parrish & nearby areas")}<h2>Dog training that starts in Parrish and travels home with you.</h2></div>
<div class="rv" data-d="100"><p>Gator Alley Dog Training is based in Parrish and serves owners in Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota, while also welcoming board-and-train clients from around the country. The page is local by design: the conversation starts with your dog's actual routines, behavior history and household goals, not a generic city-page promise.</p><p style="margin-top:28px">{btn("/contact", "Talk with Jacob")}</p></div></div></section>
{links_block()}
<section class="section contact" id="book-consultation"><div class="wrap contact-grid"><div class="rv">{eyebrow("Book your free consultation")}<h2>Pick a time that works — Jacob will confirm personally.</h2><p class="lede">Available Wednesday through Sunday, 9 AM–7 PM Eastern, in 30-minute slots. Prefer to talk first? Call <a href="tel:{TEL}">{PHONE}</a>.</p></div><div class="rv" data-d="120">{booking_embed()}</div></div></section>
</main>''' + footer()


def program_page(p):
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Service", "name": p["name"], "provider": {"@id": f"{DOMAIN}/#business"}, "areaServed": AREAS, "description": p["blurb"]}) + "</script>" + faq_ld(p["faq"])
    first = p["imgs"][0]
    fig = pfig(first[0], first[1])
    intro = "".join(f"<p>{E(t)}</p>" for t in p["intro"])
    focus = "".join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg><span>{E(f)}</span></li>' for f in p["focus"])
    loc = "".join(f"<p>{E(t)}</p>" for t in p["local"])
    second = ""
    if len(p["imgs"]) > 1:
        n, alt = p["imgs"][1]
        second = f'<section class="section" style="padding-top:0"><div class="wrap"><div class="photo wide rv" style="aspect-ratio:{"/".join(map(str, ar(n)))}">{img(n, alt)}</div></div></section>'
    return head(p["title"], p["desc"], f'/{p["slug"]}', schema(ld)) + header("programs") + f'''
<main id="main">{hero_block(f'{p["track"]} · {p["tag"]} · Gator Alley Dog Training · Parrish, Florida', p["h1"], p["lede"], btn("/contact", "Request a consultation"), fig)}
{proof_strip()}
<section class="section"><div class="wrap split"><div class="rv">{eyebrow("Gator Alley Dog Training")}<h2>Training built around real life.</h2><div class="prose">{intro}</div></div>
<div class="rv" data-d="100"><h3>Program focus</h3><ul class="fit">{focus}</ul></div></div></section>
<section class="section local"><div class="wrap story-grid"><div class="rv"><h2>Dog training for Parrish-area families.</h2></div><div class="rv prose" data-d="100">{loc}</div></div></section>
<section class="section difference"><div class="wrap story-grid"><div class="rv"><h3>Real-world exposure. Personal care. Clear standards.</h3></div><div class="rv prose" data-d="100"><p>{E(p["diff"])}</p><p style="margin-top:24px"><a class="tlink" href="/about-jacob">Meet Jacob →</a></p></div></div></section>
<section class="section method"><div class="wrap method-grid"><div class="sticky"><h2 class="rv">{E(p["how"])}</h2></div>{steps_html(p["steps"])}</div></section>
{second}
<section class="section" id="faq"><div class="wrap faq-grid"><div class="rv"><h2>Questions before you reach out.</h2><p class="lede" style="margin-top:20px">A few things owners usually ask before their consultation.</p></div><div>{faq_html(p["faq"])}</div></div></section>
{service_links(p)}
{links_block()}
<section class="section contact"><div class="wrap story-grid"><div class="rv"><h2>Talk with Jacob about your dog.</h2></div><div class="rv" data-d="100"><p class="lede">Share your dog’s age, breed, training history and goals so the right next step can be discussed.</p><p style="margin-top:28px">{btn("/contact", "Request a consultation")}</p></div></div></section>
</main>''' + footer()


def programs():
    cards = ""
    for p in PROGRAMS:
        n, alt = p["card"]
        w, h = ar(n)
        cards += (f'<a class="pcard rv" href="/{p["slug"]}"><div class="pph" style="aspect-ratio:{w}/{h}"><img src="/assets/{n}" alt="{A(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
                  f'<div class="pbody"><span class="meta">{E(p["track"])}{" · " + E(p["tag"].upper()) if p["tag"].endswith("weeks") else ""}</span><h3>{E(p["name"])}</h3></div></a>')
    gal = [("img09.jpg", "Dogs practicing calm impulse control inside a home in Parrish, Florida", "Home-based impulse-control practice for calm behavior in Parrish, FL."),
           ("img10.jpg", "Dogs practicing socialization and impulse control outdoors in Parrish, Florida", "Outdoor socialization and impulse-control work around other dogs in Parrish."),
           ("img11.jpg", "Dogs holding a down command during neighborhood obedience training in Parrish, Florida", "Neighborhood obedience training and dependable down-stays in Parrish, FL."),
           ("img12.jpg", "Jacob Soos with a young dog during puppy training in Parrish, Florida", "Personally led puppy training with Jacob Soos in Parrish."),
           ("img13.jpg", "Young puppy practicing leash skills during puppy training in Parrish, Florida", "Puppy leash skills and confidence-building in a Parrish neighborhood.")]
    gal_html = "".join(photo(n, a, c, d=i * 60) for i, (n, a, c) in enumerate(gal))
    hw = ar("prog-programs-hero.jpg")
    return head("Board & Train + Virtual Coaching in Parrish, FL | Gator Alley",
                "Custom board & train, puppy programs and live virtual coaching for dog owners in Parrish, FL and beyond. Personally trained by Jacob Soos.",
                "/programs", schema(faq_ld(PROG_FAQ))) + header("programs") + f'''
<main id="main">{hero_block("Board & Train in Parrish, FL", "Board-and-train programs for dependable real-world behavior.", "Choose the level of support that matches your dog’s needs, then speak directly with Jacob about the right fit.", btn("/contact", "Book a free call"), pfig("prog-programs-hero.jpg", "Jacob Soos with his German Shepherd, Gator Alley Dog Training", wide=True))}
{proof_strip()}
<section class="section"><div class="wrap split"><div class="rv">{eyebrow("Flagship program")}<h2>Custom Board &amp; Train</h2></div><div class="rv prose" data-d="100"><p>Every dog that comes through Gator Alley is different, so the program is built around the dog and the owner’s goals instead of a one-size-length package. Jacob starts with a consultation, identifies what’s really going on, and tailors the plan and the length of stay to match — whether that’s foundational obedience, a specific behavioral issue, or a puppy just starting out.</p></div></div></section>
<section class="section local"><div class="wrap">{section_head("Four training tracks", "Dog training programs for Parrish and nearby Florida families.", "Choose the track that best reflects your dog’s age, behavior history, and goals. Jacob discusses the right fit with owners from Parrish, Palmetto, Ellenton, Bradenton, Lakewood Ranch, and Sarasota.")}
<div class="pgrid">{cards}</div>
<div class="split two rv" style="margin-top:56px"><div class="prose"><p><strong>Flexible length, matched to the goal.</strong> The length of stay isn’t fixed in advance — it’s set after the consultation, based on what the dog needs and the outcome the owner wants. A dog working on basic manners may need less time than a dog working through significant reactivity or behavioral issues. This is explained to every owner up front once Jacob has assessed the dog.</p></div>
<div class="prose"><p><strong>Built for every dog and every issue.</strong> This program is open to all breeds, ages and temperaments — from a well-adjusted dog that just needs polish, to a dog with real behavioral or reactivity challenges. Jacob personally handles every dog and adjusts his methods to what that dog responds to.</p><p style="margin-top:24px">{btn("/contact", "Ask about Board & Train")}</p></div></div></div></section>
<section class="section"><div class="wrap story-grid"><div class="rv">{eyebrow("New program")}<h2>Puppy Head Start Program</h2><div class="prose"><p><strong>2 weeks, designed specifically for puppies.</strong> This is a shorter, focused board-and-train built to give a young puppy the best possible start before habits — good or bad — become set.</p>
<h3 style="margin:34px 0 4px">What’s covered in 2 weeks</h3>
<ul class="fit"><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg><span><strong>Basic obedience</strong> — sit, stay, place, name recognition and leash manners, introduced the right way for a young dog’s attention span.</span></li>
<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg><span><strong>Potty training</strong> — a consistent schedule and structure so the puppy goes home with reliable house-training habits already in place.</span></li>
<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg><span><strong>Exposure training</strong> — controlled introductions to new people, sounds, surfaces, and everyday situations so the puppy builds confidence instead of fear or overreaction as it grows.</span></li></ul>
<p style="margin-top:24px">Owners get a walkthrough at pickup on how to keep the routine going at home, so the two weeks of work keeps paying off long after the puppy leaves.</p><p style="margin-top:28px">{btn("/contact", "Ask about Puppy Head Start")}</p></div></div>
<div class="photo rv" data-d="100" style="aspect-ratio:{"/".join(map(str, ar("prog-puppy-leash-wide.jpg")))}">{img("prog-puppy-leash-wide.jpg", "Young puppy practicing leash skills during puppy training in Parrish, Florida")}</div></div></section>
<section class="section local"><div class="wrap story-grid"><div class="photo rv" style="aspect-ratio:{"/".join(map(str, ar("img03.jpg")))}">{img("img03.jpg", "Jacob Soos using a hand signal with a German Shepherd during training")}</div><div class="rv" data-d="100">{eyebrow("How Jacob communicates with your dog")}<h2>Full-spectrum communication, built for reliability.</h2><p>Jacob’s approach uses voice commands, leash cues, hand signals and properly conditioned e-collar work together, so your dog understands what is being asked in any environment—not just inside a quiet training space. Training is balanced: clear communication, positive reinforcement, structure, fair corrections and accountability, tailored to each individual dog.</p></div></div></section>
<section class="section"><div class="wrap">{trio([("Voice & hand signals", "Verbal commands and hand signals build the foundation for clear, consistent communication in everyday household situations."), ("Leash pressure & structure", "Leash work and daily structure build dependable obedience that carries over into real walks, guests and distractions."), ("Conditioned e-collar work", "For dogs ready for it, properly conditioned e-collar work supports off-leash reliability and real-world control. This is discussed and agreed to as part of the program terms.")])}</div></section>
<section class="section local"><div class="wrap">{section_head("Bring the real-life details", "What should Parrish-area owners discuss with Jacob?", "The consultation is the place to explain the behavior you are seeing and the life you want to share with your dog. That may include puppy foundations, leash pulling, jumping, barking, poor recall, reactivity, anxiety or another behavior-history concern.")}
{trio([("Foundations and manners", "Talk through your puppy or young dog's routines, socialization goals, household expectations and early obedience questions."), ("Everyday obedience", "Describe where communication breaks down: walks, guests, settling, recall, distractions or consistency between family members."), ("Behavior context", "For reactivity, fear, aggression or a bite history, honest detail helps Jacob determine whether a consultation and current program are an appropriate fit.")])}
<p class="note rv">Gator Alley is based in Parrish and speaks with owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota. Nearby-area language supports discovery; it is not a ranking promise.</p></div></section>
<section class="section"><div class="wrap">{section_head("Why board & train works", "Clear communication, real-world exposure and personal care.")}
{trio([("Balanced training", "The balanced approach combines clear communication, positive reinforcement, structure, fair corrections and accountability. Training is tailored to each dog using appropriate methods and tools to build confidence, obedience and reliable behavior in the real world."), ("Real-world exposure", "Your dog lives in Jacob’s home—not a facility—and trains in the environments that matter most. Household routines, public settings and everyday distractions build behavior you can use at home in Parrish and beyond."), ("Jacob trains every dog", "Every dog is personally trained and cared for by Jacob. Your dog is never passed to inexperienced staff or unfamiliar trainers; you know who is responsible for training, care, safety and progress.")])}</div></section>
<section class="section difference"><div class="wrap jacob-grid"><div class="rv">{eyebrow("Training that transfers home")}<h2>Built for daily life in Parrish and the surrounding communities.</h2>
<p>Gator Alley Dog Training is based in Parrish and serves dog owners from Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota, while also welcoming board-and-train clients from around the country.</p><p>At the end of the program, Jacob provides a detailed handover and ongoing support so owners can continue the dog’s progress at home.</p><p style="margin-top:28px">{btn("/contact", "Request a consultation")}</p></div>
<div class="photo rv" data-d="100" style="aspect-ratio:{"/".join(map(str, ar("img06.jpg")))};max-width:520px">{img("img06.jpg", "Jacob Soos working obedience with his German Shepherd")}</div></div></section>
<section class="section local"><div class="wrap">{section_head("Dog training in Parrish, Florida", "Impulse control, puppy training and obedience for real life.", "Gator Alley’s Parrish dog-training programs build practical behavior around the routines and environments that matter after dogs return home—from settling indoors to neighborhood obedience and puppy leash work.")}<div class="gal">{gal_html}</div></div></section>
<section class="section method" id="virtual-coaching"><div class="wrap">{section_head("New — one-on-one, from anywhere", "Virtual Coaching Sessions", "Jacob now also offers live virtual coaching for dog owners in Parrish and beyond — one-on-one sessions held over Zoom, built around whatever you're working through with your dog. Each session is recorded and given to you afterward to keep, plus follow-up support to keep practicing between conversations.")}
{trio([("Leash manners & recall", "Talk through walks, pulling, coming when called and how to practice around real distractions."), ("Puppy foundations", "Work through household routines, early manners, exposure goals and the questions that come with a young dog."), ("Behavior & consistency", "Discuss barking, settling, reactivity or a training plan that feels hard to keep consistent at home.")], cls="inv")}
<p class="rv" style="margin:32px 0 64px;color:#cfe0d8;max-width:46em">These are examples, not a fixed menu — bring the question you're stuck on. For serious safety concerns (bite history, significant aggression), Jacob will first discuss whether a virtual session is the right fit.</p>
<div class="vsteps">{steps_html([("Share what you need", "Tell Jacob what's happening, what you've tried and what you'd like to change. The session is planned around those priorities."), ("Meet over Zoom", "Work one-on-one through the topic you brought, with instruction tailored to your dog and your home. The session is recorded so you can rewatch it."), ("Keep learning afterward", "Get instructional videos connected to what you covered, then use follow-up support to ask questions and check on progress.")])}</div>
<p class="rv" style="margin-top:56px;color:#cfe0d8;max-width:46em">Sessions are held over Zoom, and you get the recording afterward to keep. To be confirmed by Jacob: price, session length, availability and how many follow-ups are included. This section describes the concept; exact terms will be added once he confirms them.</p></div></section>
<section class="section" id="faq"><div class="wrap faq-grid"><div class="rv">{eyebrow("Questions about the programs")}<h2>Before you choose a program.</h2></div><div>{faq_html(PROG_FAQ)}</div></div></section>
<section class="section contact"><div class="wrap story-grid"><div class="rv">{eyebrow("Join the pack")}<h2>Tell Jacob what you want to change.</h2></div><div class="rv" data-d="100"><p class="lede">Share your dog’s age, breed, biggest challenge and training goals to begin the conversation.</p><p style="margin-top:28px">{btn("/contact", "Book a free call")}</p></div></div></section>
{links_block()}
</main>''' + footer()


def about():
    gal = [("img17.jpg", "Portrait of Jacob Soos outdoors in Parrish, Florida", "Jacob Soos, owner and trainer at Gator Alley Dog Training."),
           ("img18.jpg", "Jacob, Chloe and their dog walking together", "Jacob and Chloe on an evening walk with their dog."),
           ("img19.jpg", "Two German Shepherds resting near a boat", "Down time between sessions — the dogs Jacob works with every day.")]
    media = "".join(photo(n, a, c, d=i * 100) for i, (n, a, c) in enumerate(gal))
    return head("Meet Jacob Soos, Dog Trainer in Parrish, FL | Gator Alley",
                "Jacob Soos is a professional dog trainer serving Parrish, FL and the Bradenton-Sarasota area, specializing in advanced obedience and off-leash reliability.",
                "/about-jacob", schema()) + header("about") + f'''
<main id="main">{hero_block("Meet your trainer", "Jacob Soos, dog trainer in Parrish, Florida.", "Gator Alley Dog Training is built around patient, consistent work and clearer communication between dogs and their families.", btn("/contact", "Talk with Jacob"), pfig("img14.jpg", "Jacob Soos serving in the United States Coast Guard"))}
{proof_strip()}
{split_photo("From Palmetto to Parrish", "A lifelong respect for dogs—and the work behind their behavior.", ["Born and raised in Palmetto, Florida, Jacob grew up around dogs, including dogs with challenging behaviors. His training approach was shaped by years of learning how patience, consistency and clear communication change a dog’s relationship with its owner.", "While serving in the U.S. Coast Guard along the Mississippi Gulf Coast, Jacob began training dogs to build experience and deepen that knowledge. Today he lives in Parrish with his wife and high-school sweetheart, Chloe, their German Shepherd Gator, and their cats Guru and Goose."], "img06.jpg", "Jacob Soos working obedience with his German Shepherd")}
{split_photo("A home environment", "Your family becomes part of ours.", ["During Board & Train, dogs live and learn in a real home environment—not a kennel. Daily structure, socialization and individualized work prepare them for the household routines and distractions that matter after they go home.", "Every program ends with a detailed handover session and ongoing support so owners can confidently continue their dog’s progress."], "img01.jpg", "Jacob and Chloe walking dogs in Parrish, Florida", rev=True, cls="local")}
{split_photo("Five years in the U.S. Coast Guard", "Discipline learned on the water, applied on the leash.", ["Jacob served five years in the U.S. Coast Guard as a Boatswain's Mate Second Class, including search-and-rescue, law-enforcement missions and hurricane response along the Mississippi Gulf Coast. The same structure, calm and follow-through carries directly into how he trains dogs today."], "img16.jpg", "Jacob Soos in U.S. Coast Guard uniform holding service paperwork", cls="method")}
<section class="section"><div class="wrap">{section_head("More of the story", "Palmetto roots, Coast Guard discipline, Parrish home.")}<div class="media3">{media}</div></div></section>
<section class="section local"><div class="wrap">{section_head("A practical training philosophy", "Clear communication has to work in the places real life happens.", "Jacob's work is centered on helping owners understand what their dog is communicating, what the household needs to change and how to continue the work after handover. That can mean discussing puppy foundations, common obedience challenges or a more complicated behavior history before deciding which path is appropriate.")}
{trio([("Start with context", "Age, breed, routines, environment and past behavior all matter. A useful consultation begins with the details, not a one-size-fits-all promise."), ("Practice in the real world", "Home routines, people, other pets and everyday distractions are part of why the program uses a real home environment rather than a kennel facility."), ("Carry it home", "The handover and ongoing support are designed to help owners continue clear, consistent communication after their dog returns home.")])}
<p class="note rv">Gator Alley is based in Parrish and serves nearby owners in Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota, with nationwide board-and-train availability as secondary positioning.</p></div></section>
</main>''' + footer()


def contact_page():
    return head("Contact Gator Alley Dog Training | Parrish, FL",
                "Reach Gator Alley Dog Training in Parrish, FL for a free consultation. Call, email, or fill out the form to start your dog's training plan today.",
                "/contact", schema(), embed=True) + header("contact") + f'''
<main id="main">{hero_block("Request a consultation", "Start the conversation about your dog.", "Tell Jacob what is going on, the goals you have and which board-and-train program you are considering. Puppy foundations, common obedience challenges and behavior-history cases are all useful context to include.", f'<a class="btn" href="tel:{TEL}">{PHONE}{ARROW}</a><span class="hrs">Wed–Sun, 9 AM–8 PM</span>', pfig("img01.jpg", "Jacob Soos and Chloe walking with their dogs in Parrish, Florida"))}
{proof_strip()}
<section class="section contact" id="consult"><div class="wrap contact-grid"><div class="rv">{eyebrow("Consultation request")}<h2>How can we help?</h2><div class="ways" style="margin-top:28px"><a href="tel:{TEL}">{PHONE_IC}{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div></div><div class="rv" data-d="120">{form_embed()}</div></div></section>
<section class="section contact" id="book-consultation"><div class="wrap contact-grid"><div class="rv">{eyebrow("Book your free consultation")}<h2>Pick a time that works — Jacob will confirm personally.</h2><p class="lede">Available Wednesday through Sunday, 9 AM–7 PM Eastern, in 30-minute slots. Prefer to talk first? Call <a href="tel:{TEL}">{PHONE}</a>.</p></div><div class="rv" data-d="120">{booking_embed()}</div></div></section>
<section class="section"><div class="wrap story-grid"><div class="rv">{eyebrow("Parrish dog training")}<h2>Based in Parrish. Serving nearby owners and board-and-train clients nationwide.</h2></div><div class="rv" data-d="100"><p>Gator Alley Dog Training is located at {ADDR}. Service conversations commonly begin with owners from Parrish, Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota.</p><p class="note"><strong>Important:</strong> Reach out before visiting. This is a training business, not a walk-in storefront.</p></div></div></section>
<section class="section local"><div class="wrap">{section_head("Help Jacob understand the fit", "The more context you share, the more useful the first conversation can be.")}
{trio([("Your dog's profile", "Include age, breed, health considerations, training history and the routines that matter most in your home."), ("The challenge", "Share examples of leash pulling, jumping, barking, poor recall, reactivity, anxiety, fear, aggression or other behavior concerns."), ("Your location and goals", "Let Jacob know whether you are in Parrish, Palmetto, Ellenton, Bradenton, Lakewood Ranch, Sarasota or elsewhere and what you want daily life to feel like.")])}</div></section>
</main>''' + footer()


# ---------------------------------------------------------------- local SEO pages
AREA_IMG = {"parrish": ("img01.jpg", "Jacob Soos and Chloe walking with their dogs in Parrish, Florida"),
            "bradenton": ("img03.jpg", "Jacob Soos giving a hand-signal cue to a German Shepherd during obedience training"),
            "sarasota": ("img05.jpg", "German Shepherd walking a path in Parrish, Florida"),
            "lakewood-ranch": ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator"),
            "palmetto": ("img17.jpg", "Portrait of Jacob Soos outdoors in Parrish, Florida"),
            "ellenton": ("img18.jpg", "Jacob, Chloe and their dog walking together"),
            "ruskin": ("prog-programs-hero.jpg", "Jacob Soos with his German Shepherd, Gator Alley Dog Training"),
            "apollo-beach": ("img01.jpg", "Jacob Soos and Chloe walking with their dogs in Parrish, Florida"),
            "sun-city-center": ("img18.jpg", "Jacob, Chloe and their dog walking together"),
            "riverview": ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator"),
            "brandon": ("img17.jpg", "Portrait of Jacob Soos outdoors in Parrish, Florida"),
            "tampa": ("img03.jpg", "Jacob Soos giving a hand-signal cue to a German Shepherd during obedience training"),
            "st-petersburg": ("img05.jpg", "German Shepherd walking a path in Parrish, Florida"),
            "venice": ("prog-programs-hero.jpg", "Jacob Soos with his German Shepherd, Gator Alley Dog Training"),
            "north-port": ("img04.jpg", "Jacob and Chloe with their German Shepherd Gator")}

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-7"/></svg>'


def inline(t):
    out = E(t)
    parts = out.split("**")
    return "".join(f"<strong>{x}</strong>" if i % 2 else x for i, x in enumerate(parts))


def biz_ref():
    return {"@type": "LocalBusiness", "@id": f"{DOMAIN}/#business", "name": "Gator Alley Dog Training", "telephone": TEL, "url": f"{DOMAIN}/"}


def crumbs_ld(items):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p} for i, (n, p) in enumerate(items)]}) + "</script>"


def service_ld(name, desc, area=None):
    d = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Dog training", "name": name, "description": desc, "provider": biz_ref()}
    d["areaServed"] = {"@type": "City", "name": f"{area}, FL"} if area else AREAS
    return '<script type="application/ld+json">' + json.dumps(d) + "</script>"


def chips(items):
    return '<ul class="chips">' + "".join(f'<li><a href="{h}">{E(t)}</a></li>' for t, h in items) + "</ul>"


def town_items(exclude=None):
    return [(f"Dog training in {AREAS_LOCAL[k]['town']}", f"/{AREAS_LOCAL[k]['slug']}") for k in AREA_ORDER if k != exclude]


def help_items(exclude=()):
    return [(PROBLEM_LABELS[p["slug"]], f"/{p['slug']}") for p in PROBLEMS if p["slug"] not in exclude]


LANDING_LABEL = {"puppy-training-sarasota-fl": "Puppy training in Sarasota", "puppy-training-bradenton-fl": "Puppy training in Bradenton",
                 "puppy-training-tampa-fl": "Puppy training in Tampa", "board-and-train-sarasota-fl": "Board and train in Sarasota",
                 "board-and-train-tampa-fl": "Board and train in Tampa", "virtual-dog-training": "Virtual dog training over Zoom"}

# which specialty pages and problem guides belong to which service
SERVICE_RELATED = {
    "puppy-head-start": (["puppy-training-sarasota-fl", "puppy-training-bradenton-fl", "puppy-training-tampa-fl", "virtual-dog-training"],
                         ["potty-training-puppy", "crate-training-puppy", "stop-dog-jumping", "dog-pulling-on-leash"]),
    "basic-obedience": (["board-and-train-sarasota-fl", "board-and-train-tampa-fl", "virtual-dog-training"],
                        ["dog-pulling-on-leash", "stop-dog-jumping", "stop-dog-barking", "dog-wont-come-when-called"]),
    "behavioral-issues-reactivity": (["board-and-train-sarasota-fl", "board-and-train-tampa-fl", "virtual-dog-training"],
                                     ["reactive-dog-training", "dog-wont-come-when-called", "dog-separation-anxiety", "stop-dog-barking"]),
    "puppy-foundations": (["puppy-training-sarasota-fl", "puppy-training-bradenton-fl", "puppy-training-tampa-fl", "virtual-dog-training"],
                          ["potty-training-puppy", "crate-training-puppy", "dog-separation-anxiety", "stop-dog-jumping"]),
}


def landing_items(slugs=None, exclude=()):
    return [(LANDING_LABEL[l["slug"]], f"/{l['slug']}") for l in LANDINGS if (slugs is None or l["slug"] in slugs) and l["slug"] not in exclude]


def links_block(ex_town=None, ex_help=(), ex_land=()):
    return ('<section class="section local"><div class="wrap"><div class="split two rv"><div><h3>Dog training near you</h3>'
            '<p class="muted" style="margin:10px 0 0">Gator Alley is based in Parrish and serves owners across Manatee, Sarasota and Hillsborough counties.</p>' + chips(town_items(ex_town)) + '</div>'
            '<div><h3>Help with common problems</h3><p class="muted" style="margin:10px 0 0">Guides from Jacob on the issues Florida dog owners ask about most.</p>' + chips(help_items(ex_help)) + '</div></div>'
            '<div class="rv" style="margin-top:48px"><h3>Programs by need and location</h3><p class="muted" style="margin:10px 0 0">Puppy training, board and train, and live virtual coaching.</p>' + chips(landing_items(None, ex_land)) + '</div></div></section>')


def town_programs(k):
    town = AREAS_LOCAL[k]["town"]
    items = [(LANDING_LABEL[l["slug"]], f"/{l['slug']}") for l in LANDINGS if l.get("area_slug") == k]
    items += [(q["name"], f"/{q['slug']}") for q in PROGRAMS] + [("Virtual coaching over Zoom", "/virtual-dog-training")]
    return (f'<section class="section local"><div class="wrap"><div class="rv"><h3>Training programs for {E(town)} owners</h3>'
            '<p class="muted" style="margin:10px 0 0">Every program Gator Alley offers, plus live virtual coaching.</p>' + chips(items) + '</div></div></section>')


def service_links(p):
    lands, probs = SERVICE_RELATED[p["slug"]]
    others = [(q["name"], f"/{q['slug']}") for q in PROGRAMS if q["slug"] != p["slug"]]
    return ('<section class="section local"><div class="wrap"><div class="split two rv"><div><h3>' + E(p["short"]) + ' by location</h3>'
            '<p class="muted" style="margin:10px 0 0">Where this program is available and how to get started from your town.</p>' + chips(landing_items(lands)) + '</div>'
            '<div><h3>Common problems this program solves</h3><p class="muted" style="margin:10px 0 0">Jacob’s guides on the issues owners bring to this program.</p>' + chips([(PROBLEM_LABELS[r], f"/{r}") for r in probs]) + '</div></div>'
            '<div class="rv" style="margin-top:48px"><h3>Other programs</h3>' + chips(others + [("Virtual coaching over Zoom", "/virtual-dog-training")]) + '</div></div></section>')


def prog_cards(slugs=None):
    cards = ""
    for p in PROGRAMS:
        if slugs and p["slug"] not in slugs:
            continue
        n, alt = p["card"]
        w, h = ar(n)
        cards += (f'<a class="pcard rv" href="/{p["slug"]}"><div class="pph" style="aspect-ratio:{w}/{h}"><img src="/assets/{n}" alt="{A(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
                  f'<div class="pbody"><span class="meta">{E(p["track"])} · {E(p["tag"])}</span><h3>{E(p["name"])}</h3><p>{E(p["blurb"])}</p><span class="more-l">{E(p["cta"])} {ARROW_SVG}</span></div></a>')
    return f'<div class="pgrid">{cards}</div>'


def cta_section(h2="Talk with Jacob about your dog."):
    return (f'<section class="section contact"><div class="wrap story-grid"><div class="rv"><h2>{E(h2)}</h2></div><div class="rv" data-d="100"><p class="lede">Share your dog’s age, breed, training history and goals so the right next step can be discussed. Call <a href="tel:{TEL}">{PHONE}</a> or request a consultation.</p>'
            f'<p style="margin-top:28px">{btn("/contact", "Request a consultation")}</p></div></div></section>')


HOW_STEPS = [("Consultation first", "Share your dog’s age, breed, history and goals. Jacob talks through the right fit before anything is booked."),
             ("Personal training", "Jacob trains and cares for your dog himself, in a real home environment in Parrish. No rotating staff, no group classes."),
             ("Real-world practice", "Skills are practiced around the routines and distractions of everyday life, not just a quiet training space."),
             ("Owner handoff", "You get a detailed walkthrough of the commands and routines, plus ongoing support so the training holds up at home.")]


def area_page(k):
    a = AREAS_LOCAL[k]
    town, path = a["town"], f'/{a["slug"]}'
    n, alt = AREA_IMG[k]
    if k == "parrish":
        q1 = ("Where is Gator Alley Dog Training located?", f"Gator Alley Dog Training Academy is at {ADDR}, in {a['county']}. Call {PHONE} Wednesday through Sunday or request a free consultation online.")
    else:
        q1 = (f"Do you offer dog training in {town}, FL?", f"Yes. Gator Alley Dog Training is based in Parrish and serves {town} owners with personally led board-and-train programs, plus live virtual coaching over Zoom. Contact Jacob to talk through logistics from {town}.")
    faqs = [
        q1,
        (f"Which programs are available to {town} owners?", "Four board-and-train programs: Puppy Head Start (2 weeks), Basic Obedience, Advanced Obedience, Off-Leash & Behavior Modification, and Puppy Raise & Train (12 weeks). Jacob also offers live one-on-one virtual coaching sessions over Zoom."),
        ("Will my dog be kenneled?", "No. Dogs live and learn in Jacob’s real home environment in Parrish rather than a kennel facility, and Jacob personally trains and cares for every dog throughout the program."),
        ("Can you help with reactivity, anxiety or aggression?", "Behavior history matters. Be candid about fear, aggression, reactivity or any bite history during the consultation so the situation can be discussed responsibly. It is a personalized plan, not a guaranteed outcome."),
        ("What does training cost?", "Program fit and scope are discussed during the free consultation. Contact Jacob for current availability and program details rather than relying on an assumed price."),
    ]
    paras = "".join(f"<p>{E(t)}</p>" for t in a["paras"])
    challenge_items = "".join(f'<li>{CHECK}<span><strong>{E(t)}.</strong> {E(x)}</span></li>' for t, x in a["challenges"])
    ld = service_ld(f"Dog training in {town}, FL", a["desc"], town) + faq_ld(faqs) + crumbs_ld([("Home", "/"), ("Service areas", "/service-areas"), (f"Dog training in {town}", path)])
    ctas = btn("/contact", "Request a consultation") + f'<a class="btn ghost" href="tel:{TEL}">{PHONE}</a>'
    return head(a["title"], a["desc"], path, ld) + header("areas") + f'''
<main id="main">{hero_block(f'{a["county"]} · Gator Alley Dog Training', a["h1"], a["lede"], ctas, pfig(n, alt))}
{proof_strip()}
<section class="section"><div class="wrap split"><div class="rv">{eyebrow("Local dog training")}<h2>{E(a["headline"])}</h2><div class="prose">{paras}<p>Owners here walk and train around {E(a["places"])}. {E(a["focus"])}</p></div></div>
<div class="rv" data-d="100"><h3>What {E(town)} owners ask for</h3><ul class="fit">{challenge_items}</ul></div></div></section>
<section class="section local"><div class="wrap">{section_head(f"Programs for {town} dogs", "Four board-and-train programs, one trainer.", "Every program is personally led by Jacob. The right one depends on your dog’s age, history and goals, and it is chosen together in the consultation.")}
{prog_cards()}
<p class="note rv">Not able to come to Parrish? Jacob also offers <a class="tlink" href="/programs#virtual-coaching">live virtual coaching over Zoom</a> for leash manners, puppy foundations and behavior consistency.</p></div></section>
<section class="section method"><div class="wrap method-grid"><div class="sticky"><div class="rv">{eyebrow("How it works")}</div><h2 class="rv">From first call to confident dog.</h2><p class="rv" data-d="100">Every conversation begins with your dog’s needs and your goals, not a one-size-fits-all promise.</p></div>{steps_html(HOW_STEPS)}</div></section>
<section class="section" id="faq"><div class="wrap faq-grid"><div class="rv">{eyebrow(f"Dog training in {town}")}<h2>Questions {E(town)} owners ask.</h2></div><div>{faq_html(faqs)}</div></div></section>
{town_programs(k)}
{links_block(k)}
{cta_section(f"Ready to talk about your {town} dog?")}
</main>''' + footer()


def landing_page(l):
    path = f'/{l["slug"]}'
    n, alt = l["img"]
    prog = "".join(f'<a class="pcard rv" href="/{ps}"><div class="pbody"><h3>{E(nm)}</h3><p>{E(bl)}</p><span class="more-l">See the program {ARROW_SVG}</span></div></a>' for ps, nm, bl in l["programs"])
    intro = "".join(f"<p>{E(t)}</p>" for t in l["intro"])
    who = l.get("who") or f"{l['town']} owners"
    rel = chips([(PROBLEM_LABELS[r], f"/{r}") for r in l["related"]] + ([(f"Dog training in {l['town']}", f"/{AREAS_LOCAL[l['area_slug']]['slug']}")] if l.get("area_slug") else []))
    why = "".join(f'<li>{CHECK}<span>{E(t)}</span></li>' for t in ["Personally led by Jacob, no rotating staff", "A real home environment, not a kennel", "Real-world practice around everyday distractions", "A detailed handover and ongoing support", "Consultation first, with no one-size-fits-all promise"])
    ld = service_ld(l["h1"].split(" in ")[0], l["desc"], l.get("town")) + faq_ld(l["faqs"]) + crumbs_ld([("Home", "/"), ("Programs", "/programs"), (l["h1"], path)])
    ctas = btn("/contact", "Request a consultation") + f'<a class="btn ghost" href="tel:{TEL}">{PHONE}</a>'
    return head(l["title"], l["desc"], path, ld) + header("programs") + f'''
<main id="main">{hero_block(l["eyebrow"], l["h1"], l["lede"], ctas, pfig(n, alt))}
{proof_strip()}
<section class="section"><div class="wrap split"><div class="rv">{eyebrow("Gator Alley Dog Training")}<h2>Training built around your dog and your home.</h2><div class="prose">{intro}</div></div>
<div class="rv" data-d="100"><h3>Why owners choose Gator Alley</h3><ul class="fit">{why}</ul></div></div></section>
<section class="section local"><div class="wrap">{section_head("Programs to consider", f"Where {who} usually start.", "Jacob helps you choose after hearing about your dog. Here are the programs that fit this need.")}<div class="pgrid prog-list">{prog}</div></div></section>
<section class="section method"><div class="wrap method-grid"><div class="sticky"><div class="rv">{eyebrow("How it works")}</div><h2 class="rv">Book. Train. Thrive.</h2></div>{steps_html(HOW_STEPS)}</div></section>
<section class="section" id="faq"><div class="wrap faq-grid"><div class="rv">{eyebrow(who.capitalize())}<h2>Questions before you reach out.</h2></div><div>{faq_html(l["faqs"])}</div></div></section>
<section class="section local"><div class="wrap"><div class="rv"><h3>Related help</h3>{rel}</div></div></section>
{links_block(l.get("area_slug"), (), [l["slug"]])}
{cta_section(f"Talk with Jacob about your {l['town']} dog." if l.get("town") else "Talk with Jacob about your dog.")}
</main>''' + footer()


def problem_page(p):
    path = f'/{p["slug"]}'
    n, alt = p["img"]
    ps, pn = PROB_PROGRAM[p["slug"]]
    body = ""
    for t, x in p["blocks"]:
        if t == "h":
            body += f"<h2>{E(x)}</h2>"
        elif t == "p":
            body += f"<p>{inline(x)}</p>"
        elif t in ("ul", "ol"):
            body += f"<{t}>" + "".join(f"<li>{inline(i)}</li>" for i in x) + f"</{t}>"
    rel = chips([(PROBLEM_LABELS[r], f"/{r}") for r in p["related"]])
    ld = faq_ld(p["faqs"]) + crumbs_ld([("Home", "/"), ("Programs", "/programs"), (p["h1"], path)])
    ctas = btn("/contact", "Request a consultation") + f'<a class="btn ghost" href="tel:{TEL}">{PHONE}</a>'
    return head(p["title"], p["desc"], path, ld) + header("programs") + f'''
<main id="main">{hero_block("Dog training help · Parrish, FL", p["h1"], p["lede"], ctas, pfig(n, alt))}
{proof_strip()}
<section class="section"><div class="wrap article-grid"><article class="article rv">{body}</article>
<aside class="rv" data-d="100"><div class="callout"><p class="status">The program that fits</p><h3>{E(pn)}</h3><p>Personally led by Jacob in a real home environment, with a detailed handover so the training holds up at home.</p><p style="margin-top:18px"><a class="tlink" href="/{ps}">See the program →</a></p></div>
<div class="callout"><p class="status">Serving</p><p>Parrish, Bradenton, Sarasota, Lakewood Ranch, Palmetto, Ellenton, Tampa, St. Petersburg and nearby, plus virtual coaching anywhere.</p><p style="margin-top:14px"><a class="tlink" href="/service-areas">Where we train →</a></p></div></aside></div></section>
<section class="section" id="faq"><div class="wrap faq-grid"><div class="rv">{eyebrow("Common questions")}<h2>Questions owners ask.</h2></div><div>{faq_html(p["faqs"])}</div></div></section>
<section class="section local"><div class="wrap"><div class="rv"><h3>Related help</h3>{rel}</div></div></section>
{links_block(None, [p["slug"]] + list(p["related"]))}
{cta_section("Ready to talk with Jacob?")}
</main>''' + footer()


def service_areas():
    cards = ""
    for k in AREA_ORDER:
        a = AREAS_LOCAL[k]
        cards += (f'<a class="pcard rv" href="/{a["slug"]}"><div class="pbody"><span class="meta">{E(a["county"])}</span><h3>{E(a["town"])}, FL</h3><p>{E(a["headline"])}.</p><span class="more-l">Dog training in {E(a["town"])} {ARROW_SVG}</span></div></a>')
    desc = "Gator Alley Dog Training is based in Parrish, FL and serves Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota. Board and train plus virtual coaching."
    ld = ('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "Gator Alley Dog Training service areas", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": f"Dog training in {AREAS_LOCAL[k]['town']}, FL", "url": f"{DOMAIN}/{AREAS_LOCAL[k]['slug']}"} for i, k in enumerate(AREA_ORDER)]}) + "</script>"
          + crumbs_ld([("Home", "/"), ("Service areas", "/service-areas")]))
    return head("Dog Training in Parrish, Bradenton & Sarasota | Gator Alley", desc, "/service-areas", ld) + header("areas") + f'''
<main id="main">{hero_block("Service areas · Manatee, Sarasota & Hillsborough", "Dog training across Parrish and nearby Florida.", "Based in Parrish and serving owners in Bradenton, Sarasota, Lakewood Ranch, Palmetto, Ellenton and beyond, from Venice to Tampa and St. Petersburg. Pick your town to see how Jacob can help.", btn("/contact", "Request a consultation"), pfig("img01.jpg", "Jacob Soos and Chloe walking with their dogs in Parrish, Florida"))}
{proof_strip()}
<section class="section"><div class="wrap">{section_head("Where we train", f"{len(AREA_ORDER)} communities. One personal trainer.", "The same four programs are open to owners in every town, personally led by Jacob in a real home environment, plus live virtual coaching over Zoom.")}<div class="pgrid prog-list">{cards}</div></div></section>
<section class="section local"><div class="wrap">{section_head("What we offer", "Four board-and-train programs, plus virtual coaching.", "Choose the track that fits your dog’s age, behavior history and goals.")}{prog_cards()}</div></section>
<section class="section"><div class="wrap story-grid"><div class="rv">{eyebrow("Find us")}<h2>Our Parrish location.</h2></div><div class="rv prose" data-d="100"><p>Gator Alley Dog Training Academy, LLC · {ADDR}. Call <a href="tel:{TEL}">{PHONE}</a> Wednesday through Sunday, 9 AM–8 PM.</p><p>Not sure whether your town is covered, or want to talk logistics? Ask Jacob in your consultation request. We also welcome board-and-train clients from around the country and offer live virtual coaching over Zoom.</p><p style="margin-top:24px">{btn("/contact", "Ask about your area")}</p></div></div></section>
{links_block()}
</main>''' + footer()


def llms_txt():
    L = ["# Gator Alley Dog Training", "",
         "> Dog training in Parrish, FL (Manatee County), serving Palmetto, Ellenton, Bradenton, Lakewood Ranch and Sarasota.",
         "> Personally led by Jacob Soos in a real home environment, not a kennel. Board-and-train programs for puppies and adult dogs,",
         "> plus live one-on-one virtual coaching over Zoom.", "", "## Programs"]
    for p in PROGRAMS:
        L.append(f"- {p['name']}: {DOMAIN}/{p['slug']}")
    L += ["", "## Service areas"]
    for k in AREA_ORDER:
        a = AREAS_LOCAL[k]
        L.append(f"- {a['town']}, FL: {DOMAIN}/{a['slug']}")
    L += ["", "## Local program pages"]
    for l in LANDINGS:
        L.append(f"- {l['h1']}: {DOMAIN}/{l['slug']}")
    L += ["", "## Dog training help"]
    for p in PROBLEMS:
        L.append(f"- {PROBLEM_LABELS[p['slug']]}: {DOMAIN}/{p['slug']}")
    L += ["", "## More", f"- About Jacob: {DOMAIN}/about-jacob", f"- Contact: {DOMAIN}/contact", f"- All service areas: {DOMAIN}/service-areas", ""]
    return "\n".join(L)


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


OLD = {"puppy-head-start-parrish-fl": "/puppy-head-start", "basic-obedience-parrish-fl": "/basic-obedience",
       "advanced-obedience-behavior-parrish-fl": "/behavioral-issues-reactivity", "puppy-raise-and-train-parrish-fl": "/puppy-foundations",
       "virtual-dog-training-coaching": "/programs#virtual-coaching", "about-jacob-soos": "/about-jacob"}

if __name__ == "__main__":
    pages = {"index.html": "/", "programs.html": "/programs", "about-jacob.html": "/about-jacob", "contact.html": "/contact"}
    write("index.html", home()); write("programs.html", programs()); write("about-jacob.html", about()); write("contact.html", contact_page())
    for p in PROGRAMS:
        write(f'{p["slug"]}.html', program_page(p)); pages[f'{p["slug"]}.html'] = f'/{p["slug"]}'
    write("service-areas.html", service_areas()); pages["service-areas.html"] = "/service-areas"
    for k in AREA_ORDER:
        a = AREAS_LOCAL[k]; write(f'{a["slug"]}.html', area_page(k)); pages[f'{a["slug"]}.html'] = f'/{a["slug"]}'
    for l in LANDINGS:
        write(f'{l["slug"]}.html', landing_page(l)); pages[f'{l["slug"]}.html'] = f'/{l["slug"]}'
    for p in PROBLEMS:
        write(f'{p["slug"]}.html', problem_page(p)); pages[f'{p["slug"]}.html'] = f'/{p["slug"]}'
    # drop pages from the earlier 7-page layout
    for old in OLD:
        f = os.path.join(OUT, old + ".html")
        if os.path.exists(f): os.remove(f)
    urls = "".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u in pages.values())
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    write("llms.txt", llms_txt())
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    redirects = [{"source": f"/{o}", "destination": d, "permanent": True} for o, d in OLD.items()]
    write("vercel.json", json.dumps({"cleanUrls": True, "trailingSlash": False, "redirects": redirects,
          "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]}))
    print("built", len(pages), "pages")
