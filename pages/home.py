from dash import dcc, html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, 
              title = 'My App', 
              name='home', 
              path='/')

layout = html.Div([ 
    # dcc.Location(id='url_home', refresh=False),
    html.Br(),
    html.Div(html.H1('home')),
    dbc.Container([
        dbc.Row(
            [
                html.Br(),
                html.H3('Welcome!')

            ], justify="center")
        ], fluid=True)
    ])
