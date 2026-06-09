# ==================================================
# Soal 11.11
# Gauss-Seidel
# ==================================================

import numpy as np

x = np.zeros(3)
es = 5

for i in range(100):

    old = x.copy()

    x[0] = (27 - 2*x[1] + x[2]) / 10
    x[1] = (61.5 - 3*x[0] - 2*x[2]) / (-6)
    x[2] = (-21.5 - x[0] - x[1]) / 5

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)