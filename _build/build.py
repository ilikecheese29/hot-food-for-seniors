"""Builds the site's HTML pages.

Each file in _build/pages/ holds one page's main content. The first line is a
comment with the page's settings, for example:

    <!-- {"title": "Pricing", "description": "...", "nav": "pricing"} -->

This script wraps every page in the shared <head>, header and footer below and
writes the finished file to the site's root folder. Run it after any edit:

    python _build/build.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = Path(__file__).resolve().parent / "pages"

SITE = "Warm Bowl"

NAV = [
    ("how", "how-it-works.html", "How it works"),
    ("food", "food.html", "The food"),
    ("pricing", "pricing.html", "Pricing"),
    ("safety", "safety.html", "Safety"),
    ("faq", "faq.html", "FAQ"),
]

BOWL_SVG = (
    '<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true">'
    '<path d="M15 6.5c-1.6 2.2 1.6 3.8 0 6.5M20.5 5c-1.6 2.2 1.6 3.8 0 6.5M26 6.5c-1.6 2.2 1.6 3.8 0 6.5" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
    '<path d="M5 17.5h31c0 8.3-6.9 15-15.5 15S5 25.8 5 17.5z" fill="currentColor"/>'
    '<rect x="14.5" y="33.5" width="12" height="2.5" rx="1.25" fill="currentColor"/></svg>'
)

FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500"
    "&family=Public+Sans:wght@400;500;600"
    "&family=IBM+Plex+Mono:wght@400;500"
    "&family=Noto+Serif+SC:wght@500;600"
    "&family=Noto+Sans+SC:wght@400;500"
    "&display=swap"
)


def header(active: str, lang: str) -> str:
    links = []
    for key, href, label in NAV:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{href}"{current}>{label}</a>')
    if lang == "zh":
        links.append('<a href="index.html" lang="en">English</a>')
        cta = '<a class="btn btn-primary btn-sm" href="zh.html#waitlist" lang="zh-Hans">加入候补名单</a>'
    else:
        current = ' aria-current="page"' if active == "zh" else ""
        links.append(f'<a href="zh.html" lang="zh-Hans"{current}>中文</a>')
        cta = '<a class="btn btn-primary btn-sm" href="waitlist.html">Join the waitlist</a>'
    nav_html = "\n        ".join(links + [cta])
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="Warm Bowl, home">
      {BOWL_SVG}
      <span class="brand-name">Warm Bowl</span>
      <span class="brand-zh" lang="zh-Hans">暖碗</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" aria-label="Main">
        {nav_html}
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="index.html" aria-label="Warm Bowl, home">
        {BOWL_SVG}
        <span class="brand-name">Warm Bowl</span>
        <span class="brand-zh" lang="zh-Hans">暖碗</span>
      </a>
      <p class="footer-blurb">Hot dinners from local restaurants, brought by the same trusted driver every time. Starting in Bayview Hill, Richmond Hill.</p>
    </div>
    <div>
      <h3>The service</h3>
      <ul>
        <li><a href="how-it-works.html">How it works</a></li>
        <li><a href="food.html">The food</a></li>
        <li><a href="pricing.html">Pricing</a></li>
        <li><a href="safety.html">Drivers and safety</a></li>
        <li><a href="faq.html">Questions</a></li>
      </ul>
    </div>
    <div>
      <h3>Warm Bowl</h3>
      <ul>
        <li><a href="about.html">Our story</a></li>
        <li><a href="drive.html">Drive with us</a></li>
        <li><a href="restaurants.html">For restaurants</a></li>
        <li><a href="zh.html" lang="zh-Hans">中文</a></li>
        <li><a href="privacy.html">Privacy</a></li>
      </ul>
    </div>
    <div>
      <h3>Get in touch</h3>
      <ul>
        <li><a href="mailto:warmbowlmeals@gmail.com">warmbowlmeals@gmail.com</a></li>
        <li>Prefer WhatsApp or WeChat? Say so on the <a href="waitlist.html">waitlist form</a> and we'll message you there.</li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-base">
    <span>&copy; <span data-year>2026</span> Warm Bowl. Richmond Hill, Ontario.</span>
    <span>Spring 2027 test, summer 2027 pilot.</span>
  </div>
</footer>"""


def page(meta: dict, body: str) -> str:
    lang = meta.get("lang", "en")
    html_lang = "zh-Hans" if lang == "zh" else "en-CA"
    title = meta["title"]
    full_title = title if meta.get("bare_title") else f"{title} | {SITE}"
    desc = meta["description"]
    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#f6f0e4">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header(meta.get("nav", ""), lang)}
<main id="main">
{body.strip()}
</main>
{FOOTER}
<script src="assets/js/config.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def main() -> None:
    count = 0
    for src in sorted(PAGES.glob("*.html")):
        text = src.read_text(encoding="utf-8")
        match = re.match(r"\s*<!--\s*(\{.*?\})\s*-->", text, re.S)
        if not match:
            raise SystemExit(f"{src.name}: first line must be a settings comment")
        meta = json.loads(match.group(1))
        body = text[match.end():]
        out = ROOT / src.name
        out.write_text(page(meta, body), encoding="utf-8", newline="\n")
        count += 1
        print(f"built {out.name}")
    print(f"{count} pages")


if __name__ == "__main__":
    main()
