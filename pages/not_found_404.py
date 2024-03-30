from dash import dcc, html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, 
              title = 'My App')

not_found = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Alert(html.H4("404: Not found"), color='danger'),
                html.Div("The page you are looking for is not found."),
                html.Br(),
            ]
        )
    ],
    color="dark", outline=True, body=True, style={"width": "27rem"}
)

# make layout
layout = html.Div([
    # dcc.Location(id='url_not_found', refresh=True),
    html.Br(),
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(not_found, width='auto'),
            ], justify="center")
        ], fluid=True)
    ])
