import numpy as np

# Matrix operation

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition: \n", A + B)
print("Subtraction: \n",B - A)

C = 2 * A
print("Scalar Multiplication: \n", C)

# Matrix Multipication
# Formula: (A . B)ij = Σk Aik Bkj

result = np.dot(A, B)
print("Matrix Multiplication: \n", result)

# Special Matrices
# Identity Matrix (I)
# I.A = A

I = np.eye(3)
print("Identity Matrix: \n", I)

# Zero Matrix (0)
Z =  np.zeros((2, 3))
print("Zero Matrix: \n", Z)

# Diagonal Matrix
D = np.diag([1, 2, 3])
print("Diagonal Matrix: \n", D)