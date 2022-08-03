import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from helpers.layout_helper import create_navbar, create_controls, create_result
from helpers.get_rspm_logs import format_markdown

# to do implement retrieving of packages from MySQL RSPM Database
options_for_selectize = [
    "Default Package",
    "Package One",
    "Package Two",
    "Package Three"
]

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)
app.title = "RStudio Package Manager Checker"

navbar = create_navbar(app.title)

controls = create_controls(
    id='selected-app',
    label='Select App Name',
    options=options_for_selectize,
    value=options_for_selectize[0]
)

result = create_result(
    id='selected-value',
    label='Package Building Log',
    content=options_for_selectize[0]
)

tab_main = dbc.Card(
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

tab_about = dbc.Card(
    dbc.CardBody(
        [
            html.P("Some Description", className="card-text")
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_main, label="Main"),
        dbc.Tab(tab_about, label="About")
    ]
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navbar)
            ]
        ),
        html.Br(),
        tabs
    ],
    fluid=False,
)


@app.callback(
    Output(component_id='selected-value', component_property='children'),
    Input(component_id='selected-app', component_property='value')
)
def update_output_div(input_value):
    return format_markdown(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
