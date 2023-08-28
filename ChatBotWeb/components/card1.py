from dash import html
import dash_bootstrap_components as dbc


def card1():
    card = dbc.Card(
        [
            dbc.CardImg(src="../assets/imagegraph01.jpg", top=True),
            dbc.CardBody(
                [
                    html.H4("Graph 01", className="card-title"),
                    html.P(
                        "Tenha acesso a gráficos de linhas com suporte ao chatbot.",
                        className="card-text",
                    ),
                    dbc.Button("Graph 01", color="primary", href='/graph    1'),
                ]
            ),
        ],
        style={"width": "18rem"},
    )
    return card
