import numpy as np
import matplotlib.pyplot as plt

x0 = 0.4
Ntr = 200
N = 200

r_list = np.linspace(0, 2, 1000)
R = []
X = []
for r in r_list:
    x = x0
    for _ in range(Ntr):
        x = 1 - r * x ** 2

    for _ in range(N):
        x = 1 - r * x ** 2
        R.append(r)
        X.append(x)

plt.scatter(R, X, s=0.5)

plt.axvline(x=0.75, color='red', linestyle='--', linewidth=1.5)
plt.text(0.8, -1, 'r = 0.75', color='red', fontsize=12, rotation=90)
plt.axvline(x=1.25, color='red', linestyle='--', linewidth=1.5)
plt.text(1.15, -1, 'r = 1.25', color='red', fontsize=12, rotation=90)
plt.axvline(x=1.4, color='green', linestyle='--', linewidth=1.5)
plt.text(1.45, -1, 'r ≈ 1.4', color='green', fontsize=12, rotation=90)

plt.xlabel('r', fontsize=12)
plt.ylabel('x', fontsize=12)
plt.title('Бифуркационное дерево', fontsize=13)
plt.show()
