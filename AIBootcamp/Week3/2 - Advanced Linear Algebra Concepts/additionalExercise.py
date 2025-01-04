import numpy as np

# 1. Compute eigenvalues and eigenvectors for larger matrices

print("1. Eigenvalues and Eigenvectors")
A = np.random.rand(5, 5)  # Membuat matriks acak ukuran 5x5
eigenvalues, eigenvectors = np.linalg.eig(A)  # Menghitung eigenvalues dan eigenvectors

print("Matrix A:")
print(A)  # Menampilkan matriks A
print("\nEigenvalues:")
print(eigenvalues)  # Menampilkan eigenvalues (nilai eigen)
print("\nEigenvectors:")
print(eigenvectors)  # Menampilkan eigenvectors (vektor eigen)

#==========================================================

# 2. Use SVD to reduce the dimensionality of a dataset

print("\n2. Singular Value Decomposition (SVD)")
# Membuat dataset acak dengan lebih banyak baris daripada kolom (10x5)
dataset = np.random.rand(10, 5)
print("Original Dataset:")
print(dataset)  # Menampilkan dataset asli

# Melakukan SVD menggunakan NumPy
U, S, Vt = np.linalg.svd(dataset, full_matrices=False)
# Mengurangi dimensi dengan hanya menyimpan 2 singular value terbesar
k = 2  # Jumlah singular value yang dipertahankan
U_reduced = U[:, :k]  # Mengambil kolom pertama hingga ke-k dari U
S_reduced = np.diag(S[:k])  # Membuat matriks diagonal dari k singular value terbesar
Vt_reduced = Vt[:k, :]  # Mengambil baris pertama hingga ke-k dari V^T

# Dataset tereduksi adalah hasil perkalian U_reduced dan S_reduced
reduced_dataset = U_reduced @ S_reduced
print("\nReduced Dataset (Top 2 Singular Values):")
print(reduced_dataset)  # Menampilkan dataset dengan dimensi yang direduksi

#=========================================================

# 3. Verify the property of eigenvalues: det(A - λI) = 0

print("\n3. Verify Eigenvalue Property (det(A - λI) = 0)")
lambda_ = eigenvalues[0]  # Mengambil eigenvalue pertama untuk verifikasi
I = np.eye(A.shape[0])  # Membuat matriks identitas ukuran sama dengan A
A_minus_lambda_I = A - lambda_ * I  # Menghitung matriks A - λI

# Menghitung determinan matriks A - λI
determinant = np.linalg.det(A_minus_lambda_I)
print(f"\nSelected Eigenvalue (λ): {lambda_}")  # Menampilkan eigenvalue yang dipilih
print(f"Det(A - λI): {determinant} (Should be close to 0)")  # Menampilkan hasil determinan