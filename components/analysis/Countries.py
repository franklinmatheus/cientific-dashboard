import plotly.graph_objects as go
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from urllib.request import urlopen
import json
import pycountry

def Countries(df):
    with open('data/custom.geo.json') as file:
        geojson = json.load(file)
    
    data = '; '.join(df[df.notnull()].values.astype(str)).lower()

    data_country = []
    data_count = []
    for country in pycountry.countries:
        data_country.append(country.name)
        data_count.append(data.count(country.name.lower()))
    
    #for row in df[df.notnull()].values:
        
        #places = geograpy.get_geoPlace_context(text=row)
        #data = [arr[-1].strip() for arr in [inst.split(',') for inst in row.split(';')]]
        #print(places.country_mentions)
    
    fig = go.Figure(
    data=[
        dict(type = 'choropleth',
            locations = data_country,
            locationmode = 'country names',
            autocolorscale = False,
            colorscale = 'Blues',
            text= data_country,
            z=data_count,
            marker = dict(line = dict(color = 'rgb(40,40,40)',width = 1)),
            colorbar = {'title':'Colour Range','lenmode':'fraction'},
        )
    ],
    layout=go.Layout(
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0
            ),
            geo=dict(bgcolor='rgb(40,40,40)',coastlinecolor='rgb(40,40,40)'),
            #plot_bgcolor='rgb(40,40,40)',
            paper_bgcolor='rgb(40,40,40)',
            font= {
                "family":"Verdana, Arial, Helvetica, sans-serif",
                "color": "rgb(220, 220, 220)"
            },
        )
    )
    
    return html.Div(
        className="section",
        children=[
            html.H3("Países que mais aparecem",className="section-title"),
            dcc.Graph(figure=fig)
        ]
    )