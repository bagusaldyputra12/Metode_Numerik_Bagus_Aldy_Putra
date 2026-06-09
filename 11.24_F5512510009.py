# ==================================================
# Soal 11.24
# Implementasi Thomas Algorithm
# ==================================================

import numpy as np

n = 4

a = np.array([0, -1, -1, -1], dtype=float)
b = np.array([4, 4, 4, 4], dtype=float)
c = np.array([-1, -1, -1, 0], dtype=float)
d = np.array([5, 5, 10, 23], dtype=float)

for i in range(1, n):
    m = a[i] / b[i - 1]
    b[i] = b[i] - m * c[i - 1]
    d[i] = d[i] - m * d[i - 1]

x = np.zeros(n)

x[-1] = d[-1] / b[-1]

for i in range(n - 2, -1, -1):
    x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

print("Solusi:")
print(x)