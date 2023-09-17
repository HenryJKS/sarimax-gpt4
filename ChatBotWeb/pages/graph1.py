import time

import plotly.express as px
from dash import dcc, html, callback, State, Input, Output
import dash_bootstrap_components as dbc
import dash
from ChatBotWeb.chatAPI.ModelAPI import chat_faturamento
from ChatBotWeb.components import navbar
from ChatBotWeb.query.queryFaturamento import df

data = df
data['Ano'] = data['Ano'].astype(str)

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Dashboard',
    top_navbar=True,
    path='/graph1',
    external_stylesheets=['assets/graph1.css'],
)

fig = px.line(data, x="Ano", y="Faturamento", color='Modelo')
fig.update_layout({
            'plot_bgcolor': '#d6ecfd',
            'paper_bgcolor': '#d6ecfd',
            'font': {
                'size': 12,
                'color': 'black'
            },
        })

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2("Faturamento Veículo", className='text-center mt-2'),
    ]),

    html.Hr(),

    html.Div([
        dbc.Button(
            "Fordbot",
            id="horizontal-collapse-button",
            color="primary",
            n_clicks=0,
            style={}
        ),
    ], className='mb-2'),
    html.Div(
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                    html.Div([
                        html.H6('Análise Gráfica: '),
                        dbc.InputGroup([
                            dbc.Input(id='question', type='text', placeholder='Pergunte ao Bot'),
                            dbc.Button('Enviar', id='send-response', className='btn btn-primary btn-sm')
                        ], className='mb-2'),

                        html.Div([
                        ], id='resposta')
                    ], style={'width': '100%'}),
                ),
                className='background-1',
                style={"width": "400px"},
            ),
            id="horizontal-collapse",
            is_open=True,
            dimension="width",
            style={}
        ),
        className='mb-4',
        style={"minHeight": "100px"},
    ),

    html.Div([
        dcc.Graph(
            figure=fig,
            id='graph1',
            className='border border-primary',
            style={'width': '100%', 'height': '100%', 'border-radius': '5px'},
            ),
    ], className="justify-content-center",
        style={'width': '80%', 'margin': 'auto'}),

], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


@callback(
    Output("horizontal-collapse", "is_open"),
    [Input("horizontal-collapse-button", "n_clicks")],
    [State("horizontal-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output('resposta', 'children'),
    Input('send-response', 'n_clicks'),
    State('question', 'value'),
)
def create_response(n_clicks, question):
    if not n_clicks:
        return dash.no_update

    # Verifica se o botão foi clicado
    # Tratando erros
    if question is None:
        return html.P("Insira uma pergunta", className='text-left border border-dark rounded',
                      style={'padding': '10px'})

    # Gerando resposta
    resposta = chat_faturamento(f"dados: {str(df)}, pergunta: {str(question)}")

    # Retornando para os Outputs
    return (
        html.Div([
            html.P(resposta, className='font-weight-light text-left border border-dark rounded',
                   style={'padding': '10px'})
        ]))
