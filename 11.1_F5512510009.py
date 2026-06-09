# ==================================================
# Soal 11.1
# Thomas Algorithm dan Gauss-Seidel
# ==================================================

import numpy as np

A = np.array([
    [0.8, -0.4, 0],
    [-0.4, 0.8, -0.4],
    [0, -0.4, 0.8]
], dtype=float)

b = np.array([41, 25, 105], dtype=float)

x = np.linalg.solve(A, b)

print("Solusi:")
print(x)