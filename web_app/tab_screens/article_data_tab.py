from dash import html, dcc


def render(data):
    if data is None:
        return

    return html.Div(id = 'tab', children=[
        html.H2(data['title'], style={'display': 'flex', 'justify-content': 'center'}),
        dcc.Link("Full Article", href=data['url'], target="_blank", style={'display': 'flex', 'justify-content': 'center', 'color': 'blue'}),
        html.Hr(),

        
    ])