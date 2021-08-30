from components.analysis.ArticlesPerLanguage import ArticlesPerLanguage
import dash_html_components as html
import dash_core_components as dcc

def Multivariate(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Países",
                    className='tab',
                    selected_className='tab-selected',
                    children=[html.H3("Artigos por país")]
                ),
                dcc.Tab(
                    label="Instituições",
                    className='tab',
                    selected_className='tab-selected',
                    children=[html.H3("Artigos por Intituição")]
                )
            ]
        )
    ])