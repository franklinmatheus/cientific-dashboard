from components.analysis.CoAuthorshipBrazil import CoAuthorshipBrazil
from components.analysis.CoAuthorship import CoAuthorship
import dash_html_components as html
import dash_core_components as dcc

def Graphs(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Rede de Coautoria Global",
                    className='tab',
                    selected_className='tab-selected',
                    children=[CoAuthorship(df[['Authors','Author(s) ID']])]
                ),
                dcc.Tab(
                    label="Rede de Coautoria Brasileira",
                    className='tab',
                    selected_className='tab-selected',
                    children=[CoAuthorshipBrazil(df[['Authors','Author(s) ID','Affiliations']])]
                )
            ]
        )
    ])