from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.Navbar(
        [
            html.A(dbc.NavbarBrand("FordBot", style={'margin-left': '8%'}), href="/fordbot"),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", active=True, href="/")),
                        dbc.NavItem(dbc.NavLink("Análise Financeira", href="/graph1")),
                        dbc.NavItem(dbc.NavLink("Análise Geral", href="/graph2")),
                        dbc.NavItem(dbc.NavLink("Assistencia Veículo", href="/graph3")),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Veículos Ativos", href="/graph4"),
                                dbc.DropdownMenuItem("Veículos Importados", href="/graph5"),
                            ],
                            label="Análise de Veículos",
                            nav=True,
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Enviar Email", href="/sendEmail"),
                                dbc.DropdownMenuItem("Converter Arquivo", href="/conversion"),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem("FordBot NLP", href="/feedback"),
                                dbc.DropdownMenuItem("FordBot Forecast", href='/forecast'),
                                dbc.DropdownMenuItem("FordBot Security", href="/crypto"),
                            ],
                            label="Utils",
                            nav=True,
                        ),
                    ],
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
        color="#103D82",
        dark=True,
        expand="lg",
        style={"height": "80px"}
    )
    return navbar
