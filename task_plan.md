# Plan: portfolio design refinement (Phase 2 of the 2026-10-20 audit)

**Objective:** Refine the existing portfolio look into a distinctive, coherent, accessible site where one thing leads per section, the work tells an outcome-first story, and the phone experience reaches the work fast.

Branch: `feat/design-refinement` (from `main`). One commit per task, Conventional Commits.
Screenshot binaries go in a commit of their own.

## Scope

**In scope:** every audit finding listed in the Findings map below (F1 to F24), including:
- re-capturing the 20 screenshots, plus an 800×500 phone/retina size of each
- two new short case studies
- skills evidence from the user's answers

**Out of scope:**
- **A new visual identity.** The user chose "refine current look", so Inter, JetBrains Mono, the blue accent and the light-default theme switch all stay.
- **Removing the terminal labels or the fit checker.** The user chose "keep as is", so they get accessibility and copy fixes only.
- **`build_cv.py` and the CV files.** See open question 2.
- **npm, a framework, a build step, analytics, deploy.** No push, PR or merge without an explicit ask.

## Approach

**Refinement, not redesign.** The tokens, fonts and component vocabulary stay. What changes is composition: one element leads per section, and the equal-card grids become the forms their content actually is.
- Skills become layered rows.
- Background becomes a dated timeline list.
- Q&A becomes a hairline-separated list.
- MATMAK stays dominant.

**Screenshot frame.** Every screenshot gets one consistent frame in the site's own design: a neutral bar carrying the real domain name. The bar sits outside the 16:10 image, so the frame never forces another re-capture. It keeps client brands from owning the page.

**Content uses only known facts:** the site, `build_cv.py`, and the user's 2026-10-20 answers.
- SQL Server: MATMAK, RH Partner
- JWT: MATMAK, RH Partner
- PostgreSQL: Supabase in the Flutter freelance role, after migrating from Firestore
- TypeScript and Bootstrap: university projects

**Shared CSS.** `styles.css` serves all 6 pages, so every CSS task is checked on the case pages too. Home-only restyles are scoped with home-only selectors, for example `.stats > .stat`, not `.stat`, which `.case-stats` also uses.

**Order.** Tasks are ordered so later tasks don't redo earlier ones:
1. tokens and contrast first
2. then the screenshots
3. then composition (which also defines the phone stats line)
4. then work cards, case studies, the phone pass, accessibility, cleanup, and the final review

## Findings map (from the audit; Task 10 confirms each ID is closed)

| ID | Finding | Task |
|---|---|---|
| F1 | Equal-card grids and the same section template 7 times; nothing leads after the hero | 4 |
| F2 | Work section owned by the client brands; no consistent screenshot frame | 5 |
| F3 | Chat and WhatsApp widgets visible in the MATMAK and RH Partner screenshots | 2 |
| F4 | Cards list tasks, not outcomes; 5 ✓ bullets on MATMAK | 5 |
| F5 | HPL and RH Partner have no case study | 6 |
| F6 | First project at 2,208px on phone (2.7 screens); the page is 12,554px tall | 4, 7 |
| F7 | Resume button hidden in the header below 760px | 7 |
| F8 | Phone nav strip cut at "Backg…" with no scroll hint | 7 |
| F9 | Weak stats; count-up from 0 shows wrong numbers; ~40% has no context | 4 |
| F10 | "Every item … backed by a project" is false for 5 skills | 5 |
| F11 | 77 dead tab stops on `.tags li` (main.js:57); copy says "hover", which assumes a mouse | 8 |
| F12 | Inactive slider dots at 1.48:1 (light) and 1.73:1 (dark) | 3 |
| F13 | `.status` pill at 4.28:1 on the page background; pressed filter count at 3.65:1 | 3 |
| F14 | Focus lost when Next/Prev disables at a slider end | 8 |
| F15 | Touch targets under 44px: dots 24, Copy 47×29, arrows 38, `.btn.sm` 38 | 8 |
| F16 | Reduced motion misses `.track` smooth scroll and the `::before` transitions | 8 |
| F17 | Bright screenshots glare in dark mode; lightbox colours hard-coded; `theme-color` stays light | 3 |
| F18 | 1.58 MB of 1200px JPEGs on phone; no `srcset` | 2, 5 |
| F19 | Lightbox `<img>` with no `src` (detector `broken-image`) | 3 |
| F20 | Reveal content stays invisible if main.js fails | 8 |
| F21 | Slider ARIA: no "n of 4" labels; captions announce on load; fit checker has no `fieldset`; theme switch has no name on phone; CSS glyphs read aloud | 8 |
| F22 | `.callout` one-sided border (side-tab) | 9 |
| F23 | 23 em-dashes, the `✕` in HTML, and the `✓`/`◐` glyphs in CSS | 9 |
| F24 | Weights 650/750 and mono 600 not loaded (faux weights); dead CSS; duplicate `.fit`; inline `style=` attributes; to-top button covers content on phone | 3, 7, 9 |

## Standing gates

The gates are relative to the Task 1 baseline. Each finding a later task owns may remain until that task; nothing new may appear.

**G1: Impeccable detector.** Run `.claude/skills/impeccable/scripts/impeccable detect --json portfolio/index.html portfolio/work`.
- Pass: no rule or count above the baseline.
- After Task 3: no `low-contrast` and no `broken-image`.
- After Task 9: no `side-tab`.
- The only allowed final findings are `cramped-padding` (false positive: the detector doesn't resolve `clamp()`) and `overused-font` (Inter kept by decision).
- *Amendment (Task 4, 2026-10-20):* a new `cramped-padding` hit is allowed only if it is verified as a false positive and listed here with measured evidence. Without this, G1 would block a correct design the detector misreads.
  - FP-1: `.proof-facts` is reported as "flush against border-left". Measured: text is inset 25px from the border at 1440, 1280 and 1024px, and there is no border below 1000px.

**G2: XIAS static gates.** Run `PYTHONUTF8=1 python scripts/check_no_emoji.py portfolio` and `PYTHONUTF8=1 python scripts/lint_taste.py portfolio`.
- Pass: no count above the baseline.
- After Task 9: `check_no_emoji` exits 0.
- That gate flags en dashes too, so date ranges use a hyphen or "to".

**G3: scratch `measure.py`.** Playwright against `python -m http.server` serving `portfolio/`, never file://. It measures after `document.fonts.ready`, on all pages, in both themes:
- (a) no horizontal overflow at 280, 320, 375 and 414px
- (b) every internal href and `src` resolves to a 200 response
- (c) contrast of every text node meets 4.5:1, or 3:1 for large text
- (d) explicit UI-part pairs, each meeting 3:1:
  - `.status`
  - `.filters [aria-pressed=true] span` (text, so 4.5:1)
  - the inactive dots against the surface
- (e) with `hasTouch` and `isMobile` at 375px: interactive target sizes
- Pass: (a) and (b) always. (c) to (e) are relative to the baseline until Tasks 3 and 8.

**G4: manual look in the browser pane.** At 1280px and 375px, light and dark, on every page the task's CSS can reach. With shared CSS, that means all case pages too. Screenshots are shown. There is no lint, typecheck or test suite, so G1 to G4 are the gates.

## Tasks

- [x] **1. Scratch tooling and baseline**
  - Create a venv in the session scratchpad, then `pip install playwright` and `playwright install chromium`.
  - Write `measure.py` (G3) and `capture.py` there.
  - Record the baseline below:
    - the G1 and G2 counts
    - G3 (a) to (e)
    - the height of each block above the first slider at 375×812, which shows the 1,220px target in Task 7 is reachable
  - Done when:
    1. The baseline table below is filled with real output from all 4 current pages.
    2. Nothing is broken: `git status` shows only `task_plan.md` changed.
    3. No files changed outside `task_plan.md` and the scratchpad.

- [x] **2. Tokens, contrast, theme, font weights** (F12, F13, F17, F19, F24 weights)
  - Inter becomes a variable font (`wght@400..800`). Mono 600 becomes 500.
  - New tokens: dot, scrim, on-scrim, status-on-bg. Pairs to fix:
    - `.status`: at least 4.5:1 on every background
    - pressed filter count: at least 4.5:1
    - inactive dots: at least 3:1
  - Lightbox colours move to tokens.
  - `theme-color` follows the theme.
  - Dark mode dims the screenshots slightly.
  - The lightbox `img` gets its `src` from JS only when it opens (or JS creates the element).
  - Done when:
    1. G3 (c) and (d) report 0 failures in both themes. `lint_hardcodes.py` output filtered to `#[0-9a-f]{3,8}|rgba?\(|hsla?\(` lists only the slider-arrow lines (styles.css `.arrow`) and the `theme-color` meta. Every page's font URL contains `400..800`.
    2. Nothing is broken:
       - G1 shows no `low-contrast` and no `broken-image`.
       - The theme survives a reload.
       - G4 passes on all 4 pages.
    3. No files changed outside `portfolio/css/styles.css`, `portfolio/js/main.js` and the `<head>`/lightbox markup of `portfolio/**/*.html`.

- [x] **3. Re-capture the screenshots** (F3, F18 assets)
  - Capture the 5 sites at 1440×900.
  - Reject cookie banners. Hide chat and WhatsApp widgets with injected CSS.
  - Write `<site>-<n>.jpg` at 1200×750 and `<site>-<n>-800.jpg` at 800×500.
  - Done when:
    1. Dimension check: all 20 large files are 1200×750 and all 20 small files are 800×500. A contact sheet of the 40 images has been looked at and shows no widget, popup or banner. Byte totals are reported.
    2. Nothing is broken: G3 (b) passes, and G4 shows every slider on all 4 pages loading its 4 images.
    3. No files changed outside `portfolio/assets/screens/`.

- [x] **4. Composition: one thing leads** (F1, F6 stats, F9; home page)
  - **Stats:** `.stats > .stat` is reworked with the same facts.
    - ~40% leads, with its context.
    - The rest folds into one quieter line, which is also the phone stats line.
    - The `data-count` attributes and the count-up code go.
  - **Skills:** layered rows, with the layer name and its one-line purpose on the left and tags on the right.
  - **Background:** a dated timeline list.
  - **Q&A:** a hairline-separated list. The fit checker and terminal labels stay.
  - Done when:
    1. Checked in the pane:
       - `document.querySelectorAll('[data-count]').length === 0`, and `grep -c dataset.count portfolio/js/main.js` is 0.
       - At 1280px `#skills` rows compute to 2 columns.
       - `#background` is a `ul`/`ol` whose items each contain a `.when` date.
       - The children of `.skills`, `.bg-grid` and `.qa` have no card border or background.
       - Screenshots of each section at 1280 and 375 in both themes are shown.
    2. Nothing is broken: G1 to G3 show no regression, and G4 passes on the home page and all 3 case pages, since `.case-stats` shares `.stat`.
    3. No files changed outside `portfolio/index.html`, `portfolio/css/styles.css` and `portfolio/js/main.js`.

- [ ] **5. Work storytelling and skills evidence** (F2, F4, F10, F18 markup)
  - **Every home card gets:**
    - a `.outcome` sentence
    - at most 3 `.did li`
    - the domain frame
  - **Every slider image,** on the home page and the case pages, gets `srcset` (800w, 1200w) and `sizes`.
  - **The usages go where the user said:**
    - SQL Server and JWT in the MATMAK and RH Partner card tags and text
    - PostgreSQL/Supabase in the freelance `.job`
    - TypeScript and Bootstrap in the Background university entries
  - Done when:
    1. Checked by a pane JS run, with the output shown:
       - Location checks pass for every usage above.
       - Every `#skills .tags li` text also appears in `.tags` or text outside `#skills`.
       - Every `.work .card` has a non-empty `.outcome` and at most 3 `.did li`.
       - Every `img[data-zoom]` has a `srcset`.
    2. Nothing is broken: G1 to G3 show no regression, and G4 passes on all 4 pages.
    3. No files changed outside `portfolio/index.html`, `portfolio/work/*.html` (tags, srcset and frame markup) and `portfolio/css/styles.css`.

- [ ] **6. Two new case studies** (F5)
  - Write `portfolio/work/hpl-bodyfence.html` and `portfolio/work/rh-partner.html` in the shared template.
  - Link them from their cards.
  - Re-chain the "Next case study" links into one loop of 5.
  - Done when:
    1. A fact table below maps every claim on the 2 new pages to its source: a `build_cv.py` line, an `index.html` line or the user's answer. Any claim without a source fails. Both pages render at 1280 and 375 in both themes (screenshots), and G3 (b) shows the 5 next-links forming one loop.
    2. Nothing is broken: G1 and G2 show no regression, and each new page has one h1 and no skipped heading levels.
    3. No files changed outside `portfolio/work/`, `portfolio/index.html` and `CLAUDE.md` (the case-study list).

- [ ] **7. Phone experience** (F6, F7, F8, F24 to-top)
  - **Below 760px:**
    - The contact card becomes a compact action row.
    - The header keeps a compact Resume link, on all pages.
    - The nav strip gets an edge fade that hides at the scroll end.
  - **To-top button:** it hides before it would cover the footer.
  - Done when:
    1. Measured at 375×812 after `document.fonts.ready`:
       - The top of the first project slider is at most 1,220px (baseline 2,208px).
       - The Resume link is visible in the header on all 6 pages.
       - At maximum scroll the to-top button doesn't intersect the footer text.
    2. Nothing is broken: G3 (a) shows no overflow at 280 to 414px on all pages, and G4 passes on all pages.
    3. No files changed outside `portfolio/**/*.html`, `portfolio/css/styles.css` and `portfolio/js/main.js`.

- [ ] **8. Accessibility and interaction** (F11, F14, F15, F16, F20, F21)
  - **Tags:** no `tabIndex`. The highlight works only under `(hover: hover)`, and the copy matches.
  - **Slider:**
    - Focus moves to the other arrow when one disables.
    - The caption live region stays empty on load.
    - Slides are labelled "n of 4".
  - **Touch targets:** at least 44px on coarse pointers.
  - **Reduced motion** covers `.track` and `::before`.
  - **CSS glyphs** get empty alt text.
  - **Fit checker:** `#fit` becomes a `fieldset` with a `legend`.
  - **Theme switch:** buttons get an `aria-label`.
  - **Reveal:** hiding requires a class main.js sets.
  - Done when:
    1. Every check below passes, with the output shown:
       - `li[tabindex]` count is 0.
       - Next pressed to the last slide leaves `activeElement` on a slider button.
       - Each slide has an "n of 4" label.
       - Every caption is empty before interaction.
       - `#fit` is a `FIELDSET`.
       - G3 (e) reports every target at least 44px.
       - With main.js blocked (Playwright route abort), every `.reveal` has computed opacity 1.
       - With JS on, the reveals still animate, with no flash of hidden content at first paint (screenshot at 100ms).
    2. Nothing is broken: G1 to G3 show no regression, and G4 passes on all pages.
    3. No files changed outside `portfolio/js/main.js`, `portfolio/css/styles.css` and `portfolio/**/*.html`.

- [ ] **9. P3 cleanup** (F22, F23, F24 rest)
  - `.callout` gets a full hairline and surface instead of the side border.
  - Em-dashes go. Date ranges use a hyphen or "to"; titles and headings use a colon or middot.
  - The `✓` and `◐` glyphs become CSS or SVG marks.
  - The `✕` in each page's lightbox becomes an SVG icon.
  - Remove the dead CSS (`.cover`, `.layers`, `.fit table/caption/th/td`, `.lvl`), merge the duplicate `.fit`, and move inline `style=` attributes into classes.
  - Done when:
    1. `check_no_emoji.py portfolio` exits 0, `grep -rc 'style="' portfolio --include=*.html` totals 0, and G1 shows no `side-tab`.
    2. Nothing is broken: G3 passes in full and G4 passes on all 6 pages.
    3. No files changed outside `portfolio/`.

- [ ] **10. Final verification and review**
  - Run G1 to G4 in full on all 6 pages, at 1280 and 375, in both themes.
  - Run `/impeccable audit` again.
  - Run the `code-reviewer` agent on `git diff main...` and fix or rebut every finding.
  - Update the CLAUDE.md notes on the screenshots (800w variants, capture method) and the case studies.
  - Ask the user before any merge or push.
  - Done when:
    1. Every Findings-map ID F1 to F24 is marked closed below with its evidence. The re-audit scores at least 17/20 with no P1 left (baseline 14/20).
    2. Nothing is broken: G1 to G4 are fully green, with output shown, and every code-review finding is fixed or rebutted.
    3. No files changed outside `portfolio/`, `CLAUDE.md` and `task_plan.md`.

## Files touched

- `portfolio/index.html`
- `portfolio/work/{matmak,hexis-training,xshield}.html`
- New: `portfolio/work/{hpl-bodyfence,rh-partner}.html`
- `portfolio/css/styles.css`
- `portfolio/js/main.js`
- `portfolio/assets/screens/*` (20 replaced, 20 new)
- `CLAUDE.md`
- `task_plan.md`
- Scratch, not tracked: venv, `capture.py`, `measure.py`

## Risks and open questions

1. **Resolved 2026-10-20.** User's answer: "SQL Server in Docker was RH Partner and for bodyfence for wordpres database and hexis trauning in docker and for matmak on amazon server". Applied as:
   - SQL Server: RH Partner (in Docker) and MATMAK (on an AWS server)
   - Docker: added to HEXIS Training
   - BODYFENCE: its WordPress database. No engine was named, so no database tag is added.
2. **The site and CV drift apart.** The Supabase/PostgreSQL migration and the extra SQL Server and JWT usages are not in `build_cv.py`. Should the CV get them in a follow-up?
3. **Live sites may have changed or block headless capture,** HEXIS staging in particular. The fallback is to keep that site's old screenshots, cropped clear of the widgets, and report it.
4. **Diff size.** The diff exceeds pr.md's ~400-line guideline. Mitigation: one commit per task, with the binaries in a commit of their own.
5. **Thin case studies.** The HPL/BODYFENCE page rests on one CV fact, so it will be short and honest, not padded.
6. **Header space on phone.** The case-page headers are already crowded. If the Resume link doesn't fit at 280px, it becomes icon-only with an `aria-label`.

## Baseline (filled in by Task 1, 2026-10-20, 4 pages)

**G1 detect** (exit 2), 27 findings:

| Rule | Count |
|---|---|
| broken-image | 4 |
| cramped-padding | 13 |
| low-contrast | 3 |
| overused-font | 4 |
| side-tab | 3 |

**G2:**
- no-emoji: FAIL, 27 found (exit 1)
- taste: 6 advisory findings

**G3:**
- (a) Overflow at 280, 320, 375 and 414px: none.
- (b) Links: 93 checked, 0 bad.
- (c) Contrast, light theme:
  - pressed-filter count `5`: 3.66 (index)
  - `.status`: 4.27 (index, matmak, xshield)
  - Dark theme: 0 failures.
- (d) Inactive dots: min 1.48 (light) and 1.73 (dark). All 24 fail in each theme.
- (e) Targets under 44px at 375px with touch:
  - index: 132 total, of which 77 are `li[tabindex]`, plus dots 24×24 ×15, arrows 38×38, `.btn.sm` 38 tall, Copy 47×29, theme-switch buttons 38×28, nav links ×40 tall.
  - Case pages: 19 to 21 each.

**Phone metrics (375×812):**
- First slider top: 2,222px. Page height: 12,554px.
- Blocks above it: header 105, hero text 492, contact card 518, stats 562, work head 162, filters 138.
- Making the contact card compact (about 518 → 150) and the stats a single line (about 562 → 90) brings the first slider to about 1,300. Getting under 1,220 also needs about 80px trimmed from the hero/head/filter gaps. That is reachable.

## Fact table (filled in by Task 6)

_pending_

/goal every task in task_plan.md is checked off per its own "Done when", and the project's quality gates pass
