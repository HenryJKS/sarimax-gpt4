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

layout = html.Div([
    # Navbar
    dbc.Row([
        NAVBAR
    ]),

    # MAIN
    html.Div([
        # HEADER
        html.Div(
            html.H2("Conversão de Arquivos",
                    className='title--conversion--files',
                    style={
                        'padding': '1rem 0 0'
                    }),
        ),

        # UPLOAD
        html.Div([
            dbc.Row(
                dbc.InputGroup([
                    dbc.Select(
                        id='select_conversion',
                        options=[
                            {'label': 'PDF para Docx', 'value': 'pdf'},
                            {'label': 'Docx para PDF', 'value': 'docx'}
                        ],
                    ),
                    dbc.InputGroupText(
                        id='selected_file',
                    )
                ],
                    style={
                        'display': 'flex',
                    }
                ),
                style={
                        'display': 'flex',
                        'margin': '1.5rem 0'
                    }
            ),
            dbc.Row(
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Arraste e solte ou ',
                        html.A('selecione um arquivo .docx')
                    ]),
                    multiple=False,
                    disabled=True,
                    style={
                        'display': 'flex',
                        'align-items': 'center',
                    },
                ),
                style={
                        'display': 'flex',
                        'height': '200px',
                        'align-items': 'center',
                        'margin': '1.5rem 0',
                        'border': '1px dotted #e2e2e2',
                        'border-radius': '8px',
                        'padding': '0 1rem'
                    }
            ),
            html.Div(id='output-data-upload-info'),
            html.Div(id='convert-data-info'),
        ],
            style={
                'display': 'flex',
                'margin': '2rem 0',
                'flex-direction': 'column',
                'justify-content': 'space-between',
                'align-items': 'center',
                'width': '80vw',

            }),

        html.Div([
            html.Button("Baixar arquivo", id="btn-download-txt", className="btn btn-primary"),
            dcc.Download(id='download-file-converted'),
        ], className="text-center mt-3"),
        html.Div(id='download-status'),
    ],
        style={
            'display': 'flex',
            'width': '100vw',
            'flex-direction': 'column',
            'align-items': 'center',
        }
    ),
])

download_status = None


@app.callback(
    Output('selected_file', 'children'),
    Input('select_conversion', 'value'),
)
def select_conversion_type(value):
    text_mapping = {
        'pdf': 'PDF para Docx',
        'docx': 'Docx para PDF',
    }

    selected_text = text_mapping.get(value, 'Selecione uma opção')

    return selected_text


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
            if option == 'docx':
                pdf_filename = docx_to_pdf(content, filename)
                return f"Arquivo convertido: {pdf_filename}"
            elif option == 'pdf':
                docx_filename = pdf_to_docx(content, filename)
                return f"Arquivo convertido: {docx_filename}"
        except Exception as e:
            return html.Div(f'Faça upload de um arquivo .{option}!')
        return html.Div(msg)
    else:
        raise PreventUpdate


@app.callback(
    Output('download-file-converted', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    State('convert-data-info', 'children')
)
def download_file(n_clicks, convert_data_info):
    global download_status

    if n_clicks:
        convert_data_info = str(convert_data_info).replace('[', '').replace(']', '').replace("'", '')

        match = re.search(r"Arquivo convertido: (.+)", convert_data_info)
        if match:
            filename = match.group(1)
            try:
                download_status = download_pdf(filename)
                return download_status
            except Exception as e:
                print(f'Erro ao baixar o PDF: {str(e)}')


@app.callback(
    Output('download-status', 'children'),
    Input('btn-download-txt', 'n_clicks'),
)
def update_download_file_info(n_clicks):
    if n_clicks:
        if download_status:
            return html.Div('Arquivo baixado com sucesso')
        else:
            return html.Div('Nenhum PDF encontrado para download')
    else:
        return ''


if __name__ == '__main__':
    app.run(debug=True)
