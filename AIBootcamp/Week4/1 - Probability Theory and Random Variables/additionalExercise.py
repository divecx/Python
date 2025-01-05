import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# 1. Simulate flipping a coin 10,000 times and calculate probabilities of heads/tails
coin_flips = np.random.choice(['Heads', 'Tails'], size=10000, p=[0.5, 0.5])
P_heads = np.sum(coin_flips == 'Heads') / len(coin_flips)
P_tails = np.sum(coin_flips == 'Tails') / len(coin_flips)

print("1. Coin Flip Simulation")
print(f"P(Heads): {P_heads}")
print(f"P(Tails): {P_tails}")

# 2. Compute the expectation and variance of a weighted die
# Weighted probabilities for a die
weighted_probs = [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]
die_faces = np.array([1, 2, 3, 4, 5, 6])

# Expectation and variance
expectation = np.sum(die_faces * weighted_probs)
variance = np.sum(weighted_probs * (die_faces - expectation) ** 2)

print("\n2. Weighted Die")
print(f"Expectation: {expectation}")
print(f"Variance: {variance}")

# 3. Explore other distributions
# Normal Distribution
x = np.linspace(-4, 4, 1000)
normal_pdf = norm.pdf(x, loc=0, scale=1)

# Binomial Distribution
n, p = 10, 0.5  # 10 trials, probability of success = 0.5
binomial_x = np.arange(0, n + 1)
binomial_pmf = binom.pmf(binomial_x, n, p)

# Plot the distributions
plt.figure(figsize=(12, 6))

# Normal Distribution Plot
plt.subplot(1, 2, 1)
plt.plot(x, normal_pdf, color="blue")
plt.title("Normal Distribution (μ=0, σ=1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

# Binomial Distribution Plot
plt.subplot(1, 2, 2)
plt.bar(binomial_x, binomial_pmf, color="green", alpha=0.7)
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("Number of Successes")
plt.ylabel("P(X=x)")
plt.grid(True)

plt.tight_layout()
plt.show()

# Penjelasan
# Simulasi Flipping a Coin:

# Menggunakan np.random.choice untuk melakukan simulasi flipping coin dengan 10,000 percobaan.
# Probabilitas kepala (P_heads) dan ekor (P_tails) dihitung berdasarkan jumlah hasil masing-masing.
# Expectation dan Variance of a Weighted Die:

# Menggunakan daftar probabilitas berbobot untuk setiap sisi dadu.
# Ekspektasi dihitung menggunakan rumus ∑P(x)⋅x.
# Variansi dihitung menggunakan rumus ∑P(x)⋅(x−μ)^2, dimana μ adalah ekspektasi.

# Distribusi Lainnya:
# Distribusi Normal: Menggunakan scipy.stats.norm.pdf untuk menghitung fungsi kepadatan probabilitas (PDF).
# Distribusi Binomial: Menggunakan scipy.stats.binom.pmf untuk menghitung fungsi massa probabilitas (PMF) dari distribusi binomial.
# Hasil distribusi diplot menggunakan Matplotlib.