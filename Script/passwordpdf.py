from PyPDF2 import PdfReader, PdfWriter


def add_password(input_pdf, output_pdf, password):
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)
