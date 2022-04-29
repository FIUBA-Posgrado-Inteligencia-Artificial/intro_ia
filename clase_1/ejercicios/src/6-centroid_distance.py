import numpy as np


def get_centroid_distances(C, X):
    expanded_C = C[:, None]
    distances = np.sqrt(np.sum((expanded_C - X) ** 2, axis=2))
    return distances
