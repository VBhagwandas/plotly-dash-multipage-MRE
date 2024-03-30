from dash import dash, dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc
# import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
# from dash.exceptions import PreventUpdate


register_page(__name__, 
              title = 'My App', 
              name='app2', 
              path='/app2')

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
                    html.Div('this is a page')
                ], xs=12, sm=12, md=9, lg=10, xl=10, xxl=10),

        ]
    )
