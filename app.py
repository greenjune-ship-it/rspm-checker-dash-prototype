import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.title = "RStudio Package Manager Checker"

app.layout = html.Div(
    id='main_page',
    children=[
        html.Div(
            id='app-page-header',
            children=[
                html.H2(
                    app.title
                )
            ]
        ),
        html.Div(
            id='app-page-content',
            className='control-tabs',
            children=[
                html.Div(id='app-control-tabs', children=[
                    dcc.Tabs(
                        id='app-tabs',
                        value='what-is',
                        children=[
                            dcc.Tab(
                                label='About',
                                value='what-is',
                                children=html.Div(className='control-tab', children=[
                                    html.H4(
                                        className='what-is',
                                        children='What is rspm-checker?'
                                    ),
                                    html.P('Some descriptive info about app')
                                ])
                            ),
                            dcc.Tab(
                                label='Inspect',
                                value='select-app',
                                children=html.Div(className='app-controls-block', children=[
                                    dcc.Dropdown(
                                        id='selected-app',
                                        className='app-dropdown',
                                        options=["Default", "One", "Two", "Three"],
                                        clearable=False,
                                        value="Default"
                                    )
                                ])
                            )
                        ]
                    )
                ])
            ]
        ),
        html.Div(
            id='app-container',
            children=[
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
    ]
)


@app.callback(
    Output(component_id='selected-value', component_property='children'),
    Input(component_id='selected-app', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
