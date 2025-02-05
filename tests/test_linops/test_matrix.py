import numpy as np

import probnum as pn


def test_matrix_linop_converts_numpy_matrix():
    matrix = np.asmatrix(np.eye(10))
    linop = pn.linops.Matrix(matrix)

    assert not isinstance(linop.A, np.matrix)
    assert not isinstance(linop @ np.eye(10), np.matrix)
    assert not isinstance(np.eye(10) @ linop, np.matrix)
