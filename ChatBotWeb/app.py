import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LITERA])

app.layout = html.Div([
    dash.page_container
], style={'background-color': '#e8f5ff', 'height': '100vh'})

if __name__ == '__main__':
    app.run(debug=True)
