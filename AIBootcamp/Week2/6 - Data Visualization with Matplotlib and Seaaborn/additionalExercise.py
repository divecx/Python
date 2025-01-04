# 1. create a histogram with multiple datasets overlaid

import matplotlib.pyplot as plt
import numpy as np

# Membuat dua dataset
data1 = np.random.normal(50, 10, 1000)  # Dataset 1
data2 = np.random.normal(60, 15, 1000)  # Dataset 2

# Membuat histogram
plt.hist(data1, bins=30, alpha=0.5, label='Dataset 1', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Dataset 2', color='orange')

# Menambahkan label, judul, dan legenda
plt.title('Histogram with Overlaid Datasets')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Menampilkan plot
plt.show()

#=====================================================

# 2. use seaborn to create a violin plot or 
#box plot for visualizing distributions

import seaborn as sns
import pandas as pd

# Membuat DataFrame contoh
data = {
    'Category': ['A'] * 50 + ['B'] * 50,
    'Values': np.random.normal(50, 10, 50).tolist() + np.random.normal(60, 15, 50).tolist()
}
df = pd.DataFrame(data)

# Membuat Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='Category', y='Values', data=df)
plt.title('Violin Plot of Distributions')
plt.show()

# Membuat Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Values', data=df)
plt.title('Box Plot of Distributions')
plt.show()

#==================================================

# 3. combine multiple plots in a single
#figure using Matplotlib's subplot

# Membuat dataset untuk plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Membuat subplot
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Plot pertama
ax[0, 0].plot(x, y1, label='sin(x)', color='blue')
ax[0, 0].set_title('Plot 1: sin(x)')
ax[0, 0].legend()

# Plot kedua
ax[0, 1].plot(x, y2, label='cos(x)', color='orange')
ax[0, 1].set_title('Plot 2: cos(x)')
ax[0, 1].legend()

# Plot ketiga
ax[1, 0].scatter(x, y1, color='blue', label='sin(x) scatter')
ax[1, 0].set_title('Plot 3: Scatter sin(x)')
ax[1, 0].legend()

# Plot keempat
ax[1, 1].hist(y1, bins=20, color='green', alpha=0.7, label='sin(x) hist')
ax[1, 1].set_title('Plot 4: Histogram sin(x)')
ax[1, 1].legend()

# Menambahkan layout yang rapi
plt.tight_layout()

# Menampilkan plot
plt.show()
