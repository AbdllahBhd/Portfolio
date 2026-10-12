# Project Memory (CLAUDE.md)

> This file is automatically loaded by Claude Code at the start of every session.
> Keep it short and high-signal: Claude reads it every time, so every line costs context.

## Project Overview

- **Name:** Abdellah Bouhaddi — Portfolio & CV workspace
- **What it does:** A static personal portfolio site (`portfolio/`) for a
  full-stack / .NET software engineer in Dubai, hosted on GitHub Pages, plus the
  Python scripts that generate the matching CV (DOCX + PDF) linked from the site.
- **Tech stack:**
  - Site: hand-written HTML5, CSS, vanilla JS (ES2020, `"use strict"`). No framework,
    no bundler, no build step. Inter is loaded from Google Fonts. Dark theme by
    default, light via `prefers-color-scheme` or the header toggle (stored in
    `localStorage`, applied by an inline script before first paint).
  - CV generator: Python 3.13 with `python-docx` (DOCX), `reportlab` (PDF),
    `pypdf` (audit script). No `requirements.txt` — packages are installed globally.
- **Package manager:** none. There is no `package.json`; never add npm scripts
  or `node_modules` for the site.

## Essential Commands

```bash
# Preview the site locally (or use the "portfolio" entry in .claude/launch.json)
python -m http.server 8080 --directory portfolio

# Build a NEW CV version: bumps CV_VERSION, writes the numbered .docx (root) and .pdf
# (output/pdf/), and copies the PDF to portfolio/assets/ so the next push publishes it
python build_cv.py
# Rebuild a specific number without bumping: python build_cv.py --version 23

# Reconcile CV text across every .pdf/.docx in the root and check that
# portfolio/assets/Abdellah_Bouhaddi_CV.pdf matches the baseline (read-only)
python research/audit_cv.py

# Regenerate Codex mirrors after editing .claude/skills or .claude/commands
bash scripts/sync-codex.sh
```

There is **no lint, typecheck, or test script**. The Stop hook (`done-gate.sh`)
passes through because there is no `package.json`. Verification is manual:
preview the site in a browser (desktop + 760px mobile breakpoint), and for the CV
open the generated PDF/DOCX and read it.

## Architecture Notes

- **One git repo at the workspace root** (`origin` = `github.com/AbdllahBhd/Portfolio`,
  default branch `main`). The site, CV scripts, research, and AI config are all
  tracked; generated CV files are ignored (see `.gitignore`). Only `portfolio/`
  is published.
- **Site entry point:** `portfolio/index.html` — a single page with sections
  `#top` (hero), `#work`, `#experience`, `#stack`, `#about`, `#contact`.
  Case-study pages live in `portfolio/work/` (`matmak.html`, `hexis-training.html`,
  `xshield.html`). Shared styles in `portfolio/css/styles.css`, behavior in
  `portfolio/js/main.js` (mobile menu toggle, focus management, footer year).
- **Resume download:** `portfolio/assets/Abdellah_Bouhaddi_CV.pdf` is what the
  site links to. `build_cv.py` overwrites it on every run; commit it together with
  `CV_VERSION` and the script so the pushed site always serves the latest build.
- **CV generator:** `build_cv.py` holds all CV content as Python constants near the
  top (`PROFILE`, `SKILLS`, `MATMAK_*`, `CLIENT_PROJECTS`, ...) and renders DOCX
  with `python-docx` and PDF with `reportlab`. `CV_VERSION` (tracked) is the last
  built number; every run increments it. Older `build_cv_v15..v17.py`,
  `build_cv_v16_pdf.py`, and `generate_cv.py` are frozen historical snapshots.
- **Deploy:** GitHub Pages via `.github/workflows/pages.yml`, which uploads the
  `portfolio/` folder on every push to `main` that touches it (Pages source must
  be set to "GitHub Actions" in repo settings). No server, no database, no backend.
- **`research/`** holds the portfolio market study / redesign brief
  (`portfolio-market-study-2026-09-21.md`) that drove the current site structure.
- **`tmp/`, `output/`, root-level `*.docx`/`*.pdf`/`*.png`** are generated
  artifacts and render previews. They are git-ignored; rebuild them with
  `build_cv.py` (deps in `requirements.txt`) instead of hand-editing.
- **Stylesheet conventions:** `styles.css` is readable and sectioned, with all
  colors as tokens on `:root` (dark) and `:root[data-theme="light"]` plus the
  matching `prefers-color-scheme` block. Never hardcode a color on a component.
  The three `work/*.html` case-study pages are still minified single-line files
  and share the header markup and classes of `index.html`.

## Rules

Detailed conventions live in `.claude/rules/` and are loaded automatically:

- @.claude/rules/code-style.md
- @.claude/rules/pr.md
- @.claude/rules/workflow.md

API conventions load on demand as a skill (`.claude/skills/api-conventions/`) —
only sessions that touch an API pay for them. This project currently has no API.

## Session & Context Hygiene

- When compacting this conversation, always preserve the full list of modified
  files, the current task plan status, and any verification steps used.
- Unrelated new task → suggest starting a fresh session instead of continuing here.

## Hard Constraints (always follow)

- Never commit secrets, API keys, or `.env` files.
- Never push directly to `main` — always work on a feature branch and merge via PR.
- There is no automated test suite; before claiming a site task complete, preview
  the page in a browser and say explicitly that verification was manual.
- Prefer editing existing files over creating new ones. CV changes go into
  `build_cv.py`; never create another `build_cv_vNN.py`.
