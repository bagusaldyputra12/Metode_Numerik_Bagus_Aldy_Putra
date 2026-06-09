# ==================================================
# Soal 11.20
# Vandermonde Matrix
# ==================================================

import numpy as np

x = np.array([1, 2, 3, 5])

V = np.vander(x)

print("Vandermonde Matrix:")
print(V)