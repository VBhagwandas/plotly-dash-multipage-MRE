import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc



app = Dash(__name__, suppress_callback_exceptions=True, use_pages=True)


########################################### render content  ###############################################
from layout_navbar import navbar
navbar_ = navbar()

@callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')],
    )  
def display_page(pathname):
        layout = html.Div([
            navbar_,
            html.Br(style={"line-height": "5"}),
            dash.page_container
        ])
        
        return layout

# Make the overall layout, which is rendered by the display_page() callback
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className='content')
    ])

######################## Navbar callbacks ##############################
# Toggle the collapse on small screens (navbar)
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

    
if __name__ == '__main__':
    app.run_server(debug=True)