import numpy as np
from centroid_distance import get_centroid_distances


def get_cluster_id(C, X):
    distances = get_centroid_distances(C, X)
    arg_min = np.argmin(distances, axis=0)
    return arg_min

