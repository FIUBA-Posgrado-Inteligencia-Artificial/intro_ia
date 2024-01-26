import numpy as np
from centroid_distance import get_centroid_distances


def test_get_centroid_distances():
    X = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    C = np.array([
        [1, 0, 0],
        [0, 1, 1]
    ])
    expected = np.array([
        [3.60555128, 8.36660027, 13.45362405],
        [2.44948974, 7.54983444, 12.72792206]
    ])
    result = get_centroid_distances(C, X)
    np.testing.assert_allclose(expected, result)
