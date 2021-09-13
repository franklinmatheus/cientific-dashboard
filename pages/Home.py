import dash_html_components as html
import dash_core_components as dcc
from components.analysis.NullValuesChart import NullValuesChart

def Home(df):
    return html.Div([
        dcc.Tabs(
            className='tabs-container',
            children=[
                dcc.Tab(
                    label="Dataset",
                    className='tab',
                    selected_className='tab-selected',
                    children=[
                        html.Div(
                            className="section",
                            children=[
                                html.H3("Descrição do Dataset",className="section-title"),
                                html.P('''
                                    O Dataset é composto por um conjunto de dados coletado da Scopus. 
                                    Os registros do Dataset representam publicações realizadas em conferências da área de Engenharia de Requisitos.
                                    Ao todo, 1.909 registros foram identificados após o processo de preparação do Dataset e, para cada registro,
                                    existem 46 valores; ou seja, o Dataset apresenta 46 variáveis. 
                                    Nem todas as variáveis apresentam todas as informações, existem muitos valores nulos no Dataset;
                                    o número de valores nulos por variável pode ser observado na aba "Valores Nulos".
                                ''',className="section-text"),
                                html.H3("Variáveis",className="section-title"),
                                html.Div(className="var-div",children=["Authors",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Author(s) ID",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Title",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Year",html.Span("Numérico",className="var-span"),html.Span("Independente",className="var-span")]),
                                html.Div(className="var-div",children=["Source title",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Volume",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Issue",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Art. No.",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Page start",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Page end",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Page count",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Cited by",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["DOI",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Link",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Affiliations",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Authors with affiliations",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Abstract",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Author Keywords",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Index Keywords",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Molecular Sequence Numbers",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Chemicals/CAS",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Tradenames",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Manufacturers",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Funding Details",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Funding Text 1",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Funding Text 2",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["References",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Correspondence Address",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Editors",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Sponsors",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Publisher",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Conference name",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Conference date",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Conference location",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Conference code",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["ISSN",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["ISBN",html.Span("Numérico",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["CODEN",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["PubMed ID",html.Span("-",className="var-span"),html.Span("-",className="var-span")]),
                                html.Div(className="var-div",children=["Language of Original Document",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Abbreviated Source Title",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Document Type",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Publication Stage",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Open Access",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["Source",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")]),
                                html.Div(className="var-div",children=["EID",html.Span("Textual",className="var-span"),html.Span("Dependente",className="var-span")])
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label="Valores Nulos",
                    className='tab',
                    selected_className='tab-selected',
                    children=[NullValuesChart(df)]
                )
            ]
        )
    ])