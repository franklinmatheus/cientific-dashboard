import dash_html_components as html
import dash_core_components as dcc

def Textual(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Tab 1",
                    className='tab',
                    selected_className='tab-selected',
                    children=[html.H1("Tab 1")]
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