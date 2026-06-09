# ==================================================
# Soal 11.25
# Program Cholesky
# ==================================================

import numpy as np

A = np.array([
    [25, 15, -5],
    [15, 18, 0],
    [-5, 0, 11]
], dtype=float)

L = np.linalg.cholesky(A)

print("Matriks L:")
print(L)