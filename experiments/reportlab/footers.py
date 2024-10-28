from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Complex footer function
def add_complex_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(72, 65, "Report Footer 1")
    canvas.line(72, 60, 540, 60)
    
    # Adding a subtitle
    canvas.setFont("Helvetica", 10)
    canvas.drawString(72, 50, "Subtitle or additional information")
    
    # Adding a logo (assuming you have a logo.png in the same directory)
    logo_path = "experiments/reportlab/logo.png"
    canvas.drawImage(logo_path, 450, 30, width=50, height=50)
    
    # Adding a date
    current_date = datetime.now().strftime("%Y-%m-%d")
    canvas.drawString(72, 30, f"Date: {current_date}")
    
    canvas.restoreState()

# Simple footer function
def add_simple_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(72, 50, "Report Footer 2")
    canvas.line(72, 45, 540, 45)
    canvas.restoreState()

# Generate PDF with footer on each page
def create_pdf_with_footer(filename):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    content = [
        Paragraph("Page 1 content starts here...", getSampleStyleSheet()['BodyText']), 
        PageBreak(),
        Paragraph("Page 2 content starts here...", getSampleStyleSheet()['BodyText']), 
        PageBreak(),
        Paragraph("Page 3 content starts here...", getSampleStyleSheet()['BodyText']), 
    ]
    doc.build(
        content,
        onFirstPage=add_complex_footer, onLaterPages=add_simple_footer
    )


create_pdf_with_footer("simple_report_with_footer.pdf")