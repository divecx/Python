import numpy as np

# 1. Create a 4x4 matrix and calculate
#the sum of its rows and columns

# # Membuat matriks 4x4 dengan nilai acak antara 1 hingga 10
# matrix = np.random.randint(1, 11, size=(4, 4))

# # Menghitung jumlah setiap baris
# row_sums = np.sum(matrix, axis=1)

# # Menghitung jumlah setiap kolom
# col_sums = np.sum(matrix, axis=0)

# # Menampilkan hasil
# print("Matriks 4x4:\n", matrix)
# print("Jumlah setiap baris:", row_sums)
# print("Jumlah setiap kolom:", col_sums)

# ==========================================

# 2. Write a program to normalize
#an array (scale values between 0 and 1)
# # Membuat array acak
# array = np.random.randint(10, 100, size=10)

# # Menormalisasi array
# normalized_array = (array - np.min(array)) / (np.max(array) - np.min(array))

# # Menampilkan hasil
# print("\nArray asli:", array)
# print("Array setelah normalisasi:", normalized_array)

#===============================================

# 3. Generate a random array and find the
#minimum and maximum values
# Menghasilkan array acak dengan 20 elemen
random_array = np.random.rand(20)

# Menemukan nilai minimum dan maksimum
min_value = np.min(random_array)
max_value = np.max(random_array)

# Menampilkan hasil
print("\nArray acak:", random_array)
print("Nilai minimum:", min_value)
print("Nilai maksimum:", max_value)
