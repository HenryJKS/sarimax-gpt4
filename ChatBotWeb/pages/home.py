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
    external_stylesheets=['assets/fordbot.css'],)

layout = html.Div([

    html.Div([
        NAVBAR
    ]),

    dbc.Container([
        dbc.Col([
            html.Div([
                html.H2("Home", className='text-center mt-2'),
                html.Hr(style={'color': 'black'}),
            ]),
        ]),

        html.Div([
            CAROUSEL
        ]),
    ]),


])
