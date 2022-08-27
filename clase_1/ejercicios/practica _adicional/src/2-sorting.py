import numpy as np

from clase_1.ejercicios.src.norm import vector_norm_l2


def sorting_vectors_by_norm_l2(matrix):
    norm_l2 = vector_norm_l2(matrix)
    arg_sort = np.argsort(norm_l2 * -1)
    return matrix[arg_sort, :]
