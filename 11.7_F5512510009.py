# ==================================================
# Soal 11.7
# Cholesky Matrix Diagonal
# ==================================================

import numpy as np

A = np.array([
    [9, 0, 0],
    [0, 25, 0],
    [0, 0, 4]
], dtype=float)

L = np.linalg.cholesky(A)

print(L)