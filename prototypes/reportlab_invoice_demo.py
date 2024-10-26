from invoice_model import *
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, BaseDocTemplate, Frame
from random import randint, uniform

## INVOICE GENERATION
# Define parts
engine_part = Part(name="Engine Mount", unit_price=120.50, quantity=1, core_charge=20.00)
oil_filter = Part(name="Oil Filter", unit_price=15.00, quantity=2)

# Initialize 25 parts with example data
random_parts = [
    Part(
        name=f"Part-{i+1}",
        unit_price=round(uniform(10.0, 150.0), 2),  # Random price between $10.00 and $150.00
        quantity=randint(1, 5),  # Random quantity between 1 and 5
        core_charge=round(uniform(0.0, 20.0), 2)  # Random core charge up to $20.00
    ) for i in range(25)
]

# Define labor
labor_replace_mount = Labor(description="Replace Engine Mount", hours=2.5, hourly_rate=85.00)
labor_oil_change = Labor(description="Oil Change", hours=0.5, hourly_rate=85.00)

# Initialize 10 labor items with example data
random_labor = [
    Labor(
        description=f"Labor Task-{i+1}",
        hours=round(uniform(0.5, 3.0), 1),  # Random hours between 0.5 and 3.0
        hourly_rate=85.00  # Standard hourly rate
    ) for i in range(10)
]

# Define fees
disposal_fee = Fee(description="Oil Disposal Fee", amount=10.00)

# Create an invoice and add items
invoice = Invoice(
    parts=[engine_part, oil_filter] + random_parts,
    labor=[labor_replace_mount, labor_oil_change] + random_labor,
    fees=[disposal_fee]
)

## REPORT GENERATION
def header_footer(canvas, doc):
    # Header
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(72, 750, "Auto Repair Shop Invoice")  # Header text
    canvas.line(72, 745, 540, 745)  # Header line
    
    # Footer
    canvas.setFont("Helvetica", 10)
    canvas.drawString(72, 30, "Thank you for your business!")
    canvas.drawString(450, 30, f"Page {doc.page}")
    canvas.restoreState()

# Create a PDF document
pdf_path = "invoice.pdf"
pdf = SimpleDocTemplate(pdf_path, pagesize=LETTER)

# Define a frame for content (leaving space for header and footer)
frame = Frame(72, 100, 468, 600, id='normal')  # Adjust height as needed for content

# Define a template with the custom header and footer
template = PageTemplate(id='header_footer_template', frames=frame, onPage=header_footer)
pdf.addPageTemplates([template])

# Define table data
parts_data = [["Part Name", "Unit Price", "Quantity", "Core Charge", "Total Price"]]
parts_data.extend(invoice.parts_to_array())  # Add parts as rows

# Define table data
labor_data = [["Description", "Hours", "Hourly Rate"]]
labor_data.extend(invoice.labor_to_array())  # Add parts as rows

# Create table and apply styling
parts_table = Table(parts_data)
parts_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
]))

# Create table and apply styling
labor_table = Table(labor_data)
labor_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
]))

# Build the PDF
pdf.build([parts_table, labor_table])
print(f"PDF generated at: {pdf_path}")