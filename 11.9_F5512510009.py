# ==================================================
# Soal 11.9
# Gauss-Seidel Reactor
# ==================================================

import numpy as np

x = np.zeros(3)
es = 5

for i in range(100):

    old = x.copy()

    x[0] = (3800 + 3*x[1] + x[2]) / 15
    x[1] = (1200 + 3*x[0] + 6*x[2]) / 18
    x[2] = (-350 + 4*x[0] + x[1]) / 12

    ea = np.max(np.abs((x-old)/x))*100

    if ea < es:
        break

print(x)