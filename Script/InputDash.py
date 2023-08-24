import base64
from io import BytesIO
import plotly.express as px
from dash import Dash, dcc, html, callback, State, Input, Output
import dash_bootstrap_components as dbc
import dash
from TestingOpenAI import chat

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    html.H1("Plotagem de Gráfico"),

    dbc.Col([
        dbc.Row([
            dcc.Input(id='x-values', type='text', placeholder='Valores de X separados por vírgula',
                      style={'width': '25%'}),
        ]),
        dbc.Row([
            dcc.Input(id='y-values', type='text', placeholder='Valores de Y separados por vírgula',
                      style={'width': '25%'}),
        ]),
        dbc.Row([
            html.Button('Plotar Gráfico', id='submit-button',
                        className='btn btn-primary',
                        style={'width': '25%'})
        ])
    ]),

    dbc.Container([
        dcc.Graph(id='graph'),
    ]),

    html.Div([], id='valores')

], fluid=True)


@app.callback(
    Output('graph', 'figure'),
    Output('valores', 'children'),
    Input('submit-button', 'n_clicks'),
    State('x-values', 'value'),
    State('y-values', 'value')
)
def create_graph(n_clicks, x_values_str, y_values_str):

    if not n_clicks:
        return dash.no_update, dash.no_update

    # Separa os valores
    x_values = x_values_str.split(',')
    y_values = y_values_str.split(',')

    # Verifica se o botão foi clicado
    # Tratando erros
    if x_values_str is None or y_values_str is None:
        return dash.no_update
    elif len(x_values) != len(y_values):
        return dash.no_update
    elif len(x_values) == 0 or len(y_values) == 0:
        return dash.no_update

    # Verifica se os valores são números
    try:
        x_values = [float(x) for x in x_values]
        y_values = [float(y) for y in y_values]
    except ValueError:
        return dash.no_update

    # Gerando grafico
    fig = px.line(x=x_values, y=y_values, title='Gráfico')

    frase = chat('x' + str(x_values) + 'y' + str(y_values) + 'previsão de Abril?')

    # Retornando para os Outputs
    return fig, html.H4(frase)


if __name__ == '__main__':
    app.run_server(debug=True)
