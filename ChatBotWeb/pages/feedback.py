import io

import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import base64
import plotly.express as px
from Script.analiseSentimento import analyze_sentiment

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='NLP Feedback',
    top_navbar=True,
    path='/feedback',
)

layout = dbc.Container([
    dbc.Row([
        NAVBAR
    ]),

    dcc.Upload(
        id='uploadcsv',
        children=html.Div([
            'Arraste e solte ou ',
            html.A('Selecione Arquivo')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin-top': '10px'
        },
        # Permite múltiplos arquivos para serem carregados
        multiple=False
    ),

    html.Div([

    ], id='vehicle', className='mt-2'),

    html.Div([
        dcc.Graph(id='graph-nlp')
    ], className="justify-content-center", style={'width': '80%', 'margin': 'auto', 'margin-top': '2%'}),


], fluid=True)


@callback(Output('graph-nlp', 'figure'),
          Output('vehicle', 'children'),
          Input('uploadcsv', 'contents'),
          State('uploadcsv', 'filename'))
def update_graph(contents, filename):
    if contents is not None:
        if not filename.lower().endswith('.csv'):
            return {}, html.P('Somente Arquivo .CSV', className='text-danger')

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        df = analyze_sentiment(df)
        # fazer o count de positivo e negativo
        df = df.groupby(['VEICULO', 'SENTIMENT']).size().reset_index(name='COUNT')
        fig = px.bar(df, x='VEICULO', y='COUNT', color='SENTIMENT', barmode='group')
        return fig, html.H5('Veículo: ' + df['VEICULO'][0])
    else:
        return {}, html.H5('Veículo: ')
