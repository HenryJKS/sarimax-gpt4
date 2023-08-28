import dash
from dash import html, dcc
from ChatBotWeb.components import navbar, card1
import dash_bootstrap_components as dbc

NAVBAR = navbar.create_navbar()
CARD1 = card1.card1()

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
        NAVBAR
    ]),

    dbc.Container([
        dbc.Col([
            html.Div([
                html.H1("Home", className='text-center mt-2'),
                html.Hr(style={'color': 'black'}),
            ]),
        ]),

        html.Div([

            html.Div([
                html.P("Gráfico de Linhas com suporte ao FordBot", className='p-card'),

            ], className='box-card', style={'display': 'flex', 'flex-direction': 'row', 'height': '25%'}),

            html.Div([
                html.P("Gráfico de Linhas com suporte ao FordBot", className='p-card')
            ], className='box-card', style={'display': 'flex', 'flex-direction': 'row-reverse', 'height': '25%'}),

            html.Div([
                html.P("Gráfico de Linhas com suporte ao FordBot", className='p-card')
            ], className='box-card', style={'display': 'flex', 'flex-direction': 'row', 'height': '25%'}),

            html.Div([
                html.P("Gráfico de Linhas com suporte ao FordBot", className='p-card')
            ], className='box-card', style={'display': 'flex', 'flex-direction': 'row-reverse', 'height': '25%'}),

        ], style={'display': 'flex', 'flex-direction': 'column'}),

    ])
])
