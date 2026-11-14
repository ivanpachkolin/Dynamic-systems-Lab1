import numpy as np
import matplotlib.pyplot as plt


x_list = np.linspace(-1, 1, 1000)
f = [1-1.25*(1-1.25*x**2)**2 for x in x_list]
a = (2+2*2**0.5) / 5
b = (2-2*2**0.5) / 5
c = (-4+4*6**0.5) / 10

plt.plot(x_list, f, label='график отображения f^2', color='orange', linewidth=1)
plt.plot(np.linspace(-1, 1, 1000), np.linspace(-1, 1, 1000), label="y=x",linestyle='--', color='black', linewidth=1)
plt.scatter(a, a, color='blue', s=100, zorder=5, label="точки орбиты периода 2")
plt.scatter(b, b, color='blue', s=100, zorder=5)
plt.scatter(c, c, color='green', s=100, zorder=5, label="неподвижная точка f")

plt.axvline(x=-1, color='red', linestyle='--', linewidth=1.5)
plt.axvline(x=1, color='red', linestyle='--', linewidth=1.5)

plt.xlabel('x', fontsize=12)
plt.ylabel('f', fontsize=12)
plt.title('График отображения f^2 при r=5/4', fontsize=13)
plt.xlim(-1.5, 1.5)
plt.ylim(-2, 2)
plt.grid(True, alpha=0.3)
plt.legend(loc='lower right', fontsize=10)
plt.tight_layout()
plt.show()
