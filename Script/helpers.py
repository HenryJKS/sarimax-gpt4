import base64
import os

import pythoncom
from dash import dcc
from docx2pdf import convert
from pdf2docx import Converter


def docx_to_pdf(docx_content, docx_filename):
    pythoncom.CoInitialize()

    temp_dir = 'temp_dir'
    os.makedirs(temp_dir, exist_ok=True)

    content_str = docx_content.split(",")[1]
    file_bytes = base64.b64decode(content_str)

    docx_path = os.path.join(temp_dir, docx_filename)

    with open(docx_path, 'wb') as f:
        f.write(file_bytes)

    pdf_filename = docx_filename.replace('.docx', '.pdf')
    pdf_path = os.path.join(temp_dir, pdf_filename)
    convert(docx_path, pdf_path)

    return pdf_filename

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

    docx_filename = pdf_filename.replace('.pdf', '.docx')
    docx_path = os.path.join(temp_dir, docx_filename)
    print(pdf_path)
    print(docx_path)
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()
    return docx_filename

    # print(pdf_path)
    pythoncom.CoUninitialize()


def download_pdf(filename):
    temp_dir = 'temp_dir'
    file_path = os.path.join(temp_dir, filename)

    if os.path.exists(file_path):
        if file_path.lower().endswith('.pdf'):
            with open(file_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
                return dcc.send_bytes(pdf_data, filename=filename)
        elif file_path.lower().endswith('.docx'):
            with open(file_path, "rb") as docx_file:
                docx_data = docx_file.read()
                return dcc.send_bytes(docx_data, filename=filename)
    else:
        return "Arquivo não encontrado"


def delete_files():
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
