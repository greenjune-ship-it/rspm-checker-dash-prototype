from dash import dcc, html
import dash_bootstrap_components as dbc

from helpers.get_rspm_logs import format_markdown

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


def create_navbar(title):
    return dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand(title)),
                    ]
                )
            ],
            fluid=False,
        ),
        color="dark",
        dark=True
    )


def create_controls(id, label, options, value):
    return dbc.Card(
        [
            dbc.Label(label),
            dcc.Dropdown(
                id=id,
                className='app-dropdown',
                options=options,
                clearable=False,
                value=value
            )
        ],
        body=True
    )


def create_result(id, label, content):
    return dbc.Card(
        [
            dbc.Row(dbc.Label(label)),
            dbc.Row(
                html.Div([
                    dcc.Markdown(
                        format_markdown(content),
                        id=id
                    )
                ])
            )
        ],
        body=True
    )
