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
    no bundler, no build step. CSS and the `work/*.html` pages are stored **minified
    on one line**.
  - CV generator: Python 3.13 with `python-docx` (DOCX), `reportlab` (PDF),
    `pypdf` (audit script). No `requirements.txt` — packages are installed globally.
- **Package manager:** none. There is no `package.json`; never add npm scripts
  or `node_modules` for the site.

## Essential Commands

```bash
# Preview the site locally (from the site folder, then open http://localhost:8080)
cd portfolio && python -m http.server 8080

# Build the current CV: writes the .docx to the repo root and the .pdf to output/pdf/
python build_cv_v22.py

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
  site links to. It is a hand-copied CV build; after regenerating the CV, copy the
  new PDF from `output/pdf/` over it and commit.
- **CV scripts** (`generate_cv.py`, `build_cv_v15..v22.py`, `build_cv_v16_pdf.py`)
  are versioned snapshots at the root; `build_cv_v22.py` is the latest. Each builds
  DOCX and PDF from the same inline content with `python-docx` + `reportlab`.
  `generate_cv.py` is legacy and writes to a hardcoded `D:\abdellah\New folder`.
- **Deploy:** GitHub Pages via `.github/workflows/pages.yml`, which uploads the
  `portfolio/` folder on every push to `main` that touches it (Pages source must
  be set to "GitHub Actions" in repo settings). No server, no database, no backend.
- **`research/`** holds the portfolio market study / redesign brief
  (`portfolio-market-study-2026-09-21.md`) that drove the current site structure.
- **`tmp/`, `output/`, root-level `*.docx`/`*.pdf`/`*.png`** are generated
  artifacts and render previews. They are git-ignored; rebuild them with
  `build_cv_v22.py` (deps in `requirements.txt`) instead of hand-editing.
- **Minified assets:** when editing `styles.css` or `work/*.html`, keep them on
  one line (prettify to edit, re-minify before saving) so the committed diff stays
  consistent with the existing files.

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
- Prefer editing existing files over creating new ones. Do not create a new
  `build_cv_vNN.py` unless the user asks for a new CV version.
