import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from preprocess import coauthorshipNetwork

def CoAuthorshipBrazil(df):
    data = df.copy()
    data.dropna(subset=['Affiliations'],inplace=True)
    data = data[data['Affiliations'].dropna().str.contains('Brazil')]
    node_x, node_y, edge_x, edge_y, node_size, node_text = coauthorshipNetwork(data,mincoauthor=1)

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
                    # colorscale options
                    #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                    #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                    #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                    colorscale='Bluered',
                    reversescale=True,
                    color=[],
                    size=10,
                    colorbar=dict(
                        thickness=15,
                        title='Node Connections',
                        xanchor='left',
                        titleside='right'
                    )
                )
            )
        ],
        layout=go.Layout(
            title='Rede de Coautoria Brasileira',
            showlegend=False,
            height=800,
            plot_bgcolor='rgb(40,40,40)',
            paper_bgcolor='rgb(40,40,40)',
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
        children=[dcc.Graph(id="coauthorshipglobal",figure=fig)]
    )