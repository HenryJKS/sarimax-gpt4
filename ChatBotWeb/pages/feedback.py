import io
import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import base64
import plotly.express as px
from Script.analiseSentimento import classificar_sentimento, accuracy

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

    html.Div([
        html.H2('Análise de Sentimento dos Feedbacks', className='text-center mt-2'),
    ]),

    html.Div([
        html.Hr(),
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
        html.Div([

        ], id='vehicle'),

        html.Div([

        ], id='arquivo'),
    ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between', 'margin-top': '2%'}),

    html.Div([], id='graph-nlp', className='mt-2',
             style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),

    html.Div([], id='table-nlp', className='mt-2 mb-2')

], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


@callback(Output('graph-nlp', 'children'),
          Output('vehicle', 'children'),
          Output('arquivo', 'children'),
          Output('table-nlp', 'children'),
          Input('uploadcsv', 'contents'),
          State('uploadcsv', 'filename'))
def update_graph(contents, filename):
    if contents is not None:
        if not filename.lower().endswith('.csv'):
            return None, html.P('Somente Arquivos .CSV', className='text-danger'), '', ''

       # Decodificando o arquivo
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        # Se o arquivo não tiver as colunas VEICULO e FEEDBACK, retorna erro
        if 'VEICULO' not in df.columns or 'FEEDBACK' not in df.columns:
            return None, dbc.Alert("Colunas Não Encontradas: Feedback ou Veículo", color='danger', className='mt-2 text-center',
                                   style={'width': 'auto'}), '', ''

        # chamando a função
        df = classificar_sentimento(df)

        df_agrupado = df.groupby(['VEICULO', 'SENTIMENTO_PREDICT']).size().reset_index(name='COUNT')
        df_table = df[['FEEDBACK', 'SENTIMENTO_PREDICT']]

        fig = px.pie(df_agrupado, values='COUNT', names='SENTIMENTO_PREDICT', title='Sentimento dos Feedbacks',
                     hole=0.3)

        fig.update_layout({
            'plot_bgcolor': '#d6ecfd',
            'paper_bgcolor': '#d6ecfd',
            'font': {
                'size': 12,
                'color': 'black'
            },
            'width': 800,
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
                'overflowY': 'auto',
            },
            page_size=10,
        )

        return (html.Div(dcc.Graph(figure=fig, className='border border-primary'), style={'border-radius': '5px',
                                                                                          'box-shadow': '0px 0px 5px 0px #103D82'}),
                html.H5('Veículo: ' + df['VEICULO'][0]), html.H5('Arquivo: ' + filename), table)
    else:
        return None, html.H5('Veículo: '), None, None
