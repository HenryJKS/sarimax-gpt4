import io
import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import base64
import plotly.express as px
from Script.analiseSentimento import classificar_sentimento


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

        html.Div([], id='graph-nlp'),

        html.Div([], id='table-nlp')

    ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between',
              'width': '100%', 'margin-top': '2%'}),

], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


@callback(Output('graph-nlp', 'children'),
          Output('vehicle', 'children'),
          Output('table-nlp', 'children'),
          Input('uploadcsv', 'contents'),
          State('uploadcsv', 'filename'))
def update_graph(contents, filename):
    if contents is not None:
        if not filename.lower().endswith('.csv'):
            return None, html.P('Somente Arquivos .CSV', className='text-danger'), ''

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        # chamando a função
        df = classificar_sentimento(df)

        df_agrupado = df.groupby(['VEICULO', 'SENTIMENTO_PREDICT']).size().reset_index(name='COUNT')
        df_table = df[['FEEDBACK', 'SENTIMENTO_PREDICT']]

        # Gráfico de donut
        fig = px.pie(df_agrupado, values='COUNT', names='SENTIMENTO_PREDICT', title='Sentimento dos Feedbacks', hole=0.3)

        fig.update_layout({
            'plot_bgcolor': '#d6ecfd',
            'paper_bgcolor': '#d6ecfd',
            'font': {
                'size': 12,
                'color': 'black'
            },
            'width': 700,
            'height': 500,
        })

        # Criar datatable
        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df_table.columns],
            data=df.to_dict('records'),
            style_header={
                'backgroundColor': '#103D82',
                'fontWeight': 'bold',
                'color': 'white',
                'textAlign': 'center'
            },
            style_cell={
                'textAlign': 'center',
            },
            style_table={
                'height': 'auto',
                'overflowY': 'auto'
            },
            page_size=10,
        )

        return dcc.Graph(figure=fig), html.H5('Veículo: ' + df['VEICULO'][0]), table
    else:
        return None, html.H5('Veículo: '), None
