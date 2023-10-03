import plotly.express as px
import utils

def render(df, color_map):
    # Only runs T-SNE first time.
    if 't_x' not in df.columns:
        x, y = utils.tsne_reduction(df['title_embedding'])
        df['t_x'] = x
        df['t_y'] = y
    
    fig = px.scatter(df, x='t_x', y='t_y', hover_data=['title', 'cluster_label'], color=df['cluster'].astype(str), custom_data=df,
                      color_discrete_map=color_map, title='Article Embeddings with T-SNE Reduction')
    fig.update_coloraxes(showscale=False)
    fig.update_xaxes(showgrid=False, showticklabels=False, title_text='')
    fig.update_yaxes(showgrid=False, showticklabels=False, title_text='')
    fig.update_layout(showlegend=False)
    fig.update_layout(title='Article Embeddings with T-SNE Reduction', title_x=0.5, title_font=dict(size=24))
    fig.update_traces(marker=dict(size=15, opacity=0.85, line=dict(color='black', width=2)))

    fig.update_traces(hovertemplate="""%{customdata[1]}<br>%{customdata[8]}""", )
    return fig