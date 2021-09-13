from components.analysis.KeywordNetwork import KeywordNetwork
from components.analysis.KeywordsEvolution import KeywordsEvolution
from components.analysis.WordCloud import WordCloudView
import dash_html_components as html
import dash_core_components as dcc

def Textual(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Evolução de Keywords",
                    className='tab',
                    selected_className='tab-selected',
                    children=[KeywordNetwork(df)]
                ),
                dcc.Tab(
                    label="Nuvem de palavras",
                    className='tab',
                    selected_className='tab-selected',
                    children=[WordCloudView(df)]
                )
            ]
        )
    ])