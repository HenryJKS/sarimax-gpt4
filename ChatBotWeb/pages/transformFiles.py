import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import os
import base64
from docx2pdf import convert

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='tranformFiles',
    top_navbar=True,
    path='/transform',
    external_stylesheets=[dbc.themes.LITERA]
)

layout = html.Div([
    dbc.Row([
        NAVBAR
    ]),

    html.H2("Upload de Arquivos .docx"),

    # Componente DashUploader para o upload de arquivos
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arraste e solte ou ',
                html.A('selecione um arquivo .docx')
            ]),
            multiple=False,
            style={'width': '28%'}
        ),
        html.Div(id='output-data-upload-info'),
    ]),
])


@callback(
    Output('output-data-upload-info', 'children'),
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
)
def display_and_convert_to_pdf(contents, filename):
    if contents is not None and filename is not None:
        # Criar um diretório temporário para salvar o arquivo .docx
        temp_dir = 'temp_dir'
        os.makedirs(temp_dir, exist_ok=True)
        docx_path = os.path.join(temp_dir, filename)

        # Salvar o conteúdo do arquivo .docx no diretório temporário
        with open(docx_path, 'wb') as f:
            f.write(contents[0])

        # Converter o arquivo .docx para .pdf
        pdf_filename = filename.replace('.docx', '.pdf')
        pdf_path = os.path.join(temp_dir, pdf_filename)
        convert(docx_path, pdf_path)

        # Exibir informações sobre o arquivo enviado e o link para o arquivo .pdf gerado
        return [
            html.Div(f'Arquivo carregado: {filename}, Tamanho: {os.path.getsize(docx_path)} bytes'),
            html.A(f'Link para o arquivo PDF gerado: {pdf_filename}', href=pdf_path)
        ]
    else:
        return ''




