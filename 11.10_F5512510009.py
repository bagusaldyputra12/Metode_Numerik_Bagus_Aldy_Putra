# ==================================================
# Soal 11.10
# Jacobi Iteration
# ==================================================

import numpy as np

x = np.zeros(3)
es = 5

for i in range(100):

    old = x.copy()

    x1 = (3800 + 3*old[1] + old[2]) / 15
    x2 = (1200 + 3*old[0] + 6*old[2]) / 18
    x3 = (-350 + 4*old[0] + old[1]) / 12

    x = np.array([x1, x2, x3])

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)