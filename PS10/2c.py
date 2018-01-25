#Alex Karacaoglu
#2c

import numpy as np
import matplotlib.pyplot as plt
def generate_X():
    A = np.array([[4,1.5], [1.5,1]])
    return np.random.multivariate_normal([0, 0], A, size=500).T
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
empirical_cov = np.cov(X)
print empirical_cov
eigenvalues, V = np.linalg.eig(empirical_cov)
VT = V.T
print VT
decorrelated = VT.dot(X)
scatterplot(decorrelated)
plt.show()
