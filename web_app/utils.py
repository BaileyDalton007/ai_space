from sklearn.manifold import TSNE
import numpy as np
from ast import literal_eval

"""
T-SNE Dimensionality Reduction
"""
def tsne_reduction(embed_series, dims=2, perplexity=10, random_state=42):
    # Convert to a list of lists of floats
    # https://github.com/openai/openai-cookbook/blob/main/examples/Visualizing_embeddings_in_2D.ipynb
    matrix = np.array(embed_series.apply(literal_eval).to_list())

    tsne = TSNE(n_components=dims, perplexity=perplexity, random_state=random_state, init='random', learning_rate=200)
    vis_dims = tsne.fit_transform(matrix)

    x = [x for x,y in vis_dims]
    y = [y for x,y in vis_dims]

    return x, y