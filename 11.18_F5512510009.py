# ==================================================
# Soal 11.18
# Penyelesaian Sistem Linear
# ==================================================

import numpy as np

A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
], dtype=float)

b = np.array([7.85, -19.3, 71.4])

x = np.linalg.solve(A, b)

print("Solusi:")
print(x)