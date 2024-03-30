from dash import dash, dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc

register_page(__name__, 
              title = 'My App', 
              name='app1', 
              path='/app1')


layout_ = dbc.Container([
            # dcc.Location(id='url_dashboard', refresh=True),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(html.Div('Dashboard'))
                ]
            ),
            html.Br()
        ], fluid=False)

from .side_bar_dashboard import sidebar

layout = dbc.Row(
        [
            dbc.Col(
                [
                    sidebar(),
                    html.Br(),
                ], xs=10, sm=10, md=3, lg=2, xl=2, xxl=2),


            dbc.Col(
                [
                    layout_
                ], xs=12, sm=12, md=9, lg=10, xl=10, xxl=10),

        ]
    )
