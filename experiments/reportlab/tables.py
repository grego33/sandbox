from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def create_simple_table():
    data = [
        ['Column 1', 'Column 2', 'Column 3'],
        ['Row 1, Col 1', 'Row 1, Col 2', 'Row 1, Col 3'],
        ['Row 2, Col 1', 'Row 2, Col 2', 'Row 2, Col 3'],
        ['Row 3, Col 1', 'Row 3, Col 2', 'Row 3, Col 3 with more text']
    ]

    # Calculate column widths
    margin_width  = 50
    page_width = letter[0] - margin_width * 2
    num_columns = len(data[0])
    column_width = page_width / num_columns

    table = Table(data, colWidths=[column_width] * num_columns)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    return table


def create_pdf(filename):
    document = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    elements.append(create_simple_table())
    document.build(elements)

if __name__ == "__main__":
    create_pdf("data/simple_table.pdf")