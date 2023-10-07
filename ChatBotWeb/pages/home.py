import dash
from dash import html, dcc, callback, Output, Input
from ChatBotWeb.components import navbar, card1, carousel
import dash_bootstrap_components as dbc

NAVBAR = navbar.create_navbar()
CARD1 = card1.card1()
CAROUSEL = carousel.create_carousel()

dash.register_page(
    __name__,
    path='/',
    name='Home',
    top_navbar=True,
    external_stylesheets=['assets/fordbot.css'], )

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2("Home", className='text-center mt-2'),
    ]),

    html.Div([
        html.Hr(style={'color': 'black'}),
    ]),

    dbc.Container([
        html.Div([
            CAROUSEL
        ]),
    ]),

], fluid=True)
