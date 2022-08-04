from dash import html
import dash_bootstrap_components as dbc


def create_main_tab(controls, result):
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(controls, md=4),
                        dbc.Col(result, md=8)
                    ]
                )
            ]
        ),
        className="mt-3",
        style={"border": "0px"}
    )


def create_about_tab():
    return dbc.Card(
        dbc.CardBody(
            [
                html.P("Some Description", className="card-text")
            ]
        ),
        className="mt-3",
    )
