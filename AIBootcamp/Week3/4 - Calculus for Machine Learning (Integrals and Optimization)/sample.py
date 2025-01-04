# Integrals and their application in ML 
#     - integrals: compute area under a curve, representing accumulation
#     - the definite integral of f(x) from a to b:
#             a∫b f(x) dx
#     - application in ML 
#             - probability distributions
#             - cost functions

import sympy as sp

x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2))
indefinite_integral = sp.integrate(f, x)

print("Definite Integral :", definite_integral)
print("Indefinite Integral :", indefinite_integral)

# Optimization Concepts
#     - local minimum
#     - global minimum
#     - convecx functions: ensure that any local minimum also a global minimum
#     - non-convex function in ML: most neural network loss function

# Stochastic Gradient Descent (SGD) and Its Variants
#     - optimization algorithm that uses random subsets (mini-batches) of the data to compute gradients and update parameters
#     - variants SGD: mini-batch sgd, momoentum, adam optimizer
