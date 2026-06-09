import numpy as np
import matplotlib.pyplot as plt

D = 2
U = 1
k = 0.2
dx = 2

# titik interior: x=2,4,6,8
n = 4

a = np.zeros(n-1)
b = np.zeros(n)
c = np.zeros(n-1)
d = np.zeros(n)

for i in range(n):

    a_coef = D/dx**2 + U/(2*dx)
    b_coef = -2*D/dx**2 - k
    c_coef = D/dx**2 - U/(2*dx)

    b[i] = b_coef

    if i > 0:
        a[i-1] = a_coef

    if i < n-1:
        c[i] = c_coef

# kondisi batas
d[0] = - (D/dx**2 + U/(2*dx))*80
d[-1] = - (D/dx**2 - U/(2*dx))*20

# Thomas Algorithm
for i in range(1,n):
    m = a[i-1]/b[i-1]
    b[i] = b[i] - m*c[i-1]
    d[i] = d[i] - m*d[i-1]

x = np.zeros(n)

x[-1] = d[-1]/b[-1]

for i in range(n-2,-1,-1):
    x[i] = (d[i]-c[i]*x[i+1])/b[i]

# tambahkan boundary
c_full = np.concatenate(([80],x,[20]))
x_full = np.arange(0,11,2)

print("Konsentrasi:")
for xi,ci in zip(x_full,c_full):
    print(f"x={xi:2.0f}  c={ci:.4f}")

plt.plot(x_full,c_full,marker='o')
plt.xlabel("Distance x")
plt.ylabel("Concentration c")
plt.title("Concentration Distribution")
plt.grid(True)
plt.show()