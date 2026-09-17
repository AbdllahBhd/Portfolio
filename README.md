# Abdellah Bouhaddi — Portfolio

Static personal site. Open `index.html` locally, or host it on GitHub Pages. No server or database is required.

## Local preview

Open `portfolio/index.html` in a browser, or from this folder:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Host on GitHub Pages (recommended)

This site is HTML, CSS, and JavaScript only. GitHub Pages is enough. You do not need a VPS.

1. Create a public repository, for example `AbdllahBhd.github.io` (this URL is the simplest) or `portfolio`.
2. Push the contents of this `portfolio` folder to the repository root (not nested inside another folder).
3. In GitHub: **Settings ? Pages ? Source: Deploy from a branch ? main / (root)**.
4. After a minute the site is live at:
   - `https://abdllahbhd.github.io/` if the repo is named `AbdllahBhd.github.io`
   - or `https://abdllahbhd.github.io/portfolio/` if the repo is named `portfolio`

Optional later: point a custom domain (`abdellahbouhaddi.com`) at GitHub Pages in the same Pages settings. Still no VPS.

## When you would need a VPS

Only if you add a backend later (ASP.NET, Node, a database, a contact form that stores messages, auth, and so on). This portfolio does not need that.
