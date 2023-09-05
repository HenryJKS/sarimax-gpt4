import dash
from dash import Dash, html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
from ChatBotWeb.query.queryVeiculoProblema import df
import plotly.express as px

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Dashboard',
    path='/graph3',
    top_navbar=True,
)

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2('Veículos com Problemas', className='text-center mt-2')
    ]),

    html.Div([
        html.Hr()
    ]),

    html.Div([
        html.P('Selecione o veículo: '),
        dcc.Dropdown(
            id='modelo-dropdown',
            options=[{'label': modelo, 'value': modelo} for modelo in df['MODELO'].unique()],
            value=df['MODELO'][0],
            multi=False,
        ),
    ], style={'width': '25%'}),

    html.Div([
        html.Div([], id='problemas-card')
    ], className='mt-2'),

    html.Div([
        dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            html.P(
                "This is the content of the Offcanvas. "
                "Close it by clicking on the close button, or "
                "the backdrop."
            ),
            id="offcanvas",
            title="Title",
            is_open=False,
            
        ),
    ], className='mt-2')

], fluid=True)


@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    Output('problemas-card', 'children'),
    Input('modelo-dropdown', 'value')
)
def update_problemas_card(selected_modelo):
    if selected_modelo is None:
        return ''

    # Filtra o DataFrame para obter os problemas do modelo selecionado
    problemas_modelo = df[df['MODELO'] == selected_modelo]['PROBLEMA'].unique()

    # Converte os problemas do modelo em uma lista
    problemas_lista = problemas_modelo.tolist()

    # Cria uma string com os problemas separados por vírgula
    problemas_texto = ', '.join(problemas_lista)

    return dbc.Card([
        dbc.CardHeader('Relatório do Modelo Selecionado'),
        dbc.CardBody([
            html.P(f'Modelo: {selected_modelo}'),
            html.P(f'Problemas Atuais: {problemas_texto}')
        ])
    ])
