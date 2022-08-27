from unittest import TestCase
import math
import numpy as np
from norm import vector_norm_l0, vector_norm_l1, vector_norm_l2, vector_norm_inf


class NormTestCase(TestCase):

    def test_norm_l0(self):
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        expected = np.array([4, 4])
        result = vector_norm_l0(a)
        np.testing.assert_equal(expected, result)

        a = np.array([[1, 0, 0, 4], [5, 6, 0, 8]])
        expected = np.array([2, 3])
        result = vector_norm_l0(a)
        np.testing.assert_equal(expected, result)

    def test_norm_l1(self):
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        expected = np.array([10, 26])
        result = vector_norm_l1(a)
        np.testing.assert_equal(expected, result)

        a = np.array([[-1, -2, -3, -4], [-5, -6, -7, -8]])
        expected = np.array([10, 26])
        result = vector_norm_l1(a)
        np.testing.assert_equal(expected, result)

    def test_norm_l2(self):
        a = np.array([[1, 2], [3, 4]])
        expected = np.array([math.sqrt(5), math.sqrt(25)])
        result = vector_norm_l2(a)
        np.testing.assert_allclose(expected, result)

    def test_norm_inf(self):
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        expected = np.array([4, 8])
        result = vector_norm_inf(a)
        np.testing.assert_equal(expected, result)
