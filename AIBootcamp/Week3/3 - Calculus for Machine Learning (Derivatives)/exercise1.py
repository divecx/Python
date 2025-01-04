# Compute derivatives of basic functions

import sympy as sp

# Define a function
x = sp.Symbol('x')
f = x**3 - 5*x + 7

# Compute derivative
derivative = sp.diff(f, x)

print("Function: ", f)
print("Derivative: ", derivative)