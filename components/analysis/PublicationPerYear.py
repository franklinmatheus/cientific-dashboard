import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from pages.Requirements import reqs

def PublicationsPerYear(df):
    fig = go.Figure(
    data=[
        go.Bar(name="Publicações",
            x=df['Year'].value_counts().index,
            y=df['Year'].value_counts().values,
            marker_color="rgb(46, 134, 222)"
        ),
    ],
    layout=go.Layout(
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
            html.H3("Publicações por Ano",className="section-title"),
            dcc.Graph(figure=fig),
            html.H3("Requisitos Informacionais",className="section-title"),
            html.Div(className="req-div",children=[html.H3('RI04',className="req-id"),html.P(reqs['RI04'],className="req-description")])
        ]
    )