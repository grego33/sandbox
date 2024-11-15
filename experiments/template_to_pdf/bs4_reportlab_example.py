from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def html_to_pdf(html_content, output_filename):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create a PDF document
    doc = SimpleDocTemplate(output_filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    content = []

    # Convert HTML elements to ReportLab elements
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'td']):
        if element.name == 'p':
            content.append(Paragraph(element.get_text(), styles['BodyText']))
            content.append(Spacer(1, 12))
        elif element.name.startswith('h'):
            level = int(element.name[1])
            style = styles[f'Heading{level}']
            content.append(Paragraph(element.get_text(), style))
            content.append(Spacer(1, 12))
        # Add more handling for other tags as needed

    # Build the PDF
    doc.build(content)

# Read the HTML file
with open('../../data/report.html', 'r') as html_file:
    html_content = html_file.read()

# Convert HTML to PDF
html_to_pdf(html_content, 'report.pdf')