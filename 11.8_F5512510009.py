# ==================================================
# Soal 11.8
# Gauss-Seidel Overrelaxation
# ==================================================

import numpy as np

x = np.zeros(3)
lam = 1.2
es = 5

for i in range(100):

    old = x.copy()

    x[0] = (41 + 0.4*x[1]) / 0.8
    x[0] = lam*x[0] + (1-lam)*old[0]

    x[1] = (25 + 0.4*x[0] + 0.4*x[2]) / 0.8
    x[1] = lam*x[1] + (1-lam)*old[1]

    x[2] = (105 + 0.4*x[1]) / 0.8
    x[2] = lam*x[2] + (1-lam)*old[2]

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)