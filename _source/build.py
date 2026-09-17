#!/usr/bin/env python3
"""Generates the AltaCoco Home static site (plain HTML output)."""
import os, textwrap

import os as _o
OUT = os.environ.get("SITE_OUT", os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

NAV = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Services", "services.html"),
    ("Lookbook", "lookbook.html"),
    ("Editor's Choice", "editors-choice.html"),
    ("Journal", "journal.html"),
    ("Contact", "contact.html"),
]

PH_SVGS = {
    "sofa": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M14 30v-9a5 5 0 0 1 5-5h82a5 5 0 0 1 5 5v9"/><path d="M8 30h104v14H8z"/><path d="M14 44v6M106 44v6"/><path d="M60 30v14M32 30v14M88 30v14"/></svg>""",
    "table": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M10 22h100"/><path d="M20 22v30M100 22v30M20 40h80"/><circle cx="60" cy="12" r="5"/></svg>""",
    "lamp": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M45 26l6-18h18l6 18z"/><path d="M60 26v26M48 52h24"/></svg>""",
    "chair": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M44 8h32v26H44z"/><path d="M40 34h40v8H40z"/><path d="M44 42v12M76 42v12"/></svg>""",
    "bed": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M16 14h88v34H16z"/><path d="M16 30h88"/><path d="M26 22h20v8H26zM74 22h20v8H74z"/><path d="M16 48v6M104 48v6"/></svg>""",
    "rug": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M14 12h92v36H14z"/><path d="M22 20h76v20H22z"/><path d="M8 12v36M112 12v36"/></svg>""",
    "room": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M8 52h104"/><path d="M20 52V20l40-12 40 12v32"/><path d="M34 52V34h22v18"/><path d="M70 30h18v12H70z"/></svg>""",
    "storage": """<svg viewBox="0 0 120 60" fill="none" stroke="#2a2622" stroke-width="1.4"><path d="M24 8h72v44H24z"/><path d="M24 30h72M60 8v44"/><path d="M40 19h6M74 19h6M40 41h6M74 41h6"/></svg>""",
}

IMAGES = []  # (filename, shape, page, description, search terms) — drives images/SHOT-LIST.md

SHAPE_PX = {"": "1600×1200 (4:3)", "portrait": "1200×1500 (4:5)", "wide": "1920×1080 (16:9)",
            "square": "1400×1400 (1:1)", "hero": "1250×1500 (5:6)", "tall": "1200×1600 (3:4)"}

def ph(tone="sand", label="", shape="", mark="room", img=None, desc="", terms="", page="", p=""):
    """Placeholder block. If `img` is given, an <img> for images/<img> sits on top and
    takes over when the file exists; if the file is missing the img removes itself."""
    cls = f"ph ph-{tone}" + (f" ph--{shape}" if shape else "")
    m = f'<div class="ph-mark" aria-hidden="true">{PH_SVGS[mark]}</div>' if mark else ""
    l = f'<span class="ph-label">{label}</span>' if label else ""
    i = ""
    if img:
        IMAGES.append((img, shape, page, desc or label, terms))
        alt = (desc or label).replace('"', "'")
        i = f'<img class="ph-img" src="{p}images/{img}" alt="{alt}" loading="lazy" onerror="this.remove()">'
    return f'<div class="{cls}">{m}{l}{i}</div>'


def head(title, desc, depth=0, current=None):
    p = "../" * depth
    links = "".join(
        f'<a href="{p}{href}"' + (' aria-current="page"' if current == href else "") + f'>{name}</a>'
        for name, href in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%232a2622'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-family='Georgia,serif' font-size='18' fill='%23f8f5f0'%3EA%3C/text%3E%3C/svg%3E">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}index.html">AltaCoco <span>Home</span></a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="site-nav">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="site-nav" aria-label="Primary">
      {links}
      <a class="btn" href="{p}contact.html">Start a Project</a>
    </nav>
  </div>
</header>
<main>
"""


def foot(depth=0):
    p = "../" * depth
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html">AltaCoco <span>Home</span></a>
        <p>Residential Furniture Sourcing, Styling &amp; Procurement Support</p>
        <p>522 W Riverside Ave, Ste N<br>Spokane, WA 99201-0581<br>Virtual services available across the United States</p>
        <a class="email" href="mailto:cs@altacoco.com">cs@altacoco.com</a>
      </div>
      <div>
        <h4>Studio</h4>
        <ul>
          <li><a href="{p}about.html">About</a></li>
          <li><a href="{p}services.html">Services</a></li>
          <li><a href="{p}lookbook.html">Lookbook</a></li>
          <li><a href="{p}editors-choice.html">Editor's Choice</a></li>
          <li><a href="{p}journal.html">Journal</a></li>
          <li><a href="{p}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>More</h4>
        <ul>
          <li><a href="{p}faq.html">FAQ</a></li>
          <li><a href="{p}privacy.html">Privacy</a></li>
          <li><a href="{p}terms.html">Terms</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>Product names, trademarks, and brand names belong to their respective owners. Brand references are provided for editorial, product-research, and sourcing purposes and do not imply sponsorship, endorsement, or affiliation.</p>
      <p>Prices, promotions, product specifications, and availability may change without notice.</p>
      <p>&copy; 2026 AltaCoco Home. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)


def cta_band(heading, body, btn="Start a Project", href="contact.html", p=""):
    return f"""
<section class="section section--dark cta-band">
  <div class="wrap">
    <h2>{heading}</h2>
    <p class="lede">{body}</p>
    <div class="btn-row"><a class="btn btn--ghost" href="{p}{href}">{btn}</a></div>
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME
home = head("AltaCoco Home | Furniture Sourcing & Interior Styling",
            "Residential furniture sourcing, styling, space planning, and procurement support for thoughtfully furnished homes.",
            current="index.html")
home += f"""
<section class="hero">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Residential Furniture Sourcing &amp; Styling Studio</p>
      <h1>Thoughtful Furniture for Better-Lived Spaces</h1>
      <p class="lede">We help homeowners discover, compare, and source furniture that fits their space, style, budget, and everyday life.</p>
      <p class="lede">From a single statement piece to a full-room furnishing plan, we simplify the search and bring clarity to the buying process.</p>
      <div class="btn-row">
        <a class="btn" href="contact.html">Start a Project</a>
        <a class="btn btn--ghost" href="editors-choice.html">Explore Editor's Choice</a>
      </div>
    </div>
    <div>{ph("clay", "Hero — living room photography", "hero", "room", img="home-hero.jpg", page="Home", desc="Warm, modern living room with a neutral sofa, wood accents, and natural light", terms="modern living room neutral sofa natural light")}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap split split--reverse">
    <div>{ph("sage", "Detail — material & texture", "portrait", "chair", img="home-detail.jpg", page="Home", desc="Close-up of furniture materials: wood grain, linen or bouclé upholstery, stone", terms="furniture material detail linen wood close up")}</div>
    <div class="reveal">
      <p class="eyebrow">A More Considered Way to Furnish</p>
      <h2>Good design starts with choosing the right pieces.</h2>
      <p class="lede">Furniture shopping can quickly become overwhelming: too many options, unclear dimensions, inconsistent materials, changing prices, and endless tabs.</p>
      <p class="lede"><strong>We narrow the field.</strong></p>
      <p>Our studio combines furniture sourcing, product research, space planning, and styling guidance to help clients make confident decisions without spending weeks comparing hundreds of products.</p>
      <p>Whether you are furnishing a new home, refreshing one room, or searching for one difficult-to-find piece, we focus on products that make sense both visually and practically.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Services</p>
      <h2>How We Can Help</h2>
    </div>
    <div class="grid grid-3">
      <div class="service reveal">
        <span class="num">01</span>
        <h3>Furniture Sourcing</h3>
        <p>A curated selection of furniture based on your style, room dimensions, budget, priorities, and daily needs.</p>
        <p>We compare options across brands so you do not have to.</p>
        <a class="link" href="services.html#sourcing">Learn About Sourcing</a>
      </div>
      <div class="service reveal">
        <span class="num">02</span>
        <h3>Room Styling</h3>
        <p>A cohesive furniture and decor direction for living rooms, bedrooms, dining spaces, home offices, and family spaces.</p>
        <p>We help connect the major pieces so the room feels intentional rather than assembled one item at a time.</p>
        <a class="link" href="services.html#styling">Explore Styling Services</a>
      </div>
      <div class="service reveal">
        <span class="num">03</span>
        <h3>Space Planning</h3>
        <p>Furniture scale matters as much as furniture style.</p>
        <p>We help evaluate dimensions, circulation, seating capacity, clearances, and layout before you commit to large purchases.</p>
        <a class="link" href="services.html#planning">Learn About Space Planning</a>
      </div>
      <div class="service reveal">
        <span class="num">04</span>
        <h3>Outdoor Design</h3>
        <p>Patios, decks, balconies, and covered porches furnished with the same attention to scale, comfort, and materials as any indoor room.</p>
        <p>We select outdoor seating, dining, lighting, and accessories that hold up to weather and everyday use.</p>
        <a class="link" href="services.html#outdoor">Explore Outdoor Design</a>
      </div>
      <div class="service reveal">
        <span class="num">05</span>
        <h3>Procurement Support</h3>
        <p>Once selections are finalized, we can help organize product information, coordinate orders, and streamline communication across vendors.</p>
        <a class="link" href="services.html#procurement">Learn About Procurement</a>
      </div>
      <div class="service reveal">
        <span class="num">06</span>
        <h3>Product Research &amp; Comparison</h3>
        <p>Deciding between two sofas, three dining tables, or several outdoor sets? We compare the details that matter: dimensions, materials, comfort, and value.</p>
        <a class="link" href="services.html#research">Learn About Comparisons</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Outdoor Design</p>
      <h2>Outdoor rooms deserve the same care.</h2>
      <p class="lede">A patio, deck, or balcony is another room of the house. It should be as comfortable to sit in, as easy to move through, and as considered in its materials as the living room inside.</p>
      <p>We help select outdoor sofas, dining sets, lounge chairs, lighting, planters, and rugs that look good together, fit the footprint, and stand up to sun, rain, and real use. For smaller balconies, we focus on pieces that earn their space.</p>
      <div class="btn-row"><a class="btn" href="services.html#outdoor">Explore Outdoor Design</a></div>
    </div>
    <div>{ph("sage", "Outdoor — covered patio seating", "portrait", "sofa", img="home-outdoor.jpg", page="Home", desc="Covered patio with an outdoor sofa, lounge chairs, and planters", terms="covered patio outdoor sofa modern")}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Editor's Choice</p>
      <h2>Furniture worth a closer look.</h2>
      <p class="lede">A regularly updated edit of furniture, lighting, rugs, and home products selected for strong design, useful proportions, thoughtful materials, and compelling value.</p>
      <p>We look beyond the product photo and focus on the details that matter in real homes.</p>
    </div>
    <div class="grid grid-4">
      <article class="card reveal">
        {ph("sand", "Sectional", "portrait", "sofa", img="ec-sectional.jpg", page="Home", desc="Deep neutral sectional sofa in a living room", terms="sectional sofa living room neutral")}
        <span class="card-tag">Best for Family Lounging</span>
        <h3>A Deep Sectional With Clean Lines</h3>
        <p>Generous enough for everyday lounging without looking overly bulky.</p>
        <a class="link" href="editors-choice/gather-deep-sectional-family-living.html">Explore the Pick</a>
      </article>
      <article class="card reveal">
        {ph("oat", "Dining table", "portrait", "table", img="ec-dining-table.jpg", page="Home", desc="Compact round or oval dining table in a small dining space", terms="small round dining table apartment")}
        <span class="card-tag">Best Small-Space Dining Pick</span>
        <h3>A Dining Table That Seats More Than It Looks</h3>
        <p>A compact footprint, useful proportions, and a shape that works especially well in tighter rooms.</p>
        <a class="link" href="editors-choice/hearth-round-extendable-dining-table.html">Explore the Pick</a>
      </article>
      <article class="card reveal">
        {ph("stone", "Pendant light", "portrait", "lamp", img="ec-pendant.jpg", page="Home", desc="Sculptural pendant light over a table", terms="pendant light dining sculptural")}
        <span class="card-tag">Best Statement Light</span>
        <h3>A Pendant That Can Carry the Room</h3>
        <p>Simple enough to live with long term, distinctive enough to become the focal point.</p>
        <a class="link" href="editors-choice/corfu-ceramic-pendant.html">Explore the Pick</a>
      </article>
      <article class="card reveal">
        {ph("clay", "Lounge chair", "portrait", "chair", img="ec-lounge-chair.jpg", page="Home", desc="Well-proportioned lounge chair by a window", terms="lounge chair armchair modern interior")}
        <span class="card-tag">Best Value</span>
        <h3>A Well-Proportioned Lounge Chair Under $1,000</h3>
        <p>A strong silhouette and practical dimensions at a price point that leaves room in the budget for the rest of the room.</p>
        <a class="link" href="editors-choice/ojai-wood-accent-chair.html">Explore the Pick</a>
      </article>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="editors-choice.html">View All Editor's Choice</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Lookbook</p>
      <h2>Ideas for rooms that feel collected, not overdesigned.</h2>
      <p class="lede">Explore sample furnishing concepts built around scale, comfort, material balance, and practical living.</p>
      <p>These editorial concepts illustrate how we think about furniture combinations, layout, and visual rhythm.</p>
      <div class="btn-row"><a class="btn" href="lookbook.html">Explore the Lookbook</a></div>
    </div>
    <div class="grid grid-2" style="gap:12px">
      {ph("oat", "Warm modern living room", "portrait", "room", img="lookbook-01-wide.jpg", page="Home", desc="Warm modern living room: deep neutral sofa, warm wood, sculptural lamp", terms="warm modern living room wood sofa")}
      {ph("sage", "Calm primary bedroom", "portrait", "bed", img="lookbook-03-wide.jpg", page="Home", desc="Calm bedroom with natural linen bedding, soft light, low contrast", terms="calm neutral bedroom linen bedding")}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Why Work With Us</p>
      <h2>Less searching. Better decisions.</h2>
    </div>
    <div class="grid grid-4">
      <div class="point reveal"><h3>Curated, not endless</h3><p>We reduce hundreds of possibilities to a focused selection worth considering.</p></div>
      <div class="point reveal"><h3>Dimensions first</h3><p>We pay close attention to scale, depth, height, clearances, and how furniture will actually function in a room.</p></div>
      <div class="point reveal"><h3>Across brands</h3><p>We are not limited to a single retailer or design style.</p></div>
      <div class="point reveal"><h3>Value matters</h3><p>Good design is not simply about spending more. We consider quality, materials, function, longevity, and price together.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Sourcing Across Leading Home Brands</h2>
      <p class="lede">We research and source products across a wide range of established furniture, lighting, and home brands, allowing us to compare style, dimensions, materials, availability, and value across the market.</p>
    </div>
    <ul class="brand-list clean">
      <li>Crate &amp; Barrel</li><li>CB2</li><li>West Elm</li><li>Pottery Barn</li><li>Rejuvenation</li>
      <li>Williams Sonoma Home</li><li>Design Within Reach</li><li>Lumens</li><li>Visual Comfort</li>
      <li>Four Hands</li><li>Serena &amp; Lily</li><li class="more">and more</li>
    </ul>
    <p class="disclaimer">Brand names are referenced for product research and sourcing purposes. No affiliation or endorsement is implied unless explicitly stated.</p>
  </div>
</section>
""" + cta_band("Have a room, a shortlist, or one impossible furniture decision?",
               "Tell us what you are working on. We will help you narrow the options and move forward with confidence.") + foot()
write("index.html", home)

# ---------------------------------------------------------------- ABOUT
about = head("About the Studio | AltaCoco Home",
             "AltaCoco Home is a residential furniture sourcing and styling studio based in Spokane, Washington, helping clients make better furnishing decisions.",
             current="about.html")
about += f"""
<section class="page-hero">
  <div class="wrap split">
    <div>
      <p class="eyebrow">About the Studio</p>
      <h1>A practical approach to beautiful interiors.</h1>
      <p class="lede">We are a residential furniture sourcing and styling studio focused on helping clients make better furnishing decisions.</p>
      <p class="lede">Our work sits at the intersection of design, research, and real-world usability.</p>
      <p>We believe a home does not need to be overly styled to feel considered. The right proportions, materials, colors, and functional choices can do most of the work.</p>
    </div>
    <div>{ph("oat", "Studio — interior detail", "portrait", "room", img="about-hero.jpg", page="About", desc="Considered interior corner: a chair, side table, lamp, and a plant", terms="interior corner armchair side table lamp")}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Who We Are</p>
    <h2>Led by two principal designers.</h2>
    <div class="grid grid-2 mt-2">
      <div class="point reveal">
        <h3>Yijian Gao</h3>
        <p>Co-Founder, Principal Designer</p>
      </div>
      <div class="point reveal">
        <h3>Jie Wu</h3>
        <p>Co-Founder, Principal Designer</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap split split--reverse">
    <div>{ph("stone", "Scale & dimensions", "square", "sofa", img="about-scale.jpg", page="About", desc="Tape measure, floor plan sketch, or fabric samples on a table", terms="interior design tape measure floor plan samples")}</div>
    <div class="reveal">
      <p class="eyebrow">Our Approach</p>
      <h2>Design decisions should feel clear, not complicated.</h2>
      <p>The furniture market has never offered more choice, but more choice does not always make buying easier.</p>
      <p>A sofa can look perfect online and still be too deep for the room.<br>A dining table can have the right style but the wrong proportions.<br>Two beautiful pieces can compete with each other when placed together.</p>
      <p>Our role is to help filter those decisions.</p>
      <p><strong>We evaluate products through several lenses:</strong></p>
      <ul class="checklist checklist--cols">
        <li>Scale and dimensions</li><li>Material and construction</li><li>Comfort and function</li><li>Visual compatibility</li>
        <li>Price and value</li><li>Maintenance and everyday use</li><li>Availability and lead time</li>
      </ul>
      <p class="mt-2">The goal is simple: fewer regrets and a home that feels more cohesive.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Who We Work With</p>
      <h2>Homeowners at every stage of furnishing.</h2>
      <ul class="checklist">
        <li>Homeowners furnishing a new home</li>
        <li>Families upgrading high-use spaces</li>
        <li>Clients refreshing one room at a time</li>
        <li>Busy professionals who want a curated shortlist</li>
        <li>Clients comparing products across multiple retailers</li>
        <li>Anyone who wants thoughtful guidance before making a large furniture purchase</li>
      </ul>
    </div>
    <div class="reveal">
      <p class="eyebrow">Location</p>
      <h3>Based in Spokane, Washington</h3>
      <p class="lede">522 W Riverside Ave, Ste N<br>Spokane, WA 99201-0581</p>
      <p class="lede">Virtual furniture sourcing and design support available for clients across the United States.</p>
      <div class="mt-2">{ph("sage", "Pacific Northwest", "wide", "room", img="about-location.jpg", page="About", desc="Pacific Northwest landscape or a home exterior among evergreens", terms="pacific northwest home evergreen trees")}</div>
    </div>
  </div>
</section>
""" + cta_band("Tell Us About Your Space", "Share a room, a shortlist, or a single decision you are weighing. We will help you find the right starting point.", "Tell Us About Your Space") + foot()
write("about.html", about)

# ---------------------------------------------------------------- SERVICES
def svc(id_, num, title, intro, incl_title, incl, best_title=None, best=None, extra_html=""):
    best_html = f"<div><h4>{best_title}</h4><p>{best}</p></div>" if best else ""
    return f"""
<div class="service-block" id="{id_}">
  <div>
    <span class="num">{num}</span>
    <h2>{title}</h2>
    <div class="lede">{intro}</div>
    {extra_html}
  </div>
  <div class="aside">
    <div>
      <h4>{incl_title}</h4>
      <ul class="checklist">{"".join(f"<li>{i}</li>" for i in incl)}</ul>
    </div>
    {best_html}
  </div>
</div>"""

services = head("Furniture Sourcing & Styling Services | AltaCoco Home",
                "Furniture sourcing, room styling, space planning, outdoor design, product research, and procurement support for residential interiors.",
                current="services.html")
services += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Services</p>
    <h1>Furniture decisions, made easier.</h1>
    <p class="lede">Choose a focused service for one decision or combine services for a more complete furnishing plan.</p>
  </div>
</section>
<section class="section--tight">
  <div class="wrap">
    {svc("sourcing", "01", "Furniture Sourcing",
         "<p>Finding furniture is easy. Finding the right furniture is harder.</p><p>We create a curated shortlist based on your room, budget, style direction, functional needs, and preferred brands.</p>",
         "May Include", ["Furniture research", "Cross-brand comparisons", "Product shortlists", "Dimensions and specification review", "Material comparisons", "Alternative options", "Value assessment", "Availability review"],
         "Best For", "Clients who know what category they need but do not want to spend hours comparing products.")}
    {svc("styling", "02", "Room Styling",
         "<p>For clients who want individual pieces to work together as a complete room.</p><p>We develop a coordinated furnishing direction that considers furniture, rugs, lighting, textiles, finishes, and visual balance.</p>",
         "May Include", ["Furniture selection", "Rug sizing", "Lighting suggestions", "Material coordination", "Color direction", "Styling recommendations", "Product pairing"],
         "Best For", "Living rooms, bedrooms, dining rooms, family rooms, home offices, and other residential spaces.")}
    {svc("planning", "03", "Space Planning",
         "<p>Before choosing furniture, we help answer the most important question:</p><p><strong>Will it actually fit well?</strong></p><p>We review furniture dimensions in relation to the room, circulation, seating, and surrounding pieces.</p>",
         "May Include", ["Layout recommendations", "Sofa and sectional sizing", "Dining table sizing", "Rug sizing", "Walkway clearances", "Furniture spacing", "Scale comparison"])}
    {svc("outdoor", "04", "Outdoor Design",
         "<p>Patios, decks, balconies, and covered porches are rooms too. They deserve the same attention to scale, comfort, and materials as the spaces inside.</p><p>We help select outdoor furniture, lighting, planters, and accessories that look good together, fit the footprint, and hold up to weather and everyday use.</p>",
         "May Include", ["Outdoor sofa, lounge, and dining selection", "Weather-resistant material comparison (teak, aluminum, performance fabrics)", "Layout for patios, decks, and balconies", "Shade, lighting, and planter suggestions", "Indoor–outdoor continuity with adjoining rooms", "Small-balcony solutions", "Covers, storage, and maintenance guidance"],
         "Best For", "Covered patios, decks, rooftop terraces, balconies, garden dining areas, and outdoor living rooms.")}
    {svc("procurement", "05", "Procurement Support",
         "<p>For clients who already have selections or have completed a sourcing project with us.</p><p>We help simplify the ordering stage by organizing product information and coordinating the purchasing process.</p>",
         "May Include", ["Product specification review", "Vendor coordination", "Order organization", "Availability checks", "Delivery-information coordination", "Product substitutions when availability changes"])}
    {svc("research", "06", "Product Research &amp; Comparison",
         "<p>Trying to decide between two sofas, three dining tables, or several outdoor sets?</p><p>We provide focused research centered on the details that matter.</p>",
         "Typical Comparison Criteria", ["Dimensions", "Materials", "Construction", "Comfort", "Maintenance", "Warranty information", "Price", "Current value", "Best use case"])}
  </div>
</section>
""" + cta_band("Start a Project", "Not sure which service fits? Send us your room, shortlist, or product links and we will help determine the right starting point.") + foot()
write("services.html", services)

# ---------------------------------------------------------------- LOOKBOOK
def concept(num, title, label, body, priorities, tones, marks, shots, shot_terms):
    media = "".join(
        ph(t, l, "", m, img=f"lookbook-{num}-{k}.jpg", page=f"Lookbook {num}", desc=d, terms=q)
        for t, l, m, k, d, q in zip(tones, ["Wide view", "Detail", "Detail"], marks, ["wide", "detail-a", "detail-b"], shots, shot_terms))
    return f"""
<article class="concept reveal">
  <div class="concept-media">{media}</div>
  <div>
    <span class="concept-label">{label}</span>
    <span class="num">Concept {num}</span>
    <h2>{title}</h2>
    <p class="lede">{body}</p>
    <h4>Design Priorities</h4>
    <ul class="checklist">{"".join(f"<li>{p}</li>" for p in priorities)}</ul>
  </div>
</article>"""

lookbook = head("Furniture & Interior Lookbook | AltaCoco Home",
                "Explore editorial room concepts focused on furniture scale, materials, layout, comfort, and practical residential design.",
                current="lookbook.html")
lookbook += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Lookbook</p>
    <h1>Editorial room concepts for real-life spaces.</h1>
    <p class="lede">Our Lookbook explores furniture combinations, layouts, materials, and styling directions through sample concepts.</p>
    <p class="lede">These are editorial design studies created to show how we approach scale, balance, and product selection.</p>
    <p class="notice mt-2">The concepts below are editorial design studies, not completed client projects. Each is labeled as an Editorial Concept or Design Study.</p>
  </div>
</section>
<section class="section--tight">
  <div class="wrap">
    {concept("01", "Warm Modern Living Room", "Editorial Concept",
             "A comfortable living room built around a deep neutral sofa, warm wood, sculptural lighting, and soft textural contrast.",
             ["Comfortable everyday seating", "Warm but restrained palette", "Durable materials", "Layered lighting", "Minimal visual clutter"],
             ["clay", "oat", "sand"], ["room", "sofa", "lamp"],
             ["Warm modern living room: deep neutral sofa, warm wood, sculptural lamp", "Detail: wood side table and textured throw", "Detail: sculptural floor or table lamp"],
             ["warm modern living room wood sofa", "wood side table throw detail", "sculptural lamp interior"])}
    {concept("02", "Family-Friendly Living Space", "Design Study",
             "A practical family room with generous seating, forgiving materials, rounded forms, and flexible storage.",
             ["Kid-friendly circulation", "Comfortable sectional seating", "Easy-clean surfaces", "Soft edges", "Functional storage"],
             ["sage", "stone", "oat"], ["room", "sofa", "storage"],
             ["Family room with generous sectional, rounded forms, and storage", "Detail: performance fabric or rounded ottoman", "Detail: built-in or freestanding storage with baskets"],
             ["family room sectional kids friendly", "rounded ottoman fabric detail", "living room storage baskets"])}
    {concept("03", "Calm Primary Bedroom", "Editorial Concept",
             "A quiet bedroom palette centered around natural materials, soft lighting, generous bedding, and low visual contrast.",
             ["Relaxed proportions", "Warm neutral textiles", "Simple bedside storage", "Layered lighting", "Minimal ornament"],
             ["oat", "sand", "stone"], ["bed", "lamp", "storage"],
             ["Calm bedroom with natural linen bedding, soft light, low contrast", "Detail: bedside lamp and nightstand", "Detail: layered neutral textiles"],
             ["calm neutral bedroom linen bedding", "nightstand bedside lamp", "neutral bedding textiles detail"])}
    {concept("04", "Compact Dining Room", "Design Study",
             "A dining setup designed for smaller footprints without sacrificing seating capacity or visual presence.",
             ["Efficient table dimensions", "Comfortable circulation", "Lightweight chair profiles", "Focused pendant lighting", "Flexible seating"],
             ["stone", "clay", "sage"], ["table", "chair", "lamp"],
             ["Compact dining room with a small table and light chairs", "Detail: dining chair profile", "Detail: pendant over the table"],
             ["small dining room round table", "dining chair detail", "dining pendant light"])}
    {concept("05", "Covered Patio Living Room", "Design Study",
             "An outdoor living space treated like an indoor one: deep weatherproof seating, a low table, layered planters, and lighting that makes the space usable after dark.",
             ["Weather-resistant materials", "Comfortable lounge seating", "Shade and evening lighting", "Continuity with the adjoining interior", "Easy seasonal maintenance"],
             ["sage", "oat", "stone"], ["sofa", "chair", "lamp"],
             ["Covered patio with an outdoor sofa, lounge chairs, low table, and planters", "Detail: outdoor cushions, teak or aluminum frame, and a planter", "Detail: outdoor dining table on a deck or balcony"],
             ["covered patio outdoor sofa modern", "outdoor furniture teak cushion detail", "balcony dining table modern"])}
  </div>
</section>
""" + cta_band("Want a concept built around your room?", "Share your dimensions, style direction, and priorities. We will develop a furnishing direction that fits how you actually live.") + foot()
write("lookbook.html", lookbook)

# ---------------------------------------------------------------- EDITOR'S CHOICE
CATS = ["Sofas & Sectionals", "Chairs", "Dining Tables", "Beds", "Storage", "Lighting", "Rugs", "Kids", "Outdoor",
        "Small-Space Picks", "Family-Friendly Picks", "Splurge-Worthy Pieces", "Best Value"]
def slug(s): return s.lower().replace("&", "and").replace(" ", "-")

import sys as _sys, os as _os2
_sys.path.insert(0, _os2.path.dirname(_os2.path.abspath(__file__)))
from products import PRODUCTS, CHECKED

def short_price(pr):
    return pr.split(" ")[0].split(",")[0] if pr.startswith("$") and "," not in pr.split(" ")[0] else pr.split(" ")[0]

def pick_card(pd):
    return f"""
<article class="pick reveal" data-cats="{",".join(slug(c) for c in pd["cats"])}">
  {ph(pd["tone"], "Product photography", "portrait", pd["mark"], img=pd["img"], page="Editor's Choice", desc=pd["title"], terms="")}
  <span class="card-tag">{pd["tag"]}</span>
  <h3>{pd["title"]}</h3>
  <p>{pd["summary"]}</p>
  <div class="meta"><span>{pd["brand"]}</span><span>{pd["product"]}</span><span>{short_price(pd["price"])}</span></div>
  <a class="link" href="editors-choice/{pd["slug"]}.html">Explore the Pick</a>
</article>"""

ec = head("Editor's Choice: Furniture & Home Picks | AltaCoco Home",
          "A curated edit of furniture, lighting, rugs, and home products selected for design, proportions, functionality, and value.",
          current="editors-choice.html")
ec += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Editor's Choice</p>
    <h1>The pieces we think are worth knowing about.</h1>
    <p class="lede">Editor's Choice is our ongoing edit of furniture, lighting, rugs, outdoor pieces, and home products that stand out for design, proportions, materials, functionality, or value.</p>
    <p class="lede">This is not an endless product catalog. It is a smaller collection of products we believe deserve a closer look.</p>
    <p class="notice mt-2">Prices and availability may change. Always confirm current product details with the retailer before purchasing. Prices shown were checked on {CHECKED}.</p>
  </div>
</section>
<section class="section--tight">
  <div class="wrap">
    <div class="chip-row" role="list" aria-label="Filter by category">
      <a class="chip is-active" href="#" data-filter="all">All</a>
      {"".join(f'<a class="chip" href="#" data-filter="{slug(c)}">{c}</a>' for c in CATS)}
    </div>
  </div>
</section>
<section class="section section--tight">
  <div class="wrap">
    <div class="grid grid-3">
      {"".join(pick_card(pd) for pd in PRODUCTS)}
    </div>
    <p class="disclaimer">Product names and brand names belong to their respective owners and are referenced for editorial and sourcing purposes; no affiliation or endorsement is implied. Retail prices, promotions, availability, and lead times can change; confirm current information with the retailer before purchasing.</p>
  </div>
</section>
""" + cta_band("Need help comparing a pick with another option?", "Contact us for furniture sourcing and product comparison support.", "Start a Project") + foot()
write("editors-choice.html", ec)

# ---------------------------------------------------------------- PRODUCT POSTS
def related_products(pd, n=3):
    same = [q for q in PRODUCTS if q["slug"] != pd["slug"] and set(q["cats"]) & set(pd["cats"])]
    other = [q for q in PRODUCTS if q["slug"] != pd["slug"] and q not in same]
    return "".join(f'<li><a href="{q["slug"]}.html">{q["title"]}</a><span class="status">{q["tag"]}</span></li>' for q in (same + other)[:n])

for pd in PRODUCTS:
    lis = lambda items: "".join(f"<li>{x}</li>" for x in items)
    paras = lambda items: "".join(f"<p>{x}</p>" for x in items)
    seat_row = f'<tr><th>Seating / Fit</th><td>{pd["seat"]}</td></tr>' if pd["seat"] and pd["seat"] != "—" else ""
    post = head(f'{pd["title"]} | Editor\'s Choice | AltaCoco Home',
                f'Editor\'s Choice: {pd["brand"]} {pd["product"]}. {pd["summary"]}', depth=1, current="editors-choice.html")
    post += f"""
<section class="post-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../editors-choice.html">Editor's Choice</a> &nbsp;/&nbsp; {pd["cats"][0]}</p>
    <h1>{pd["title"]}</h1>
    <p class="lede">{pd["brand"]} &middot; {pd["product"]}</p>
    <div class="mt-3">{ph(pd["tone"], "Product", "wide", pd["mark"], img=pd["img"], page="Product post", desc=pd["title"], terms="", p="../")}</div>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap post-layout">
    <div class="post-body">
      <h2>Why We Like It</h2>
      {paras(pd["why"])}
      <h2>Design Notes</h2>
      <ul class="checklist">{lis(pd["notes"])}</ul>
      <h2>What to Consider</h2>
      {paras(pd["consider"])}
      <h2>Why It Is in Editor's Choice</h2>
      <p class="callout">{pd["why_ec"]}</p>
      <h2>Styling Pairing</h2>
      <p>Pair with:</p>
      <ul class="checklist">{lis(pd["pairing"])}</ul>
      <p class="notice mt-3">Specifications and prices were taken from the retailer's product page on {CHECKED}. Prices, promotions, and availability change; verify current details with the retailer before purchasing. We have not tested this product in person unless stated. Brand and product names belong to their owners; no affiliation is implied.</p>
    </div>
    <aside>
      <table class="spec-table">
        <tr><th>Brand</th><td>{pd["brand"]}</td></tr>
        <tr><th>Product</th><td>{pd["product"]}</td></tr>
        <tr><th>Category</th><td>{pd["category"]}</td></tr>
        <tr><th>Price</th><td>{pd["price"]}</td></tr>
        <tr><th>Dimensions</th><td>{pd["dims"]}</td></tr>
        {seat_row}
        <tr><th>Materials</th><td>{pd["material"]}</td></tr>
        <tr><th>Best For</th><td>{pd["best_for"]}</td></tr>
        <tr><th>Reviews at retailer</th><td>{pd["reviews"]}</td></tr>
        <tr><th>Last Checked</th><td>{CHECKED}</td></tr>
      </table>
      <div class="btn-row">
        <a class="btn btn--ghost" href="{pd["url"]}" target="_blank" rel="nofollow noopener">View at {pd["brand"].split(" (")[0]}</a>
      </div>
      <p class="eyebrow" style="margin-top:2.5rem">More picks</p>
      <ul class="article-list">{related_products(pd)}</ul>
    </aside>
  </div>
</section>
""" + cta_band("Need help comparing this piece with another option?", "Contact us for furniture sourcing and product comparison support.", "Start a Project", "contact.html", "../") + foot(1)
    write(f'editors-choice/{pd["slug"]}.html', post)

# ---------------------------------------------------------------- JOURNAL
import sys, os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from articles import ARTICLES

CAT_ORDER = ["Buying Guides", "Product Comparisons", "Design Notes"]

def journal_group(name):
    lis = ""
    for a in ARTICLES:
        if a["cat"] != name: continue
        lis += f'<li><div><a href="journal/{a["slug"]}.html">{a["title"]}</a><p class="dek">{a["dek"]}</p></div><span class="status">{a["mins"]} min read</span></li>'
    return f'<div class="journal-group reveal"><h2>{name}</h2><ul class="article-list">{lis}</ul></div>'

journal = head("Furniture Buying Guides & Design Notes | AltaCoco Home",
               "Practical furniture buying guides, comparisons, sizing advice, and residential design notes.",
               current="journal.html")
journal += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Journal</p>
    <h1>Notes on furniture, rooms, and buying well.</h1>
    <p class="lede">Practical guides and design observations for making better furniture decisions.</p>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap">
    {"".join(journal_group(c) for c in CAT_ORDER)}
  </div>
</section>
""" + cta_band("Have a question a guide has not answered?", "Send us your room, shortlist, or product links and we will help you think it through.") + foot()
write("journal.html", journal)

def related(a, n=3):
    same = [b for b in ARTICLES if b["cat"] == a["cat"] and b["slug"] != a["slug"]]
    other = [b for b in ARTICLES if b["cat"] != a["cat"]]
    picks = (same + other)[:n]
    return "".join(f'<li><a href="{b["slug"]}.html">{b["title"]}</a><span class="status">{b["cat"]}</span></li>' for b in picks)

for a in ARTICLES:
    page = head(f'{a["title"]} | Journal | AltaCoco Home', a["desc"], depth=1, current="journal.html")
    page += f"""
<section class="post-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../journal.html">Journal</a> &nbsp;/&nbsp; {a["cat"]}</p>
    <h1>{a["title"]}</h1>
    <p class="lede">{a["dek"]}</p>
    <div class="mt-3">{ph(a["tone"], "Article", "wide", a["mark"], img=a["img"], page="Journal article", desc=a["title"], terms="", p="../")}</div>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap">
    <div class="article-body">
      <p class="article-meta">{a["cat"].rstrip("s") if a["cat"] != "Design Notes" else "Design Note"} &middot; {a["mins"]} min read</p>
      {a["body"]}
    </div>
    <div class="article-body mt-3">
      <p class="eyebrow" style="margin-top:2.5rem">Related reading</p>
      <ul class="article-list">{related(a)}</ul>
    </div>
  </div>
</section>
""" + cta_band(a["cta"][0], a["cta"][1], "Start a Project", "contact.html", "../") + foot(1)
    write(f'journal/{a["slug"]}.html', page)

# ---------------------------------------------------------------- CONTACT
def select(name, opts):
    o = "".join(f"<option>{x}</option>" for x in opts)
    return f'<select id="{slug(name)}" name="{name}"><option value="">Select…</option>{o}</select>'

contact = head("Contact | AltaCoco Home",
               "Tell us what you're working on. Furniture sourcing, room styling, space planning, and product comparison support for residential clients.",
               current="contact.html")
contact += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Tell us what you're working on.</h1>
    <p class="lede">Whether you need help furnishing an entire room or simply deciding between two sofas, send us a few details and we will take it from there.</p>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap split contact-grid">
    <form class="form" id="contact-form" novalidate>
      <div class="field"><label for="name">Name</label><input id="name" name="Name" type="text" autocomplete="name" required></div>
      <div class="field"><label for="email">Email</label><input id="email" name="Email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="location">Location</label><input id="location" name="Location" type="text" placeholder="City, State"></div>
      <div class="field"><label for="project-type">Project Type</label>{select("Project Type", ["Furniture Sourcing", "Room Styling", "Space Planning", "Outdoor Design", "Product Comparison", "Procurement Support", "Other"])}</div>
      <div class="field"><label for="room">Room</label>{select("Room", ["Living Room", "Bedroom", "Dining Room", "Home Office", "Kids Room", "Patio / Deck / Balcony", "Whole Home", "Other"])}</div>
      <div class="field"><label for="approximate-furniture-budget">Approximate Furniture Budget</label>{select("Approximate Furniture Budget", ["Under $5,000", "$5,000–$10,000", "$10,000–$25,000", "$25,000–$50,000", "$50,000+"])}</div>
      <div class="field"><label for="timeline">Timeline</label>{select("Timeline", ["As soon as possible", "Within 1 month", "1–3 months", "3–6 months", "Flexible"])}</div>
      <div class="field full"><label for="project">Tell Us About Your Project</label><textarea id="project" name="Tell Us About Your Project"></textarea></div>
      <div class="field full"><label for="links">Optional Product Links</label><textarea id="links" name="Optional Product Links" style="min-height:90px" placeholder="Paste any product links you are considering"></textarea></div>
      <div class="full">
        <button class="btn" type="submit">Start the Conversation</button>
        <p class="form-status mt-1" id="form-status" aria-live="polite"></p>
        <p class="form-note">We typically reply within two business days.</p>
      </div>
    </form>
    <aside class="contact-aside">
      <div>
        <h3>Prefer email?</h3>
        <a class="email" href="mailto:cs@altacoco.com">cs@altacoco.com</a>
      </div>
      <div>
        <h3>Studio</h3>
        <p>AltaCoco Home<br>522 W Riverside Ave, Ste N<br>Spokane, WA 99201-0581<br>Virtual services available across the United States</p>
      </div>
      <div>
        <h3>Helpful to include</h3>
        <ul class="checklist">
          <li>Room dimensions, if you have them</li>
          <li>A few photos of the space</li>
          <li>Links to pieces you are considering</li>
          <li>Anything you are keeping</li>
        </ul>
      </div>
      {ph("oat", "Studio", "square", "room", img="contact-studio.jpg", page="Contact", desc="Desk with samples, notebook, and a laptop, or a styled shelf", terms="interior designer desk samples")}
    </aside>
  </div>
</section>
""" + foot()
write("contact.html", contact)

# ---------------------------------------------------------------- FAQ
FAQ = [
    ("What types of projects do you take on?", "We support projects ranging from a single furniture decision to full-room sourcing and styling, indoors and out."),
    ("Do you only work with specific furniture brands?", "No. We research and source across a wide range of furniture, lighting, rug, and home brands based on the needs of each project."),
    ("Can you help if I already know what I want?", "Absolutely. Many clients come to us with a shortlist and want help comparing dimensions, materials, value, or alternative options."),
    ("Do you offer virtual services?", "Yes. Furniture sourcing, product comparison, and many styling services can be completed remotely."),
    ("Can you help with furniture dimensions and layout?", "Yes. Scale and fit are central to our process. We can review furniture dimensions and help evaluate how pieces work together within a room."),
    ("Do you sell furniture directly?", "Our primary service is furniture sourcing, styling, research, and procurement support. Specific purchasing arrangements may vary by project and vendor."),
    ("Are prices shown in Editor's Choice always current?", "No. Retail prices, promotions, availability, and lead times can change. Always confirm current information with the retailer before purchasing."),
    ("Do you work on outdoor spaces?", "Yes. Patios, decks, balconies, and covered porches get the same process as indoor rooms: layout, scale, seating comfort, and materials that hold up to weather. We source outdoor furniture, lighting, and accessories across brands."),
    ("Are the Lookbook projects real client projects?", "Any editorial or sample work is clearly identified as an <strong>Editorial Concept</strong>, <strong>Sample Concept</strong>, or <strong>Design Study</strong>."),
]
faq = head("FAQ | AltaCoco Home", "Answers to common questions about our furniture sourcing, styling, space planning, and Editor's Choice.", current=None)
faq += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">FAQ</p>
    <h1>Common questions.</h1>
    <p class="lede">If you do not see your question here, send us a note and we will get back to you.</p>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap">
    <div class="faq">
      {"".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for i, (q, a) in enumerate(FAQ))}
    </div>
  </div>
</section>
""" + cta_band("Still have a question?", "Tell us what you are working on and we will point you to the right starting place.") + foot()
write("faq.html", faq)

# ---------------------------------------------------------------- LEGAL
def legal(title, h1, body):
    page = head(f"{title} | AltaCoco Home", f"{title} for AltaCoco Home.")
    page += f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">{title}</p>
    <h1>{h1}</h1>
    <p class="muted small">Last updated: [Date]</p>
  </div>
</section>
<section class="section--tight" style="padding-bottom: clamp(64px, 9vw, 128px)">
  <div class="wrap legal">
    <p class="notice">Placeholder text. Replace with a policy reviewed for your business before launch.</p>
    {body}
  </div>
</section>
""" + foot()
    return page

write("privacy.html", legal("Privacy Policy", "Privacy Policy", """
<h2>Information we collect</h2>
<p>When you contact us through the website or by email, we receive the details you choose to share, such as your name, email address, location, and information about your project.</p>
<h2>How we use it</h2>
<p>We use this information to respond to your inquiry, provide the services you request, and communicate with you about your project. We do not sell personal information.</p>
<h2>Third-party links</h2>
<p>Editor's Choice and Journal content may link to retailer websites. Those sites have their own privacy practices, which we do not control.</p>
<h2>Contact</h2>
<p>Questions about this policy can be sent to <a href="mailto:cs@altacoco.com">cs@altacoco.com</a>.</p>
"""))

write("terms.html", legal("Terms of Use", "Terms of Use", """
<h2>Editorial content</h2>
<p>Editor's Choice, Lookbook, and Journal content is provided for general informational and editorial purposes. Product names, trademarks, and brand names belong to their respective owners, and references do not imply sponsorship, endorsement, or affiliation.</p>
<h2>Prices and availability</h2>
<p>Prices, promotions, specifications, and availability shown or referenced on this site may change without notice. Confirm current details with the retailer before purchasing.</p>
<h2>Concept work</h2>
<p>Editorial concepts, sample concepts, and design studies are illustrative and are labeled as such. They do not represent completed client projects unless explicitly stated.</p>
<h2>Services</h2>
<p>Specific service scope, fees, and purchasing arrangements are agreed in writing for each project.</p>
<h2>Contact</h2>
<p>Questions about these terms can be sent to <a href="mailto:cs@altacoco.com">cs@altacoco.com</a>.</p>
"""))


# ---------------------------------------------------------------- SHOT LIST
seen = {}
for fn, shape, page, desc, terms in IMAGES:
    if fn in seen:
        if page not in seen[fn][1]:
            seen[fn][1] += " + " + page
    else:
        seen[fn] = [shape, page, desc, terms]
seen = dict(sorted(seen.items()))
rows = "\n".join(f"| `{fn}` | {SHAPE_PX[sh]} | {pg} | {d} | {t} |" for fn, (sh, pg, d, t) in seen.items())
shot = f"""# Photo shot list

Save photos into this `images/` folder using **exactly these filenames** (lowercase, `.jpg`). Every slot on the site
is already wired: as soon as a file exists it replaces the placeholder block automatically, with no HTML edits.
If a file is missing, the placeholder stays, so photos can be added gradually. (`home-hero.jpg` is already in place.
A set of drawn stand-ins is kept in `_illustrations/` — copy any of them up a level if you want one temporarily.)

Sizes are minimums; larger is fine. Photos are cropped to fit (centered), so keep the subject near the middle.
Free sources whose license allows commercial website use: Unsplash (unsplash.com) and Pexels (pexels.com).
Search terms are suggestions. Keep a consistent look: warm, natural light, neutral palettes, uncluttered rooms.

After adding photos, run `./optimize-images.sh` from this folder (uses macOS `sips`, nothing to install) to resize
anything oversized to a web-friendly 2000px and re-save JPEGs at quality 82.

{len(seen)} images total.

| Filename | Min size (ratio) | Used on | What it should show | Search terms |
|---|---|---|---|---|
{rows}
"""
write("images/SHOT-LIST.md", shot)
write("images/optimize-images.sh", """#!/bin/bash
# Resizes every .jpg/.jpeg/.png in this folder to max 2000px on the long edge and
# re-saves JPEGs at quality 82. macOS only (uses the built-in `sips`). Originals are overwritten.
cd "$(dirname "$0")"
for f in *.jpg *.jpeg *.png; do
  [ -e "$f" ] || continue
  sips -Z 2000 "$f" >/dev/null
  case "$f" in *.jpg|*.jpeg) sips -s format jpeg -s formatOptions 82 "$f" --out "$f" >/dev/null ;; esac
  echo "optimized $f"
done
""")
print("done", len(seen), "images")
