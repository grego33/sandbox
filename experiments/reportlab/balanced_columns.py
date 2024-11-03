from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, BalancedColumns, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create a sample document
doc = SimpleDocTemplate("enhanced_balanced_columns_example.pdf", pagesize=letter)

# Define styles
styles = getSampleStyleSheet()
body_text_style = styles["BodyText"]
title_style = styles["Title"]

# Sample content with multiple paragraphs
paragraphs = [
    Paragraph("Introduction", title_style),
    Paragraph("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.""", body_text_style),
    Spacer(1, 0.2 * inch),
    
    Paragraph("Background", title_style),
    Paragraph("""Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""", body_text_style),
    Spacer(1, 0.2 * inch),

    Paragraph("Analysis", title_style),
    Paragraph("""Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Cras mattis consectetur purus sit amet fermentum. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum.""", body_text_style),
    Spacer(1, 0.2 * inch),

    Paragraph("Conclusion", title_style),
    Paragraph("""Curabitur blandit tempus porttitor. Maecenas sed diam eget risus varius blandit sit amet non magna. Vestibulum id ligula porta felis euismod semper. Nullam quis risus eget urna mollis ornare vel eu leo.""", body_text_style)
]

# Define BalancedColumns to create a two-column layout
balanced_columns = BalancedColumns(
    paragraphs,  # List of paragraphs to balance across columns
    nCols=3,     # Number of columns
    needed=3 * inch,  # Minimum height needed for the flowable
    showBoundary=True  # Show column boundaries for visualization
)

# Build the document with the BalancedColumns flowable
doc.build([balanced_columns])
