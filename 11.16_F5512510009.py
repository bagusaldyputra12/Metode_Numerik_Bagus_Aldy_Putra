# ==================================================
# Soal 11.16
# Matrix Inverse dan Condition Number
# ==================================================

import numpy as np

A = np.array([
    [1, 1/2, 1/3],
    [1, 2/3, 1/2],
    [1, 3/4, 3/5]
], dtype=float)

A_inv = np.linalg.inv(A)
cond_num = np.linalg.cond(A)

print("Inverse Matrix:")
print(A_inv)

print("\nCondition Number:")
print(cond_num)