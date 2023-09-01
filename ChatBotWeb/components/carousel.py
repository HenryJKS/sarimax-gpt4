import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input


def create_carousel():
    carousel = dbc.Card(
        [
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(label="Gráficos Inteligentes", tab_id="tab-1"),
                        dbc.Tab(label="FordBot", tab_id="tab-2"),
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
                html.P('''São gráficos onde são analisados profundamente por um inteligência artificial, 
                onde ele irá extrair insights e informações valiosas mais rápido para o usuário.''')
            ], style={'float': 'left', 'width': '50%'}),

            html.Img(src='assets/imagesteste.jpg',
                     style={'border-radius': '10px', 'float': 'right', 'width': '50%', 'height': '60vh'})
        ], style={'height': '60vh', 'background-color': '#0C0F22', 'color': 'white', 'border-radius': '10px'})
    elif active_tab == 'tab-2':
        return html.P("Conteudo 2")
    else:
        return html.P("ERROR")
