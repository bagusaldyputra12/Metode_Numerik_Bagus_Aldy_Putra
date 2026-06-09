# ==================================================
# Soal 11.19
# Hilbert Matrix
# ==================================================

import numpy as np

n = 4

H = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        H[i, j] = 1 / (i + j + 1)

print("Hilbert Matrix:")
print(H)

print("\nCondition Number:")
print(np.linalg.cond(H))