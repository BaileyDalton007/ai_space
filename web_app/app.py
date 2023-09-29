# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px

import plot
from tab_screens import cluster_data_tab, article_data_tab, raw_data_tab

# Incorporate data
df = pd.read_csv('cluster_data.csv', sep='\t')

# Define a custom color palette based on the number of unique categories
custom_colors = px.colors.qualitative.Set1[:len(df['cluster'].unique())]
color_map = {str(category): color for category, color in zip(df['cluster'].unique(), custom_colors)}

# Initialize the app
app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div(children=[
    html.Div(children='AI Issues Outline'),
    html.Hr(),

    html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'height': '80vh'}, children=[
        dcc.Graph(style={'width': '100vh'}, figure=plot.render(df, color_map), id='graph'),


        html.Div(style={'width': '100vh'}, children=[
        dcc.Tabs(id="data-tab", value='article_info', children=[
            dcc.Tab(label='Cluster Data', value='cluster_data'),
            dcc.Tab(label='Article Info', value='article_info'),
            dcc.Tab(label='Raw Data', value='raw_data'),
        ]),
        html.Div(id='data-tab-content'),
        ])

    ]),

     dcc.Store(id='memory-output')
])

@callback(
    Output('memory-output', 'data'),
    Input('graph', 'clickData')
)
def click_data(clickData):
    if clickData is None:
        return None
    else:
        # Parses the point data into a more usable format.
        data_arr = clickData['points'][0]['customdata']
        return {df.columns[i]: data_arr[i] for i in range(len(df.columns))}

@callback(
    Output('data-tab-content', 'children'),
    Input('memory-output', 'data'),
    Input('data-tab', 'value')
)
def render_content(data, tab):
    if tab == 'cluster_data':
        return cluster_data_tab.render(df, data, color_map)
    elif tab == 'article_info':
        return article_data_tab.render(data)
    elif tab == 'raw_data':
        return raw_data_tab.render(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)