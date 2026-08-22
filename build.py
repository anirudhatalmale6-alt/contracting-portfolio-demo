#!/usr/bin/env python3
"""Static builder for the Meridian Trading & Contracting design demo.

Everything here maps 1:1 onto the WordPress theme that follows:
  PROJECTS  -> a 'project' custom post type
  gallery   -> the post's image gallery field
  writeup   -> the post editor content
  facts     -> custom fields (client, location, value, ...)
So the markup you sign off on is the markup the theme will output.
"""
import html
import json
import os
import re

OUT = os.path.dirname(os.path.abspath(__file__))

BRAND = "Meridian"
BRAND_FULL = "Meridian Trading &amp; Contracting"
TAGLINE = "Trading &amp; Contracting"

# --------------------------------------------------------------------------
# project data
# --------------------------------------------------------------------------

PROJECTS = [
    {
        "slug": "riverside-logistics-hub",
        "title": "Riverside Logistics Hub",
        "sector": "industrial",
        "sector_label": "Industrial",
        "excerpt": "A 14,000 m² distribution warehouse delivered from bare plot to "
                   "handover in eleven months, including the full MEP package.",
        "facts": [
            ("Client", "Riverside Freight Group"),
            ("Location", "Port District, Sector 4"),
            ("Contract value", "4.6 M"),
            ("Scope", "Design &amp; build, civil, structural, MEP"),
            ("Built area", "14,000 m²"),
            ("Completed", "March 2025"),
            ("Duration", "11 months"),
        ],
        "images": [
            ("p2a", "Batching plant and delivery fleet staged on the north apron",
             "Concrete supply was brought on site rather than bought in — it held the pour schedule through a wet February."),
            ("p2b", "Structural steel frame at week 19",
             "Primary frame topped out four days ahead of programme."),
            ("p2c", "Warehouse envelope before cladding",
             "Clear internal height of 12.5 m with no intermediate columns across the pick aisles."),
            ("p1b", "Mobile crane lifting the final roof truss",
             "The 40 t lift was sequenced for a Sunday to keep the access road open on working days."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>Riverside Freight Group needed a distribution facility that could take
38 trailer movements a day and be operational before the peak season. The plot
was a former hardstanding with unrecorded services and a high water table, so
the programme risk sat almost entirely in the ground rather than in the
building.</p>
<p>We were appointed on a design-and-build basis, which let us bring the
structural and MEP designers into the same room as the groundworks team from
week one instead of pricing a finished drawing set.</p>

<h2>What we delivered</h2>
<ul>
  <li>Site investigation, enabling works and 6,200 m³ of cut and fill</li>
  <li>Piled raft foundation with a power-floated 250 mm slab</li>
  <li>1,850 t structural steel frame and composite roof deck</li>
  <li>Insulated cladding envelope with 14 dock levellers</li>
  <li>Full MEP package — LV distribution, sprinkler, HVAC, BMS</li>
  <li>External works: 9,000 m² of heavy-duty paving, gatehouse, weighbridge</li>
</ul>

<h2>The ground problem</h2>
<p>Trial pits found a perched water table 1.4 m below the finished floor level
and two abandoned drainage runs that appeared on none of the utility records.
Rather than stop and re-price, we moved the piling rig to the southern half of
the plot and ran a dewatering scheme on the north while the design was revised.</p>
<blockquote>
  The site never went quiet. That is the difference between a contractor who
  plans around a problem and one who waits for an instruction.
  <footer>— Operations Director, Riverside Freight Group</footer>
</blockquote>

<h3>Programme recovery</h3>
<p>The revised foundation added nine days of work but the parallel sequencing
absorbed all of it. Steel erection started on the original date.</p>

<div class="tablewrap">
<table>
  <caption class="sr-only">Key project milestones against programme</caption>
  <thead>
    <tr><th scope="col">Milestone</th><th scope="col">Planned</th><th scope="col">Actual</th></tr>
  </thead>
  <tbody>
    <tr><td>Enabling works complete</td><td>Week 6</td><td>Week 6</td></tr>
    <tr><td>Foundations signed off</td><td>Week 14</td><td>Week 15</td></tr>
    <tr><td>Steel frame topped out</td><td>Week 20</td><td>Week 19</td></tr>
    <tr><td>Envelope watertight</td><td>Week 31</td><td>Week 30</td></tr>
    <tr><td>Practical completion</td><td>Week 48</td><td>Week 47</td></tr>
  </tbody>
</table>
</div>

<h2>Outcome</h2>
<p>Handover came a week early with a snag list of 31 items, all closed inside
14 days. The client has since instructed us on a second phase — a 3,000 m²
temperature-controlled annexe on the same plot. You can see our other
industrial work on the <a href="projects.html">projects page</a>, or
<a href="contact.html">talk to us about a similar build</a>.</p>
""",
    },
    {
        "slug": "al-noor-commercial-tower",
        "title": "Al Noor Commercial Tower",
        "sector": "buildings",
        "sector_label": "Buildings",
        "excerpt": "Eighteen storeys of Grade-A office space, built over a live "
                   "retail podium that never closed for a single trading day.",
        "facts": [
            ("Client", "Al Noor Holdings"),
            ("Location", "Central Business District"),
            ("Contract value", "22.4 M"),
            ("Scope", "Main contractor — structure &amp; envelope"),
            ("Built area", "31,600 m²"),
            ("Completed", "September 2024"),
            ("Duration", "26 months"),
        ],
        "images": [
            ("p1a", "Curtain wall reaching level 14", "The unitised system was installed from inside the slab edge — no external mast climbers on a city-centre footprint."),
            ("p1c", "Podium works with the retail units trading below", "All noisy activity was restricted to 06:00–09:00 by agreement with the tenants."),
            ("p1d", "Core formwork and post-tensioned slab", "A four-day floor cycle held from level 3 upward."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>An eighteen-storey commercial tower on a constrained city plot, built over
an existing two-storey retail podium that had to keep trading throughout.
Access was from a single street frontage with no laydown area.</p>

<h2>Approach</h2>
<p>Every load was delivered just-in-time to a booked slot. We ran a digital
delivery diary that the subcontractors booked into themselves, which cut
vehicle waiting on the street from an average of 41 minutes to under 8.</p>
<ul>
  <li>Post-tensioned flat slabs on a four-day cycle</li>
  <li>Slipformed central core, 14 m ahead of the frame</li>
  <li>Unitised curtain wall, 1,240 panels, installed from within</li>
  <li>Temporary works designed to transfer podium loads around the live units</li>
</ul>

<h2>Working over a live podium</h2>
<p>The retail tenants had a contractual right to trade. We designed a crash
deck over the full podium roof and monitored it weekly, and moved every
percussive operation into a pre-agreed morning window. Across 26 months the
podium lost no trading days.</p>

<h2>Outcome</h2>
<p>Completed to programme and handed over with a BREEAM Excellent rating.
See more of our <a href="projects.html">commercial building work</a>.</p>
""",
    },
    {
        "slug": "northgate-office-fitout",
        "title": "Northgate Office Fit-Out",
        "sector": "interiors",
        "sector_label": "Interiors",
        "excerpt": "A 2,400 m² CAT-B fit-out over four floors, turned around in "
                   "fourteen weeks while the client stayed in the building.",
        "facts": [
            ("Client", "Northgate Advisory"),
            ("Location", "Northgate Square"),
            ("Contract value", "1.9 M"),
            ("Scope", "CAT-B fit-out, joinery, AV, furniture"),
            ("Built area", "2,400 m²"),
            ("Completed", "January 2025"),
            ("Duration", "14 weeks"),
        ],
        "images": [
            ("p3a", "Reception desk and waiting area after handover", "The slatted timber desk was made in our own workshop and installed in one overnight shift."),
            ("p3b", "Client-facing lounge on level one", "Dark oak and blackened steel, all joinery made in our own workshop."),
            ("p3c", "Circulation spine linking the four floors", "Glazed partitions kept daylight reaching the core."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>Northgate Advisory wanted to consolidate five departments onto four floors
without moving out. The fit-out therefore had to run floor by floor, with each
one handed back fully operational before the next was stripped.</p>

<h2>Sequence</h2>
<ol>
  <li>Level 4 stripped and rebuilt while levels 1–3 stayed occupied</li>
  <li>Staff decanted upward one floor at a time</li>
  <li>Reception rebuilt last, over two consecutive weekends</li>
</ol>

<h3>Acoustics</h3>
<p>The client's main complaint about the old space was noise. We built a full
mock-up bay on level 4 and tested three ceiling treatments with the staff in
it before committing. The chosen build-up brought the measured reverberation
time down from 0.9 s to 0.45 s.</p>

<h2>Outcome</h2>
<p>Delivered in fourteen weeks with zero days of lost occupancy.
<a href="contact.html">Ask us about your own fit-out</a>.</p>
""",
    },
    {
        "slug": "sabkha-road-mep-package",
        "title": "Sabkha Road MEP Package",
        "sector": "mep",
        "sector_label": "MEP",
        "excerpt": "Mechanical, electrical and plumbing for a six-building "
                   "campus, coordinated in 3D before a single hanger was drilled.",
        "facts": [
            ("Client", "Sabkha Development Authority"),
            ("Location", "Sabkha Road Campus"),
            ("Contract value", "7.1 M"),
            ("Scope", "MEP design coordination and installation"),
            ("Built area", "6 buildings / 19,800 m²"),
            ("Completed", "June 2025"),
            ("Duration", "17 months"),
        ],
        "images": [
            ("p4a", "Plant room pipework during commissioning", "Every valve was tagged and photographed into the O&amp;M manual as it was fitted."),
            ("p4b", "Primary distribution above the service corridor", "Clash-detected in 3D before fabrication — no site cutting of ductwork."),
            ("p4c", "Main LV distribution board", "Two independent supplies with automatic changeover for the data hall."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>Six buildings sharing a central energy centre, with a small data hall that
required N+1 resilience on both power and cooling. The consultant's design was
issued at concept stage only, so the coordination sat with us.</p>

<h2>Coordination</h2>
<p>We modelled every service above ceiling in 3D and ran clash detection
against the structural model weekly. 412 clashes were resolved on screen. The
practical result is that nothing was cut to fit on site, and the ceiling void
came in 90 mm shallower than the concept allowance.</p>

<h2>Commissioning</h2>
<ul>
  <li>Witnessed testing on all 38 systems</li>
  <li>Full seasonal commissioning across summer and winter</li>
  <li>Photographic O&amp;M manuals, asset-tagged and handed over digitally</li>
  <li>Two days of operator training for the client's facilities team</li>
</ul>

<h2>Outcome</h2>
<p>Handed over with zero outstanding commissioning items — unusual on a campus
this size, and the direct result of coordinating before fabricating.</p>
""",
    },
    {
        "slug": "coastal-link-bridge-approach",
        "title": "Coastal Link Bridge Approach",
        "sector": "infrastructure",
        "sector_label": "Infrastructure",
        "excerpt": "1.8 km of approach road and embankment for a new estuary "
                   "crossing, built under a live traffic management plan.",
        "facts": [
            ("Client", "Regional Highways Authority"),
            ("Location", "Estuary Crossing, North Bank"),
            ("Contract value", "9.8 M"),
            ("Scope", "Earthworks, drainage, pavement, structures"),
            ("Built area", "1.8 km carriageway"),
            ("Completed", "November 2024"),
            ("Duration", "15 months"),
        ],
        "images": [
            ("p5b", "The completed approach and crossing", "Alignment was set out from a single control network shared with the bridge contractor."),
            ("p5a", "Embankment formation and drainage", "72,000 m³ of imported fill, placed and compacted in 300 mm layers."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>Build the northern approach to a new estuary crossing — embankment,
drainage, pavement and two retaining structures — while the existing coast
road stayed open to two-way traffic throughout.</p>

<h2>Traffic and environment</h2>
<p>The works ran alongside a designated wetland. All drainage discharged
through a settlement pond before reaching the estuary, and turbidity was
sampled twice daily during earthworks. No exceedance was recorded in fifteen
months.</p>

<h2>Outcome</h2>
<p>Opened to traffic on the contractual date. The client's own audit recorded
zero defects on the pavement handover.</p>
""",
    },
    {
        "slug": "marina-ridge-villas",
        "title": "Marina Ridge Villas",
        "sector": "residential",
        "sector_label": "Residential",
        "excerpt": "Twelve waterfront villas built to a single detail set, each "
                   "one finished to its buyer's chosen specification.",
        "facts": [
            ("Client", "Marina Ridge Developments"),
            ("Location", "Marina Ridge"),
            ("Contract value", "6.3 M"),
            ("Scope", "Main contractor — shell, finishes, landscaping"),
            ("Built area", "12 villas / 5,400 m²"),
            ("Completed", "May 2025"),
            ("Duration", "19 months"),
        ],
        "images": [
            ("p6a", "Completed villa with pool terrace", "Pools, decking and soft landscaping were all delivered in the main contract."),
            ("p6b", "Street elevation of the first four units", "One structural detail set, four external finish options."),
        ],
        "writeup": """
<h2>Brief</h2>
<p>Twelve villas sold off-plan, each buyer choosing from a menu of finish
packages. The structure had to be identical across all twelve to keep the cost
down; the visible finishes had to look bespoke.</p>

<h2>How we kept it repeatable</h2>
<ul>
  <li>One structural and MEP detail set across all twelve plots</li>
  <li>Four external finish options and three internal packages</li>
  <li>Choices locked at first-fix — after that, variations were priced</li>
  <li>The same trade gangs rotated plot to plot in a fixed sequence</li>
</ul>
<p>Repeating the sequence meant plot 12 was built in 61% of the man-hours that
plot 1 took.</p>

<h2>Outcome</h2>
<p>All twelve handed over inside a five-week window, with buyer-specific
finishes correct on first inspection.</p>
""",
    },
]

SECTORS = [
    ("all", "All projects"),
    ("buildings", "Buildings"),
    ("industrial", "Industrial"),
    ("interiors", "Interiors"),
    ("mep", "MEP"),
    ("infrastructure", "Infrastructure"),
    ("residential", "Residential"),
]

CAPS = [
    ("01", "General Contracting", "Single point of responsibility from site set-up to handover, with our own labour on the critical trades."),
    ("02", "Design &amp; Build", "One contract for design and delivery, so the buildability question gets asked before the drawing is issued."),
    ("03", "MEP Services", "Mechanical, electrical and plumbing coordinated in 3D, installed and commissioned by our own teams."),
    ("04", "Trading &amp; Supply", "Materials, plant and equipment sourced through our own supply desk — the same rates we build on."),
]

ARROW = ('<svg width="15" height="10" viewBox="0 0 15 10" fill="none" aria-hidden="true">'
         '<path d="M0 5h13M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="square"/></svg>')
TICK = ('<svg width="15" height="12" viewBox="0 0 15 12" fill="none" aria-hidden="true">'
        '<path d="M1 6l4.5 4.5L14 1.5" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="square"/></svg>')
CAM = ('<svg width="13" height="12" viewBox="0 0 13 12" fill="none" aria-hidden="true">'
       '<rect x=".8" y="2.3" width="11.4" height="8.9" stroke="currentColor" stroke-width="1.3"/>'
       '<circle cx="6.5" cy="6.7" r="2.3" stroke="currentColor" stroke-width="1.3"/>'
       '<path d="M4.4 2.3l.9-1.5h2.4l.9 1.5" stroke="currentColor" stroke-width="1.3"/></svg>')
CHEV_L = ('<svg width="12" height="20" viewBox="0 0 12 20" fill="none" aria-hidden="true">'
          '<path d="M10 1L2 10l8 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="square"/></svg>')
CHEV_R = ('<svg width="12" height="20" viewBox="0 0 12 20" fill="none" aria-hidden="true">'
          '<path d="M2 1l8 9-8 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="square"/></svg>')
XMARK = ('<svg width="15" height="15" viewBox="0 0 15 15" fill="none" aria-hidden="true">'
         '<path d="M1 1l13 13M14 1L1 14" stroke="currentColor" stroke-width="1.7"/></svg>')
ZOOM = ('<svg width="13" height="13" viewBox="0 0 13 13" fill="none" aria-hidden="true">'
        '<circle cx="5.4" cy="5.4" r="4.5" stroke="currentColor" stroke-width="1.4"/>'
        '<path d="M8.8 8.8L12.4 12.4M3.6 5.4h3.6M5.4 3.6v3.6" stroke="currentColor" stroke-width="1.4"/></svg>')

# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------


def head(title, desc, canonical, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://example.com/{canonical}">
<meta name="theme-color" content="#0d1012">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://example.com/assets/img/full/hero.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%230d1012'/><text x='16' y='23' font-family='Arial' font-size='19' font-weight='bold' fill='%23e79a24' text-anchor='middle'>M</text></svg>">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="demobar"><b>Design demo</b> &nbsp;·&nbsp; placeholder company, placeholder photos and text — the layout, gallery and CMS structure are the real deliverable.</div>
"""


def masthead(active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<div class="utility">
  <div class="wrap">
    <div class="utility__set">
      <span class="utility__tag">Est. 2004</span>
      <span>Licensed general contractor &amp; trading house</span>
    </div>
    <div class="utility__set utility__set--right">
      <span>Mon–Sat, 08:00–18:00</span>
      <a href="contact.html">Request a quotation</a>
    </div>
  </div>
</div>

<header class="masthead">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand__mark" aria-hidden="true">M</span>
      <span>
        <span class="brand__name">{BRAND}</span>
        <span class="brand__sub">{TAGLINE}</span>
      </span>
    </a>

    <nav class="nav" id="primary-nav" aria-label="Primary">
      {link('index.html', 'Home', 'home')}
      {link('projects.html', 'Projects', 'projects')}
      {link('index.html#capabilities', 'Capabilities', 'caps')}
      {link('index.html#about', 'About', 'about')}
      {link('contact.html', 'Contact', 'contact')}
      <a class="btn" href="contact.html">Request a quote {ARROW}</a>
    </nav>

    <div class="masthead__cta">
      <a class="btn" href="contact.html">Request a quote {ARROW}</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="primary-nav">
        <span></span><span></span><span></span>
        <span class="sr-only">Menu</span>
      </button>
    </div>
  </div>
</header>
"""


def footer():
    proj_links = "\n".join(
        f'        <li><a href="project-{p["slug"]}.html">{p["title"]}</a></li>'
        for p in PROJECTS[:5])
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot__top">
      <div class="foot__brand">
        <a class="brand" href="index.html">
          <span class="brand__mark" aria-hidden="true">M</span>
          <span><span class="brand__name">{BRAND}</span>
          <span class="brand__sub">{TAGLINE}</span></span>
        </a>
        <p class="foot__blurb">General contracting, design &amp; build and materials
        supply. Twenty-one years, 240 completed projects, one point of responsibility.</p>
      </div>
      <div>
        <h3>Projects</h3>
        <ul>
{proj_links}
          <li><a href="projects.html">View all &rarr;</a></li>
        </ul>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="index.html#capabilities">Capabilities</a></li>
          <li><a href="index.html#about">About us</a></li>
          <li><a href="index.html#sectors">Sectors</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h3>Get in touch</h3>
        <ul>
          <li>Unit 14, Industrial Avenue<br>Port District</li>
          <li><a href="tel:+10000000000">+1 000 000 0000</a></li>
          <li><a href="contact.html">Request a quotation</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__bottom">
      <span>&copy; 2026 {BRAND_FULL}. Demo content.</span>
      <span>Built as a design demo — company name, figures and photography are placeholders.</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def project_card(p, klass="", eager=False):
    img = p["images"][0][0]
    loading = "" if eager else ' loading="lazy"'
    size = "full" if "hero" in klass else "thumb"
    dims = 'width="1600" height="1000"' if size == "full" else 'width="800" height="500"'
    return f"""      <a class="pcard {klass} rv" href="project-{p['slug']}.html" data-sector="{p['sector']}">
        <div class="pcard__media">
          <img src="assets/img/{size}/{img}.webp" {dims}{loading} decoding="async"
               alt="{p['title']} — {html.escape(p['images'][0][1], quote=True)}">
          <span class="pcard__badge">{p['sector_label']}</span>
          <span class="pcard__count">{CAM} {len(p['images'])} photos</span>
        </div>
        <div class="pcard__body">
          <h3>{p['title']}</h3>
          <div class="pcard__meta">
            <span>{p['facts'][1][1]}</span>
            <span>{p['facts'][5][1]}</span>
          </div>
          <p class="pcard__excerpt">{p['excerpt']}</p>
          <span class="pcard__more">View project {ARROW}</span>
        </div>
      </a>
"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------


def build_index():
    caps = "\n".join(f"""      <div class="caps__item rv">
        <div class="caps__num">{n}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>""" for n, t, d in CAPS)

    cards = (project_card(PROJECTS[0], "pcard--hero", eager=True)
             + project_card(PROJECTS[1])
             + project_card(PROJECTS[2])
             + project_card(PROJECTS[3]))

    sectors = "\n".join(
        f'      <div><span>{i:02d}</span> {label}</div>'
        for i, (_, label) in enumerate(SECTORS[1:], start=1))

    org_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "name": "Meridian Trading & Contracting",
        "url": "https://example.com/",
        "description": "General contracting, design and build, MEP services and materials supply.",
        "foundingDate": "2004",
        "address": {"@type": "PostalAddress", "streetAddress": "Unit 14, Industrial Avenue",
                    "addressLocality": "Port District"},
    }, indent=2)

    body = f"""{masthead('home')}
<main id="main">

  <section class="hero">
    <div class="hero__media">
      <img src="assets/img/full/hero.webp" width="1600" height="1000" fetchpriority="high" decoding="async"
           alt="Crawler crane working on a Meridian construction site at first light">
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow eyebrow--light">Trading &amp; contracting since 2004</p>
      <h1 class="hero__title">We build the things<br>that <em>have to work.</em></h1>
      <p class="hero__lede">Warehouses, towers, roads and fit-outs — delivered by one
      contractor who carries the design, the trades and the supply chain. Look at what
      we have finished, then judge us on it.</p>
      <div class="hero__actions">
        <a class="btn" href="projects.html">See our projects {ARROW}</a>
        <a class="btn btn--ghost-light" href="contact.html">Request a quotation</a>
      </div>
    </div>
    <div class="wrap">
      <div class="hero__stats">
        <div><b>240</b><span>Projects completed</span></div>
        <div><b>21</b><span>Years in operation</span></div>
        <div><b>380</b><span>People on the books</span></div>
        <div><b>96%</b><span>Delivered on programme</span></div>
      </div>
    </div>
  </section>

  <section class="section" id="capabilities">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow">What we do</p>
          <h2 class="section__title">Four capabilities, one point of responsibility.</h2>
        </div>
        <p class="section__note">We self-deliver the trades that decide a programme and
        buy the rest through our own trading desk. Fewer interfaces, fewer excuses.</p>
      </div>
      <div class="caps">
{caps}
      </div>
    </div>
  </section>

  <section class="section section--paper2" id="projects">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow">Selected work</p>
          <h2 class="section__title">Projects we are happy to be judged on.</h2>
        </div>
        <p class="section__note">Every entry carries the full photo set and a written
        account of how the job actually ran — including the parts that went sideways.</p>
      </div>
      <div class="pgrid">
{cards}      </div>
      <p style="margin-top:36px"><a class="btn btn--ghost" href="projects.html">View all projects {ARROW}</a></p>
    </div>
  </section>

  <section class="section" id="about">
    <div class="wrap">
      <div class="split">
        <div class="split__media rv">
          <img src="assets/img/full/about.webp" width="1600" height="1000" loading="lazy" decoding="async"
               alt="Meridian site engineer reviewing drawings on a live construction site">
          <div class="split__stamp"><b>2004</b><span>Founded</span></div>
        </div>
        <div class="rv">
          <p class="eyebrow">About us</p>
          <h2 class="section__title">A contractor that owns the whole problem.</h2>
          <p>Meridian started as a materials trading house and grew into a
          general contractor — which is an unusual direction to travel, and it shows in
          how we work. We know what the steel costs before we price the frame.</p>
          <ul class="ticklist">
            <li>{TICK} Directly employed site teams on groundworks, concrete and MEP</li>
            <li>{TICK} In-house joinery workshop and plant yard</li>
            <li>{TICK} Own trading desk for materials and equipment supply</li>
            <li>{TICK} ISO 9001 and 45001 certified, with a full-time HSE manager</li>
          </ul>
          <p style="margin-top:30px"><a class="btn btn--ghost" href="contact.html">Talk to us {ARROW}</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--dark section--tight" id="sectors">
    <div class="wrap">
      <p class="eyebrow eyebrow--light">Sectors</p>
      <h2 class="section__title" style="margin-bottom:34px">Where we work</h2>
      <div class="sectors">
{sectors}
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap">
      <div>
        <h2>Have a project? Send us the drawings.</h2>
        <p>Tell us the scope and the date you need it finished. You will get a
        named contact and a written response within two working days.</p>
      </div>
      <a class="btn" href="contact.html">Request a quotation {ARROW}</a>
    </div>
  </section>

</main>
"""
    ld = f'<script type="application/ld+json">\n{org_ld}\n</script>\n'
    return (head("Meridian Trading &amp; Contracting — General Contractor &amp; Materials Supply",
                 "General contracting, design and build, MEP and materials supply since 2004. "
                 "See 240 completed warehouse, commercial, road and fit-out projects.",
                 "", ld)
            + body + footer())


def build_projects():
    filters = "\n".join(
        f'      <button type="button" data-filter="{key}" aria-pressed="{"true" if key == "all" else "false"}">{label}</button>'
        for key, label in SECTORS)

    cards = "".join(project_card(p, "pcard--wide", eager=(i < 2))
                    for i, p in enumerate(PROJECTS))

    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Projects — Meridian Trading & Contracting",
        "hasPart": [{"@type": "CreativeWork", "name": p["title"],
                     "url": f"https://example.com/project-{p['slug']}.html",
                     "abstract": re.sub(r"\s+", " ", p["excerpt"])} for p in PROJECTS],
    }, indent=2)

    body = f"""{masthead('projects')}
<main id="main">

  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a> <span>/</span> Projects
      </nav>
      <h1>Every project, photographed and written up.</h1>
      <p>{len(PROJECTS)} entries in this demo. On the live site this page grows by itself —
      publish a project in the admin and it appears here, in its sector filter, in the
      sitemap and in the footer.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2 class="sr-only">All projects</h2>
      <div class="filters" data-filters>
{filters}
      </div>
      <div class="pgrid">
{cards}      </div>
      <p data-empty hidden style="color:var(--muted)">No projects in that sector yet.</p>
    </div>
  </section>

  <section class="cta">
    <div class="wrap">
      <div>
        <h2>Want your job on this page next?</h2>
        <p>Send us the scope and the programme. Written response in two working days.</p>
      </div>
      <a class="btn" href="contact.html">Request a quotation {ARROW}</a>
    </div>
  </section>

</main>
"""
    extra = f'<script type="application/ld+json">\n{ld}\n</script>\n'
    return (head("Projects — Meridian Trading &amp; Contracting",
                 "Completed warehouse, commercial tower, road, MEP and fit-out projects, "
                 "each with a full photo gallery and a written account of delivery.",
                 "projects.html", extra)
            + body + footer())


def build_project(p, nxt):
    slides = [{
        "full": f"assets/img/full/{img}.webp",
        "thumb": f"assets/img/thumb/{img}.webp",
        "alt": f"{p['title']} — {alt}",
        "title": alt,
        "caption": cap,
    } for img, alt, cap in p["images"]]

    thumbs = "\n".join(
        f"""        <button type="button" data-thumb aria-current="{'true' if i == 0 else 'false'}">
          <img src="{s['thumb']}" width="800" height="500" loading="lazy" decoding="async" alt="Show photo {i+1}: {html.escape(s['title'], quote=True)}">
        </button>""" for i, s in enumerate(slides))

    facts = "\n".join(f"        <dt>{k}</dt>\n        <dd>{v}</dd>" for k, v in p["facts"])

    gal_json = html.escape(json.dumps(slides), quote=True)

    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": p["title"],
        "url": f"https://example.com/project-{p['slug']}.html",
        "abstract": re.sub(r"\s+", " ", p["excerpt"]),
        "dateCreated": p["facts"][5][1],
        "locationCreated": {"@type": "Place", "name": p["facts"][1][1]},
        "image": [f"https://example.com/assets/img/full/{i[0]}.webp" for i in p["images"]],
        "provider": {"@type": "GeneralContractor", "name": "Meridian Trading & Contracting"},
    }, indent=2)

    body = f"""{masthead('projects')}
<main id="main">

  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a> <span>/</span>
        <a href="projects.html">Projects</a> <span>/</span> {p['title']}
      </nav>
      <p class="eyebrow eyebrow--light" style="margin-top:22px">{p['sector_label']}</p>
      <h1>{p['title']}</h1>
      <p>{p['excerpt']}</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="pdetail">

        <div>
          <div data-gallery="{gal_json}">
            <div class="gal__stage" data-open-lb>
              <img data-stage-img src="{slides[0]['full']}" width="1600" height="1000"
                   fetchpriority="high" decoding="async" alt="{html.escape(slides[0]['alt'], quote=True)}">
              <button class="gal__nav gal__nav--prev" type="button" data-step="-1">
                {CHEV_L}<span class="sr-only">Previous photo</span>
              </button>
              <button class="gal__nav gal__nav--next" type="button" data-step="1">
                {CHEV_R}<span class="sr-only">Next photo</span>
              </button>
              <span class="gal__zoom">{ZOOM} <i class="is-mouse">Click to enlarge</i><i class="is-touch">Tap to enlarge</i></span>
            </div>
            <div class="gal__thumbs">
{thumbs}
            </div>
          </div>

          <div class="prose">
{p['writeup'].strip()}
          </div>
        </div>

        <aside class="facts">
          <div class="facts__head">Project facts</div>
          <dl>
{facts}
          </dl>
          <div class="facts__foot">
            <a class="btn" href="contact.html">Discuss a similar job {ARROW}</a>
          </div>
        </aside>

      </div>

      <div class="nextproj">
        <span style="color:var(--muted)">{len(p['images'])} photos in this gallery — use the arrows, your keyboard, or swipe on mobile.</span>
        <a href="project-{nxt['slug']}.html">
          <img src="assets/img/thumb/{nxt['images'][0][0]}.webp" width="800" height="500" loading="lazy" decoding="async" alt="">
          <span><small>Next project</small><b>{nxt['title']}</b></span>
          {ARROW}
        </a>
      </div>
    </div>
  </section>

</main>

<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Project photo viewer">
  <div class="lb__bar">
    <span data-lb-pos>1 / {len(slides)}</span>
    <span>{p['title']}</span>
    <button class="lb__close" type="button">{XMARK}<span class="sr-only">Close viewer</span></button>
  </div>
  <div class="lb__stage">
    <button class="lb__nav lb__nav--prev" type="button" data-lb-step="-1">{CHEV_L}<span class="sr-only">Previous photo</span></button>
    <img data-lb-img src="" alt="">
    <button class="lb__nav lb__nav--next" type="button" data-lb-step="1">{CHEV_R}<span class="sr-only">Next photo</span></button>
  </div>
  <p class="lb__cap" data-lb-cap></p>
</div>
"""
    extra = f'<script type="application/ld+json">\n{ld}\n</script>\n'
    desc = re.sub(r"\s+", " ", p["excerpt"])
    return (head(f"{p['title']} — {BRAND_FULL}", desc,
                 f"project-{p['slug']}.html", extra)
            + body + footer())


def build_contact():
    body = f"""{masthead('contact')}
<main id="main">

  <section class="phead">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span>/</span> Contact</nav>
      <h1>Tell us what you need built.</h1>
      <p>Scope, location and the date it has to be finished. You get a named contact
      and a written response within two working days.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="contactgrid">
        <div>
        <h2 class="sr-only">Enquiry form</h2>
        <form data-demo-form novalidate>
          <div class="field">
            <label for="c-name">Your name</label>
            <input id="c-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="c-company">Company</label>
            <input id="c-company" name="company" type="text" autocomplete="organization">
          </div>
          <div class="field">
            <label for="c-phone">Phone</label>
            <input id="c-phone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="c-sector">Type of work</label>
            <select id="c-sector" name="sector">
              <option>General contracting</option>
              <option>Design &amp; build</option>
              <option>MEP package</option>
              <option>Fit-out</option>
              <option>Materials supply</option>
            </select>
          </div>
          <div class="field">
            <label for="c-msg">Scope and programme</label>
            <textarea id="c-msg" name="message" required></textarea>
          </div>
          <button class="btn" type="submit">Send enquiry {ARROW}</button>
          <p data-form-msg hidden style="margin-top:18px;color:var(--steel)"></p>
        </form>
        </div>

        <div class="infocard">
          <h3>Direct contact</h3>
          <dl>
            <dt>Head office</dt>
            <dd>Unit 14, Industrial Avenue<br>Port District</dd>
            <dt>Telephone</dt>
            <dd><a href="tel:+10000000000">+1 000 000 0000</a></dd>
            <dt>Hours</dt>
            <dd>Monday to Saturday, 08:00–18:00</dd>
            <dt>Tenders</dt>
            <dd>Send drawings and the bill of quantities with your enquiry and we
            will confirm receipt the same day.</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

</main>
"""
    return (head(f"Contact — {BRAND_FULL}",
                 "Request a quotation from Meridian Trading &amp; Contracting. "
                 "Written response within two working days.",
                 "contact.html")
            + body + footer())


# --------------------------------------------------------------------------

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {name:52s} {len(content.encode()) / 1024:6.1f} KB")


def main():
    print("building demo…")
    write("index.html", build_index())
    write("projects.html", build_projects())
    for i, p in enumerate(PROJECTS):
        write(f"project-{p['slug']}.html",
              build_project(p, PROJECTS[(i + 1) % len(PROJECTS)]))
    write("contact.html", build_contact())

    urls = ["", "projects.html", "contact.html"] + [f"project-{p['slug']}.html" for p in PROJECTS]
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>https://example.com/{u}</loc></url>\n" for u in urls)
          + "</urlset>\n")
    write("sitemap.xml", sm)
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: https://example.com/sitemap.xml\n")


if __name__ == "__main__":
    main()
