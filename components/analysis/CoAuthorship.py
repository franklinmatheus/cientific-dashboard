import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from preprocess import coauthorshipNetwork
from pages.Requirements import reqs

def CoAuthorship(df):
    data = df.copy()
    node_x, node_y, edge_x, edge_y, node_size, node_text = coauthorshipNetwork(data,mincoauthor=8)

    fig = go.Figure(
        data=[
            go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.5, color='#888'),
                hoverinfo='none',
                mode='lines'),
            go.Scatter(
                x=node_x,
                y=node_y,
                mode='markers',
                hoverinfo='text',
                text=node_text,
                marker_color=node_size,
                marker=dict(
                    showscale=True,
                    colorscale='Bluered',
                    reversescale=True,
                    color=[],
                    size=10,
                    colorbar=dict(
                        thickness=15,
                        title='Coautores',
                        xanchor='left',
                        titleside='right'
                    )
                )
            )
        ],
        layout=go.Layout(
            showlegend=False,
            plot_bgcolor='rgb(40,40,40)',
            paper_bgcolor='rgb(40,40,40)',
            margin=dict(
                l=50,
                r=50,
                b=0,
                t=0,
                pad=2
            ),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            font= {
                "family":"Verdana, Arial, Helvetica, sans-serif",
                "color": "rgb(220, 220, 220)"
            }
        )
    )

    return html.Div(
        className="section",
        children=[
            html.H3("Rede de Coautoria Global",className="section-title"),
            dcc.Graph(id="coauthorship",figure=fig),
            html.H3("Requisitos Informacionais",className="section-title"),
            html.Div(className="req-div",children=[html.H3('RI07',className="req-id"),html.P(reqs['RI07'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI08',className="req-id"),html.P(reqs['RI08'],className="req-description")])
        ]
    )