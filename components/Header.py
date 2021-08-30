import dash_html_components as html

def Header():
    return html.Div(
            className="wrapper",
            children=[
                html.H1(
                    className="title-header",
                    children=["Dashboard"]
                )
            ]
        )