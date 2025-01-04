import pandas as pd

# 1. create a dataset of sales data and group
#it by region or product category

# Membuat dataset penjualan
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product_Category': ['A', 'B', 'A', 'B', 'B', 'A', 'B', 'A'],
    'Year': [2022, 2022, 2023, 2023, 2022, 2023, 2022, 2023],
    'Sales': [1500, 2000, 1800, 2200, 1700, 1900, 2100, 2300]
}
df = pd.DataFrame(data)

# Mengelompokkan berdasarkan Region
grouped_by_region = df.groupby('Region').sum()

# Mengelompokkan berdasarkan Product_Category
grouped_by_category = df.groupby('Product_Category').sum()

# Menampilkan hasil pengelompokan
print("Data asli:\n", df)
print("\nTotal penjualan per Region:\n", grouped_by_region)
print("\nTotal penjualan per Product_Category:\n", grouped_by_category)

#========================================================

# 2. use pivot_table to calculate total sales
#per region and per year

# Membuat pivot table
pivot_table = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Year',
    aggfunc='sum',
    fill_value=0
)

# Menampilkan pivot table
print("\nPivot Table: Total penjualan per Region dan per Tahun:\n", pivot_table)


#==================================================

# 3. create a custom aggregation function to calculate
#the vaiance for each group

# Fungsi untuk menghitung varians
def calculate_variance(group):
    return group.var()

# Mengelompokkan data berdasarkan Region dan menghitung varians penjualan
variance_by_region = df.groupby('Region')['Sales'].agg(calculate_variance)

# Mengelompokkan data berdasarkan Product_Category dan menghitung varians penjualan
variance_by_category = df.groupby('Product_Category')['Sales'].agg(calculate_variance)

# Menampilkan hasil varians
print("\nVarians penjualan per Region:\n", variance_by_region)
print("\nVarians penjualan per Product_Category:\n", variance_by_category)
