from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Define the header for the first page
def first_page_header(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(inch, LETTER[1] - inch, "First Page Header")
    canvas.restoreState()

# Define the header for the following pages
def following_pages_header(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 12)
    canvas.drawString(inch, LETTER[1] - inch, "Following Pages Header")
    canvas.restoreState()

# Create the PDF document
def create_pdf(filename):
    class MyDocTemplate(BaseDocTemplate):
        def afterFlowable(self, flowable):
            if isinstance(flowable, Paragraph):
                print(f'{self.page}: {flowable.getPlainText()}')
            if self.page == 1:
                self.handle_nextPageTemplate('FollowingPages')

    doc = MyDocTemplate(filename, pagesize=LETTER, showBoundary=1)
 
    styles = getSampleStyleSheet()
    story = []

    # Add some content
    for i in range(100):
        story.append(Paragraph(f"This is paragraph {i+1}.", styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    # Define frames
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 2 * inch, id='normal')
    second_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 1 * inch, id='smaller_top_margin')
   
    # Define page templates
    first_page_template = PageTemplate(id='FirstPage', frames=frame, onPage=first_page_header)
    following_pages_template = PageTemplate(id='FollowingPages', frames=second_frame, onPage=following_pages_header)

    # Add templates to the document
    doc.addPageTemplates([first_page_template, following_pages_template])

    # Build the document
    doc.build(story)

# Create the PDF
create_pdf("pagetemplates_demo.pdf")