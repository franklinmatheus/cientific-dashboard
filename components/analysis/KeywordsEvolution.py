import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from string import punctuation
from pages.Requirements import reqs

def KeywordsEvolution(df):
    data = {'word':[],'year':[]}
    
    for index,row in df[df['Author Keywords'].notna()].iterrows():
        if (row['Author Keywords']):
            for keyword in row['Author Keywords'].split(';'):
                temp = keyword.lower()
                for punc in punctuation:
                    temp = temp.replace(punc, ' ').replace('  ',' ')

                data['word'].append(temp.strip())
                data['year'].append(row['Year'])
    
    df_keywords = pd.DataFrame.from_dict(data)
    years = df_keywords['year'].unique()
    top20 = df_keywords['word'].value_counts().head(20).index.tolist()
    df_keywords = df_keywords[df_keywords['word'].isin(top20)].pivot_table(columns=['year'],index='word',aggfunc=len).fillna(0).transpose().reset_index()
    
    fig = go.Figure(
    data=[
        go.Scatter(name=top20[0],x=years,y=df_keywords[top20[0]],connectgaps=True),
        go.Scatter(name=top20[1],x=years,y=df_keywords[top20[1]],connectgaps=True),
        go.Scatter(name=top20[2],x=years,y=df_keywords[top20[2]],connectgaps=True),
        go.Scatter(name=top20[3],x=years,y=df_keywords[top20[3]],connectgaps=True),
        go.Scatter(name=top20[4],x=years,y=df_keywords[top20[4]],connectgaps=True),
        go.Scatter(name=top20[5],x=years,y=df_keywords[top20[5]],connectgaps=True),
        go.Scatter(name=top20[6],x=years,y=df_keywords[top20[6]],connectgaps=True),
        go.Scatter(name=top20[7],x=years,y=df_keywords[top20[7]],connectgaps=True),
        go.Scatter(name=top20[8],x=years,y=df_keywords[top20[8]],connectgaps=True),
        go.Scatter(name=top20[9],x=years,y=df_keywords[top20[9]],connectgaps=True),
        go.Scatter(name=top20[10],x=years,y=df_keywords[top20[10]],connectgaps=True),
        go.Scatter(name=top20[11],x=years,y=df_keywords[top20[11]],connectgaps=True),
        go.Scatter(name=top20[12],x=years,y=df_keywords[top20[12]],connectgaps=True),
        go.Scatter(name=top20[13],x=years,y=df_keywords[top20[13]],connectgaps=True),
        go.Scatter(name=top20[14],x=years,y=df_keywords[top20[14]],connectgaps=True),
        go.Scatter(name=top20[15],x=years,y=df_keywords[top20[15]],connectgaps=True),
        go.Scatter(name=top20[16],x=years,y=df_keywords[top20[16]],connectgaps=True),
        go.Scatter(name=top20[17],x=years,y=df_keywords[top20[17]],connectgaps=True),
        go.Scatter(name=top20[18],x=years,y=df_keywords[top20[18]],connectgaps=True),
        go.Scatter(name=top20[19],x=years,y=df_keywords[top20[19]],connectgaps=True),
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
            html.H3("Evolução de Keywords",className="section-title"),
            dcc.Graph(figure=fig),
            html.H3("Requisitos Informacionais",className="section-title"),
            html.Div(className="req-div",children=[html.H3('RI05',className="req-id"),html.P(reqs['RI05'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI06',className="req-id"),html.P(reqs['RI06'],className="req-description")])
        ]
    )