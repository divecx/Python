import numpy as np

arr = np.array([1,2,3,4])
# print(arr)

zeroes = np.zeros((3,3))
# print(zeroes)

ones = np.ones((2,4))
# print(ones)

range_array = np.arange(1, 100, 3)
# print(range_array)

linspace_array = np.linspace(0, 10, 4)
# print(linspace_array)

#============================================
# matriks
import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshape = arr.reshape((3,3))
# print(reshape)

# arr = np.array([1, 2, 3])
# expanded = arr[:, np.newaxis]
# print(expanded)

#===========================================
# Basic operation on arrays
import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# arr = np.array([4, 16, 25])

# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))

#==============================================
# array indexing, slicing, and reshaping
import numpy as np

#indexing
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])

#slicing
print(arr[1:4])
print(arr[:3])
print(arr[3:])

# reshaping
reshaped = arr.reshape(2,3)
print(reshaped)

