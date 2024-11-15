import pdfkit

# Note this example requires wkhtmltopdf
# install with 'brew install wkhtmltopdf'

# Path to the HTML file
html_file = '../../data/report.html'

# Path to the output PDF file
pdf_file = '../../data/report.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file)

print("PDF generated successfully!")