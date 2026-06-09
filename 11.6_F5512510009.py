# ==================================================
# Soal 11.6
# Cholesky Decomposition
# ==================================================

import numpy as np

A = np.array([
    [8, 20, 15],
    [20, 80, 50],
    [15, 50, 60]
], dtype=float)

L = np.linalg.cholesky(A)

print("Matriks L:")
print(L)