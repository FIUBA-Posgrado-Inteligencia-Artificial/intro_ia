import numpy as np
from cluster_id import get_cluster_id


def test_get_cluster_id():
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
        1, 1, 1
    ])
    result = get_cluster_id(C, X)
    np.testing.assert_equal(expected, result)