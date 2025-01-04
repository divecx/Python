# Probability basics
#     - conditional probability
#         the probability of event A given that event B has occurred
#         P(A|B) = P(A n B)/P(B)
#     - Bayes' Theorem
#         P(A|B) = P(B|A)P(A)/P(B)
#             P(A): Prior probability
#             P(B|A): Likelihood
#             P(B): Evidence

def bayes_theorem(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

# Common probability distribustions

import numpy as np
import matplotlib.pyplot as plt

# Gaussian (Normal) Distribution: bell-shaped curve with mean (miu) and standard deviation
# mu, sigma = 0, 1
# x = np.linspace(-4, 4, 100)
# y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# plt.plot(x, y)
# plt.title("Gaussian Distribution")
# plt.show()

# Bernoulli Distribution: describes outcomes of a binary experiment
# p = 0.6
# plt.bar([0, 1], [1-p, p], color="blue")
# plt.title("Bernoulli Distribution")
# plt.xticks([0, 1], labels=["0 (Failure)", "1 (Success)"])
# plt.show()

# Binomial Distribution: models the number of successes in n independent Bernoulli trials
from scipy.stats import binom

# n, p = 10, 0.5
# x = np.arange(0, n+1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y, color="green")
# plt.title("Binomial Distribution")
# plt.show()

# Poisson Distribution: models the number of events in a fixed interval of time or space
from scipy.stats import poisson

# lam = 3
# x = np.arange(0, 10)
# y = poisson.pmf(x, lam)
# plt.bar(x, y, color="orange")
# plt.title("Poisson Distribution")
# plt.show()

#=====================================================
# Application in Machine Learning

# 1. Gaussian Distribution
#     - used in gaussian naive bayes and kernel density estimation
# 2. Bernoulli Distribution
#     - models binary classification problems
# 3. Binomial Distribution
#     - used in logistic regression to model binary outcomes
# 4. Poisson Distribution
#     - models count data