from dash import html, dcc
import plotly.express as px
import json

cluster_labels = dict()
with open ('web_app/cluster_labels.json', 'r') as f:
    cluster_labels = json.load(f)

def render(df, data):
    if data is None:
        return


    # Define a custom color palette based on the number of unique categories
    custom_colors = px.colors.qualitative.Set1[:len(df['cluster'].unique())]
    color_discrete_map = {category: color for category, color in zip(df['cluster'].unique(), custom_colors)}

    fig = px.pie(names=df['cluster'].value_counts().index.astype(str), values=df['cluster'].value_counts(),
                  color_discrete_map=color_discrete_map, color=df['cluster'].value_counts().index)

    # Create a map to pull out the portion of the currently selected cluster
    pull_arr = df['cluster'].value_counts().index == data['cluster']
    pull_arr = pull_arr.astype(int) * 0.2
    fig.update_traces(pull=pull_arr, selector=dict(type='pie'))

    fig.update_layout(showlegend=False)

    return html.Div(id = 'tab', children=[
        dcc.Graph(
            figure=fig
        ),

        html.H2(data['cluster_label']),
        html.H4(data['cluster_desc'])
    ])