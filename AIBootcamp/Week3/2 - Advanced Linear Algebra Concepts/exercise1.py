# Calculate Determinant and Inverse of a Matrix

import numpy as np

A = np.array([[2, 0, 4], [4, 5, 6], [7, 8, 9]])

determinant = np.linalg.det(A)

print("Determinant: \n", determinant)

if determinant != 0:
    inverse = np.linalg.inv(A)
    print("Inverse: \n", inverse)
else:
    print("Matrix is singular and does not have an inverse.")
