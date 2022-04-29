import numpy as np


def vector_norm_l0(matrix):
    mask = matrix > 0
    return np.sum(mask, axis=1)


def vector_norm_l1(matrix):
    abs_m = np.abs(matrix)
    return np.sum(abs_m, axis=1)


def vector_norm_l2(matrix):
    return np.sqrt(np.sum(matrix ** 2, axis=1))


def vector_norm_inf(m):
    return np.max(m, axis=1)
