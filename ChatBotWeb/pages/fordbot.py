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
    ])
], fluid=True)
