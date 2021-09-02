import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

def NullValuesChart(df):
    fig = go.Figure(
    data=[
        go.Bar(name="Valores Válidos",
            x=df.columns,y=df.notna().sum(axis=0),
            marker_color="rgb(46, 134, 222)"
            
        ),
        go.Bar(name="Valores Nulos",
            x=df.columns,y=df.isna().sum(axis=0),
            marker_color="rgb(238, 82, 83)"
        ),
    ],
    layout=go.Layout(
            barmode='stack',
            margin=dict(
                l=50,
                r=50,
                b=50,
                t=50,
                pad=2
            ),
            plot_bgcolor='rgb(40,40,40)',
            paper_bgcolor='rgb(40,40,40)',
            font= {
                "family":"Verdana, Arial, Helvetica, sans-serif",
                "color": "rgb(220, 220, 220)"
            }
        )
    )

    return html.Div(
        className="section",
        children=[
            html.H3("Valores Nulos no Dataset",className="section-title"),
            dcc.Graph(id="nullvalueschart",figure=fig)
        ]
    )