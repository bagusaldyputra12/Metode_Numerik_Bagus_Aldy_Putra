# ==================================================
# Soal 11.2
# Matrix Inverse dengan LU Decomposition
# ==================================================

import numpy as np
from scipy.linalg import lu

A = np.array([
    [2.04, -1, 0, 0],
    [-1, 2.04, -1, 0],
    [0, -1, 2.04, -1],
    [0, 0, -1, 2.04]
], dtype=float)

P, L, U = lu(A)

A_inv = np.linalg.inv(A)

print("Inverse Matrix:")
print(A_inv)