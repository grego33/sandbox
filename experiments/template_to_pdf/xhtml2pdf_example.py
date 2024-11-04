from xhtml2pdf import pisa

with open('report.html', 'r') as html_file:
    html_content = html_file.read()

with open('report.pdf', 'wb') as pdf_file:
    pisa.CreatePDF(html_content, dest=pdf_file)