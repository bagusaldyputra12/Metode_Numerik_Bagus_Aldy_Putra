# ==================================================
# Soal 11.13
# Gauss-Seidel Overrelaxation
# ==================================================

import numpy as np

x = np.zeros(3)
lam = 1.2
es = 5

for i in range(100):

    old = x.copy()

    x1 = (-38 + 6*x[1] + x[2]) / 2
    x[0] = lam*x1 + (1-lam)*old[0]

    x2 = (34 - 3*x[0] - 7*x[2])
    x[1] = lam*x2 + (1-lam)*old[1]

    x3 = (20 + 8*x[0] - x[1]) / (-2)
    x[2] = lam*x3 + (1-lam)*old[2]

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)