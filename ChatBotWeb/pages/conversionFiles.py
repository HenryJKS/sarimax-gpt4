import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import os
import base64
import pandas as pd
import pythoncom
from docx2pdf import convert

from Script.helpers import docx_to_pdf, delete_dir

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='conversionFiles',
    top_navbar=True,
    path='/conversion',
    external_stylesheets=[dbc.themes.LITERA]
)

layout = html.Div([
    # Navbar
    dbc.Row([
        NAVBAR
    ]),

    # Título
    html.H2("Conversão de Arquivos", className='text-center mt-2'),

    html.Hr(),

    # Selecionar tipo de arquivo
    html.Div(
        dbc.ButtonGroup(
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem('PDF to Docx', id='pdf_to_docx', key=1),
                    dbc.DropdownMenuItem('Docx to PDF', id='docx_to_pdf', key=2),
                ],
                label="Selecione o tipo de conversão",
                group=True,
                id='select_conversion',
            ),
            className="justify-content-center",
        ),
        style={"display": "flex, w"},
    ),

    html.Hr(),

    html.Div(id="selected_file"),

    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arraste e solte ou ',
                html.A('selecione um arquivo .docx')
            ]),
            multiple=False,
            style={'width': '28%'},
        ),
        html.Div(id='output-data-upload-info'),
    ]),

    html.Div([
        html.Button("Baixar arquivo", id="btn-download-txt", className="btn btn-primary"),
        dcc.Download(id='download-pdf-converted'),
    ], className="text-center mt-3"),
])


@callback(
    Output('selected_file', 'children'),
    [
        Input('pdf_to_docx', 'n_clicks'),
        Input('docx_to_pdf', 'n_clicks'),
    ]
)
def transform_files(a1, a2):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ''
    else:
        item_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if item_id == "pdf_to_docx":
            return 'pdf_to_docx'
        elif item_id == 'docx_to_pdf':
            return 'docx_to_pdf'


@callback(
    Output('output-data-upload-info', 'children'),
    [
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename')
    ]
)
def display_and_convert_to_pdf(content, filename):
    if content is not None and filename is not None:

        docx_to_pdf(content, filename)

        return [
            html.Div(f"Arquivo carregado: {filename}"),
        ]
    else:
        return ''


@callback(
    Output('download-pdf-converted', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    prevent_initial_call=True,
)
def download_pdf(n_clicks):
    temp_dir = 'temp_dir'
    files = os.listdir(temp_dir)

    pdfs = [file for file in files if file.lower().endswith('.pdf')]
    if pdfs:
        for pdf in pdfs:
            pdf_path = f'{temp_dir}/{pdf}'

            with open(pdf_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
                return dcc.send_bytes(pdf_data, filename=pdf_path)
