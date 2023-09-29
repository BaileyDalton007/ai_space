from dash import html, dcc
import plotly.express as px

def render(df, data, color_map):
    if data is None:
        return

    fig = px.pie(names=df['cluster'].value_counts().index.astype(str), values=df['cluster'].value_counts(),
                  color_discrete_map=color_map, color=df['cluster'].value_counts().index.astype(str))

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