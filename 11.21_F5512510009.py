# ==================================================
# Soal 11.21
# Augmented Matrix
# ==================================================

import numpy as np

A = np.array([
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
], dtype=float)

b = np.array([2, -1, 4])

aug = np.column_stack((A, b))

print("Augmented Matrix:")
print(aug)