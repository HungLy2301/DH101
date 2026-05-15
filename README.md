# Hung Ly — DH 101 Portfolio

A portfolio of critical making, research, and reflection on AI, power, and accountability.
Built for DH 101: Critical Making in the Age of AI · Denison University · Spring 2026.

🌐 **Live site:** [hungly2301.github.io](https://hungly2301.github.io/)

---

## What this is

This repository contains a complete portfolio website documenting twelve
projects ("makes") produced across the semester. Each make is a different
artifact form — a comic, a GIF, a Twine game, a counter-map, a network
diagram, an infographic, a data visualization, a speculative newspaper — and
each one extends the same central argument: that AI is not a tool but a
system of power, and that part of the work of seeing it clearly is making
its hidden costs visible.

The site itself is a fifth artifact: an attempt to make the argument visible
through editorial design, careful accessibility, and transparent attribution.

---

## Structure

```
DH101/
├── docs/                       ← GitHub Pages source
│   ├── index.html              ← Home page
│   ├── about.html              ← About me
│   ├── journey.html            ← All 12 makes (with search + filter)
│   ├── final-reflection.html   ← Final reflection essay
│   ├── design-ai-usage.html    ← How I use AI
│   ├── ethics.html             ← Ethics page
│   ├── sustainability-accessibility.html
│   ├── styles.css              ← Design system
│   ├── script.js               ← Interactions (dark mode, search, etc.)
│   ├── makes/
│   │   ├── make1.html  · The Anatomy of an Image (DALL·E)
│   │   ├── make2.html  · Two Selves, One Algorithm (Selfies)
│   │   ├── make3.html  · Cream-Puff Boys (Comic)
│   │   ├── make4.html  · Progress Loop (GIF)
│   │   ├── make5.html  · What Voyant and GPT Can't Feel (Text Analysis)
│   │   ├── make6.html  · The Map They Didn't Draw (Counter-Map)
│   │   ├── make7.html  · I Have No Node (Networks)
│   │   ├── make8.html  · Strange Inventory (Tracery Bot)
│   │   ├── make9.html  · The Invisible Workforce (Infographic)
│   │   ├── make10.html · The Interview (Twine Game)
│   │   ├── make11.html · What the Cloud Drinks (Datawrapper)
│   │   └── make12.html · The Last Human Therapist (Speculative)
│   └── assets/                 ← Images, GIFs, embedded HTML, resume
├── makes/                      ← Source markdown for each make
├── reflections/                ← Source markdown for each weekly reflection
└── README.md                   ← This file
```

---

## Features

- **Editorial design system** — custom typography (Fraunces + Newsreader),
  scholarly palette, asymmetric grids, generous spacing.
- **Light + dark mode** — toggleable, respects `prefers-color-scheme`,
  persists in localStorage.
- **Responsive** — works on desktop and mobile; tested at 375px, 768px,
  1280px, 1920px viewports.
- **Accessible** — semantic HTML, ordered headings, alt text on every image,
  WCAG AA contrast in both themes, `prefers-reduced-motion` respected.
- **Filter + search** — on the Journey page, filter by project type and
  search across all 12 makes.
- **Embedded artifacts** — the Twine game, speculative newspaper, Datawrapper
  map, and Google My Maps are embedded via iframe, not screenshotted.

---

## Technical notes

- **Static site** — no build step, no frameworks, no server. Just HTML, CSS,
  and ~100 lines of vanilla JavaScript.
- **No analytics or trackers** — only third-party requests are Google Fonts
  and the three iframe embeds.
- **Image compression** — all images under 500KB; lazy-loaded where below
  the fold.
- **Hosted on GitHub Pages** from the `/docs` folder.

---

## Local development

To run this site locally:

```bash
# clone the repo
git clone https://github.com/hungly2301/DH101.git
cd DH101/docs

# open with any static server, e.g.
python3 -m http.server 8000
# then visit http://localhost:8000
```

Or just open `docs/index.html` directly in a browser.

---

## Course context

DH 101: Critical Making in the Age of AI · Spring 2026
Instructor: [Course instructor at Denison University]
Final portfolio rubric weights: Reflections (25), Making Quality (25),
Transparency &amp; Ethics (20), Design &amp; Accessibility (15),
Technical Execution (15).

---

## Contact

- Hung (Harry) Ly — Financial Economics, Denison University
- Email: [ly_h1@denison.edu](mailto:ly_h1@denison.edu)
- LinkedIn: [hung-ly-seniorconsultant](https://www.linkedin.com/in/hung-ly-seniorconsultant/)
- GitHub: [@hungly2301](https://github.com/hungly2301)

---

© 2026 Hung Ly. Reflections, artifacts, and writing are released for
educational viewing. Please contact me before reuse.