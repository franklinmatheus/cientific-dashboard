import plotly.express as px
import dash_html_components as html
import plotly.graph_objects as go
from string import punctuation
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import base64
from pages.Requirements import reqs

def WordCloudView(df):
    words = {}
    for index,row in df[df["Author Keywords"].notna()].iterrows():
        for keyword in row["Author Keywords"].split(";"):
            temp = keyword.lower()
            for punc in punctuation:
                temp = temp.replace(punc, " ").replace("  "," ")

            if temp in words:
                words[temp] = words[temp] + 1
            else:
                words[temp] = 1

    elipse_mask = np.array(Image.open("static/elipse_format.png"))
    wordcloud = WordCloud(background_color="#282828",
                            max_words=100,
                            prefer_horizontal=1,
                            mask=elipse_mask,
                            width=1200,
                            height=800,
                            colormap='cool')
    wordcloud.generate_from_frequencies(words)

    file_name = "static/wordcloud.png"
    wordcloud.to_file(file_name)
    encoded_image = base64.b64encode(open(file_name, "rb").read())

    img = Image.open(file_name)
    fig = px.imshow(img)
    fig.update_layout(go.Layout(
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=0
            ),
            plot_bgcolor='rgb(40,40,40)',
            paper_bgcolor='rgb(40,40,40)',
            font= {
                "family":"Verdana, Arial, Helvetica, sans-serif",
                "color": "rgb(220, 220, 220)"
            }
        ))
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return html.Div(
        className="section",
        children=[
            html.H3("Nuvem de palavras",className="section-title"),
            html.Img(className="wordcloud",src="data:image/png;base64,{}".format(encoded_image.decode())),
            html.H3("Requisitos Informacionais",className="section-title"),
            html.Div(className="req-div",children=[html.H3('RI13',className="req-id"),html.P(reqs['RI13'],className="req-description")]),
        ]
    )