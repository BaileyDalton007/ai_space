from dash import html, dcc


def render(data):
    if data is None:
        return html.H3("Select a point on the plot to view data.")

    comments_list = []
    if data['comments'] is not None:
        [comments_list.append(bullet) for bullet in data['comments'].split('\n') if bullet != ""]
    
    return html.Div(id = 'tab', children=[
        html.H2(data['title'], style={'display': 'flex', 'justify-content': 'center'}),
        dcc.Link("Full Article", href=data['url'], target="_blank", style={'display': 'flex', 'justify-content': 'center', 'color': 'blue'}),
        html.Hr(),

        html.Ul(children=[html.Li(bullet.strip(" - ")) for bullet in data['summary'].split('\n') if bullet != ""]),
        
        html.H3('Commentary', style={'display': 'flex', 'justify-content': 'center'}),
        html.Hr(),
        html.Ul(children=[html.Li(bullet) for bullet in comments_list])
    ])