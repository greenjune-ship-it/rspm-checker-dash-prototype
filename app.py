import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.title = "RStudio Package Manager Checker"

app.layout = html.Div(
    id='app-container',
    children=[
        html.Div(
            id='header-area',
            children=[
                html.H1(
                    id='header-title',
                    children="RStudio Package Manager Checker"
                ),
                html.P(
                    id='header-description',
                    children="Application description"
                )
            ]
        ),
        html.Div(
            id='menu-area',
            children=[
                html.Div(
                    className='menu-title',
                    children='Menu Title'
                ),
                dcc.Dropdown(
                    id='appname-filter',
                    className='dropdown',
                    options=["Default", "One", "Two", "Three"],
                    clearable=False,
                    value="Default"
                )
            ]
        ),
        html.Br(),
        html.Div(
            id='logs-container',
            children=[
                html.Div(
                   id="selected-value"
                )
            ]
        )
    ]
)


@app.callback(
    Output(component_id='selected-value', component_property='children'),
    Input(component_id='appname-filter', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
