from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
import pandas as pd


def create_pdf(dataframe, filename, chat_log, selected_data):
    # Crie um buffer de bytes para armazenar o PDF
    buffer = BytesIO()

    # Crie um documento PDF com o ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Adicione os dados selecionados ao PDF
    elements = []

    styles = getSampleStyleSheet()

    # Adicione os dados da tabela
    data = [dataframe.columns.tolist()] + dataframe.values.tolist()
    table = Table(data)

    centered_title_style = ParagraphStyle(
        'CenteredTitle',
        parent=styles['Heading1'],
        alignment=1,  # 1 significa centralizado
    )

    # Adicione "RELATÓRIO FORD" centralizado
    title = Paragraph("RELATÓRIO FORD", centered_title_style)
    elements.append(title)
    elements.append(Spacer(1, 20))

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
    elements.append(table)

    # elements.append(Paragraph("Dados Selecionados:", styles['Normal']))
    # for entry in selected_data:
    #     elements.append(Paragraph(entry, styles['Normal']))

    elements.append(Spacer(1, 20))
    # Adicione o log de perguntas e respostas do chat
    elements.append(Paragraph("Chat Log:", styles['Heading1']))
    if chat_log is not None:
        for entry in chat_log:
            question, answer = entry
            elements.append(Paragraph(f"Pergunta: {question}", styles['Normal']))
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(f"Resposta: {answer}", styles['Normal']))
            elements.append(Spacer(1, 30))
    else:
        elements.append(Paragraph("Nenhuma pergunta foi feita", styles['Normal']))

    # Construa o PDF
    doc.build(elements)

    # Salve o PDF no arquivo especificado
    with open(filename, 'wb') as f:
        f.write(buffer.getvalue())


