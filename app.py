# import of external libraries
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# import of structural components
from components.Header import Header
from components.Sidebar import Sidebar

# import the pages
from pages.Home import Home
from pages.Multivariate import Multivariate
from pages.Temporal import Temporal
from pages.Graphs import Graphs
from pages.Textual import Textual
from pages.Requirements import Requirements

app = Dash(__name__)
server = app.server

scopus = pd.read_excel("./data/data_cleaned.xlsx",index_col=0)

# main page layout
app.layout = html.Div(
    className="container",
    children=[
        dcc.Location(id='url', refresh=False),
        Header(),
        Sidebar(),
        html.Div(
            className="content",
            id="content"
        ),
    ]
)

@app.callback(Output('content', 'children'),
              [Input('url', 'pathname')])
def render(pathname):
    if pathname == "/":
        return Home(scopus)
    elif pathname == "/multivariados":
        return Multivariate(scopus)
    elif pathname == "/temporais":
        return Temporal(scopus)
    elif pathname == "/grafos":
        return Graphs(scopus)
    elif pathname == "/textuais":
        return Textual(scopus)
    elif pathname == "/requisitos":
        return Requirements(scopus)

if __name__ == '__main__':
    app.run_server(debug=True)