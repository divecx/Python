import numpy as np

# 1. Create a 3d random array
#and compute statistics along specific axes

# # Membuat array 3D acak dengan ukuran (3, 4, 5) dan nilai antara 0 dan 100
# array_3d = np.random.rand(3, 4, 5) * 100

# # Menghitung rata-rata di sepanjang sumbu 0
# mean_axis_0 = np.mean(array_3d, axis=0)

# # Menghitung nilai maksimum di sepanjang sumbu 1
# max_axis_1 = np.max(array_3d, axis=1)

# # Menghitung nilai minimum di sepanjang sumbu 2
# min_axis_2 = np.min(array_3d, axis=2)

# # Menampilkan hasil
# print("Array 3D:\n", array_3d)
# print("\nRata-rata di sepanjang sumbu 0:\n", mean_axis_0)
# print("\nNilai maksimum di sepanjang sumbu 1:\n", max_axis_1)
# print("\nNilai minimum di sepanjang sumbu 2:\n", min_axis_2)

# ============================================================

# 2. write a program to generate a dataset
#of random floats and normalize the values between 0 and 1

# # Membuat dataset float acak dengan ukuran 50
# dataset = np.random.uniform(10.0, 100.0, size=50)

# # Menormalisasi dataset
# normalized_dataset = (dataset - np.min(dataset)) / (np.max(dataset) - np.min(dataset))

# # Menampilkan hasil
# print("\nDataset asli:\n", dataset)
# print("\nDataset setelah normalisasi:\n", normalized_dataset)

# ============================================================
# 3. implement conditional replacement to create
#a binary mask for values above a threshold

# Membuat array acak dengan nilai antara 0 dan 50
random_array = np.random.randint(0, 50, size=(5, 5))

# Menentukan threshold
threshold = 25

# Membuat mask biner: 1 untuk nilai di atas threshold, 0 untuk lainnya
binary_mask = np.where(random_array > threshold, 1, 0)

# Menampilkan hasil
print("\nArray asli:\n", random_array)
print("\nMask biner untuk nilai di atas threshold (25):\n", binary_mask)
