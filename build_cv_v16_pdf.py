"""Create a polished PDF counterpart of CV v16 from the final DOCX content."""

from pathlib import Path
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml.ns import qn
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Abdellah_Bouhaddi_Full_Stack_Software_Engineer_CV_v16.docx"
OUT = ROOT / "output" / "pdf" / "Abdellah_Bouhaddi_Full_Stack_Software_Engineer_CV_v16.pdf"

BLACK = colors.HexColor("#000000")
BODY = colors.HexColor("#20272B")
MUTED = colors.HexColor("#555F66")
ACCENT = colors.HexColor("#0B6763")


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=20, leading=21, textColor=BLACK, spaceAfter=3),
        "tagline": ParagraphStyle("Tagline", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.4, leading=11.2, textColor=BLACK, spaceAfter=7),
        "contact": ParagraphStyle("Contact", parent=base["Normal"], fontName="Helvetica", fontSize=9.1, leading=10.2, textColor=BODY, spaceAfter=2),
        "links": ParagraphStyle("Links", parent=base["Normal"], fontName="Helvetica", fontSize=9.1, leading=10.2, textColor=ACCENT, spaceAfter=10),
        "h1": ParagraphStyle("H1", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=11.3, textColor=BLACK, spaceBefore=7, spaceAfter=4, keepWithNext=True),
        "h2": ParagraphStyle("H2", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.0, leading=10.8, textColor=BLACK, keepWithNext=True),
        "date": ParagraphStyle("Date", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.8, leading=10.0, textColor=ACCENT, alignment=TA_RIGHT),
        "h3": ParagraphStyle("H3", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.4, leading=10.3, textColor=BLACK, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        "body": ParagraphStyle("Body", parent=base["Normal"], fontName="Helvetica", fontSize=9.2, leading=10.9, textColor=BODY, spaceAfter=3),
        "meta": ParagraphStyle("Meta", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.9, leading=10.0, textColor=ACCENT, spaceAfter=3, keepWithNext=True),
        "bullet": ParagraphStyle("Bullet", parent=base["Normal"], fontName="Helvetica", fontSize=9.1, leading=10.7, textColor=BODY, leftIndent=14, firstLineIndent=-8, bulletIndent=4, spaceAfter=3),
        "skill": ParagraphStyle("Skill", parent=base["Normal"], fontName="Helvetica", fontSize=8.9, leading=10.2, textColor=BODY, spaceAfter=2),
        "footer": ParagraphStyle("Footer", parent=base["Normal"], fontName="Helvetica", fontSize=7.5, leading=8, textColor=MUTED, alignment=TA_RIGHT),
    }


def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawRightString(letter[0] - 0.65 * inch, 0.31 * inch, f"ABDELLAH BOUHADDI  |  {doc.page}")
    canvas.restoreState()


def has_page_break(paragraph):
    return any(node.get(qn("w:type")) == "page" for node in paragraph._p.iter(qn("w:br")))


def rich_label(text):
    if ": " not in text:
        return escape(text)
    label, value = text.split(": ", 1)
    return f"<b>{escape(label)}:</b> {escape(value)}"


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    source = Document(SOURCE)
    s = styles()
    story = []
    previous_style = None

    for index, paragraph in enumerate(source.paragraphs):
        if has_page_break(paragraph):
            previous_style = None
            continue

        text = paragraph.text.strip()
        style_name = paragraph.style.name
        if index == 0:
            story.append(Paragraph("ABDELLAH BOUHADDI", s["name"]))
        elif index == 1:
            story.append(Paragraph("FULL STACK SOFTWARE ENGINEER&nbsp;&nbsp; | &nbsp;&nbsp;<font color='#0B6763'>C#&nbsp;&nbsp; ASP.NET CORE&nbsp;&nbsp; REACT</font>", s["tagline"]))
        elif index == 2:
            story.append(Paragraph(escape(text), s["contact"]))
        elif index == 3:
            story.append(Paragraph(
                "<link href='https://abdllahbhd.github.io/Portfolio' color='#0B6763'>Portfolio</link>"
                "&nbsp;&nbsp; | &nbsp;&nbsp;"
                "<link href='https://www.linkedin.com/in/abdellah-bouhaddi-1688421a9/' color='#0B6763'>LinkedIn</link>"
                "&nbsp;&nbsp; | &nbsp;&nbsp;"
                "<link href='https://github.com/AbdllahBhd' color='#0B6763'>GitHub</link>",
                s["links"],
            ))
        elif style_name == "Heading 1":
            story.append(Paragraph(escape(text), s["h1"]))
        elif style_name == "Heading 2":
            if "\t" not in text:
                if text == "HEXIS Training Centre  Staging":
                    story.append(PageBreak())
                story.append(Paragraph(escape(text), s["h3"]))
                previous_style = style_name
                continue
            role, date = text.split("\t", 1)
            row = Table(
                [[Paragraph(escape(role), s["h2"]), Paragraph(escape(date), s["date"])]],
                colWidths=[5.0 * inch, 2.2 * inch],
                hAlign="LEFT",
            )
            row.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]))
            story.append(row)
        elif style_name == "List Bullet":
            story.append(Paragraph(escape(text), s["bullet"], bulletText="•"))
        elif index in (66, 67, 68, 69):
            label, url = text.split(": ", 1)
            story.append(Paragraph(f"<b>{escape(label)}:</b> <link href='{escape(url)}' color='#0B6763'>{escape(url)}</link>", s["skill"]))
        elif previous_style == "Heading 2":
            story.append(Paragraph(escape(text), s["meta"]))
        elif index in (7, 8, 9, 10, 11, 12, 63, 64):
            story.append(Paragraph(rich_label(text), s["skill"]))
        elif text:
            story.append(Paragraph(escape(text), s["body"]))

        previous_style = style_name

    pdf = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.52 * inch,
        bottomMargin=0.52 * inch,
        title="Abdellah Bouhaddi Full Stack Software Engineer CV",
        author="Abdellah Bouhaddi",
        subject="Full stack and .NET software engineering roles in Dubai and the UAE",
    )
    pdf.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    print(OUT)


if __name__ == "__main__":
    build()
