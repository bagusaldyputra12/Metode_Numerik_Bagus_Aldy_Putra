# ==================================================
# Soal 11.22
# Matrix Inverse
# ==================================================

import numpy as np

A = np.array([
    [4, 2],
    [3, 1]
], dtype=float)

A_inv = np.linalg.inv(A)

print("Inverse Matrix:")
print(A_inv)