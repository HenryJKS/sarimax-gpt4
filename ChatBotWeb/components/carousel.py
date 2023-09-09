import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input


def create_carousel():
    carousel = dbc.Card(
        [
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(label="Gráficos Inteligentes", tab_id="tab-1"),
                        dbc.Tab(label="Versatilidade", tab_id="tab-2"),
                        dbc.Tab(label="Facilidade", tab_id='tab-3')
                    ],
                    id="card-tabs",
                    active_tab="tab-1",
                )
            ),
            dbc.CardBody(html.Div(id="card-content"))],
        style={})

    return carousel


@callback(Output("card-content", "children"),
          [Input("card-tabs", "active_tab")])
def tab_content(active_tab):
    if active_tab == 'tab-1':
        return html.Div([
            html.Div([
                html.H4("Gráficos Inteligentes", className='text-center mt-2'),

                html.P('''São gráficos onde são analisados profundamente por uma inteligência artificial, 
                        onde ele irá extrair insights e informações valiosas mais rápido para o usuário.''',
                       className='text-center'),

                html.P('''A intenção é que um analista consiga ter uma perfomance melhor com o auxílio da 
                        inteligência. ''', className='text-center'),

            ], style={'width': '50%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

            html.Img(src='assets/imagetab1.jpg',
                     style={'border-radius': '10px', 'float': 'right', 'width': '50%', 'height': '60vh'})

        ], style={'height': '60vh', 'background-color': '#0C0F22', 'color': 'white', 'border-radius': '10px',
                  'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})
    elif active_tab == 'tab-2':
        return html.Div([
            html.Div([
                html.H4("Versatilidade", className='text-center mt-2'),

                html.P('''Um dos pontos fortes é a versatilidade, pois o usuário 
                pode escolher quais dados ele quer a análise, onde os dados podem ser extraido 
                através de um banco de dados, ou até mesmo de um arquivo .csv, .xlsx''',
                       className='text-center')

            ], style={'width': '50%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

            html.Img(src='assets/imagetab1.jpg',
                     style={'border-radius': '10px', 'float': 'right', 'width': '50%', 'height': '60vh'})
        ], style={'height': '60vh', 'background-color': '#0C0F22', 'color': 'white', 'border-radius': '10px',
                  'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})
    elif active_tab == 'tab-3':
        return html.Div([
            html.Div([
                html.H4("Facilidade", className='text-center mt-2'),

                html.P('''Com a versatilidade a facilidade vem junto, já que todo esse processo de 
                       leitura de dados pode 
                       ser feito na própria interface web, sem a necessidade de mexer no código.''',
                       className='text-center')

            ], style={'width': '50%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

            html.Img(src='assets/imagetab1.jpg',
                     style={'border-radius': '10px', 'float': 'right', 'width': '50%', 'height': '60vh'})
        ], style={'height': '60vh', 'background-color': '#0C0F22', 'color': 'white', 'border-radius': '10px',
                  'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})
    else:
        return html.P("ERROR")
