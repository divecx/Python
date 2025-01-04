import numpy as np
import matplotlib.pyplot as plt

# 1. Visualize the loss function's surface and the SGD optimization path

# # Fungsi loss: f(x, y) = x^2 + y^2
# def loss_function(x, y):
#     return x**2 + y**2

# # Gradien dari fungsi loss
# def gradient(x, y):
#     return np.array([2*x, 2*y])

# # Implementasi SGD
# def sgd(start, learning_rate, iterations):
#     path = [start]
#     point = np.array(start, dtype=float)
#     for _ in range(iterations):
#         grad = gradient(*point)
#         point -= learning_rate * grad
#         path.append(point.copy())
#     return np.array(path)

# # Visualisasi permukaan fungsi loss
# x_vals = np.linspace(-3, 3, 100)
# y_vals = np.linspace(-3, 3, 100)
# X, Y = np.meshgrid(x_vals, y_vals)
# Z = loss_function(X, Y)

# # Jalur optimisasi
# start = [2, 2]
# learning_rate = 0.1
# iterations = 50
# path = sgd(start, learning_rate, iterations)

# plt.figure(figsize=(10, 8))
# plt.contour(X, Y, Z, levels=50, cmap='viridis')
# plt.plot(path[:, 0], path[:, 1], 'ro-', label='Jalur SGD')
# plt.scatter(0, 0, color='black', label='Minimum', s=100)
# plt.title("Visualisasi Jalur Optimisasi SGD")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

#===========================================================

# 2. Implement Mini-Batch SGD and compare it with vanilla SGD

# Dataset sederhana
np.random.seed(42)
data_x = np.linspace(-5, 5, 100)
data_y = 2 * data_x + 3 + np.random.normal(0, 1, size=data_x.shape)

# Mini-Batch SGD
def mini_batch_sgd(x, y, learning_rate, batch_size, epochs):
    m = len(x)
    weights = np.random.rand()
    bias = np.random.rand()
    losses = []

    for _ in range(epochs):
        indices = np.random.permutation(m)
        x, y = x[indices], y[indices]
        for i in range(0, m, batch_size):
            x_batch = x[i:i+batch_size]
            y_batch = y[i:i+batch_size]

            y_pred = weights * x_batch + bias
            grad_w = -2 * np.sum((y_batch - y_pred) * x_batch) / len(x_batch)
            grad_b = -2 * np.sum(y_batch - y_pred) / len(x_batch)

            weights -= learning_rate * grad_w
            bias -= learning_rate * grad_b

        # Hitung loss untuk seluruh dataset
        y_pred_all = weights * x + bias
        losses.append(np.mean((y - y_pred_all)**2))

    return weights, bias, losses

# Jalankan Mini-Batch SGD
batch_size = 10
epochs = 100
learning_rate = 0.01
_, _, mini_batch_losses = mini_batch_sgd(data_x, data_y, learning_rate, batch_size, epochs)

# Vanilla SGD (batch size sama dengan seluruh dataset)
_, _, vanilla_losses = mini_batch_sgd(data_x, data_y, learning_rate, len(data_x), epochs)

# Plot Kurva Loss
plt.figure(figsize=(10, 6))
plt.plot(mini_batch_losses, label="Mini-Batch SGD")
plt.plot(vanilla_losses, label="Vanilla SGD")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Perbandingan Mini-Batch SGD vs Vanilla SGD")
plt.legend()
plt.show()

#=====================================================

# 3. Use Adam optimizer for a more complex dataset

# Implementasi manual Adam optimizer pada dataset sederhana
def adam_optimizer(x, y, learning_rate, epochs):
    m = len(x)
    weights = np.random.rand()
    bias = np.random.rand()
    losses = []

    # Parameter Adam
    beta1 = 0.9
    beta2 = 0.999
    epsilon = 1e-8
    m_w, m_b = 0, 0
    v_w, v_b = 0, 0

    for t in range(1, epochs + 1):
        indices = np.random.permutation(m)
        x, y = x[indices], y[indices]
        grad_w_total, grad_b_total = 0, 0

        for i in range(m):
            x_i = x[i]
            y_i = y[i]
            y_pred = weights * x_i + bias
            grad_w = -2 * (y_i - y_pred) * x_i
            grad_b = -2 * (y_i - y_pred)

            grad_w_total += grad_w
            grad_b_total += grad_b

        grad_w_total /= m
        grad_b_total /= m

        # Update m dan v
        m_w = beta1 * m_w + (1 - beta1) * grad_w_total
        m_b = beta1 * m_b + (1 - beta1) * grad_b_total
        v_w = beta2 * v_w + (1 - beta2) * (grad_w_total**2)
        v_b = beta2 * v_b + (1 - beta2) * (grad_b_total**2)

        # Bias correction
        m_w_hat = m_w / (1 - beta1**t)
        m_b_hat = m_b / (1 - beta1**t)
        v_w_hat = v_w / (1 - beta2**t)
        v_b_hat = v_b / (1 - beta2**t)

        # Update parameter
        weights -= learning_rate * m_w_hat / (np.sqrt(v_w_hat) + epsilon)
        bias -= learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)

        # Hitung loss
        y_pred_all = weights * x + bias
        losses.append(np.mean((y - y_pred_all)**2))

    return weights, bias, losses

# Jalankan Adam optimizer
epochs = 100
learning_rate = 0.01
_, _, adam_losses = adam_optimizer(data_x, data_y, learning_rate, epochs)

# Plot kurva loss
plt.figure(figsize=(10, 6))
plt.plot(adam_losses, label="Adam Optimizer")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss Menggunakan Adam Optimizer")
plt.legend()
plt.show()
