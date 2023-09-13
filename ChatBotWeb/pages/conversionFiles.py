import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import os
import base64
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
    dbc.Row([
        NAVBAR
    ]),

    html.H2([
        "Conversão de Arquivos"
    ], className='text-center mt-2'),

    html.Hr(),

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
        ),
    ),

    html.Hr(),

    html.Div(
        id="naosei"
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
])


@app.callback(
    Output('naosei', 'children'),
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
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
)
def display_and_convert_to_pdf(contents, filename):
    if contents is not None and filename is not None:
        temp_dir = 'temp_dir'
        os.makedirs(temp_dir, exist_ok=True)
        docx_path = os.path.join(temp_dir, filename)



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


if __name__ == '__main__':
    app.run(debug=True)
