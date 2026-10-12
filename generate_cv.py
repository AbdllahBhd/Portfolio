"""Generate an ATS-optimized professional CV for Abdellah Bouhaddi."""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Twips, Cm

from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT_DIR = r"D:\abdellah\New folder"
DOCX_PATH = rf"{OUTPUT_DIR}\Abdellah_Bouhaddi_Backend_Developer_CV_v14.docx"
PDF_PATH = rf"{OUTPUT_DIR}\Abdellah_Bouhaddi_Backend_Developer_CV_v14.pdf"

NAVY = RGBColor(0x1B, 0x36, 0x5D)
NAVY_HEX = "#1B365D"
DARK = RGBColor(0x22, 0x22, 0x22)
GRAY = RGBColor(0x44, 0x44, 0x44)


def set_run_font(run, name="Calibri", size=11, bold=False, italic=False, color=DARK):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def set_paragraph_format(paragraph, before=0, after=0, line=1.08, space_after_pt=None):
    pf = paragraph.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after if space_after_pt is None else space_after_pt)
    pf.line_spacing = line
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE


def add_bottom_border(paragraph, color="1B365D", size="12"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_section_heading(doc, text):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=10, after=4, line=1.0)
    run = p.add_run(text.upper())
    set_run_font(run, size=12, bold=True, color=NAVY)
    add_bottom_border(p)
    return p


def add_body(doc, text, size=10.5, after=4, justify=True):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=0, after=after, line=1.08)
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    set_run_font(run, size=size)
    return p


def add_bullet(doc, text, size=10.5):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=0, after=1.5, line=1.05)
    p.paragraph_format.left_indent = Inches(0.18)
    p.paragraph_format.first_line_indent = Inches(-0.14)
    run = p.add_run("- " + text)
    set_run_font(run, size=size)
    return p


def add_job_header(doc, title, dates):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=12, after=0, line=1.0)
    tab_stops = p.paragraph_format.tab_stops
    tab_stops.add_tab_stop(Inches(7.3), WD_TAB_ALIGNMENT.RIGHT)
    run = p.add_run(title)
    set_run_font(run, size=12, bold=True, color=NAVY)
    p.add_run("\t")
    run = p.add_run(dates)
    set_run_font(run, size=10, italic=True, color=GRAY)
    return p


def add_company_line(doc, text):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=0, after=2, line=1.0)
    run = p.add_run(text)
    set_run_font(run, size=10.5, italic=True, color=GRAY)
    return p


def add_subhead(doc, text):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=6, after=1, line=1.0)
    p.paragraph_format.left_indent = Inches(0.08)
    run = p.add_run(text)
    set_run_font(run, size=10, bold=False, italic=True, color=GRAY)
    return p


def add_skill_line(doc, label, value):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=0, after=1.5, line=1.05)
    run = p.add_run(f"{label}: ")
    set_run_font(run, size=10.5, bold=True, color=NAVY)
    run = p.add_run(value)
    set_run_font(run, size=10.5)
    return p


def configure_list_style(doc):
    styles = doc.styles
    style = styles["List Bullet"]
    font = style.font
    font.name = "Calibri"
    font.size = Pt(10.5)
    font.color.rgb = DARK


def build_docx():
    doc = Document()
    configure_list_style(doc)

    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.45)
    section.left_margin = Inches(0.6)
    section.right_margin = Inches(0.6)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = DARK
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    name = doc.add_paragraph()
    name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(name, before=0, after=1, line=1.0)
    run = name.add_run("ABDELLAH BOUHADDI")
    set_run_font(run, size=20, bold=True, color=NAVY)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(title, before=0, after=2, line=1.0)
    run = title.add_run("Software Engineer  |  .NET  |  Full Stack")
    set_run_font(run, size=11, bold=False, color=NAVY)

    contact = doc.add_paragraph()
    contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(contact, before=0, after=0, line=1.0)
    run = contact.add_run(
        "Dubai, United Arab Emirates  |  +971 58 534 2499  |  douibouhaddi@gmail.com"
    )
    set_run_font(run, size=10.5)

    links = doc.add_paragraph()
    links.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(links, before=0, after=2, line=1.0)
    run = links.add_run(
        "github.com/AbdllahBhd  |  linkedin.com/in/abdellah-bouhaddi-1688421a9  |  abdllahbhd.github.io/Portfolio"
    )
    set_run_font(run, size=10.5)

    add_section_heading(doc, "Professional Summary")
    add_body(
        doc,
        "Software Engineer with 3+ years building full-stack business software in C# and ASP.NET Core; earlier Java Spring Boot at Tech-Instinct. "
        "I handle delivery as well as code: Linux servers, hosting, DNS, payments, CI/CD, monitoring, and production releases. "
        "At MATMAK I work on the ASP.NET Core SaaS with the team and deliver client sites from setup through public launch (including live XSHIELD), "
        "modernized the SaaS UI, and improved API/database performance by about 40%. "
        "I use Cursor and OpenAI Codex and review and test changes before release.",
        after=2,
    )

    add_section_heading(doc, "Technical Skills")
    add_skill_line(
        doc,
        "Languages",
        "C#, Java, SQL, Dart, PHP, JavaScript, TypeScript",
    )
    add_skill_line(
        doc,
        "Backend",
        "ASP.NET Core (.NET 6/8), ASP.NET Web API, RESTful APIs, Entity Framework Core, LINQ, Dependency Injection, JWT/OAuth, Swagger/OpenAPI, SOLID principles, design patterns, Spring Boot, Hibernate, microservices, Docker, OOP",
    )
    add_skill_line(
        doc,
        "Frontend and Mobile",
        "HTML5, CSS3, Bootstrap, Razor Pages, React, Laravel, Filament, Angular, TypeScript, Flutter, Android, WordPress, WooCommerce",
    )
    add_skill_line(
        doc,
        "Databases",
        "SQL Server, PostgreSQL, MySQL, MongoDB, Firebase Firestore; schema design, query optimization, stored procedures (where applicable)",
    )
    add_skill_line(
        doc,
        "Cloud and DevOps",
        "AWS EC2, Linux server provisioning and hardening, Docker, containerized deployments, Nginx, SSL/TLS, GitHub Actions, Jenkins, CI/CD, Git",
    )
    add_skill_line(
        doc,
        "Payments and Observability",
        "Stripe (subscriptions, invoicing, webhooks), Network International; Prometheus, Grafana, Loki, Promtail",
    )
    add_skill_line(
        doc,
        "Practices",
        "Agile, Scrum, SDLC, Jira, code reviews, secure coding, unit testing (xUnit, JUnit), integration testing",
    )
    add_skill_line(
        doc,
        "AI-assisted development",
        "Cursor, OpenAI Codex, MCP (Model Context Protocol), custom agent skills",
    )

    add_section_heading(doc, "Professional Experience")

    add_job_header(doc, "Full Stack Developer", "June 2024 – Present")
    add_company_line(doc, "MATMAK  |  Dubai, United Arab Emirates")

    for bullet in [
        "Took ownership of an existing ASP.NET Core SaaS and PPF cutting platform, maintaining production stability while extending APIs, Razor Pages, and business features.",
        "Structure a modular multi-project .NET solution (API, Client, Admin, Models, Services) for authentication, subscriptions, invoicing, cutting operations, pricing, and credits.",
        "Redesigned customer-facing pages and the admin CMS from a dated, minimal interface to a modern, professional UI/UX.",
        "Integrate Stripe for one-time payments, recurring subscriptions, invoicing, and webhook-based status updates.",
        "Reduce query latency and read/write time by 40% through Entity Framework Core tuning and database schema redesign.",
        "Work directly with management on platform features, client projects, GitHub, production releases, and day-to-day delivery with the team.",
        "Ship frontend and backend features with Cursor and OpenAI Codex, reviewing and validating changes before release.",
    ]:
        add_bullet(doc, bullet)

    add_subhead(doc, "Within this role at MATMAK — DevOps, deployment, and infrastructure")
    for bullet in [
        "Provision new Linux cloud and VPS servers from purchase through production go-live: OS setup and configuration, SSH access, security hardening, firewalls, Nginx reverse proxy, SSL/TLS, and application runtime deployment.",
        "Manage AWS EC2, automated backups, and staging environments; deploy ASP.NET Core APIs and web applications on Linux with Nginx.",
        "Implement CI/CD with GitHub Actions, and monitor production with Prometheus, Grafana, Loki, and Promtail.",
    ]:
        add_bullet(doc, bullet)

    add_subhead(doc, "Within this role at MATMAK — Client project: XSHIELD (WooCommerce, production)")
    for bullet in [
        "Delivered the live WordPress / WooCommerce store at xshield-protect.com end to end: Linux server provisioning, domain, Google Workspace email, hosting, DNS, custom development, and production go-live.",
        "Built custom pages, PHP customizations, and API integrations beyond standard WordPress, and developed custom plugins (including import/export) with AI-assisted development.",
        "Created and configured Stripe and Network International (UAE) payment gateways for secure e-commerce checkout.",
    ]:
        add_bullet(doc, bullet)

    add_subhead(doc, "Within this role at MATMAK — Client project: HEXIS Training Centre, France (Laravel, Filament, React — staging)")
    for bullet in [
        "Architected and built a multilingual training platform in staging: Laravel (PHP) backend, Filament admin CMS, and React.js public frontend; currently ahead of production launch.",
        "Delivered planning, certifications, locations, registrations, transactional emails, and Hex'pert registration (emailed quiz link, auto-submit, scoring, and results).",
        "Owned system design and implementation using AI-assisted development with Cursor, OpenAI Codex, custom agent skills, and MCP; reviewed and validated all changes before release.",
    ]:
        add_bullet(doc, bullet)

    add_subhead(doc, "Within this role at MATMAK — Client project: HEXIS PRECUT LAB / BODYFENCE (WordPress, production)")
    for bullet in [
        "Developed and enhanced a custom WordPress PHP plugin for bodyfence.net/hpl (HEXIS PRECUT LAB) integrating with a dedicated MATMAK API instance.",
        "Extended site pages and forms with custom shortcodes (for example, fetching and displaying vehicle pattern data and car kits from the API).",
    ]:
        add_bullet(doc, bullet)

    add_subhead(doc, "Within this role at MATMAK — Web infrastructure and IT administration")
    for bullet in [
        "Purchase and configure domains and subdomains, set up Google Workspace and professional email, and point DNS to production and staging deployments.",
        "Maintain additional WordPress sites for performance, security, and usability.",
    ]:
        add_bullet(doc, bullet)

    add_job_header(doc, "Mobile Application Developer (Flutter) — Freelance", "April 2024 – June 2024")
    add_company_line(doc, "Self-Employed  |  Dubai, United Arab Emirates")
    for bullet in [
        "Developed cross-platform Android and iOS applications using Flutter (Dart) with responsive UI and native-like performance.",
        "Integrated Firebase Authentication, Cloud Firestore, Cloud Storage, and push notifications, and built custom Material Design navigation flows.",
    ]:
        add_bullet(doc, bullet)

    add_job_header(doc, "Backend Developer — Java Spring Boot", "September 2023 – April 2024")
    add_company_line(doc, "Tech-Instinct  |  Béjaïa, Algeria")
    for bullet in [
        "Took ownership of an existing Spring Boot production codebase, maintaining REST APIs and improving reliability without a greenfield rewrite.",
        "Developed and maintained Spring Boot microservices running in Docker, with each service deployed in its own container.",
        "Designed database schemas and optimized SQL queries, improving query performance by 35% and supporting greater scalability.",
        "Wrote unit and integration tests with JUnit, achieving over 90% code coverage and strengthening release quality.",
        "Diagnosed and resolved production defects, contributing to 99% system stability and reduced downtime.",
    ]:
        add_bullet(doc, bullet)

    add_job_header(doc, "Part-Time Instructor, Computer Science", "September 2022 – June 2023")
    add_company_line(
        doc,
        "Higher School of Computer Science and Technology (ESTIN) and University Abderrahmane Mira  |  Béjaïa, Algeria",
    )
    for bullet in [
        "Mentored 100+ students in programming, algorithms, computer networks, web, and mobile development, and created practical lab materials.",
    ]:
        add_bullet(doc, bullet)

    add_section_heading(doc, "Education")

    add_job_header(doc, "Master's Degree in Software Engineering", "2020 – 2022")
    add_company_line(doc, "University Abderrahmane Mira  |  Béjaïa, Algeria")
    add_body(
        doc,
        "Thesis: Progressive Web B2C e-commerce application. Built a full-stack platform using MongoDB, Express.js, React, and Node.js (MERN stack), including real-time inventory management, payment processing, and a responsive checkout flow.",
        size=10.5,
        after=2,
    )

    add_job_header(doc, "Bachelor's Degree in Computer Science", "2017 – 2020")
    add_company_line(doc, "University Abderrahmane Mira  |  Béjaïa, Algeria")
    add_body(
        doc,
        "Projects: Inventory Management Software (Java); AI-powered game in desktop C++ and Android Studio using the Minimax algorithm. Active member of the Computer Science Club.",
        size=10.5,
        after=2,
    )

    add_section_heading(doc, "Certifications")
    add_body(
        doc,
        "Java Developer Certificate  |  Béjaïa, Algeria  |  January 2020 – March 2020",
        after=1,
        justify=False,
    )
    add_body(
        doc,
        "Huawei Certification in Cloud Computing  |  Béjaïa, Algeria",
        after=2,
        justify=False,
    )

    add_section_heading(doc, "Additional Information")
    add_skill_line(
        doc,
        "Languages",
        "Kabyle (Native), Arabic (Fluent), English (Fluent), French (Fluent)",
    )

    doc.save(DOCX_PATH)
    print(f"Wrote {DOCX_PATH}")


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.42 * inch,
        title="Abdellah Bouhaddi - Software Engineer CV",
        author="Abdellah Bouhaddi",
    )

    styles = getSampleStyleSheet()
    name_style = ParagraphStyle(
        "Name",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=HexColor(NAVY_HEX),
        spaceAfter=2,
    )
    headline_style = ParagraphStyle(
        "Headline",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=13,
        alignment=TA_CENTER,
        textColor=HexColor(NAVY_HEX),
        spaceAfter=2,
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        textColor=black,
        spaceAfter=4,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=HexColor(NAVY_HEX),
        spaceBefore=6,
        spaceAfter=2,
    )
    body_style = ParagraphStyle(
        "BodyJust",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.6,
        leading=12.0,
        alignment=TA_JUSTIFY,
        textColor=black,
        spaceAfter=2,
    )
    body_left = ParagraphStyle(
        "BodyLeft",
        parent=body_style,
        alignment=TA_LEFT,
        spaceAfter=2,
    )
    job_title_style = ParagraphStyle(
        "JobTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11.2,
        leading=14,
        textColor=HexColor(NAVY_HEX),
        spaceBefore=12,
        spaceAfter=0,
    )
    company_style = ParagraphStyle(
        "Company",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9.6,
        leading=12,
        textColor=HexColor("#444444"),
        spaceAfter=2,
    )
    subhead_style = ParagraphStyle(
        "Subhead",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9.4,
        leading=12,
        textColor=HexColor("#555555"),
        leftIndent=6,
        spaceBefore=5,
        spaceAfter=1,
    )
    skill_style = ParagraphStyle(
        "Skill",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.6,
        leading=12.0,
        textColor=black,
        spaceAfter=1.2,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.6,
        leading=12.0,
        textColor=black,
        leftIndent=12,
        bulletIndent=0,
        spaceAfter=1.1,
    )

    story = []

    def section(title):
        story.append(Paragraph(title.upper(), section_style))
        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=HexColor(NAVY_HEX),
                spaceBefore=0,
                spaceAfter=4,
            )
        )

    def job(title, dates, company):
        story.append(Paragraph(f"{title}  |  {dates}", job_title_style))
        story.append(Paragraph(company, company_style))

    def bullets(items):
        for item in items:
            story.append(Paragraph(f"-  {item}", bullet_style))

    def skill(label, value):
        story.append(
            Paragraph(f"<b>{label}:</b> {value}", skill_style)
        )

    story.append(Paragraph("ABDELLAH BOUHADDI", name_style))
    story.append(
        Paragraph(
            "Software Engineer  |  .NET  |  Full Stack",
            headline_style,
        )
    )
    story.append(
        Paragraph(
            "Dubai, United Arab Emirates  |  +971 58 534 2499  |  douibouhaddi@gmail.com<br/>"
            "github.com/AbdllahBhd  |  linkedin.com/in/abdellah-bouhaddi-1688421a9  |  abdllahbhd.github.io/Portfolio",
            contact_style,
        )
    )

    section("Professional Summary")
    story.append(
        Paragraph(
            "Software Engineer with 3+ years building full-stack business software in C# and ASP.NET Core; earlier Java Spring Boot at Tech-Instinct. "
            "I handle delivery as well as code: Linux servers, hosting, DNS, payments, CI/CD, monitoring, and production releases. "
            "At MATMAK I work on the ASP.NET Core SaaS with the team and deliver client sites from setup through public launch (including live XSHIELD), "
            "modernized the SaaS UI, and improved API/database performance by about 40%. "
            "I use Cursor and OpenAI Codex and review and test changes before release.",
            body_style,
        )
    )

    section("Technical Skills")
    skill("Languages", "C#, Java, SQL, Dart, PHP, JavaScript, TypeScript")
    skill(
        "Backend",
        "ASP.NET Core (.NET 6/8), ASP.NET Web API, RESTful APIs, Entity Framework Core, LINQ, Dependency Injection, JWT/OAuth, Swagger/OpenAPI, SOLID principles, design patterns, Spring Boot, Hibernate, microservices, Docker, OOP",
    )
    skill("Frontend and Mobile", "HTML5, CSS3, Bootstrap, Razor Pages, React, Laravel, Filament, Angular, TypeScript, Flutter, Android, WordPress, WooCommerce")
    skill(
        "Databases",
        "SQL Server, PostgreSQL, MySQL, MongoDB, Firebase Firestore; schema design, query optimization, stored procedures (where applicable)",
    )
    skill("Cloud and DevOps", "AWS EC2, Linux server provisioning and hardening, Docker, containerized deployments, Nginx, SSL/TLS, GitHub Actions, Jenkins, CI/CD, Git")
    skill(
        "Payments and Observability",
        "Stripe (subscriptions, invoicing, webhooks), Network International; Prometheus, Grafana, Loki, Promtail",
    )
    skill("Practices", "Agile, Scrum, SDLC, Jira, code reviews, secure coding, unit testing (xUnit, JUnit), integration testing")
    skill(
        "AI-assisted development",
        "Cursor, OpenAI Codex, MCP (Model Context Protocol), custom agent skills",
    )

    section("Professional Experience")

    job("Full Stack Developer", "June 2024 – Present", "MATMAK  |  Dubai, United Arab Emirates")
    bullets(
        [
            "Took ownership of an existing ASP.NET Core SaaS and PPF cutting platform, maintaining production stability while extending APIs, Razor Pages, and business features.",
            "Structure a modular multi-project .NET solution (API, Client, Admin, Models, Services) for authentication, subscriptions, invoicing, cutting operations, pricing, and credits.",
            "Redesigned customer-facing pages and the admin CMS from a dated, minimal interface to a modern, professional UI/UX.",
            "Integrate Stripe for one-time payments, recurring subscriptions, invoicing, and webhook-based status updates.",
            "Reduce query latency and read/write time by 40% through Entity Framework Core tuning and database schema redesign.",
            "Work directly with management on platform features, client projects, GitHub, production releases, and day-to-day delivery with the team.",
            "Ship frontend and backend features with Cursor and OpenAI Codex, reviewing and validating changes before release.",
        ]
    )

    story.append(Paragraph("Within this role at MATMAK — DevOps, deployment, and infrastructure", subhead_style))
    bullets(
        [
            "Provision new Linux cloud and VPS servers from purchase through production go-live: OS setup and configuration, SSH access, security hardening, firewalls, Nginx reverse proxy, SSL/TLS, and application runtime deployment.",
            "Manage AWS EC2, automated backups, and staging environments; deploy ASP.NET Core APIs and web applications on Linux with Nginx.",
            "Implement CI/CD with GitHub Actions, and monitor production with Prometheus, Grafana, Loki, and Promtail.",
        ]
    )

    story.append(KeepTogether([
        Paragraph("Within this role at MATMAK — Client project: XSHIELD (WooCommerce, production)", subhead_style),
        Paragraph("-  Delivered the live WordPress / WooCommerce store at xshield-protect.com end to end: Linux server provisioning, domain, Google Workspace email, hosting, DNS, custom development, and production go-live.", bullet_style),
        Paragraph("-  Built custom pages, PHP customizations, and API integrations beyond standard WordPress, and developed custom plugins (including import/export) with AI-assisted development.", bullet_style),
        Paragraph("-  Created and configured Stripe and Network International (UAE) payment gateways for secure e-commerce checkout.", bullet_style),
    ]))

    story.append(KeepTogether([
        Paragraph("Within this role at MATMAK — Client project: HEXIS Training Centre, France (Laravel, Filament, React — staging)", subhead_style),
        Paragraph("-  Architected and built a multilingual training platform in staging: Laravel (PHP) backend, Filament admin CMS, and React.js public frontend; currently ahead of production launch.", bullet_style),
        Paragraph("-  Delivered planning, certifications, locations, registrations, transactional emails, and Hex'pert registration (emailed quiz link, auto-submit, scoring, and results).", bullet_style),
        Paragraph("-  Owned system design and implementation using AI-assisted development with Cursor, OpenAI Codex, custom agent skills, and MCP; reviewed and validated all changes before release.", bullet_style),
    ]))

    story.append(KeepTogether([
        Paragraph("Within this role at MATMAK — Client project: HEXIS PRECUT LAB / BODYFENCE (WordPress, production)", subhead_style),
        Paragraph("-  Developed and enhanced a custom WordPress PHP plugin for bodyfence.net/hpl (HEXIS PRECUT LAB) integrating with a dedicated MATMAK API instance.", bullet_style),
        Paragraph("-  Extended site pages and forms with custom shortcodes (for example, fetching and displaying vehicle pattern data and car kits from the API).", bullet_style),
    ]))

    story.append(KeepTogether([
        Paragraph("Within this role at MATMAK — Web infrastructure and IT administration", subhead_style),
        Paragraph("-  Purchase and configure domains and subdomains, set up Google Workspace and professional email, and point DNS to production and staging deployments.", bullet_style),
        Paragraph("-  Maintain additional WordPress sites for performance, security, and usability.", bullet_style),
    ]))

    job(
        "Mobile Application Developer (Flutter) — Freelance",
        "April 2024 – June 2024",
        "Self-Employed  |  Dubai, United Arab Emirates",
    )
    bullets(
        [
            "Developed cross-platform Android and iOS applications using Flutter (Dart) with responsive UI and native-like performance.",
            "Integrated Firebase Authentication, Cloud Firestore, Cloud Storage, and push notifications, and built custom Material Design navigation flows.",
        ]
    )

    job(
        "Backend Developer — Java Spring Boot",
        "September 2023 – April 2024",
        "Tech-Instinct  |  Béjaïa, Algeria",
    )
    bullets(
        [
            "Took ownership of an existing Spring Boot production codebase, maintaining REST APIs and improving reliability without a greenfield rewrite.",
            "Developed and maintained Spring Boot microservices running in Docker, with each service deployed in its own container.",
            "Designed database schemas and optimized SQL queries, improving query performance by 35% and supporting greater scalability.",
            "Wrote unit and integration tests with JUnit, achieving over 90% code coverage and strengthening release quality.",
            "Diagnosed and resolved production defects, contributing to 99% system stability and reduced downtime.",
        ]
    )

    job(
        "Part-Time Instructor, Computer Science",
        "September 2022 – June 2023",
        "Higher School of Computer Science and Technology (ESTIN) and University Abderrahmane Mira  |  Béjaïa, Algeria",
    )
    bullets(
        [
            "Mentored 100+ students in programming, algorithms, computer networks, web, and mobile development, and created practical lab materials.",
        ]
    )

    section("Education")
    job("Master's Degree in Software Engineering", "2020 – 2022", "University Abderrahmane Mira  |  Béjaïa, Algeria")
    story.append(
        Paragraph(
            "Thesis: Progressive Web B2C e-commerce application. Built a full-stack platform using MongoDB, Express.js, React, and Node.js (MERN stack), including real-time inventory management, payment processing, and a responsive checkout flow.",
            body_style,
        )
    )
    job("Bachelor's Degree in Computer Science", "2017 – 2020", "University Abderrahmane Mira  |  Béjaïa, Algeria")
    story.append(
        Paragraph(
            "Projects: Inventory Management Software (Java); AI-powered game in desktop C++ and Android Studio using the Minimax algorithm. Active member of the Computer Science Club.",
            body_style,
        )
    )

    section("Certifications")
    story.append(
        Paragraph(
            "Java Developer Certificate  |  Béjaïa, Algeria  |  January 2020 – March 2020",
            body_left,
        )
    )
    story.append(
        Paragraph("Huawei Certification in Cloud Computing  |  Béjaïa, Algeria", body_left)
    )
    story.append(
        Paragraph(
            "<b>Languages:</b> Kabyle (Native), Arabic (Fluent), English (Fluent), French (Fluent)",
            skill_style,
        )
    )

    doc.build(story)
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    build_docx()
    build_pdf()
