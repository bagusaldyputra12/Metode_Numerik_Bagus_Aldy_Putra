# ==================================================
# Soal 11.4
# Verifikasi Cholesky
# ==================================================

import numpy as np

A = np.array([
    [6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]
], dtype=float)

L = np.linalg.cholesky(A)

print("Matriks L:")
print(L)

print("\nL * LT:")
print(L @ L.T)