import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import dash
from ChatBotWeb.components import navbar
from ChatBotWeb.chatAPI.ModelAPI import forecast

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from Script.previsaoDemanda import erro_padrao, intervalo_confianca_inferior, intervalo_confianca_superior, df_previsao, \
    df, media

df.reset_index(inplace=True)
df_real = df[['ANO', 'UNIDADES_VENDIDAS']]
df_final = pd.concat([df_real, df_previsao], ignore_index=True)

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df_final['ANO'], y=df_final['UNIDADES_VENDIDAS'], mode='lines', name='Real')
)
fig.add_trace(
    go.Scatter(x=df_final[df_final['ANO'] >= 2023]['ANO'], y=df_final[df_final['ANO'] >= 2023]['UNIDADES_VENDIDAS'],
               mode='lines', name='Previsão')
)

fig.update_layout(
    title='Real x Previsão',
    xaxis_title='Ano',
    yaxis_title='Unidades Vendidas',
    legend_title='Legendas',
    font=dict(
        family="Times New Roman",
        size=14,
        color="black"
    )
)

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='ML Forecast',
    top_navbar=True,
    path='/forecast',
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
            html.H2('Previsão de Importação Veículos Elétricos', className='text-center mt-2'),
        ], style={'text-align': 'center'})
    ]),

    html.Div([
        html.Hr(),
    ]),

    html.Div([
        html.Div([
            dbc.Button("FordBot ML", id="opencanvasforecast", n_clicks=0),
            dbc.Offcanvas(
                html.Div([
                    html.H4('Converse com o Bot', className='text-center'),
                    html.Hr(),
                    html.H6('Faça sua pergunta:', className='mt-2'),
                    dcc.Textarea(style={'width': '100%'}, id='question-forecast'),
                    html.Button('Perguntar', id='send-question-forecast', className='btn btn-secondary'),
                    html.Div([
                    ], className='mt-4', id='response-forecast')
                ]),
                id="offcanvasforecast",
                is_open=False,
                placement='end'
            ),
        ], className='mt-2'),
    ]),

    html.Div([
        html.Div([
            html.H5(f'Avaliação Machine Learning', style={'color': '#103d82ff'}),
            html.Hr(),
            html.H5(F'Previsão 2023 ≅ {int(media[0])} Vendas', style={'color': '#103d82ff'}),
            html.H5(f'Erro Padrão 2023 ≅ {round(erro_padrao[0], 2)}', style={'color': '#103d82ff'}),
            html.H5(f'Intervalo de Confiança Inferior 2023 ≅ {round(intervalo_confianca_inferior[0], 2)}',
                    style={'color': '#103d82ff'}),
            html.H5(f'Intervalo de Confiança Superior 2023 ≅ {round(intervalo_confianca_superior[0], 2)}',
                    style={'color': '#103d82ff'}),
            html.Hr(),
            html.H5(f'Previsão 2024 ≅ {int(media[1])} Vendas', style={'color': '#103d82ff'}),
            html.H5(f'Erro Padrão 2024 ≅ {round(erro_padrao[1], 2)}', style={'color': '#103d82ff'}),
            html.H5(f'Intervalo de Confiança Inferior 2024 ≅ {round(intervalo_confianca_inferior[1], 2)}',
                    style={'color': '#103d82ff'}),
            html.H5(f'Intervalo de Confiança Superior 2024 ≅ {round(intervalo_confianca_superior[1], 2)}',
                    style={'color': '#103d82ff'}),
        ], style={'text-align': 'start', 'border-radius': '5px', 'box-shadow': '0px 0px 5px 0px #103D82',
                  'padding': '1%'}),

        dcc.Graph(
            figure=fig, className='border border-primary',
            style={'width': '50%', 'height': '80%', 'border-radius': '5px'}),

    ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between', 'margin-top': '2%'}),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
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
    ], style={'margin-top': '2%'}),

], fluid=True)


@callback(Output("offcanvasforecast", "is_open"),
          Input("opencanvasforecast", "n_clicks"),
          [State("offcanvasforecast", "is_open")],
          )
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(Output('response-forecast', 'children'),
          Input('send-question-forecast', 'n_clicks'),
          State('question-forecast', 'value'))
def response(n_clicks, question):
    if not n_clicks:
        return dash.no_update
    elif n_clicks is None:
        return dash.no_update

    resposta = forecast(f'tabela1: {str(df)}, tabela2: {str(df_previsao)}, pergunta: {str(question)}')

    if question is None:
        return (
            html.P('Insira um pergunta', className='text-center border border-dark rounded', style={'padding': '2%'})
        )
    return (
        html.P(resposta, className='text-center border border-dark rounded', style={'padding': '2%'})
    )
