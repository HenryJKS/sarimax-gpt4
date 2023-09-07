import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import time

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LITERA])

app.layout = html.Div([
    dash.page_container,
    dcc.Loading(fullscreen=True, type="circle", color="#103D82", id='loading'),
    dcc.Location(id='url', refresh=False)
], style={'background-color': '#e8f5ff', 'height': '100vh'})


@app.callback(
    Output('loading', 'children'),
    Input('url', 'pathname')
)
def loading(pathname):
    time.sleep(1)
    return None


if __name__ == '__main__':
    app.run(debug=True)
