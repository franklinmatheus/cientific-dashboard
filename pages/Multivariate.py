from components.analysis.Countries import Countries
from components.analysis.ArticlesPerConference import ArticlesPerConference
import dash_html_components as html
import dash_core_components as dcc

def Multivariate(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Conferências",
                    className='tab',
                    selected_className='tab-selected',
                    children=[ArticlesPerConference(df)]
                ),
                dcc.Tab(
                    label="Países",
                    className='tab',
                    selected_className='tab-selected',
                    children=[Countries(df['Affiliations'])]
                )
            ]
        )
    ])