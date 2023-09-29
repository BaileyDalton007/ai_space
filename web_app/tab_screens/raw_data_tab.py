from dash import html, dcc


def render(data):
    if data is None:
        return
    return html.Div(id = 'tab', children=[
        html.Table(
            #html.Tr([html.Th('Raw Data Table')]),
            [html.Tr([html.Td(str(key)), html.Td(str(data[key]))]) for key in data.keys()]
        )
    ])