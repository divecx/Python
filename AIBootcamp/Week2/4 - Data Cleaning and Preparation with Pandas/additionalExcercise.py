import pandas as pd
import numpy as np

# 1. Drop clumns with more than 50% missing values

# # Membuat DataFrame contoh dengan nilai yang hilang
# data = {
#     'A': [1, 2, np.nan, 4, 5],
#     'B': [np.nan, 2, 3, 4, np.nan],
#     'C': [1, np.nan, np.nan, np.nan, 5],
#     'D': [1, 2, 3, 4, 5]
# }
# df = pd.DataFrame(data)

# # Menghitung persentase nilai yang hilang di setiap kolom
# missing_percent = df.isnull().mean()

# # Debugging: Tampilkan persentase nilai yang hilang
# print("Persentase nilai yang hilang:\n", missing_percent)

# # Menghapus kolom dengan lebih dari 50% nilai yang hilang
# df_cleaned = df.loc[:, missing_percent <= 0.5]

# # Menampilkan hasil
# print("\nDataFrame asli:\n", df)
# print("\nDataFrame setelah menghapus kolom dengan >50% nilai yang hilang:\n", df_cleaned)

#============================================================

# 2. merge three datasets and analyze relationships 
#between them

# # Membuat tiga DataFrame contoh
# df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value1': [10, 20, 30]})
# df2 = pd.DataFrame({'ID': [2, 3, 4], 'Value2': [15, 25, 35]})
# df3 = pd.DataFrame({'ID': [1, 3, 4], 'Value3': [5, 10, 15]})

# # Menggabungkan DataFrame berdasarkan kolom 'ID'
# merged_df = pd.merge(df1, df2, on='ID', how='outer')
# merged_df = pd.merge(merged_df, df3, on='ID', how='outer')

# # Menampilkan hasil penggabungan
# print("\nDataFrame hasil penggabungan:\n", merged_df)

# # Analisis hubungan: Menghitung korelasi antar kolom
# correlation = merged_df.corr()

# print("\nKorelasi antar kolom:\n", correlation)


#===================================================

# 3. convert categorical data to numerical using
#one-hot encoding

# Membuat DataFrame dengan kolom kategoris
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'], 'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Menggunakan One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['Name', 'City'])

# Menampilkan hasil
print("\nDataFrame asli:\n", df)
print("\nDataFrame setelah One-Hot Encoding:\n", df_encoded)
