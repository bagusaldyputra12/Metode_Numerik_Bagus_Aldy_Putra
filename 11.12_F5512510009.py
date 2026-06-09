# ==================================================
# Soal 11.12
# Gauss-Seidel Relaxation
# ==================================================

import numpy as np

x = np.zeros(3)
lam = 0.95
es = 5

for i in range(100):

    old = x.copy()

    x1 = (50 - x[1] - 12*x[2]) / (-3)
    x[0] = lam*x1 + (1-lam)*old[0]

    x2 = (6*x[0] - x[2] - 3)
    x[1] = lam*x2 + (1-lam)*old[1]

    x3 = (40 - 6*x[0] - 9*x[1])
    x[2] = lam*x3 + (1-lam)*old[2]

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)