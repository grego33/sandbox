from jinja2 import Environment, FileSystemLoader
import json

def format_currency(value):
    return "${:,.2f}".format(value)

def get_parts_total(services):
    total = 0
    for service in services:
        for item in service.get('parts', []):
            price = item.get('price', 0)
            qty = item.get('quantity', 1)
            total += price * qty
    return total

def get_labor_total(services):
    total = 0
    for service in services:
        rate = service.get('labor_rate', 0)
        hours = service.get('labor_hrs', 1)
        total += rate * hours
    return total


# Load the data from the JSON file
with open('invoice_body_v2.json', 'r') as json_file:
    data = json.load(json_file)
    
# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))

# Add the custom currency filter to the environment
env.filters['currency'] = format_currency
env.filters['get_parts_total'] = get_parts_total
env.filters['get_labor_total'] = get_labor_total

template = env.get_template('template_invoice.html')

# Render the template with the data
html_output = template.render(data)

# Save the rendered HTML to a file
with open('../../data/invoice_report.html', 'w') as html_file:
    html_file.write(html_output)

print("HTML report generated successfully!")

from weasyprint import HTML

# Note this example requires pango
# install with 'brew install pango'

# Path to the HTML file
html_file = '../../data/invoice_report.html'

# Path to the output PDF file
pdf_file = '../../data/invoice_report.pdf'

# Convert HTML to PDF
HTML(html_file).write_pdf(pdf_file)

print("PDF generated successfully!")