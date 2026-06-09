# ==================================================
# Soal 11.17
# Sistem Persamaan Linear
# ==================================================

import numpy as np

A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
], dtype=float)

b = np.array([27, -61.5, -21.5])

x = np.linalg.solve(A, b)

print("Solusi:")
print(x)