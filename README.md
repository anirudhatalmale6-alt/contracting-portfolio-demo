# Trading & Contracting — portfolio site design demo

A design demo for a projects-led contracting website. Everything on screen is a
placeholder: "Meridian Trading & Contracting" is not a real company, the photos are
stock stand-ins, and the figures are invented. The **layout, gallery behaviour and
content structure** are the real deliverable.

## What it demonstrates

- Projects grid with sector filtering
- Project detail page: image gallery (lightbox, next/prev, keyboard, swipe),
  rich write-up (headings, lists, quote, table, links) and a fact sheet
- Fully responsive, mobile-first
- SEO: unique titles/descriptions, canonical URLs, Open Graph, JSON-LD, sitemap

## Measured Lighthouse scores (mobile preset)

| Page | Performance | Accessibility | Best practices | SEO |
|---|---|---|---|---|
| Home | 89 | 100 | 100 | 100 |
| Projects | 97 | 100 | 100 | 100 |
| Project detail | 95 | 100 | 100 | 100 |
| Contact | 100 | 100 | 100 | 100 |

Desktop preset scores 100 on performance across all pages.

## Structure

`build.py` generates the static HTML from a single `PROJECTS` list. That list maps
1:1 onto the WordPress custom post type that follows, so the markup signed off here
is the markup the theme outputs.

    python3 build.py
    python3 -m http.server 8000
