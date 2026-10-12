# Portfolio study and redesign brief

Abdellah Bouhaddi · 21 September 2026 · Target: full-stack / .NET software engineering roles in Dubai and the UAE.

## Recommendation

Position Abdellah as a **full-stack software engineer with a .NET foundation and practical production-delivery experience**. Show the work before a long skills inventory. Make frontend implementation, business workflows, integration, and operations visible together.

Feature three complementary stories: improving MATMAK's existing .NET platform with its team; architecting the HEXIS training application; and delivering XSHIELD through launch. Keep Java backend work, HPL integrations, teaching, mobile development, education, languages, and operational details accessible at the appropriate depth.

The next design should be a restrained, image-led engineering portfolio: concise introduction, real product evidence, clear contribution labels, dedicated project pages, and reliable mobile navigation. The recommendation is about information hierarchy first. A particular color, font, or animation is a design hypothesis, not a conclusion proven by the job market.

## 1. What informed this study

### Evidence and limits

| Input | Work completed | What it can establish |
| --- | --- | --- |
| Local CV collection | Extracted and compared the content of 22 root files: 14 PDFs and 8 DOCX files. Reviewed the latest baseline and unique differences across versions. | Candidate-provided experience, changes in positioning, details lost during shortening, contradictory wording. Not independent verification of employment or metrics. |
| Portfolio implementation | Read the current HTML, CSS, and JavaScript. | Content hierarchy, links, declared breakpoints, source-level defects. Not a rendered usability or accessibility test. |
| Dubai hiring sample | Six relevant employer/recruiter postings documented below. | Qualitative examples of role requirements. Not market-wide percentages, salary conclusions, or a complete UAE vacancy census. |
| Peer portfolios | Six public sites reviewed for extractable content and structure, including five related engineering profiles and one frontend reference. One additional case-study page inspected. | How peers communicate expertise and evidence. Not proof that their sites generated interviews. |
| UX and quality guidance | Nielsen Norman Group, W3C, and Google's web.dev. | Research-backed reading principles and technical acceptance criteria. Not a guarantee of recruiter preference. |

Searches combined Dubai/UAE with .NET, ASP.NET Core, full-stack, React, and Angular; direct employer and recruiter sources were preferred over job aggregators. The sample is deliberately target-specific and therefore not suitable for estimating technology market share. Most sampled roles are Dubai-based; this is not separate Abu Dhabi or Sharjah market research.

All sources were accessed during this study on 21 September 2026. Search crawl dates and relative posting ages are not reliable publication dates. Several career pages are undated, and indexed content may be stale. A visible posting does not establish that recruitment remains open. An aggregator described one Michael Page role differently; its original page requires 7+ years, so the original is used and the role is marked as a stretch reference.

The in-app browser reported no available browser. Therefore **visual comparison, responsive screenshots, interaction testing, and performance measurements remain unperformed**. This is a completed desk study and implementation brief, not a completed visual-design validation. No recruiter interviews, user tests, application submissions, or outreach were conducted.

### What was wrong with the previous decision process

The earlier updates relied mainly on CV content and design judgment; there was no documented peer or hiring benchmark. Reading CVs did not, by itself, establish the correct visual hierarchy. The designs overemphasized backend terminology, presented summary cards as if they were full case studies, and did not adequately substantiate interface work with real product evidence.

The earlier file-count statement also needs precision: there are 14 PDFs and 8 DOCX files in the root. The portfolio contains a fifteenth PDF, but it is a byte-identical copy of v14, not another CV version. The read-only reconciliation script is [audit_cv.py](audit_cv.py). The PDF skill was used for text reconciliation; no claim is made about auditing every CV's visual layout.

## 2. Dubai hiring evidence

These are requirement examples, not endorsements or a list of confirmed live vacancies.

| Source and role | Requirements relevant to the portfolio | Decision for Abdellah |
| --- | --- | --- |
| [Thrifty Car Rental UAE — .NET/React Full Stack Developer](https://ae.linkedin.com/jobs/view/net-react-full-stack-developer-at-thrifty-car-rental-uae-4459928493) | C#/.NET, React components and state, responsive interfaces, REST, EF Core, SQL Server, authentication, testable code; cloud exposure is a plus. | Make frontend proof prominent. Show a business feature from UI through API/data, with implementation detail rather than only a React badge. |
| [ECS ME — .NET Developer / ReactJS](https://ecsme.freshteam.com/jobs/XBAyMJM7Z1db/net-developer-reactjs) | 3+ years relevant .NET development, React and JS/TS, APIs/microservices, SQL Server/PostgreSQL, Azure/AWS; performance and responsive integration also mentioned. | MATMAK and HEXIS are complementary evidence, but do not present HEXIS as a .NET/React application: its backend is Laravel. |
| [iQuasar EMEA — Full Stack .NET / Angular](https://iquasar-emea.com/careers/) | ASP.NET Core, Angular, HTML/CSS/JS/TS, database work, APIs, security, testing, collaboration; cloud and CI/CD preferred. | Put production delivery behind the software story. Treat Angular depth as an evidence question, not a keyword to inflate. |
| [SoftHub — Angular & .NET Core](https://softhub.odoo.com/jobs/full-stack-developer-angular-net-core-8) | Three years of professional Angular, .NET APIs, SQL, external integrations, designer/product collaboration and CI/CD; React and cloud are optional. | A skills-list mention of Angular is insufficient for this specific requirement. Prioritize roles matching demonstrated frontend experience. |
| [Samsotech — ASP.NET Developers, Dubai](https://samsotech-id.com/careers.html) | 3–5 years, existing-system maintenance and refactoring, SQL, application layers, testing/deployment, security, customer and cross-cultural communication; includes SSRS/SSIS. | Existing-system improvement is valuable, not inferior to greenfield work. Use MATMAK modernization and management collaboration; do not add SSRS/SSIS without evidence. |
| [Michael Page — Full Stack Engineer, .NET & React](https://www.michaelpage.ae/job-detail/full-stack-engineer-net-react/ref/jn-082025-6820398) | Original recruiter page asks for 7+ years, .NET/C#, React, Azure/Azure SQL, enterprise work, CI/CD and teamwork. | Senior/stretch comparator, not evidence of immediate eligibility. Azure is a possible development area, not an existing credential to imply. |

### Interpretation

The sample supports four connected priorities: application development across frontend and backend; API/data integration; maintainable, testable changes; and delivery in a team. The listings above show React and Angular variants, so a generic “full-stack” label needs project-specific evidence. This is an inference from the sample, not a UAE-wide demand ranking.

The best candidate-specific differentiator is the combination already present in the CV: work on an existing production product, customer/admin interface modernization, billing integrations, database tuning, and deployment responsibilities. Client projects demonstrate breadth and autonomy. They should support the .NET positioning without being reduced to minor WordPress tasks or allowed to turn the whole homepage into a web-design-agency pitch.

### Evidence gaps, not invented qualifications

| Requirement | Evidence available | How to handle it |
| --- | --- | --- |
| .NET backend and data | MATMAK API, EF Core, SQL, business workflows | Lead with it and document one actual engineering decision. |
| Modern frontend | MATMAK Razor Pages/interface modernization; HEXIS React; MERN thesis | Show real screens and a frontend workflow. Separate production, staging, and academic experience. |
| Angular | Listed in the latest CV; no detailed professional Angular project in the reviewed collection | Do not market as extensive professional Angular experience until an example is supplied. |
| SQL Server / TypeScript | Listed skills, but project-level depth is not clear | Associate each with the actual project and work performed before placing it in prominent claims. |
| Azure | Sampled roles mention it; candidate evidence emphasizes AWS/Linux | Describe real AWS delivery. Consider Azure learning separately; do not relabel AWS experience as Azure. |
| Testing/security | JUnit claims, xUnit in skills, authentication and server hardening | Explain test scope and a real security decision. Do not infer a mature test suite from a tool list. |
| Team communication | Management collaboration, client delivery, teaching, languages | Include short concrete examples. Testimonials only with real attribution and permission. |

## 3. Public portfolio benchmark

This is a **content and information-architecture benchmark**. Visual quality, motion, mobile behavior, and measured performance were not scored. All achievements on peer sites are their authors' claims, not independently verified results. More senior profiles are communication references, not a standard Abdellah must pretend to match.

| Reference | Observed pattern | Apply / avoid |
| --- | --- | --- |
| [Adel Lajil](https://portfolio.adellajil.com/) — .NET, Angular, Azure | Specific technical/domain positioning; selected projects include images, scope and ownership labels; independent products are distinguished from professional contributions. | Apply contribution labels and project evidence. Avoid copying seniority, enterprise scale claims, or the full volume of homepage sections. |
| [Juan Pablo Valdez Torres](https://www.jpablo.dev/) — .NET and modern frontend | Projects explain migration, storage, integrations and implementation; screenshots and case-study links accompany them. | Apply problem-specific project titles and modernization stories. Decorative code snippets are optional and would not prove Abdellah's engineering. A linked case page could not be fetched, so its depth was not verified. |
| [Todd McIntosh](https://www.resonancemedia.ca/) — full-stack, including .NET/Laravel/React | Describes business applications, maintenance, frontend/backend contributions and payment integrations; project images appear before an extensive skills inventory. | Apply concrete scope across mixed stacks. Avoid a very long tool catalog and similarly detailed treatment for every old project. |
| [Moayed Mahmoud](https://moayedmahmoud.com/) and [InvenTrack case study](https://moayedmahmoud.com/work/inventrack-cloud-inventory-management-platform) — business software/.NET | Selected work leads to separate problem/solution/stack/impact pages with screenshots, live links and source links. The case identifies a prototype. | Apply layered detail and honest product status. Do not turn intended benefits into measured production impact. Current site says Calgary; an older Dubai resume is not current location evidence. |
| [Hisham Ramadan](https://www.hisham.ws/) — Dubai-based lead/backend engineer | Clear Dubai identity, backend/reliability focus, dated testimonials with named colleagues and roles, resume and blog links. | Apply credible attribution and collaboration evidence. Seniority and prominent employers are not transferable; this is not a full-stack visual benchmark. |
| [Brittany Chiang](https://brittanychiang.com/) — frontend reference | Clear role, concise experience entries, technology tags, project images, writing and links to fuller archives. | Apply selective detail and clear navigation to more evidence. Do not clone the layout or infer that a frontend specialist's presentation is ideal for UAE .NET hiring. |

The useful common lesson is not “copy a popular template.” It is to connect expertise to specific work and provide routes to deeper evidence. Abdellah's opportunity is to make the link between his interfaces, application logic, and real releases unusually easy to understand.

## 4. Current portfolio audit

These findings refer to the files present during this study; line numbers may change after implementation.

| Priority | Finding and evidence | Recommended correction |
| --- | --- | --- |
| P0 | `portfolio/css/styles.css:1014`: at widths up to 760px, `.project-link` is hidden. Those anchors are the only outbound links for XSHIELD, HEXIS Training, HPL and HEXIS ME. | Keep visible text links on mobile. Verify all four by touch and keyboard. |
| P0 | `styles.css:1025` hides `.brand-name` under 540px. The hero does not otherwise visibly name Abdellah. | Put the full name in the hero at every viewport. The accessible brand label is useful, but does not replace visible identity. |
| P1 | Hero has a 720px desktop minimum and a heading up to 96px. A statistics strip and “What I bring” precede selected work. | Shorten the opening and put selected work directly after it; confirm actual first-project visibility in a rendered prototype. |
| P1 | No product screenshots or dedicated case-study pages are present in the portfolio folder. | Add real, permitted product evidence and genuine project pages. Do not fabricate a dashboard and present it as shipped work. |
| P1 | “Measured outcomes” displays precise figures without measurement context. Latest CV summary says “about 40%.” | Put metrics within their projects and preserve uncertainty. Explain measurement scope before treating a number as verified. |
| P1 | React and other frontend technologies sit under “Additional,” despite the full-stack objective. | Give frontend its own group and link it to MATMAK/HEXIS examples. |
| P1 | Mobile navigation is hidden by default and requires JavaScript to open. | Make core navigation usable without JS; enhance to a collapsible menu only when the script is running. |
| P2 | Java Sep 2023–Apr 2024 appears before Flutter Apr–Jun 2024. | Use consistent reverse chronology, with Flutter before Java. |
| P2 | Several card regions have fixed minimum heights, and some text uses small font sizes. | Use content-led heights, readable body copy, and tighter grouping; measure contrast and zoom behavior rather than guessing. |
| P2 | Metadata does not include a canonical URL or a share image. | Verify the published URL and base path, then add accurate sharing metadata and a suitable original share card. |

Keep useful existing work: the skip link, semantic sections, menu Escape handling, reduced-motion support, direct contact links, and downloadable CV. They still need browser verification; their presence is not a full accessibility pass.

### Public project-link checks

The public [MATMAK page](https://matmaksolutions.com/en) exposes vehicle-kit/product content, and [HEXIS Middle East](https://hexis-me.com/) exposes a regional site. These establish public destinations, not authorship or the candidate's full internal contributions.

The web fetcher could not retrieve XSHIELD and the HEXIS staging URL during this check. That is **not proof those sites are offline**. Retest in a browser before publishing links. Keep staging labeled as staging, and verify that its public URL actually represents the Laravel/React implementation described in v14. Do not infer the technology stack from the URL alone.

## 5. Decision criteria for the redesign

Use this order when two design choices compete:

1. **Truth and attribution:** Is the claim supported, and is Abdellah's contribution clear?
2. **Role relevance:** Does it help evaluate a full-stack/.NET candidate for the intended opportunities?
3. **Comprehension:** Can a reader identify the problem, contribution, and result without decoding jargon?
4. **Evidence:** Can the reader inspect a screenshot, explanation, public artifact, or substantiated outcome?
5. **Usability:** Does the action work on mobile, with a keyboard, and under zoom?
6. **Visual hierarchy:** Does size, spacing, and contrast direct attention to the important content?
7. **Completeness and maintainability:** Are secondary details findable, and can the site stay accurate?

These are proposed project criteria, not measured recruiter weights. Avoid fake precision such as scoring a color scheme “92% recruiter-friendly.”

## 6. Content and navigation blueprint

### Homepage hierarchy

```text
Name + navigation: Work / Experience / About / Contact / Resume
  Introduction: Full-stack Software Engineer · Dubai, UAE
  Short value statement + core technologies + work/resume actions
Selected work
  MATMAK: .NET product engineering and interface modernization
  HEXIS Training: application design, React experience, business workflows
  XSHIELD: integrations, checkout, end-to-end delivery
More engineering work
  HPL/API integration + Java backend + other verified projects
Experience, in reverse chronological order
Capabilities tied to projects + concise delivery practice
About: education, teaching, certifications, languages
Contact: opportunities first, collaboration also welcome
```

Keep a brief homepage summary of each important area. Separate project pages hold details, not hidden hover panels. This applies progressive disclosure: an overview supports quick orientation, while clearly labeled links expose deeper material. [NN/G: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)

Use meaningful headings such as “Subscription billing and customer interfaces,” rather than slogans that could describe anyone. Descriptive headings and grouped content support scanning; this does not mean every reader follows a fixed F-shaped pattern or spends an exact number of seconds. [NN/G: Scanning with headings](https://www.nngroup.com/articles/layer-cake-pattern-scanning/)

### Proposed opening copy

> Abdellah Bouhaddi
>
> Full-stack Software Engineer
>
> Dubai, UAE · C# / ASP.NET Core · React / Razor Pages
>
> I build and improve business software—from customer interfaces and APIs to payments and production releases. At MATMAK, I contribute to an established .NET platform and deliver client applications from setup through launch.

Primary action: **Explore my work**. Secondary action: **Download resume**. Keep email and LinkedIn easy to find. No “available immediately,” visa status, notice period, or senior title without confirmation. The adjacent technology labels describe skills across projects, not a claim that MATMAK's frontend uses React.

### Featured project briefs

| Project | Homepage story | Evidence and detail to prepare |
| --- | --- | --- |
| MATMAK | Improve an existing .NET product: customer/admin interfaces, subscriptions, payments, data access and releases. Label “Production · Team contribution.” | Approved before/after UI images if available; one business flow; modular solution diagram; actual role boundaries; EF Core/schema optimization explanation; measurement context. |
| HEXIS Training | Build a multilingual application spanning registration, scheduling, certification and assessment. Label “Staging · Client project at MATMAK.” | Public React screen plus Filament admin screen with safe data; registration/quiz sequence; one real design tradeoff; validation/testing scope. Do not present the project as production until confirmed. |
| XSHIELD | Deliver an e-commerce application through custom functionality, payment integration and launch. Label “Production · Client project at MATMAK.” | Product/checkout screens, custom PHP/plugin contribution, import/export or API example, deployment responsibilities. No transactions or payment tests on the live store during portfolio research. |

Each case study should answer: What did the business need? What already existed? What did I personally do? What constraint shaped the solution? What did I build across frontend/backend? How did I test and release it? What changed? What remains limited?

Keep each case concise enough to scan, with optional deeper sections. Two or three purposeful screenshots are better than a large gallery without captions. A diagram must explain a real relationship, not decorate a technology list. Separate independently measured results, CV-reported results, and qualitative outcomes.

## 7. Preserve the small details without giving everything equal weight

| CV material | Proposed location | Treatment |
| --- | --- | --- |
| Auth, subscriptions, invoicing, pricing, credits, cutting operations | MATMAK summary + case study | Group around business workflows; retain detailed feature scope below the overview. |
| API/Client/Admin/Models/Services projects | MATMAK technical detail | Describe a modular multi-project solution. Folder names alone do not establish microservices. |
| EF Core tuning, redundant tables, joins and schema changes | MATMAK performance section | Recover useful specificity from older CVs; confirm exactly which changes belong to the reported result. |
| Nesting API deployment, API instrumentation, metrics, dashboards and alerts | Delivery section inside MATMAK case | Details appear more explicitly in earlier versions and should not disappear into “DevOps.” |
| Server purchase/setup, SSH, firewalls, Nginx, TLS, runtimes | Delivery capability + project detail | Demonstrates practical responsibility; avoid publishing hostnames, security configurations, access paths or secrets. |
| AWS EC2, backups, staging, GitHub Actions | MATMAK delivery detail | Explain release safety and operational work; do not invent disaster-recovery test results. |
| Stripe subscriptions/invoices/webhooks | MATMAK integration detail | Explain a verified lifecycle or failure case; do not claim idempotency or retries unless implemented. |
| Stripe + Network International, PHP/plugins/import-export | XSHIELD case | Show engineering beyond basic CMS configuration. |
| HEXIS planning, locations, certification, registration, emails | HEXIS case | Show the user/staff workflow rather than listing unrelated features. |
| Hex'pert emailed quiz link, auto-submit, scores/results | HEXIS deeper workflow | Useful concrete evidence of state, validation and automation. |
| HPL/BODYFENCE custom plugin, shortcodes, vehicle patterns and kits | Visible additional-project card + detail | Strong integration evidence, not a footnote labeled only WordPress. |
| HEXIS ME / other WordPress maintenance | Additional work | Current portfolio says “built”; CV names additional maintenance without assigning this specific site. Verify authorship and scope before retaining the stronger claim. |
| Java Spring Boot, RH Partner, Docker, SQL, JUnit | Experience + engineering project detail | Keep separate from .NET claims. Preserve existing-codebase work and collaboration. |
| Flutter/Firebase, responsive Material interfaces | Experience + additional work | Shows mobile breadth; do not imply public app links or releases that were not supplied. |
| Teaching 100+ students, practical labs, algorithms/networks/web/mobile | About + experience | Concrete communication and mentoring evidence. Not a reason to count teaching as .NET industry tenure. |
| Master's MERN PWA, inventory, checkout, payments | Education/project archive | Label academic. Useful frontend/full-stack foundation. |
| Bachelor's Java inventory, C++/Android Minimax, CS club | Education details/archive | Retain foundations without marketing a Minimax project as modern AI/ML expertise. |
| Java certificate, Huawei cloud certification | About + CV | Use verified names/dates. Do not reuse the old ambiguous Huawei 2014–2017 date. |
| Kabyle, Arabic, English, French | About + CV | Preserve proficiency levels from the CV; multilingual collaboration is useful context. |
| Cursor, Codex, custom skills, MCP | Short “How I work” note + relevant case | Explain that generated changes are reviewed/tested. Tool use alone does not establish AI-engineering specialization. |
| High-school mathematics and older educational detail | Full background archive/CV if desired | Available detail, not homepage priority after a master's and professional work. |

### Accuracy rules

- Use the latest CV for corrected project scope/status; recover older detail only when it does not contradict later corrections.
- Keep team contribution distinct from whole-product authorship and end-to-end client delivery.
- Do not convert “40% faster” into “40% lower latency” without confirming the metric. A reduction in time and an increase in throughput are different measures.
- For 40%, 35%, and 90%+, obtain the workload/module, baseline, measurement method and relevant period. If unavailable, use scoped CV-reported language or omit the number from prominent claims.
- Do not recast “99% system stability” as a verified uptime SLA. Its meaning is unclear.
- Avoid broad years-of-experience banners until dates and what counts as professional development are reconciled. “3+ years” must not become “3+ years of .NET” by implication.
- Never invent users, revenue, conversion improvement, uptime, testimonials or performance results.

## 8. UI direction and quality standards

### Proposed visual system — a starting point to test

Choose a calm light-neutral surface, dark readable text, and one restrained accent. Let real product images provide variety. Reuse Manrope if it works in the prototype; a font replacement is not a goal. Avoid large blocks of generic claims, decorative terminal text, excessive technology pills, animated counters, carousels for important work, and scroll-controlled effects.

| Element | Starting specification |
| --- | --- |
| Page width | Approximately 1160–1240px maximum, with comfortable side padding |
| Body type | 16–18px; 1.5–1.7 line height; paragraphs approximately 60–75 characters wide |
| Heading scale | Approximately 48–64px desktop hero, 32–40px mobile; validate wrapping with the real copy |
| Secondary text | Generally 13–14px; avoid tiny uppercase labels carrying essential information |
| Spacing | Consistent 8px-based scale; roughly 64–96px between major desktop sections, 40–64px mobile |
| Cards | Content-led height, consistent caption/metadata placement, subtle borders, no giant empty areas |
| Imagery | Real project screens with explanatory captions, explicit dimensions and responsive sizes |
| Interaction | Visible links, clear hover/focus, optional brief transitions, no motion required to understand content |
| Mobile | Single-column reading order; all project actions and identity remain available |

These dimensions and visual choices are design judgments. They are not WCAG requirements or established UAE recruiter preferences. Build a small desktop/mobile prototype before applying them to every page. No AI-generated interface should masquerade as an actual project screenshot.

### Non-negotiable acceptance criteria

- Check normal text contrast at least 4.5:1, and qualifying large text at least 3:1. Muted text and button labels count too. [W3C: Contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- Design ordinary standalone controls around 44px for comfortable use. WCAG 2.2 AA's target-size minimum is 24 by 24 CSS pixels with specified exceptions; 44px is our more generous design target, not that AA minimum. [W3C: Target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Test reflow at 320 CSS pixels and text enlargement; no loss of essential content or unnecessary horizontal reading scroll. Complex diagrams may need their own accommodation. [W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Verify keyboard access, visible focus, sensible heading order, meaningful image alternatives, working skip navigation, and reduced-motion behavior. Do not hide content until an animation runs.
- Target LCP at or below 2.5 seconds, INP at or below 200ms, and CLS at or below 0.1 at the 75th percentile of real visits, assessed separately for mobile and desktop. Lab checks catch regressions but do not substitute for field evidence; a Lighthouse page load does not directly measure INP. [Google: Web Vitals](https://web.dev/articles/vitals)
- Keep the static implementation unless a real requirement justifies changing it. Avoid a framework rewrite merely to make the portfolio look more modern.

## 9. Implementation sequence and verification

1. **Reconcile evidence.** Confirm contribution boundaries, current staging status, permitted screenshots and metric wording. The copy can progress without unverified numerical claims.
2. **Create the content model.** Write three project summaries and one complete MATMAK case study. Assign every retained CV detail a home using the table above.
3. **Prototype the direction.** Build the hero plus one real project section at desktop and mobile widths. Review identity, emphasis, image treatment and readability before extending the visual system.
4. **Implement the site.** Add dedicated case pages, fix mobile actions and navigation, correct chronology, and organize capabilities by demonstrated use. Keep current contact details and CV available.
5. **Run technical QA.** Test 320/390/768/1440px, keyboard navigation, zoom, no-JS behavior, reduced motion, all internal/outbound links, CV download, and the deployed base path. Check metadata, image alternatives, image dimensions, missing assets, and console errors. Measure performance and accessibility; record actual results.
6. **Run a small comprehension review.** Recruit a few reviewers representing hiring, engineering and nontechnical collaboration. Ask them to identify Abdellah's role/location, explain one project and his contribution, distinguish team work from individual scope, find the resume, and find contact information. This review is proposed, not already conducted.

Success means readers can understand and verify the relevant work, and essential actions work consistently. It does not mean a high Lighthouse score alone, a specific aesthetic, or a guaranteed interview rate. Optional future analytics can track case-study visits, resume-download clicks and contact-link clicks; clicks are proxies, not proof of a downloaded file, sent email or recruiter interest. Do not install tracking or collect personal information as part of this study.

### Inputs still needed for the strongest case studies

- Approved project screenshots, especially MATMAK's interface changes and HEXIS's React/admin workflows. Use synthetic or redacted data for private views.
- One concrete difficult decision per featured project, including the actual constraint and chosen tradeoff.
- Scope and measurement context for the CV percentages, if they should be prominent.
- Verification of HEXIS's current implementation URL/status and the specific HEXIS ME authorship claim.
- Optional genuine recommendations from collaborators, with permission to publish.

These gaps do not prevent creating a clear portfolio. They limit what can responsibly be claimed and illustrated. No private source code, production data, customer information or internal administration screen should be published without permission.

## Delivery status

The research and redesign brief are saved separately from the portfolio. The current website has **not been visually redesigned, deployed, or patched during this study**. The next build now has documented content priorities, sources, a preservation map, concrete corrections, and testable acceptance criteria. Visual validation remains a separate required step, not something this document claims to have completed.
