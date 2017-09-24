import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
 
neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
transfer = np.zeros((9, 9))
for k in range(9):
    for neigh in range(4): transfer[neighbor[k][neigh], k] += 0.25

def dot_pow(matrix, times):
    return reduce(np.dot, [matrix]*times)

N_tras = range(1, 100, 10)
eigs1 = []
eigs2 = []
for n in N_tras:
    eigenvalues, eigenvectors = np.linalg.eig(dot_pow(transfer, n))
    eigenvalues = eigenvalues.real
    eigenvalues.sort()
    print(eigenvalues)
    eigs1.append(eigenvalues)

plt.figure()
plt.plot( N_tras, eigs1)
# plt.plot( N_tras, eigs2, "b--" )
# plt.legend()
plt.show()
# eigenvalues, eigenvectors = np.linalg.eig(transfer)
# print(eigenvalues)
#
# you may print(the eigenvectors by uncommenting the following lines...
#for iter in range(9):
#    print(eigenvalues[iter]
#    for i in range(9):
#       print(eigenvectors[i][iter]

