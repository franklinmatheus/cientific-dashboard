import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_table

def ArticlesPerConference(df):
    conferences = df['Conference name']
    conferences = conferences.replace(r'\w*\d\w*','',regex=True).replace(r'IEEE/ACM|IEEE|ICSE','',regex=True).str.strip().str.replace('  ', ' ').str.rsplit(',',1).str[0]

    conferences = conferences.map(
        {
            "International Workshop on Managing Requirements Knowledge, MaRK', Held in Conjunction with the  Requirements Engineering Conference"
                :"International Workshop on Managing Requirements Knowledge",
            "Workshop on Requirements Engineering, WER , at the Ibero-American Conference on Software Engineering, Congresso Ibero-Americano em Engenharia de Software"
                :"Workshop on Requirements Engineering",
            "International Workshop on Empirical Requirements Engineering, EmpiRE , Co-located with Requirements Engineering"
                :"International Workshop on Empirical Requirements Engineering",
            "Workshop em Engenharia de Requisitos, WER - Requirements Engineering Workshop"
                :"Workshop on Requirements Engineering",
            "International Workshop on Requirements Engineering: Foundation for Software Quality, REFSQ , in Conjunction with the International Conference on Advanced"
                :"International Workshop on Requirements Engineering: Foundation for Software Quality",
            "First International Workshop on Visualization in Requirements Engineering, REV , at the  Requirements Engineering Conference"
                :"International Workshop on Visualization in Requirements Engineering",
            "Requirements Engineering and Law"
                :"International Workshop on Requirements Engineering and Law",
            "International Workshop on Requirements Engineering for Electronic Voting Systems, REVOTE - In Conjunction with the  International Requirements Engineering Conference "
                :"International Workshop on Requirements Engineering for Electronic Voting Systems",
            "International Working Conference on Requirements Engineering: Foundation for Software Quality, REFSQ "
                :"International Working Conference on Requirements Engineering: Foundation for Software Quality",
            "Ibero-American Conference on Software Engineering, CIbSE and Workshop on Requirements Engineering"
                :"Ibero-American Conference on Software Engineering and Workshop on Requirements Engineering",
            "Workshop on Empirical Requirements Engineering"
                :"International Workshop on Empirical Requirements Engineering",
            "Requirements Engineering Education and Training"
                :"International Workshop on Requirements Engineering Education and Training",
            "Workshop on Requirements Engineering for Systems, Services and Systems-of-Systems"
                :"International Workshop on Requirements Engineering for Systems, Services, and Systems-of-Systems",
            "Model-Driven Requirements Engineering Workshop"
                :"International Model-Driven Requirements Engineering Workshop",
            "International Workshop on Learning from Other Disciplines for Requirements Engineering"
                :"International Workshop on Learning from other Disciplines for Requirements Engineering"
        }
    ).fillna(conferences)

    names = conferences.value_counts().index.tolist()
    values = conferences.value_counts().values.tolist()
    
    compact_names = names[:9]
    compact_names.append("Outras (" + str(len(values[9:])) +")")
    compact_values = values[:9]
    compact_values.append(sum(values[9:]))

    fig = go.Figure(
    data=[
        go.Pie(name="Publicações",
            values=compact_values,
            labels=compact_names,
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

    table_values = [{"Nome":names[i],"Quantidade de artigos":values[i]} for i in range(9,len(names[9:]))]

    return html.Div(
        className="section",
        children=[
            html.H3("Artigos por Conferência",className="section-title"),
            dcc.Graph(figure=fig),
            html.H3("Outras Conferências",className="section-title"),
            html.P("Aqui, as conferências que foram agrupadas no gráfico acima são listadas.",className="section-text"),
            dash_table.DataTable(
                columns=[{"name":"Nome","id":"Nome"},{"name":"Quantidade de artigos","id":"Quantidade de artigos"}],
                data=table_values,
                style_header={
                    'backgroundColor': 'rgb(29, 29, 29)',
                    'color': 'rgb(220, 220, 220)',
                    'border': '0px',
                    'text-align': 'center'
                },
                style_cell={
                    'backgroundColor': 'rgb(40, 40, 40)',
                    'color': 'rgb(220, 220, 220)',
                    'border': '1px solid rgba(95, 95, 95, 0.1)',
                    'text-align': 'left',
                    
                },
                style_data_conditional=[
                    {
                        'if': {
                            'state': 'selected'  # 'active' | 'selected'
                        },
                        'backgroundColor': 'rgba(10, 189, 227, 0.9)',
                        'border': '1px solid rgba(10, 189, 227, 0.9)',
                        'color': 'rgb(40, 40, 40)'
                    }
                ]
            )
        ]
    )