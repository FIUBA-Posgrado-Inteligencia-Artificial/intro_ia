from unittest import TestCase
import numpy as np
from sorting import sorting_vectors_by_norm_l2


class SortTestCase(TestCase):

    def test_sorting_by_norm_l2(self):
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        sorted_a = sorting_vectors_by_norm_l2(a)
        np.testing.assert_equal(np.array([[5, 6, 7, 8], [1, 2, 3, 4]]), sorted_a)

        a = np.array([[1, 2, 3, 4], [10, 11, 12, 13], [5, 6, 7, 8]])
        sorted_a = sorting_vectors_by_norm_l2(a)
        np.testing.assert_equal(np.array([[10, 11, 12, 13], [5, 6, 7, 8], [1, 2, 3, 4]]), sorted_a)
