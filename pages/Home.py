import dash_html_components as html
import dash_core_components as dcc
from components.analysis.NullValuesChart import NullValuesChart

def Home(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Dataset",
                    className='tab',
                    selected_className='tab-selected',
                    children=[html.H3("Descrição do dataset")]
                ),
                dcc.Tab(
                    label="Valores Nulos",
                    className='tab',
                    selected_className='tab-selected',
                    children=[NullValuesChart(df)]
                )
            ]
        )
    ])