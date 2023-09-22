import dash
from dash import Output, Input, dcc, State, callback, html
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import plotly.express as px
from ChatBotWeb.query.queryModeloImportado import df
from ChatBotWeb.chatAPI.ModelAPI import chat_importado

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='Veículos Importados',
    path='/graph5',
    top_navbar=True,
)

layout = dbc.Container([

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.H2("Importação de Veículos por Ano", className='text-center mt-2')
    ]),

    html.Div([
        html.Hr()
    ]),

html.Div([
            dbc.Button("FordBot Imports", id="open-offcanvas-import", n_clicks=0, className='mb-2'),
            dbc.Offcanvas(
                html.Div([
                    html.H4('Converse com o Bot', className='text-center'),
                    html.Hr(),
                    html.H6('Faça sua pergunta:', className='mt-2'),
                    dcc.Textarea(style={'width': '100%'}, id='question-import'),
                    html.Button('Perguntar', id='send-question-import', className='btn btn-secondary'),
                    html.Div([
                    ], className='mt-4', id='responseimport')
                ]),
                id="offcanvas-import",
                is_open=False,
                placement='end'
            ),
        ]),

    html.Div([
        dcc.Graph(
            figure=px.bar(df, x="Modelo", y="Importado", animation_frame="Ano", color="Modelo",
                          hover_name="Modelo", range_y=[0, df['Importado'].max()])
            , className='border border-primary',
            style={'width': '100%', 'height': '100%', 'border-radius': '5px'})
    ], className="justify-content-center",
        style={'width': '80%', 'margin': 'auto'}),

], fluid=True)

@callback(
    Output('responseimport', 'children'),
    Input('send-question-import', 'n_clicks'),
    State('question-import', 'value')
)
def response(n_clicks, question):
    if not n_clicks:
        return dash.no_update
    elif n_clicks is None:
        return dash.no_update

    resposta = chat_importado(f'dados: {df}, pergunta: {question}')

    if question is None:
        return (
            html.P('Insira um pergunta', className='text-center border border-dark rounded', style={'padding': '2%'})
        )
    return (
        html.P(resposta, className='text-center border border-dark rounded', style={'padding': '2%'})
    )


@callback(
    Output("offcanvas-import", "is_open"),
    Input("open-offcanvas-import", "n_clicks"),
    [State("offcanvas-import", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open
