def navbar():
    import dash
    from dash import html
    import dash_bootstrap_components as dbc
    
    nav_item_dashboard = dbc.NavLink("my dashboard", href=dash.page_registry['pages.app1']['path'])
    nav_item_profile = dbc.NavLink("my profile", href=dash.page_registry['pages.profile1']['path'])

    # NavBar Layout
    navbar = dbc.Navbar(
        dbc.Container(
        [
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Col([dbc.Collapse(
                dbc.Nav(
                    [
                        nav_item_dashboard,
                        nav_item_profile
                    ],
                    navbar=True, pills=True, className="ml-auto" #class_name="w-100"
                ),
                id="navbar-collapse",
                navbar=True
            ),
            ], class_name="flex-grow-1", width="auto", align="right"),
        ], fluid=True,
        ),
        class_name="mb-5",
        sticky='top'
    )
    return navbar
