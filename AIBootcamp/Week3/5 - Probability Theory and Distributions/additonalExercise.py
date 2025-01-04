import numpy as np
import matplotlib.pyplot as plt

# 1. Create and visualize a multinominal distribution for multi-class data

# Probabilitas untuk tiga kelas
probabilities = [0.5, 0.3, 0.2]
n_trials = 1000
n_samples = 500

# Sampling dari distribusi multinomial
multinomial_samples = np.random.multinomial(n_trials, probabilities, size=n_samples)

# Visualisasi distribusi multinomial
plt.figure(figsize=(10, 6))
plt.bar(range(multinomial_samples.shape[1]), np.mean(multinomial_samples, axis=0), color='blue', alpha=0.7)
plt.xticks(range(len(probabilities)), [f"Class {i+1}" for i in range(len(probabilities))])
plt.title("Distribusi Multinomial untuk Data Multi-Kelas")
plt.xlabel("Kelas")
plt.ylabel("Frekuensi Rata-rata")
plt.show()

#=================================================

# 2. Compare Gaussian and uniform distributios for continous data

# Gaussian distribution
mean, std_dev = 0, 1
gaussian_data = np.random.normal(mean, std_dev, size=1000)

# Uniform distribution
low, high = -2, 2
uniform_data = np.random.uniform(low, high, size=1000)

# Visualisasi distribusi Gaussian dan Uniform
plt.figure(figsize=(10, 6))
plt.hist(gaussian_data, bins=30, alpha=0.7, label="Gaussian", color="blue", density=True)
plt.hist(uniform_data, bins=30, alpha=0.7, label="Uniform", color="green", density=True)
plt.title("Perbandingan Distribusi Gaussian dan Uniform")
plt.xlabel("Nilai")
plt.ylabel("Kepadatan")
plt.legend()
plt.show()

#===================================================

# 3. Use probability distributions to simulate and analyze real-world datasets

# Contoh simulasi data waktu kedatangan pelanggan
arrival_rate = 2  # Rata-rata 2 pelanggan per satuan waktu (distribusi Poisson)
simulation_time = 100  # Total waktu simulasi
customer_arrivals = np.random.poisson(arrival_rate, size=simulation_time)

# Contoh simulasi data skor ujian siswa (Gaussian)
mean_score = 75
std_dev_score = 10
n_students = 500
exam_scores = np.random.normal(mean_score, std_dev_score, size=n_students)

# Visualisasi dataset simulasi
plt.figure(figsize=(12, 6))

# Plot waktu kedatangan pelanggan
plt.subplot(1, 2, 1)
plt.bar(range(simulation_time), customer_arrivals, color='purple', alpha=0.7)
plt.title("Simulasi Kedatangan Pelanggan")
plt.xlabel("Waktu")
plt.ylabel("Jumlah Pelanggan")

# Plot skor ujian siswa
plt.subplot(1, 2, 2)
plt.hist(exam_scores, bins=20, color='orange', alpha=0.7, density=True)
plt.title("Distribusi Skor Ujian Siswa")
plt.xlabel("Skor")
plt.ylabel("Kepadatan")

plt.tight_layout()
plt.show()


# Penjelasan Program
# Distribusi Multinomial:

# Digunakan untuk data multi-kelas di mana setiap sampel dialokasikan ke satu dari beberapa kelas berdasarkan probabilitas.
# Frekuensi rata-rata dihitung dari beberapa pengambilan sampel.
# Distribusi Gaussian vs Uniform:

# Gaussian (Normal): Data terdistribusi di sekitar mean dengan penyebaran yang diatur oleh standar deviasi.
# Uniform: Data tersebar secara merata antara batas atas dan bawah.
# Histogram membandingkan kedua distribusi ini.
# Simulasi Dataset Dunia Nyata:

# Distribusi Poisson: Digunakan untuk memodelkan jumlah kedatangan pelanggan dalam satuan waktu.
# Distribusi Gaussian: Digunakan untuk memodelkan skor ujian siswa.
# Kedua simulasi ini divisualisasikan menggunakan histogram atau grafik batang.





