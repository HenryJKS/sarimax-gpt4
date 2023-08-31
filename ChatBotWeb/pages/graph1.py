import plotly.express as px
from dash import dcc, html, callback, State, Input, Output
import dash_bootstrap_components as dbc
import dash
from ChatBotWeb.chatAPI.ModelAPI import chat
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
    external_stylesheets=[dbc.themes.LITERA]
)

layout = dbc.Container([

    html.Link(rel="stylesheet", href="ChatBotWeb/assets/style.css"),

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2("Faturamento por Ano", className='text-center mt-2'),
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

                        html.Div(id='resposta')
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
            figure=px.bar(data, x='Ano', y='Faturamento', color='Faturamento', barmode='group', ), id='graph')
    ], className="justify-content-center", style={'width': '80%', 'margin': 'auto'}),

    # html.Div([
    # ], id='valores'),
], fluid=True, style={'background-color': 'rgb(233,243,240)', 'height': '100%'})


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
        return dash.no_update

    # Gerando resposta
    resposta = chat('Ano: ' + str(data['Ano']) + 'Faturamento: ' + str(data['Faturamento']) + str(question))

    # Retornando para os Outputs
    return html.Div([
        html.P(resposta, className='font-weight-light')
    ], className='text-center border border-dark rounded'),
