from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def save_report_as_pdf(text: str, filename: str = "research_report.pdf"):
    """Convert structured text into PDF"""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    for line in text.split("\n"):
        if line.startswith("## "):
            story.append(Paragraph(f"<b>{line[3:]}</b>", styles["Heading2"]))
        elif line.startswith("# "):
            story.append(Paragraph(f"<b>{line[2:]}</b>", styles["Heading1"]))
        else:
            story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    doc.build(story)
    print(f"✅ Report saved as {filename}")
