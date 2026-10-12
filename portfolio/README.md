# Abdellah Bouhaddi — Portfolio

Static personal site: HTML, CSS, and JavaScript only. No server or database.

This folder is published to GitHub Pages by the workflow in
`.github/workflows/pages.yml` at the repository root. Every push to `main` that
touches `portfolio/` redeploys the site.

## Local preview

From this folder:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Updating the resume

`assets/Abdellah_Bouhaddi_CV.pdf` is the file the site links to. After
rebuilding the CV from the repository root (`python build_cv_v22.py`), copy the
new PDF from `output/pdf/` over this file and commit it.

## One-time GitHub Pages setup

In the GitHub repository: **Settings → Pages → Source: GitHub Actions**.
The site is then live at `https://abdllahbhd.github.io/Portfolio/`.
A custom domain can be added in the same settings page.
