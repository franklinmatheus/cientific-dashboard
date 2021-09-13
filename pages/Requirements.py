import dash_html_components as html
import dash_core_components as dcc

reqs = {
    'RI01':'A visualização deve permitir a análise da proporção de publicações por conferência.',
    
    'RI02':'A visualização deve indicar quais são os países das instituições citadas nas publicações.',
    'RI03':'A visualização deve permitir a análise dos países mais presentes nas publicações.',
    
    'RI04':'A visualização deve permitir a análise do número de publicações por ano.',
    
    'RI05':'A visualização deve apresentar as 20 keywords mais recorrentes das publicações.',
    'RI06':'A visualização deve permitir a análise da evolução das 20 keywords mais recorrentes ao longo dos anos.',
    
    'RI07':'A visualização deve apresentar os autores que apresentam mais de 8 coautores.',
    'RI08':'A visualização deve permitir a análise dos principais grupos de coautoria mundial.',

    'RI09':'A visualização deve apresentar os autores brasileiros.',
    'RI10':'A visualização deve permitir a análise dos principais grupos de coautoria brasileiros.',

    'RI11':'A visualização deve apresentar as keywords que apresentam mais de 15 ocorrências.',
    'RI12':'A visualização deve permitir a análise das keywords que mais aparecem juntas nas publicações.',

    'RI13':'A visualização deve permitir a análise das 100 keywords mais recorrentes das publicações.',
}

def Requirements(df):
    return html.Div(
        className="section",
        children=[
            html.H3("Requisitos Informacionais",className="section-title"),
            html.Div(className="req-div",children=[html.H3('RI01',className="req-id"),html.P(reqs['RI01'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI02',className="req-id"),html.P(reqs['RI02'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI03',className="req-id"),html.P(reqs['RI03'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI04',className="req-id"),html.P(reqs['RI04'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI05',className="req-id"),html.P(reqs['RI05'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI06',className="req-id"),html.P(reqs['RI06'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI07',className="req-id"),html.P(reqs['RI07'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI08',className="req-id"),html.P(reqs['RI08'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI09',className="req-id"),html.P(reqs['RI09'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI10',className="req-id"),html.P(reqs['RI10'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI11',className="req-id"),html.P(reqs['RI11'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI12',className="req-id"),html.P(reqs['RI12'],className="req-description")]),
            html.Div(className="req-div",children=[html.H3('RI13',className="req-id"),html.P(reqs['RI13'],className="req-description")]),
        ]
    )