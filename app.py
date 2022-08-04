import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from helpers.layout_helper import create_navbar, create_controls, create_result
from helpers.tabs_helper import create_main_tab, create_about_tab
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

tab_main = create_main_tab(controls, result)
tab_about = create_about_tab()

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navbar)
            ]
        ),
        html.Br(),
        dbc.Tabs(
            [
                dbc.Tab(tab_main, label="Main"),
                dbc.Tab(tab_about, label="About")
            ]
        )
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
