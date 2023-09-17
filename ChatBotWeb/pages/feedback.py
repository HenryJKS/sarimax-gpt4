import io
import dash
import pandas as pd
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
from ChatBotWeb.components import navbar
import base64
import plotly.express as px
from Script.analiseSentimento import classificar_sentimento, accuracy
from ChatBotWeb.chatAPI.ModelAPI import nlp
import openpyxl

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='NLP Feedback',
    top_navbar=True,
    path='/feedback',
)

layout = dbc.Container([
    html.Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css'),
    html.Link(rel='stylesheet',
              href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'),

    dbc.Row([
        NAVBAR
    ]),

    html.Div([
        html.Div([
            html.H2('Análise ML Sentimentos', className='text-center mt-2'),
            html.A(
                html.I(className='fa fa-question-circle', style={'color': '#103d82ff', 'font-size': '25px'}),
                id='my-icon',
                href='#',
                style={'position': 'absolute', 'right': '0', 'top': '50%', 'transform': 'translateY(-50%)'}
            ),
        ], style={'position': 'relative', 'text-align': 'center'})
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
            html.H5(f'Machine Learning Accuracy ≅ {accuracy * 100}% ', className='mt-2', style={'color': '#103d82ff'}),
        ]),

        html.Div([

        ], id='arquivo'),

        html.Div([

        ], id='vehicle'),

    ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between', 'margin-top': '2%'}),

    html.Div([
        html.Div([
            dbc.Button("FordBot", id="opencanvasnlp", n_clicks=0),
            dbc.Offcanvas(
                html.Div([
                    html.H4('Converse com o Bot', className='text-center'),
                    html.Hr(),
                    html.H6('Faça sua pergunta:', className='mt-2'),
                    dcc.Textarea(style={'width': '100%'}, id='question-nlp'),
                    html.Button('Perguntar', id='send-question-nlp', className='btn btn-secondary'),
                    html.Div([
                    ], className='mt-4', id='response-nlp')
                ]),
                id="offcanvasnlp",
                is_open=False,
                placement='end'
            ),
        ], className='mt-2'),
    ]),

    html.Div([], id='graph-nlp', className='mt-2',
             style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),

    html.Div([], id='table-nlp', className='mt-2 mb-2'),

    dcc.Store(id='dfglobal_nlp', storage_type='memory'),

], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


@callback(Output("offcanvasnlp", "is_open"),
          Input("opencanvasnlp", "n_clicks"),
          [State("offcanvasnlp", "is_open")],
          )
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(Output('graph-nlp', 'children'),
          Output('vehicle', 'children'),
          Output('arquivo', 'children'),
          Output('table-nlp', 'children'),
          Output('dfglobal_nlp', 'data'),
          Input('uploadcsv', 'contents'),
          State('uploadcsv', 'filename'),
          )
def update_graph(contents, filename):
    if contents is not None:
        if not filename.lower().endswith('.xlsx'):
            return None, dbc.Alert("Somente Arquivos .XLSX", color='danger'), '', '', dash.no_update

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        if filename.lower().endswith('.xlsx'):
            df = pd.read_excel(io.BytesIO(decoded))

        # Se o arquivo não tiver as colunas VEICULO e FEEDBACK, retorna erro
        if 'VEICULO' not in df.columns or 'FEEDBACK' not in df.columns:
            return None, dbc.Alert("Colunas Não Encontradas: Feedback ou Veículo", color='danger',
                                   className='text-center',
                                   style={'width': 'auto'}), '', '', dash.no_update

        # chamando a função
        df = classificar_sentimento(df)

        dfglobal_nlp = df.to_json(date_format='iso', orient='split')

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
                html.H5('Produto Ford: ' + df['VEICULO'][0]), html.H5('Arquivo: ' + filename), table, dfglobal_nlp)
    else:
        return None, html.H5('Produto Ford: Nenhum', style={'color': '#103d82ff'}), None, None, dash.no_update


@callback(Output('response-nlp', 'children'),
          Input('send-question-nlp', 'n_clicks'),
          State('question-nlp', 'value'),
          State('dfglobal_nlp', 'data'))
def response(n_clicks, question, dfglobal_nlp):
    if not n_clicks:
        return dash.no_update
    elif n_clicks is None:
        return dash.no_update

    resposta = nlp(f"dados: {str(dfglobal_nlp)}, pergunta: {question}")

    if question is None:
        return (
            html.P('Insira um pergunta', className='text-center border border-dark rounded', style={'padding': '2%'})
        )
    return (
        html.P(resposta, className='text-center border border-dark rounded', style={'padding': '2%'})
    )


@callback(Output('my-icon', 'children'),
          Input('my-icon', 'n_clicks'))
def info(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return html.A(
            html.I(className="fa fa-question-circle", style={'color': '#103d82ff', 'font-size': '25px'}),
            id='my-icon',
            href='#',
        ), dbc.Modal(
            [
                dbc.ModalHeader("Informações"),
                dbc.ModalBody(
                    html.P('''
                    Nesta página você pode analisar o sentimento dos feedbacks enviados pelos clientes. 
                    Para isso, basta carregar o arquivo .xlsx com as colunas VEICULO e FEEDBACK. 
                    O modelo irá classificar o sentimento dos feedbacks em positivo ou negativo. 
                    Você também pode conversar com o FordBot, basta clicar no botão FordBot e fazer sua pergunta. 
                    O FordBot irá responder de acordo com os dados carregados. 
                    ''')
                ),
                dbc.ModalFooter(
                ),
            ],
            id="modal",
            is_open=True,
            centered=True,
        )

