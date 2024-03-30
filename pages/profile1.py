from dash import dcc, html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, 
              title = 'My App', 
              name='profile1', 
              path='/profile1')

layout = html.Div([ 
    # dcc.Location(id='url_home', refresh=False),
    html.Br(),
    dbc.Container([
        dbc.Row(
            [
                html.Br(),
                html.H3('Welcome user!'),
                html.Div('your profile page')

            ], justify="center")
        ], fluid=True)
    ])
