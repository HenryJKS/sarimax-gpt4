# -*- coding: utf-8 -*-
import base64
import datetime
import pandas as pd
import io
from dash import dcc, html, Input, Output, callback, dash_table, State
import dash
import dash_bootstrap_components as dbc
from ChatBotWeb.chatAPI.ModelAPI import chat
from ChatBotWeb.components import navbar

dataframe_gpt = None

# Variável global para armazenar o DataFrame carregado

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Dashboard',
    top_navbar=True,
    path='/graph2',
    external_stylesheets=['assets/graph2.css'],
)

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arraste e Solte ou ',
                html.A('Selecione o Arquivo')
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
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ]),

    html.Div([
        dbc.Button(
            "Fordbot",
            id="horizontal-collapse-button-export",
            color="primary",
            n_clicks=0,
            style={}
        ),
    ], className='mb-2 mt-2'),
    html.Div(
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                    html.Div([
                        html.H6('Análise Gráfica: '),
                        dbc.InputGroup([
                            dbc.Input(id='question-export', type='text', placeholder='Pergunte ao Bot'),
                            dbc.Button('Enviar', id='send-response-export', className='btn btn-primary btn-sm')
                        ], className='mb-2'),

                        html.Div(id='resposta-export')
                    ], style={'width': '100%'}),
                ),
                className='background-1',
                style={"width": "400px"},
            ),
            id="horizontal-collapse-export",
            is_open=True,
            dimension="width",
            style={}
        ),
        className='mb-4',
        style={"minHeight": "100px"},
    ),
], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


def parse_contents(contents, filename, date):
    global dataframe_gpt
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('latin-1', errors='ignore')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            f'Erro ao processar arquivo, erro: {e}'
        ])

    dataframe_gpt = df

    return html.Div([
        html.H5('Arquivo: ' + filename),
        # html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns],
            style_header={
                'backgroundColor': '#103D82',
                'fontWeight': 'bold',
                'color': 'white',
                'textAlign': 'center'
            },
            style_cell={
                'textAlign': 'center',
            },
            style_table={
                'height': 'auto',
                'overflowY': 'auto'
            },
            page_size=10
        ),

        html.Hr(),
    ])


@callback(
    Output("horizontal-collapse-export", "is_open"),
    [Input("horizontal-collapse-button-export", "n_clicks")],
    [State("horizontal-collapse-export", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output('resposta-export', 'children'),
    Input('send-response-export', 'n_clicks'),
    State('question-export', 'value'),
)
def create_response(n_clicks, question):
    if not n_clicks:
        return dash.no_update

    # Verifica se o botão foi clicado
    # Tratando erros
    if question is None:
        return dash.no_update

    # Gerando resposta
    resposta = chat('dados: ' + str(dataframe_gpt) + str(question))

    # Retornando para os Outputs
    return html.Div([
        html.P(resposta, className='font-weight-light')
    ], className='text-center border border-dark rounded'),


@callback(Output('output-data-upload', 'children'),
          Input('upload-data', 'contents'),
          State('upload-data', 'filename'),
          State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
