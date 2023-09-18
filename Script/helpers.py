import base64
import os

import pythoncom
from dash import dcc
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


def pdf_to_docx(pdf_content, pdf_filename):
    pythoncom.CoInitialize()

    temp_dir = 'temp_dir'
    os.makedirs(temp_dir, exist_ok=True)

    content_str = pdf_content.split(",")[1]
    file_bytes = base64.b64decode(content_str)

    pdf_path = os.path.join(temp_dir, pdf_filename)

    with open(pdf_path, 'wb') as f:
        f.write(file_bytes)

    pdf_filename = pdf_filename.replace('.pdf', '.docx')
    docx_path = os.path.join(temp_dir, pdf_filename)
    convert(pdf_path, docx_path)

    # print(pdf_path)
    pythoncom.CoUninitialize()


def download_pdf():
    temp_dir = 'temp_dir'
    files = os.listdir(temp_dir)

    pdfs = [file for file in files if file.lower().endswith('.pdf')]
    if pdfs:
        for pdf in pdfs:
            pdf_path = f'{temp_dir}/{pdf}'

            with open(pdf_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
                return dcc.send_bytes(pdf_data, filename=pdf_path)


def delete_files():
    print('teste')
    temp_dir = 'temp_dir'

    if os.path.exists(temp_dir) and os.path.isdir(temp_dir):
        files = os.listdir(temp_dir)

        for file in files:
            file_path = os.path.join(temp_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Erro ao excluir arquivo/diretório {file_path}: {e}")
