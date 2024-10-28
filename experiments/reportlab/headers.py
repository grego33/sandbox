from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Complex header function
def add_complex_header(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(72, 750, "Report Header 1")
    canvas.line(72, 745, 540, 745)
    
    # Adding a subtitle
    canvas.setFont("Helvetica", 10)
    canvas.drawString(72, 735, "Subtitle or additional information")
    
    # Adding a logo (assuming you have a logo.png in the same directory)
    logo_path = "experiments/reportlab/logo.png"
    canvas.drawImage(logo_path, 450, 720, width=50, height=50)
    
    # Adding a date
    current_date = datetime.now().strftime("%Y-%m-%d")
    canvas.drawString(72, 720, f"Date: {current_date}")
    
    canvas.restoreState()

# Simple header function
def add_simple_header(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(72, 750, "Report Header 2")
    canvas.line(72, 745, 540, 745)
    canvas.restoreState()

# Generate PDF with header on each page
def create_pdf_with_header(filename):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    content = [
        Paragraph("Page 1 content goes here...", getSampleStyleSheet()['BodyText']), 
        PageBreak(),
        Paragraph("Page 2 content goes here...", getSampleStyleSheet()['BodyText']), 
        PageBreak(),
        Paragraph("Page 3 content goes here...", getSampleStyleSheet()['BodyText']), 
    ]
    doc.build(
        content,
        onFirstPage=add_complex_header, onLaterPages=add_simple_header
    )

# Create the PDF
create_pdf_with_header("simple_report_with_header.pdf")