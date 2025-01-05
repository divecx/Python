# Create and analyze random variables

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

# Discrete random variable: Dice roll
# outcomes = [1, 2, 3, 4, 5, 6]
# probabilities = [1/6] * 6
# plt.bar(outcomes, probabilities, color="blue", alpha=0.7)
# plt.title("PMF of a Dice Roll")
# plt.xlabel("Outcomes")
# plt.ylabel("Probability")
# plt.show()

# Continues random variable: uniform distribution 
x = np.linspace(0, 1, 10)
pdf = uniform.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, color="red")
plt.title("PDF of Uniform(0,1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()