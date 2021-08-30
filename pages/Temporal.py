import dash_html_components as html
import dash_core_components as dcc
from components.analysis.PublicationPerYear import PublicationsPerYear

def Temporal(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Publicações",
                    className='tab',
                    selected_className='tab-selected',
                    children=[PublicationsPerYear(df)]
                ),
                dcc.Tab(
                    label="Tab 2",
                    className='tab',
                    selected_className='tab-selected',
                    children=[html.H1("Tab 2")]
                )
            ]
        )
    ])