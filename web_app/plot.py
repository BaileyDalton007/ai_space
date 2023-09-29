import plotly.express as px
import utils

def render(df, col_chosen):
    # Define a custom color palette based on the number of unique categories
    custom_colors = px.colors.qualitative.Set1[:len(df['cluster'].unique())]
    color_discrete_map = {str(category): color for category, color in zip(df['cluster'].unique(), custom_colors)}

    x, y = utils.tsne_reduction(df[col_chosen])
    fig = px.scatter(df, x=x, y=y, hover_data=['title', 'cluster_label'], color=df['cluster'].astype(str), custom_data=df, color_discrete_map=color_discrete_map)
    fig.update_coloraxes(showscale=False)
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_layout(showlegend=False)
    return fig