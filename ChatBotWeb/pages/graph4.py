import dash
from dash import callback, html, dcc, Input, Output, State
from ChatBotWeb.components import navbar
import dash_bootstrap_components as dbc
import plotly.express as px
from ChatBotWeb.query import queryVeiulosAtivos
from ChatBotWeb.chatAPI.ModelAPI import chat_map

df_map = queryVeiulosAtivos.df
df_gpt = queryVeiulosAtivos.df_gpt

fig = px.scatter_mapbox(
    df_map,
    lat='LATITUDE',
    lon='LONGITUDE',
    hover_name='CIDADE',
    hover_data={'ESTADO': True, 'VEICULOS_ATIVOS': True, 'LATITUDE': False, 'LONGITUDE': False},
    labels={'ESTADO': 'Estado', 'VEICULOS_ATIVOS': 'Veículos Ativos'},
    color_discrete_sequence=["blue"],
    zoom=4,
    height=600
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(mapbox_bounds={"west": -85, "east": -28, "south": -40, "north": 10})

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Dashboard',
    path='/graph4',
    top_navbar=True,
)

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.Div([
            html.H2('Veículos Ativos em Tempo Real', className='text-center')
        ]),

        html.Div([
            dbc.Button("FordBot Mapa", id="open-offcanvas-map", n_clicks=0),
            dbc.Offcanvas(
                html.Div([
                    html.H4('Converse com o Bot', className='text-center'),
                    html.Hr(),
                    html.H6('Faça sua pergunta:', className='mt-2'),
                    dcc.Textarea(style={'width': '100%'}, id='question-map'),
                    html.Button('Perguntar', id='send-question-map', className='btn btn-secondary'),
                    html.Div([
                    ], className='mt-4', id='responsemap')
                ]),
                id="offcanvas-map",
                is_open=False,
                placement='end'
            ),
        ], style={}),
    ], className='mt-2'),

    html.Div([
        html.Hr()
    ]),

    html.Div([
        dcc.Graph(figure=fig, style={'width': '100%'})
    ])

], fluid=True)


@callback(
    Output('responsemap', 'children'),
    Input('send-question-map', 'n_clicks'),
    State('question-map', 'value')
)
def response(n_clicks, question):
    if not n_clicks:
        return dash.no_update
    elif n_clicks is None:
        return dash.no_update

    resposta = chat_map(f'dados: {df_gpt}, pergunta: {question}')

    if question is None:
        return (
            html.P('Insira um pergunta', className='text-center border border-dark rounded', style={'padding': '2%'})
        )
    return (
        html.P(resposta, className='text-center border border-dark rounded', style={'padding': '2%'})
    )


@callback(
    Output("offcanvas-map", "is_open"),
    Input("open-offcanvas-map", "n_clicks"),
    [State("offcanvas-map", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open
