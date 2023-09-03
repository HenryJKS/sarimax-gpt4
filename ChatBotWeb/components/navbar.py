from dash import html
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
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Enviar Email", href="/sendEmail"),
                                dbc.DropdownMenuItem("Transformar Arquivo", href="/transform"),
                                dbc.DropdownMenuItem("Something else here", href="#"),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem("Separated link", href="#"),
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
