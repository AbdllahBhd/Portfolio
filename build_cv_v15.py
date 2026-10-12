"""Build Abdellah Bouhaddi CV v15 as an ATS-safe DOCX.

Design base: compact_reference_guide.
Named resume overrides: 0.62in page margins, 9.6pt body, 1.05 line spacing,
and compact heading/list rhythm to target a readable two-page engineering CV.
"""
from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Abdellah_Bouhaddi_Full_Stack_Software_Engineer_CV_v15.docx"

INK = RGBColor(0x19, 0x2B, 0x34)
ACCENT = RGBColor(0x16, 0x64, 0x5B)
MUTED = RGBColor(0x52, 0x63, 0x6B)
RULE = "BFCBCD"
FONT = "Calibri"


def font(run, size=9.6, bold=False, italic=False, color=INK):
    run.font.name = FONT
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FONT)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def paragraph_format(p, before=0, after=2.2, line=1.05, keep_next=False):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.keep_with_next = keep_next


def bottom_rule(p, color=RULE, size="8"):
    ppr = p._p.get_or_add_pPr()
    borders = ppr.find(qn("w:pBdr"))
    if borders is None:
        borders = OxmlElement("w:pBdr")
        ppr.append(borders)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)


def add_hyperlink(p, text, url, size=9.4):
    rel = p.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), rel)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "16645B")
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    size_el = OxmlElement("w:sz")
    size_el.set(qn("w:val"), str(int(size * 2)))
    fonts = OxmlElement("w:rFonts")
    for attr in ("ascii", "hAnsi", "eastAsia"):
        fonts.set(qn(f"w:{attr}"), FONT)
    rpr.extend([fonts, color, underline, size_el])
    text_el = OxmlElement("w:t")
    text_el.text = text
    r.extend([rpr, text_el])
    link.append(r)
    p._p.append(link)


def add_section(doc, text):
    p = doc.add_paragraph(style="Heading 1")
    paragraph_format(p, before=6, after=3, line=1.0, keep_next=True)
    r = p.add_run(text.upper())
    font(r, 10.5, True, color=ACCENT)
    bottom_rule(p)
    return p


def add_summary(doc, text):
    p = doc.add_paragraph()
    paragraph_format(p, after=2.5, line=1.06)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    font(p.add_run(text), 9.8)


def add_skill(doc, label, text):
    p = doc.add_paragraph()
    paragraph_format(p, after=1.1, line=1.0)
    font(p.add_run(label + ": "), 9.4, True, color=ACCENT)
    font(p.add_run(text), 9.4)


def add_role(doc, title, dates, organization, location):
    p = doc.add_paragraph(style="Heading 2")
    paragraph_format(p, before=5.5, after=0.4, line=1.0, keep_next=True)
    tabs = p.paragraph_format.tab_stops
    tabs.add_tab_stop(Inches(7.1), 2)
    font(p.add_run(title), 10.25, True, color=INK)
    p.add_run("\t")
    font(p.add_run(dates), 8.8, True, color=MUTED)
    c = doc.add_paragraph()
    paragraph_format(c, after=1.4, line=1.0, keep_next=True)
    font(c.add_run(organization), 9.1, True, color=ACCENT)
    font(c.add_run(" | " + location), 9.0, italic=True, color=MUTED)


def add_subrole(doc, text):
    p = doc.add_paragraph(style="Heading 3")
    paragraph_format(p, before=3.5, after=0.8, line=1.0, keep_next=True)
    font(p.add_run(text), 9.25, True, color=MUTED)


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    paragraph_format(p, after=1.1, line=1.02)
    font(p.add_run(text), 9.6)
    return p


def set_keep_lines(p):
    ppr = p._p.get_or_add_pPr()
    ppr.append(OxmlElement("w:widowControl"))


def add_page_number(section):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    paragraph_format(p, before=0, after=0, line=1.0)
    font(p.add_run("ABDELLAH BOUHADDI  |  "), 8, color=MUTED)
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    separate = OxmlElement("w:fldChar"); separate.set(qn("w:fldCharType"), "separate")
    value = OxmlElement("w:t"); value.text = "1"
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color"); color.set(qn("w:val"), "52636B")
    size = OxmlElement("w:sz"); size.set(qn("w:val"), "16")
    rpr.extend([color, size]); r.extend([rpr, begin, instr, separate, value, end]); p._p.append(r)


def configure_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), FONT)
    normal._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), FONT)
    normal.font.size = Pt(9.6)
    normal.font.color.rgb = INK
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        s = doc.styles[name]
        s.font.name = FONT
        s._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), FONT)
        s._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), FONT)
    style = doc.styles["List Bullet"]
    style.font.name = FONT
    style.font.size = Pt(9.6)
    style._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), FONT)
    style._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), FONT)
    pf = style.paragraph_format
    pf.left_indent = Inches(0.30)
    pf.first_line_indent = Inches(-0.16)
    pf.tab_stops.add_tab_stop(Inches(0.30))


def build():
    doc = Document()
    configure_styles(doc)
    section = doc.sections[0]
    section.page_width = Inches(8.5); section.page_height = Inches(11)
    section.top_margin = Inches(0.52); section.bottom_margin = Inches(0.52)
    section.left_margin = Inches(0.62); section.right_margin = Inches(0.62)
    section.header_distance = Inches(0.25); section.footer_distance = Inches(0.25)
    add_page_number(section)

    name = doc.add_paragraph()
    paragraph_format(name, after=0.2, line=1.0)
    font(name.add_run("ABDELLAH BOUHADDI"), 20, True, color=INK)
    title = doc.add_paragraph()
    paragraph_format(title, after=2.5, line=1.0)
    font(title.add_run("FULL-STACK SOFTWARE ENGINEER  |  .NET / C#"), 10.7, True, color=ACCENT)
    contact = doc.add_paragraph()
    paragraph_format(contact, after=0.5, line=1.0)
    font(contact.add_run("Dubai, UAE  |  +971 58 534 2499  |  douibouhaddi@gmail.com"), 9.4)
    links = doc.add_paragraph()
    paragraph_format(links, after=3, line=1.0)
    add_hyperlink(links, "Portfolio", "https://abdllahbhd.github.io/Portfolio")
    font(links.add_run("  |  "), 9.15, color=MUTED)
    add_hyperlink(links, "LinkedIn", "https://www.linkedin.com/in/abdellah-bouhaddi-1688421a9/")
    font(links.add_run("  |  "), 9.15, color=MUTED)
    add_hyperlink(links, "GitHub", "https://github.com/AbdllahBhd")
    bottom_rule(links, color="16645B", size="10")

    add_section(doc, "Professional Profile")
    add_summary(doc, "Full-stack software engineer with 3+ years building and improving business applications across ASP.NET Core, frontend interfaces, SQL, payments, and production delivery. At MATMAK, contribute to an established .NET SaaS with the engineering team and deliver client applications from implementation through launch. Earlier experience includes Java Spring Boot services, Flutter applications, and computer science instruction.")

    add_section(doc, "Core Skills")
    add_skill(doc, "Backend", "C#, ASP.NET Core 6/8, Web API, EF Core, LINQ, REST, JWT/OAuth, Swagger/OpenAPI, Java, Spring Boot")
    add_skill(doc, "Frontend & mobile", "Razor Pages, React, JavaScript, TypeScript, HTML5, CSS3, Bootstrap, Flutter, Firebase")
    add_skill(doc, "Data", "SQL Server, PostgreSQL, MySQL, MongoDB, Firestore; schema design, query optimization, stored procedures")
    add_skill(doc, "Delivery", "AWS EC2, Linux, Docker, Nginx, SSL/TLS, GitHub Actions, Jenkins, CI/CD, backups, DNS")
    add_skill(doc, "Integrations & quality", "Stripe, Network International, webhooks, xUnit, JUnit, integration testing, Prometheus, Grafana, Loki")
    add_skill(doc, "Additional application work", "Laravel, Filament, PHP, WordPress, WooCommerce, Angular; Git, Jira, Agile/Scrum")

    add_section(doc, "Professional Experience")
    add_role(doc, "Full Stack Developer", "Jun 2024 - Present", "MATMAK", "Dubai, UAE")
    for item in [
        "Contribute to an existing ASP.NET Core SaaS and PPF cutting platform with the engineering team, extending REST APIs, Razor Pages, and business workflows for authentication, subscriptions, invoicing, pricing, credits, and cutting operations.",
        "Modernized customer-facing pages and the administration interface, connecting frontend changes to application services and data workflows.",
        "Integrated Stripe for one-time payments, recurring subscriptions, invoicing, and webhook-based status updates.",
        "Improved affected EF Core and database read/write operations by about 40% through query tuning and schema redesign.",
        "Work within a modular .NET solution spanning API, Client, Admin, Models, and Services projects, and collaborate directly with management on priorities and releases.",
        "Provision and secure Linux cloud/VPS environments; configure Nginx, TLS, AWS EC2, staging, automated backups, GitHub Actions, and monitoring with Prometheus, Grafana, Loki, and Promtail.",
    ]: add_bullet(doc, item)
    add_subrole(doc, "Selected client delivery at MATMAK")
    for item in [
        "XSHIELD (production): delivered a WooCommerce store through launch, including custom PHP/plugins and APIs, Stripe and Network International payments, Linux hosting, domain/DNS, and Google Workspace.",
        "HEXIS Training Centre (staging): architected a multilingual Laravel/Filament/React application for planning, locations, registrations, certifications, email, and a scored quiz workflow with automatic submission.",
        "HEXIS PRECUT LAB / BODYFENCE (production): enhanced a custom WordPress plugin and shortcodes that connect vehicle patterns, car kits, pages, and forms to a dedicated MATMAK API.",
    ]: add_bullet(doc, item)

    add_section(doc, "Earlier Experience")
    add_role(doc, "Mobile Application Developer", "Apr 2024 - Jun 2024", "Freelance", "Dubai, UAE")
    add_bullet(doc, "Built cross-platform Flutter applications with responsive Material interfaces, Firebase Authentication, Firestore, Cloud Storage, push notifications, and custom navigation flows.")
    breaker = doc.add_paragraph()
    paragraph_format(breaker, after=0, line=1.0)
    breaker.add_run().add_break(WD_BREAK.PAGE)
    add_section(doc, "Earlier Experience - Continued")
    add_role(doc, "Backend Developer - Java Spring Boot", "Sep 2023 - Apr 2024", "Tech-Instinct", "Bejaia, Algeria")
    for item in [
        "Maintained an existing Spring Boot production codebase and REST microservices deployed in separate Docker containers for the RH Partner HR and payroll SaaS.",
        "Designed schemas and optimized SQL queries, improving affected query performance by 35%; diagnosed production defects and supported releases.",
        "Wrote JUnit unit and integration tests, achieving more than 90% coverage in the tested scope and strengthening release confidence.",
    ]: add_bullet(doc, item)
    add_role(doc, "Part-Time Computer Science Instructor", "Sep 2022 - Jun 2023", "ESTIN & University Abderrahmane Mira", "Bejaia, Algeria")
    add_bullet(doc, "Mentored 100+ students and created practical labs in programming, algorithms and data structures, computer networks, web development, and mobile development.")

    add_section(doc, "Education")
    add_role(doc, "Master's Degree in Software Engineering", "2020 - 2022", "University Abderrahmane Mira", "Bejaia, Algeria")
    add_bullet(doc, "Thesis: MERN progressive web e-commerce application with real-time inventory, payment processing, and a responsive checkout flow.")
    add_role(doc, "Bachelor's Degree in Computer Science", "2017 - 2020", "University Abderrahmane Mira", "Bejaia, Algeria")
    add_bullet(doc, "Projects: Java inventory management software; desktop C++ and Android game implementations using the Minimax algorithm. Active Computer Science Club member.")

    add_section(doc, "Certifications & Languages")
    add_skill(doc, "Certifications", "Java Developer Certificate (Jan-Mar 2020); Huawei Certification in Cloud Computing")
    add_skill(doc, "Languages", "Kabyle (native); Arabic, English, and French (fluent)")

    add_section(doc, "Engineering Workflow")
    add_summary(doc, "Use Cursor, OpenAI Codex, custom agent skills, and MCP where useful; review, test, and validate changes before release. Work across code review, secure delivery, troubleshooting, and direct communication with management and teammates.")

    add_section(doc, "Selected Links")
    for label, url in [
        ("Portfolio", "https://abdllahbhd.github.io/Portfolio"),
        ("XSHIELD", "https://xshield-protect.com/"),
        ("HEXIS PRECUT LAB / BODYFENCE", "https://www.bodyfence.net/en/hpl/"),
        ("RH Partner", "https://rh-partner.com/"),
    ]:
        p = doc.add_paragraph()
        paragraph_format(p, after=1, line=1.0)
        font(p.add_run(label + ": "), 9.25, True, color=ACCENT)
        add_hyperlink(p, url, url, 9.25)

    for p in doc.paragraphs:
        set_keep_lines(p)
    doc.core_properties.title = "Abdellah Bouhaddi - Full-Stack Software Engineer CV"
    doc.core_properties.subject = "Full-stack and .NET software engineering"
    doc.core_properties.author = "Abdellah Bouhaddi"
    doc.core_properties.keywords = "C#, ASP.NET Core, .NET, React, SQL, Dubai, UAE, Full Stack"
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
