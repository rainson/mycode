import numpy as np
from functools import reduce
import matplotlib.pylab as plt

epsilon = 0.01
transfer = [[ epsilon, 1.0 - epsilon ],
            [ 1.0 - epsilon, epsilon ]]


def dot_pow(matrix, times):
    return reduce(np.dot, [matrix]*times)

N_tras = range(1, 1000, 1)
eigs1 = []
eigs2 = []
for n in N_tras:
    eigenvalues, eigenvectors = np.linalg.eig(dot_pow(transfer, n))
    print(eigenvalues)
    eigs1.append(eigenvalues[0])
    eigs2.append(eigenvalues[1])

plt.figure()
plt.plot( N_tras, eigs1, "r--")
plt.plot( N_tras, eigs2, "b--" )
plt.show()

print(eigenvalues)
 
# you may print(the eigenvectors by uncommenting the following lines...
#for iter in range(2):
#    print(eigenvalues[iter]
#    for i in range(2):
#       print(eigenvectors[i][iter]

