#Alex Karacaoglu
#Code for part 2a, hit run and the plot will show

import numpy as np
import matplotlib.pyplot as plt
def generate_X():
    A = np.array([[4,-2], [-2,3]])
    return np.random.multivariate_normal([0, 0], A, size=1000).T
def scatterplot(X):
    plt.figure()
    plt.subplot(aspect='equal')
    plt.scatter(X[0,:], X[1,:], alpha=0.5, zorder=3)
    plt.xlim([-6, 6])
    plt.ylim([-4, 4])
    plt.grid(axis='both', ls=':', alpha=0.5)
    return
X = generate_X()
scatterplot(X)
plt.show()

