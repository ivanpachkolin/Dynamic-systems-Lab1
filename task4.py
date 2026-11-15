import numpy as np
import matplotlib.pyplot as plt
import math


x0 = 0.4
Ntr = 200
N = 400

r_list = np.linspace(0, 2, 1000)
lambda_list = []

for r in r_list:
    x = x0
    for _ in range(Ntr):
        x = 1 - r * x ** 2
    S = 0
    for _ in range(N):
        x = 1 - r * x ** 2
        if x == 0 or r == 0:
            S = -math.inf
        else:
            S = S + math.log(abs(-2*r*x))
    lambda_list.append(S / N)

    
#r≈1.4
plt.plot(r_list, lambda_list, label='λ(r)', color='orange', linewidth=1)

plt.axhline(y=0, color='red', linestyle='--', linewidth=1.5)

plt.xlabel('r', fontsize=12)
plt.ylabel('λ', fontsize=12)
plt.title('График λ(r)', fontsize=13)
plt.show()
