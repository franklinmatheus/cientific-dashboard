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
    layout={
        "barmode":"stack",
        "title_text":"Valores Nulos e Válidos no Dataset",
        "plot_bgcolor": "rgb(40,40,40)",
        "paper_bgcolor": "rgb(40,40,40)",
        "font": {
            "family":"Verdana, Arial, Helvetica, sans-serif",
            "color": "rgb(220, 220, 220)"
        }
    })

    return html.Div(
        className="section",
        children=[dcc.Graph(id="nullvalueschart",figure=fig)]
    )