import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

def PublicationsPerYear(df):
    fig = go.Figure(
    data=[
        go.Bar(name="Publicações",
            x=df['Year'].value_counts().index,
            y=df['Year'].value_counts().values,
            marker_color="rgb(46, 134, 222)"
        ),
    ],
    layout={
        "barmode":"stack",
        "title_text":"Publicações por Ano",
        "plot_bgcolor": "rgb(40,40,40)",
        "paper_bgcolor": "rgb(40,40,40)",
        "font": {
            "family":"Verdana, Arial, Helvetica, sans-serif",
            "color": "rgb(220, 220, 220)"
        }
    })

    return html.Div(
        className="section",
        children=[dcc.Graph(figure=fig)]
    )