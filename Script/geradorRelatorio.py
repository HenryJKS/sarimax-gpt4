from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
import pandas as pd

def create_pdf(dataframe, filename):
    # Crie um buffer de bytes para armazenar o PDF
    buffer = BytesIO()

    # Crie um documento PDF com o ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Converta o DataFrame em uma lista de listas para criar a tabela
    data = [dataframe.columns.tolist()] + dataframe.values.tolist()
    table = Table(data)

    # Estilize a tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)),
                        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
                        ('GRID', (0, 0), (-1, 0), 2, (0, 0, 0))])

    table.setStyle(style)

    # Adicione a tabela ao documento PDF
    elements = [table]

    # Construa o PDF
    doc.build(elements)

    # Salve o PDF no arquivo especificado
    with open(filename, 'wb') as f:
        f.write(buffer.getvalue())
