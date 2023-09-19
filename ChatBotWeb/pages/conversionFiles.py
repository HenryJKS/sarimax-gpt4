import re

import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from ChatBotWeb.components import navbar
import os

from Script.helpers import docx_to_pdf, pdf_to_docx, download_pdf, delete_files

app = dash.Dash(__name__, use_pages=False, external_stylesheets=[dbc.themes.LITERA], title='FordBot')
NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='conversionFiles',
    top_navbar=True,
    path='/conversion',
    external_stylesheets=['assets/conversionFiles.css']
)

app.layout = html.Div([
    # Navbar
    dbc.Row([
        NAVBAR
    ]),

    # Título
    html.H2("Conversão de Arquivos", className='title--conversion--files'),

    html.Hr(),

    # Selecionar tipo de arquivo
    dbc.Row(
        dbc.Col(
            dcc.Dropdown(
                id='select_conversion',
                options=[
                    {'label': 'PDF para Docx', 'value': 'DOCX'},
                    {'label': 'Docx para PDF', 'value': 'PDF'}
                ],
                className="custom-dropdown",  # Classe CSS personalizada
                style={'width': '200px'},  # Largura personalizada
            ),
            className="mt-3"
        )
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
            disabled=True,
            style={'width': '28%'},
        ),
        html.Div(id='output-data-upload-info'),
        html.Div(id='convert-data-info'),
    ]),

    html.Div([
        html.Button("Baixar arquivo", id="btn-download-txt", className="btn btn-primary"),
        dcc.Download(id='download-pdf-converted'),
    ], className="text-center mt-3"),
    html.Div(id='download-data-info'),
])


@app.callback(
    Output('selected_file', 'children'),
    [
        Input('select_conversion', 'value'),
    ]
)
def select_conversion_type(value):
    ctx = dash.callback_context
    msg = ''

    if not ctx.triggered:
        return ''
    else:
        if value == 'DOCX':
            msg = 'pdf_to_docx'
        elif value == 'PDF':
            msg = 'docx_to_pdf'
        return html.Div(msg)


@app.callback(
    Output('output-data-upload-info', 'children'),
    [
        Input('select_conversion', 'value'),
        Input('upload-data', 'filename')
    ],
)
def update_display(option, filename):
    if filename is not None and option is not None:

        return [
            html.Div(f"Arquivo carregado: {filename}"),
        ]
    else:
        return ''


@app.callback(
    Output('upload-data', 'disabled'),  # Atualiza a propriedade 'disabled' do componente upload-data
    Input('select_conversion', 'value')
)
def update_upload_data_availability(selected_option):
    # Habilita o componente upload-data apenas se uma opção for selecionada no dropdown
    return selected_option is None


@app.callback(
    Output('convert-data-info', 'children'),
    [
        Input('select_conversion', 'value'),
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename')
    ],
    prevent_initial_call=True,
)
def convert_files(option, content, filename):
    msg = ''

    if content is not None and filename is not None:
        try:
            if option == 'PDF':
                pdf_filename = docx_to_pdf(content, filename)
            elif option == 'DOCX':
                docx_filename = pdf_to_docx(content, filename)
                return f"Arquivo convertido: {docx_filename}",
        except Exception as e:
            return html.Div(f'Faça upload de um arquivo {str(filename).split(".")[1]}!')
        return html.Div(msg)
    else:
        raise PreventUpdate


@app.callback(
    Output('download-data-info', 'children'),
    Input('btn-download-txt', 'n_clicks'),
    State('convert-data-info', 'children')
)
def download_file(n_clicks, convert_data_info):
    if n_clicks is None:
        return ''

    convert_data_info = str(convert_data_info).replace('[', '').replace(']', '').replace("'", '')

    match = re.search(r"Arquivo convertido: (.+)", convert_data_info)
    if match:
        filename = match.group(1)
        try:
            download_pdf(filename)
            return html.Div(f'PDF baixado com sucesso: {filename}')
        except Exception as e:
            return html.Div(f'Erro ao baixar o PDF: {str(e)}')
    else:
        return html.Div('Nenhum PDF encontrado para download')


if __name__ == '__main__':
    app.run(debug=True)
