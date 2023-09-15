import base64
import os

import pythoncom
from docx2pdf import convert


def docx_to_pdf(docx_content, docx_filename):
    print(docx_filename)
    pythoncom.CoInitialize()

    temp_dir = 'temp_dir'
    os.makedirs(temp_dir, exist_ok=True)

    content_str = docx_content.split(",")[1]
    file_bytes = base64.b64decode(content_str)

    docx_path = os.path.join(temp_dir, docx_filename)
    print(docx_path)

    with open(docx_path, 'wb') as f:
        f.write(file_bytes)

    pdf_filename = docx_filename.replace('.docx', '.pdf')
    pdf_path = os.path.join(temp_dir, pdf_filename)
    convert(docx_path, pdf_path)

    # print(pdf_path)
    pythoncom.CoUninitialize()


def pdf_to_docx():
    pass


def delete_dir():
    os.remove('../ChatBotWeb/temp_dir')
