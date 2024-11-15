from weasyprint import HTML

# Note this example requires pango
# install with 'brew install pango'

# Path to the HTML file
html_file = '../../data/report.html'

# Path to the output PDF file
pdf_file = '../../data/report.pdf'

# Convert HTML to PDF
HTML(html_file).write_pdf(pdf_file)

print("PDF generated successfully!")