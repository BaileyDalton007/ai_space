import plotly.express as px
import utils

def render(df, color_map):
    # Only runs T-SNE first time
    if 't_x' not in df.columns:
        x, y = utils.tsne_reduction(df['title_embedding'])
        df['t_x'] = x
        df['t_y'] = y
    
    fig = px.scatter(df, x='t_x', y='t_y', hover_data=['title', 'cluster_label'], color=df['cluster'].astype(str), custom_data=df, color_discrete_map=color_map)
    fig.update_coloraxes(showscale=False)
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_layout(showlegend=False)
    return fig