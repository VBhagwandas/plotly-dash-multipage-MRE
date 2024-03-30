import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    nav_links.append(dbc.NavLink([html.Div('App 1')], href='/app1', active='exact'))
    nav_links.append(dbc.NavLink([html.Div('App 2')], href='/app2', active='exact'))

    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True
                   )