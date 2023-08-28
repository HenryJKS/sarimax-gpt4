
import plotly.express as px
from dash import Dash, dcc, html, callback, State, Input, Output
import dash_bootstrap_components as dbc
import dash
from ChatBotWeb.chatAPI.ModelAPI import chat
from ChatBotWeb.components import navbar

NAVBAR = navbar.create_navbar()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])

app.layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H1("Graphs", className='text-center mt-2'),
    ]),

    html.Hr(),

    html.Div([
        dcc.Input(id='x-values', type='text', placeholder='Valores de X', ),
    ]),

    html.Div([
        dcc.Input(id='y-values', type='text', placeholder='Valores de Y', ),
    ], className='mt-2'),

    html.Div([
        html.Button('Plotar Gráfico', id='submit-button',
                    className='btn btn-outline-primary')
    ], className='mt-2 mb-2'),

    html.Div([
        dcc.Graph(id='graph', className='mb-2'),
    ], className="justify-content-center", style={'width': '60%', 'margin': 'auto'}),

    html.Div([
        html.H6('Análise Gráfica: ')
    ]),

    html.Div([
    ], id='valores'),

    html.Div([
        dcc.Input(id='question', type='text', placeholder='Digite uma dúvida: '),
        html.Button('Enviar', id='send-response', className='btn btn-outline-primary'),
        html.Div(id='resposta')
    ], style={'width': '50%'}),

    dcc.Store(id='shared-data', data=None)

], fluid=True)


@callback(
    Output('shared-data', 'data'),
    Output('graph', 'figure'),
    Output('valores', 'children'),
    Input('submit-button', 'n_clicks'),
    State('x-values', 'value'),
    State('y-values', 'value')
)
def create_graph_stored_data(n_clicks, x_values_str, y_values_str):
    if not n_clicks:
        return dash.no_update, dash.no_update, dash.no_update

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
    fig = px.line(x=x_values, y=y_values, title='Line Graph')

    frase = chat('Eixo x:' + str(x_values) + 'Eixo y:' + str(y_values))

    # Retornando para os Outputs
    return {'x_values': x_values, 'y_values': y_values, 'frase': frase}, fig, html.P(frase, className='font-weight-light')


@callback(
    Output('resposta', 'children'),
    Input('send-response', 'n_clicks'),
    State('question', 'value'),
    State('shared-data', 'data')
)
def create_response(n_clicks, question, shared_data):
    if not n_clicks:
        return dash.no_update

    if shared_data is None:
        return dash.no_update

    #Get dos dados
    x = shared_data.get('x_values')
    y = shared_data.get('y_values')

    # Verifica se o botão foi clicado
    # Tratando erros
    if question is None:
        return dash.no_update

    # Gerando resposta
    resposta = chat(str(x) + str(y) + str(question))

    # Retornando para os Outputs
    return html.P(resposta, className='font-weight-light')


if __name__ == '__main__':
    app.run_server(debug=True)
