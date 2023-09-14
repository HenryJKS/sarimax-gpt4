import os

import dash
from dash import Input, Output, State, callback, dcc, html
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
from Script.passwordpdf import add_password
import base64
import io

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Crypto PDF',
    top_navbar=True,
    path='/crypto',
)

layout = dbc.Container([
    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2('FordBot Security', className='text-center mt-2'),
    ]),

    html.Div([
        html.Hr()
    ]),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arraste e solte ou ',
            html.A('Selecione Arquivos')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin-top': '10px'
        },
        # Permite múltiplos arquivos para serem carregados
        multiple=False
    ),

    html.Div([
        dbc.InputGroup([
            dcc.Input(
                id='pdf-password',
                type='password',
                placeholder='Senha'
            ),
            html.Button('Enviar', id='submit-button', n_clicks=0, className='btn btn-info text-center')
        ]),
    ], className='mt-2'),

    html.Div([

    ], id='pdf-list'),

    html.Div(id='output-data-upload-pdf'),

], fluid=True)


@callback(Output('output-data-upload-pdf', 'children'),
          Input('submit-button', 'n_clicks'),
          State('upload-data', 'contents'),
          State('upload-data', 'filename'),
          State('pdf-password', 'value')
          )
def parse_contents(n_clicks, contents, filename, password):
    if n_clicks > 0:
        if not contents:
            return html.Div([
                dbc.Alert("Insira um Arquivo PDF !", color='danger', className='mt-2 text-center',
                          style={'width': 'auto'}),
            ])
        elif not password:
            return html.Div([
                dbc.Alert("Insira uma Senha !", color='danger', className='mt-2 text-center',
                          style={'width': 'auto'}),
            ])
        elif not filename.lower().endswith('.pdf'):
            return html.Div([
                dbc.Alert("Insira Somente Arquivo .PDF !", color='danger', className='mt-2 text-center',
                          style={'width': 'auto'}),
            ])
        elif filename.lower().endswith('.pdf'):
            # Decodifica o arquivo PDF
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)

            # Criar o arquivo PDF criptografado
            pdf = io.BytesIO(decoded)
            add_password(pdf, f'fordcrypt_{filename}', password)

            # Ler o arquivo PDF criptografado
            with open(f'fordcrypt_{filename}', 'rb') as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')

            # Deletar o arquivo PDF criptografado
            os.remove(f'fordcrypt_{filename}')

            # Retorna o arquivo PDF criptografado
            return html.Div([
                dbc.Alert("Arquivo Criptografado com Sucesso!", color='success', className='mt-2 text-center',
                          style={'width': 'auto'}),
                # Usa o componente de visualização de PDF do Dash
                html.Iframe(src=f'data:application/pdf;base64,{base64_pdf}', width='100%', height='700')
            ])

        return html.Div([
            html.P('Erro ao Criptografar Arquivo', className='text-danger')
        ])


@callback(Output('pdf-list', 'children'),
          Input('upload-data', 'filename'))
def pdf_list(filename):
    if filename is not None:
        return html.Div([
            html.P(f'Arquivo Selecionado: {filename}', className='text-info mt-2', style={'text-height': '100px'})
        ])

