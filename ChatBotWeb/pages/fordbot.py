from ChatBotWeb.components import navbar
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='FordBot',
    top_navbar=True,
    path='/fordbot',
    external_stylesheets=[dbc.themes.LITERA]
)

layout = dbc.Container([
    dbc.Row([
        NAVBAR
    ]),

    html.Link(rel="stylesheet", href="ChatBotWeb/assets/fordbot.css"),

    html.Div([
        html.Main(className="page-container", children=[
            html.H1(children=["Quem é FordBot ?"]),
            html.P(children=[
                "FordBot é uma inteligência artificial especializada em análise de dados. Onde ele receberá os dados "
                "dos gráficos e responderá a perguntas relacionadas a eles."]),
            html.P(children=[
                "Dúvidas sobre previsões ou cálculos ele "
                "garantirá uma resposta assertiva.",
            ]),
            html.P(children=[
                "A tecnologia usada é a engine GPT 4.0 com o API da OpenAI.",
            ]),
            html.P(children=[
                "Propósito: Um dos motivos pela invenção é trazer agilidade e praticidade para o usuário, onde ele "
                "possa tomar decisões mais rápidas e assertivas."
            ]),
            html.P(children=[
                "Limitações: O FordBot só é treinado para responder perguntas relacionado aos dados recebidos pelo "
                "gráfico."
            ]),
        ])
    ])
], fluid=True, className='')
