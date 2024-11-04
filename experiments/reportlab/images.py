from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import qrcode

def generate_qr_code(data):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def create_pdf_with_qr_code(filename, qr_code_data):
    # Generate QR code
    qr_code_image = generate_qr_code(qr_code_data)

    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    content = []

    # Add a paragraph
    content.append(Paragraph("This is a QR code example:", styles['BodyText']))
    content.append(Spacer(1, 12))

    # Add the QR code image
    qr_code_img = Image(qr_code_image, width=100, height=100)
    content.append(qr_code_img)

    # Build the PDF
    doc.build(content)

# Example usage
qr_code_data = "https://example.com"
filename = "report_with_qr_code.pdf"
create_pdf_with_qr_code(filename, qr_code_data)