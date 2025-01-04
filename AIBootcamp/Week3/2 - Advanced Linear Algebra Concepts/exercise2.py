# Compute Eigenvalues and Eigenvectors

import numpy as np

A = np.array([[4, -2], [1, 1]])

eigval, eigvec = np.linalg.eig(A)

print("EigValues: ", eigval)
print("EigVectors: \n", eigvec)