#!/usr/bin/env python3
"""
Optional. Regenerates the HTML pages from the shared shell in this file.

You do NOT need this to run the site — the .html files it produces are ordinary
static pages you can edit by hand. Use it only when you want to change something
that appears on every page (the navigation, the footer, the meta tags), so you
don't have to make the same edit eight times.

    cd _tools && python3 build.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = "BiomE Lab"
TAGLINE = "Biodiversity Genomics &amp; Evolution"
BASE_URL = "https://kulkarni-lab.github.io"

NAV = [
    ("research.html", "Research"),
    ("people.html", "People"),
    ("publications.html", "Publications"),
    ("news.html", "News"),
    ("spiderindia.html", "SpiderIndia"),
    ("join.html", "Join us"),
    ("students.html", "Students"),
    ("contact.html", "Contact"),
]

LOGO = """<svg viewBox="0 0 100 100" class="mark" aria-hidden="true" focusable="false">
  <g fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round">
    <path d="M44 50 H11"/>
    <path d="M52.5 44.6 L66.5 14.7"/>
    <path d="M54.1 45.7 L76.9 21.7"/>
    <path d="M55.3 47.2 L84.5 31.8"/>
    <path d="M55.9 49.0 L88.5 43.7"/>
    <path d="M55.9 51.0 L88.5 56.3"/>
    <path d="M55.3 52.8 L84.5 68.2"/>
    <path d="M54.1 54.3 L76.9 78.3"/>
    <path d="M52.5 55.4 L66.5 85.3"/>
  </g>
  <circle cx="50" cy="50" r="4.6" fill="currentColor"/>
  <circle class="mark-lone" cx="10" cy="50" r="5.4"/>
  <circle class="mark-tip" cx="66.9" cy="13.7" r="5.4"/>
  <circle class="mark-tip" cx="77.6" cy="21.0" r="5.4"/>
  <circle class="mark-tip" cx="85.4" cy="31.3" r="5.4"/>
  <circle class="mark-tip" cx="89.5" cy="43.5" r="5.4"/>
  <circle class="mark-tip" cx="89.5" cy="56.5" r="5.4"/>
  <circle class="mark-tip" cx="85.4" cy="68.7" r="5.4"/>
  <circle class="mark-tip" cx="77.6" cy="79.0" r="5.4"/>
  <circle class="mark-tip" cx="66.9" cy="86.3" r="5.4"/>
</svg>"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/{page}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{base}/{page}">
<meta property="og:image" content="{base}/assets/img/og-card.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="shell header-inner">
    <a class="wordmark" href="index.html">
      {logo}
      <span class="wordmark-text">
        <span class="wordmark-name">BiomE Lab</span>
        <span class="wordmark-sub">Biodiversity Genomics &amp; Evolution &middot; CSIR-CCMB</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
{nav}
    </nav>
  </div>
</header>

<main id="main">
"""

FOOT = """</main>

<footer class="site-footer">
  <div class="shell">
    <div class="footer-grid">
      <div>
        <h4>BiomE Lab</h4>
        <address>
          Laboratory for Conservation of Endangered Species (LaCONES)<br>
          CSIR-Centre for Cellular and Molecular Biology<br>
          162 Pillar, PVNR Expressway, Attapur Ring Road<br>
          Hyderguda, Hyderabad 500 048, India
        </address>
      </div>
      <div>
        <h4>Pages</h4>
        <ul>
          <li><a href="research.html">Research</a></li>
          <li><a href="people.html">People</a></li>
          <li><a href="publications.html">Publications</a></li>
          <li><a href="news.html">News</a></li>
          <li><a href="students.html">Students and interns</a></li>
        </ul>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="https://scholar.google.co.in/citations?user=xo9jTM0AAAAJ&amp;hl=en">Google Scholar</a></li>
          <li><a href="https://github.com/kulkarni-lab">GitHub</a></li>
          <li><a href="https://www.inaturalist.org/projects/spiderindia">SpiderIndia on iNaturalist</a></li>
          <li><a href="https://www.ccmb.res.in/">CSIR-CCMB</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="mailto:siddharth@csirccmb.org">siddharth@csirccmb.org</a></li>
          <li><a href="tel:+914024006427">+91 40 2400 6427</a></li>
          <li><a href="join.html">Open positions</a></li>
        </ul>
      </div>
    </div>
    <div class="colophon">
      <span>&copy; <span id="year">2026</span> BiomE Lab, CSIR-CCMB. Photographs by lab members unless noted.</span>
      <em>&ldquo;At what point is a wasp ever going to have a chat with a spider?&rdquo; &mdash; Karl Pilkington</em>
    </div>
  </div>
</footer>

<script src="data/publications.js"></script>
<script src="data/people.js"></script>
<script src="data/projects.js"></script>
<script src="data/news.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'      <a href="{href}"{cur}>{label}</a>')
    return "\n".join(out)


def build(page, title, desc, body):
    html = HEAD.format(title=title, desc=desc, base=BASE_URL, page=page,
                       logo=LOGO, nav=nav_html(page)) + body + FOOT
    with open(os.path.join(ROOT, page), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", page)


if __name__ == "__main__":
    import pages
    for spec in pages.PAGES:
        build(*spec)
