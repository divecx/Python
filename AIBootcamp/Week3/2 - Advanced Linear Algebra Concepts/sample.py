# Determinants and Inverse of a Matrix 

import numpy as np

# 1. Determinants
#     - scalar value that provides information about a matrix's properties
#     - only for square matrices
#     - det(A) = 0, the matrix A is singular
#     - det(A)! = 0, is invertible
#     - Geomatric interpretation
#         - for a 2x2 matrix, the determinant represents the scalling factor of the area formed by its column vectors
#     - formula for 2x2 matrix: 
#         det([[a, b], [c, d]]) = ad - bc

A = np.array([[2, 3], [1, 4]])
determinant = np.linalg.det(A)

print("Determinant: ", determinant)

# 2. inverse of a matrix
#     - denoted as A^-1
#     - product of a matrix and its inverse is the identity matrix: AxA^-1 = I 
#     - matrix is invertible only if det(A) ≠ 0
#     - formula for 2x2 2x2 matrix:
#         A^-1 = 1/det(A) ([[d, -b], [-c, a]])

inverse = np.linalg.inv(A)
print("Inverse of A: \n", inverse)

# 3. Eigenvalues and Eigenvectors
#     - If A . v = λ . v, then
#         - v is an elgenvector
#         - λ is the eigenvalue
#     - Geometric interpretation
#         - eigenvectors point in the direction where the matrix transformation streches or compresses vector
#         - eigenvalues indicate the factor of stretching of compression
#     - Properties
#         - Matrix of size n x n has n n eigenvalues and eigenvectors
#         - eigenvalues can be real or complex
#         - for a symmetric matrix, eigenvalues are always real

eigenValues, eigenVectors = np.linalg.eig(A)
# print("EigentVal: \n", eigenValues)
# print("EigentVectors: \n", eigenVectors)

B = np.array([[4, 2], [1, 1]])
eigval, eigvec = np.linalg.eig(B)
print("EigVal: \n", eigval)
print("EigVec: \n", eigvec)

# 4. Introduction to Matrix Decompositon
#         - process of breaking a m;atrix into simpler components to analyze or solve problems
#     - Singular Value Decomposition (SVD)
#         - SVD decomposes a matrix A A into three matrices: A = U . Σ . V^T 
#             U: Left singular vectors (orthogonal matrix)
#             Σ: Diagonal matrix of singular values (non-negative)
#             V^T: Right singular vectors (orthogonal matrix)

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)