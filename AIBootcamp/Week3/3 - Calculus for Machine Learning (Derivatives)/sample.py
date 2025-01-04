# Derivatives and Their Role in Optimization
#   - measures the rate at which a function changes with respect to its input
#   - for a function f(x), the deravtive f'(x) indicates the slope of the tangent line at a point x
#   - common derivatives
#       for f(x) = x^2, f'(x) = 2x
#       for f(x) = sin(x), f'(x) = cos(x)

import sympy as sp

x = sp.Symbol('x')
f = x**2
derivative1 = sp.diff(f, x)

y = sp.Symbol('y')
h = sp.cos(y)
derivative2 = sp.diff(h, y)

print("Derivative1: ", derivative1)
print("Derivative2: ", derivative2)

# Partial Derivatives
#     - measures how a function changes with respect to one variable while keeping other variables constant
#     - for f(x, y) = x^2 + y^2, partial derivatives are:
#             af/ax = 2x, af/ay = 2y
# Gradients
#     - vector of all partial derivatives, indicating the direction of the steepestt ascent
#     - for f(x,y) = x^2 + y^2, the gradient is:
#               m  = [[af/ax],[af/ay]] = [2x, 2y]

x, y = sp.symbols('x y')
f = x**2 + y**2
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Partial Derivatives: ", grad_x, grad_y )

# Gradient Descent Optimization Algorithm
#     - iterative optimization algorithm used to minimize a function
#     - updates parameters in the direction of the negative gradient to find the minimun
#     - update rule:  θ =  θ-α∇f(θ)
#          θ: parameters of the model 
#          α: learning rate (step size)
