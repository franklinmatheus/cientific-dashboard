import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

def Sidebar():
    return html.Div(
        className="sidebar",
        children=[
            dbc.Nav([
                    dbc.NavLink("Home", href="/", className="sidebar-item", active="exact"),
                    html.H3("Visualizações de dados", className="sidebar-title"),
                    dbc.NavLink("Multivariados", href="/multivariados", className="sidebar-item", active="exact"),
                    dbc.NavLink("Temporais", href="/temporais", className="sidebar-item", active="exact"),
                    dbc.NavLink("Grafos", href="/grafos", className="sidebar-item", active="exact"),
                    dbc.NavLink("Textuais", href="/textuais", className="sidebar-item", active="exact"),
                    html.H3("Detalhes", className="sidebar-title"),
                    dbc.NavLink("Requisitos Informacionais", href="/requisitos", className="sidebar-item", active="exact"),
                ],
                vertical=True,
                pills=True
            )
            
        ]
    )