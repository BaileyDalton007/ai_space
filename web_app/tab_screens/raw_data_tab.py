from dash import html, dcc


def render(data):
    if data is None:
        return html.H3("Select a point on the plot to view data.")
    
    return html.Div(id = 'tab', children=[
        html.Table(
            [html.Tr([html.Td(str(key)), html.Td(str(data[key]))]) for key in data.keys()]
        )
    ])