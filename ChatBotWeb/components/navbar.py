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
                        dbc.NavItem(dbc.NavLink("Graph", href="/graph1")),
                        dbc.NavItem(dbc.NavLink("Graph2", href="/graph2")),
                        dbc.NavItem(dbc.NavLink("Graph3", href="/graph3")),
                        dbc.NavItem(dbc.NavLink("Graph4", href="/graph4")),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Enviar Email", href="/sendEmail"),
                                dbc.DropdownMenuItem("Converter Arquivo", href="/conversion"),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem("FordBot NLP", href="/feedback"),
                                dbc.DropdownMenuItem("FordBot Security", href="/crypto"),
                            ],
                            label="Opções",
                            nav=True,
                        ),
                    ],
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
            # dbc.Form(
            #     [
            #         dbc.Input(type="search", placeholder="Search"),
            #         dbc.Button("Search", color="secondary"),
            #     ],
            #     className="form-inline d-flex",
            # ),
        ],
        color="#103D82",
        dark=True,
        expand="lg",
        style={"height": "80px"}
    )
    return navbar
