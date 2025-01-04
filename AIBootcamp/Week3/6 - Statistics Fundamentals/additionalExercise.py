import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Visualize the distribution of data and highlight mean, median, and mode using Matplotlib

# Contoh data
np.random.seed(0)
data = np.random.normal(loc=50, scale=10, size=1000)

# Menghitung mean, median, dan modus
mean = np.mean(data)
median = np.median(data)

# Mengakses modus dengan benar
mode_result = stats.mode(data, keepdims=True)  # Gunakan keepdims untuk menjaga bentuk array
mode = mode_result.mode[0]  # Ambil nilai modus

# Visualisasi histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black', density=True)
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median:.2f}')
plt.axvline(mode, color='orange', linestyle='dashed', linewidth=2, label=f'Mode: {mode:.2f}')
plt.title('Distribusi Data dengan Mean, Median, dan Modus')
plt.xlabel('Nilai')
plt.ylabel('Kepadatan')
plt.legend()
plt.grid(True)
plt.show()

#=================================================

# 2. Perform hypothesis testing on real-world dataset (e.g., comparing exam scores of two groups)

# Mengunduh dataset dari GitHub
import urllib.request
import pandas as pd

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
filename = 'tips.csv'
urllib.request.urlretrieve(url, filename)

# Membaca dataset
data = pd.read_csv(filename)

# Misalkan kita ingin membandingkan total_bill antara pelanggan pria dan wanita
male_bills = data[data['sex'] == 'Male']['total_bill']
female_bills = data[data['sex'] == 'Female']['total_bill']

# Uji t independen
t_stat, p_value = stats.ttest_ind(male_bills, female_bills)

print(f'Uji t: Statistik t = {t_stat:.4f}, p-value = {p_value:.4f}')

#=========================================================

# 3. Calculate confidence intervals for proportions in a dataset

# Misalkan kita ingin menghitung interval kepercayaan 95% untuk proporsi pelanggan yang memberikan tip lebih dari 5 dolar
n = len(data)
x = np.sum(data['tip'] > 5)
p_hat = x / n

# Interval kepercayaan menggunakan distribusi normal
z = stats.norm.ppf(0.975)  # untuk 95% CI
se = np.sqrt((p_hat * (1 - p_hat)) / n)
ci_lower = p_hat - z * se
ci_upper = p_hat + z * se

print(f'Proporsi pelanggan yang memberikan tip > $5: {p_hat:.4f}')
print(f'Interval kepercayaan 95%: ({ci_lower:.4f}, {ci_upper:.4f})')