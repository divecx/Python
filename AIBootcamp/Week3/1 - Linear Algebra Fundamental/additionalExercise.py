# 1. compute the determinant and inverse of a 
#2x2 matrix using numpy

import numpy as np

# Definisikan matriks 2x2
matrix = np.array([[4, 7],
                   [2, 6]])

# Hitung determinan
det = np.linalg.det(matrix)
print(f"Determinant of the matrix: {det}")

# Hitung invers jika determinan tidak nol
if det != 0:
    inverse = np.linalg.inv(matrix)
    print("Inverse of the matrix:")
    print(inverse)
else:
    print("Matrix is singular and does not have an inverse.")

# =====================================================

# 2. verify properties of matrix multiplication

# Definisikan dua matriks
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[2, 0],
              [1, 3]])

# Verifikasi properti distributif: A(B + C) = AB + AC
C = np.array([[0, 1],
              [4, 2]])
left_side = A @ (B + C)
right_side = A @ B + A @ C

print("\nVerifying distributive property:")
print("A(B + C):")
print(left_side)
print("AB + AC:")
print(right_side)
print("Distributive property holds:", np.array_equal(left_side, right_side))

# Verifikasi bahwa AB ≠ BA (perkalian matriks tidak komutatif secara umum)
AB = A @ B
BA = B @ A
print("\nMatrix Multiplication is Non-Commutative:")
print("AB:")
print(AB)
print("BA:")
print(BA)
print("AB equals BA:", np.array_equal(AB, BA))

# ==================================================

# 3. create a block diagonal matrix using numpy

# Definisikan beberapa blok matriks
block1 = np.array([[1, 2],
                   [3, 4]])
block2 = np.array([[5, 6],
                   [7, 8]])
block3 = np.array([[9]])

# Membuat matriks diagonal blok
block_diag_matrix = np.block([
    [block1, np.zeros((2, 2)), np.zeros((2, 1))],
    [np.zeros((2, 2)), block2, np.zeros((2, 1))],
    [np.zeros((1, 2)), np.zeros((1, 2)), block3]
])

print("\nBlock Diagonal Matrix:")
print(block_diag_matrix)
