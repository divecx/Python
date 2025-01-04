import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, hessian, lambdify

# 1. Use sympy to compute second-order
#derivatives (Hessian matrix)

x, y = symbols('x y')
# Mendefinisikan fungsi kuadrat
f = x**2 + y**2 + 3*x*y - 4*x - 2*y + 5

# Menghitung gradien dan matriks Hessian
grad_f = [diff(f, var) for var in (x, y)]
hessian_f = hessian(f, (x, y))
print("Gradien:", grad_f)
print("Matriks Hessian:")
print(hessian_f)

# Mengonversi fungsi dan gradien menjadi fungsi yang dapat dipanggil
grad_f_func = lambdify((x, y), grad_f)
f_func = lambdify((x, y), f)

#======================================================

# 2. Implement gradient descent with multiple learning
#rates and compare convergence speed

def gradient_descent(start_point, learning_rate, max_iter=50, tol=1e-6):
    point = np.array(start_point, dtype=float)
    history = [point.copy()]

    for _ in range(max_iter):
        grad = np.array(grad_f_func(*point), dtype=float)
        new_point = point - learning_rate * grad
        history.append(new_point.copy())

        # Mengecek konvergensi
        if np.linalg.norm(new_point - point) < tol:
            break

        point = new_point

    return np.array(history)

# Titik awal dan berbagai learning rate
start = [2, 2]
learning_rates = [0.01, 0.1, 0.5]

# Menjalankan gradient descent untuk setiap learning rate
histories = {lr: gradient_descent(start, lr) for lr in learning_rates}

# ======================================================

# 3. Visualize the gradient descent process 
#on a quadratic function 

x_vals = np.linspace(-3, 3, 100)
y_vals = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_func(X, Y)

plt.figure(figsize=(12, 8))
plt.contour(X, Y, Z, levels=50, cmap='viridis')

# Plot jalur untuk setiap learning rate
for lr, history in histories.items():
    plt.plot(history[:, 0], history[:, 1], marker='o', label=f'LR = {lr}')
    plt.scatter(history[-1, 0], history[-1, 1], label=f'Konvergen (LR = {lr})', s=100)

plt.title("Gradient Descent pada Fungsi Kuadrat")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()