import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import os
import base64
import pandas as pd
import pythoncom
from docx2pdf import convert

NAVBAR = navbar.create_navbar()

app = dash.Dash(__name__, use_pages=False, external_stylesheets=[dbc.themes.LITERA])

"""dash.register_page(
    __name__,
    name='cnoversionFiles',
    top_navbar=True,
    path='/conversion',
    external_stylesheets=[dbc.themes.LITERA]
)"""

app.layout = html.Div([
    # Navbar
    dbc.Row([
        NAVBAR
    ]),

    #Título
    html.H2([
        "Conversão de Arquivos"
    ], className='text-center mt-2'),

    html.Hr(),

    # Selecionar tipo de arquivo
    html.Div(
        dbc.ButtonGroup(
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem('PDF to Docx', id='pdf_to_docx', key=1),
                    dbc.DropdownMenuItem('Docx to PDF', id='docx_to_pdf', key=2), ],
                label="Selecione o tipo de conversão",
                group=True,
                id='select_conversion'
            ),
            className="justify-content-center",
        ),
        style={"display": "flex, w"}
    ),

    html.Hr(),

    html.Div(
        id="selected_file"
    ),

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

    html.Div([
        html.Button("Baixar arquivo", id="btn-download-txt"),
        dcc.Download(id='download-pdf')
    ])
])


@app.callback(
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


@app.callback(
    Output('output-data-upload-info', 'children'),
    [
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename')
    ]
)
def display_and_convert_to_pdf(content, filename):
    if content is not None and filename is not None:
        content_str = content.split(",")[1]
        file_bytes = base64.b64decode(content_str)

        temp_dir = 'temp_dir'
        os.makedirs(temp_dir, exist_ok=True)

        docx_path = os.path.join(temp_dir, filename)

        with open(docx_path, 'wb') as f:
            f.write(file_bytes)

        pythoncom.CoInitialize()

        pdf_filename = filename.replace('.docx', '.pdf')
        pdf_path = os.path.join(temp_dir, pdf_filename)
        convert(docx_path, pdf_path)

        print(pdf_path)
        pythoncom.CoUninitialize()

        return [
            html.Div(f"Arquivo carregado: {filename}"),
        ]
    else:
        return ''


@app.callback(
    Output('download-pdf', 'data'),
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


if __name__ == '__main__':
    app.run(debug=True)
