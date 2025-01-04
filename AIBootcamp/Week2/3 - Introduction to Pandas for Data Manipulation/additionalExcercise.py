import pandas as pd

# 1. Load a local excel file and 
#explore its structure

# # Memuat file Excel lokal (ganti 'file.xlsx' dengan nama file yang Anda miliki)
# file_path = "test.xlsx"
# excel_data = pd.read_excel(file_path)

# # Menampilkan beberapa baris pertama
# print("Data dari file Excel:\n", excel_data.head())

# # Menampilkan informasi tentang struktur data
# print("\nInformasi struktur data:\n")
# print(excel_data.info())

# # Menampilkan ringkasan statistik deskriptif
# print("\nStatistik deskriptif:\n")
# print(excel_data.describe())

#==========================================================

# 2. Create a DataFrame form a dictionary
#and add a new calculated column

# Membuat DataFrame dari dictionary
data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Nilai1': [85, 90, 78],
    'Nilai2': [88, 76, 95]
}

df = pd.DataFrame(data)

# Menambahkan kolom baru yang berisi rata-rata nilai
df['Rata-rata'] = (df['Nilai1'] + df['Nilai2']) / 2

# Menampilkan DataFrame
print("\nDataFrame dengan kolom tambahan:\n", df)

#========================================================

# 3. Save filtered data to a new CSV file

# Memfilter data berdasarkan kondisi (contoh: rata-rata lebih dari 80)
filtered_data = df[df['Rata-rata'] > 80]

# Menyimpan data terfilter ke file CSV baru
filtered_data.to_csv('filtered_data.csv', index=False)

# Menampilkan pesan sukses
print("\nData terfilter telah disimpan ke 'filtered_data.csv'.")
