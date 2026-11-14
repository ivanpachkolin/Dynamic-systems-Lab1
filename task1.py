import numpy as np
import matplotlib.pyplot as plt


r_stable = np.linspace(0.002, 0.75, 1000)
r_unstable = np.linspace(0.7502, 2, 1000)
x1 = [(-1+(1+4*r)**0.5) / (2*r) for r in r_stable]
x2 = [(-1+(1+4*r)**0.5) / (2*r) for r in r_unstable]


plt.plot(r_stable, x1, label='устойчивая область', color='green', linewidth=1)
plt.plot(r_unstable, x2, label='неустойчивая область', color='blue', linewidth=1)
plt.scatter(2, -1, color='blue', s=100, zorder=5)

plt.scatter(
    0.75, 2/3,
    s=100,
    facecolor='white',
    edgecolor='green',
    linewidth=2,
    zorder=5,
)

plt.axhline(y=-1, color='red', linestyle='--', linewidth=1.5)
plt.axvline(x=0, color='red', linestyle='--', linewidth=1.5)
plt.axhline(y=1, color='red', linestyle='--', linewidth=1.5)
plt.axvline(x=2, color='red', linestyle='--', linewidth=1.5)

plt.xlabel('r', fontsize=12)
plt.ylabel('x', fontsize=12)
plt.title('График зависимости неподвижных точек от параметра r', fontsize=13)
plt.xlim(-1, 3)
plt.ylim(-2, 2)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()
