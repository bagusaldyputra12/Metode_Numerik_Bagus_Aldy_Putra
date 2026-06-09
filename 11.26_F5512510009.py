# ==================================================
# Soal 11.26
# Program Gauss-Seidel
# ==================================================

import numpy as np

x = np.zeros(3)

for k in range(50):

    x[0] = (12 - x[1] - x[2]) / 5
    x[1] = (15 - 2*x[0] - x[2]) / 7
    x[2] = (20 - x[0] - 2*x[1]) / 10

print("Solusi:")
print(x)