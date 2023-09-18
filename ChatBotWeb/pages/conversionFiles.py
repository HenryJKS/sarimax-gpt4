import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from ChatBotWeb.components import navbar
import os

from Script.helpers import docx_to_pdf, pdf_to_docx, download_pdf, delete_files

app = dash.Dash(__name__, use_pages=False, external_stylesheets=[dbc.themes.LITERA], title='FordBot')

NAVBAR = navbar.create_navbar()

'''
dash.register_page(
    __name__,
    name='conversionFiles',
    top_navbar=True,
    path='/conversion',
    external_stylesheets=[dbc.themes.LITERA]
)
'''

app.layout = html.Div([
    # Navbar
    dbc.Row([
        NAVBAR
    ]),

    # Título
    html.H2("Conversão de Arquivos", className='text-center mt-2'),

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
            style={'width': '28%'},
        ),
        html.Div(id='output-data-upload-info'),
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
        Input('upload-data', 'filename')
    ],
)
def update_display(filename):
    if filename is not None:

        return [
            html.Div(f"Arquivo carregado: {filename}"),
        ]
    else:
        return ''


@app.callback(
    Output('download-data-info', 'children'),
    [
        Input('btn-download-txt', 'n_clicks'),
        Input('select_conversion', 'value'),
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename')
    ],
    prevent_initial_call=True,
)
def convert_to_pdf(n_clicks, option, content, filename):
    if n_clicks is None:
        return ''

    msg = ''

    if option is not None and content is not None and filename is not None:
        if option == 'PDF':
            docx_to_pdf(content, filename)

            download_pdf()
            msg = 'PDF baixado com sucesso!'
        elif option == 'DOCX':
            pdf_to_docx(content, filename)
        delete_files()
        return html.Div(msg)
    else:
        raise PreventUpdate


if __name__ == '__main__':
    app.run(debug=True)
