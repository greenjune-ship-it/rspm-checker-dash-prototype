import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from helpers.layout_helper import create_navbar, create_controls, create_result

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "RStudio Package Manager Checker"

navbar = create_navbar(app.title)

controls = create_controls(
    id='selected-app',
    label='Select App Name',
    options=["Default", "One", "Two", "Three"],
    value='Default'
)

result = create_result(
    id='selected-value',
    label='Result'
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navbar)
            ],
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(result, md=8)
            ],
        ),
    ],
    fluid=False,
)


@app.callback(
    Output(component_id='selected-value', component_property='children'),
    Input(component_id='selected-app', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
