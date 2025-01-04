# # # Defining Functions with def

# # def function_name(parameters):
# #     #Code block
# #     return result

# #=======================================#

# # Function with parameters and return value
# def add_numbers():
#     return a + b

# result = add_numbers(10, 3)
# print("Sum: ", result)

# #=======================================#

# # Scope and Lifetime of Variables

# # Local Scope
# def greet():
#     message = "Hello World"
#     print(message)
    
# greet()
# # print(message) # akan eror jika digunakan karena message adalah local scope variable

# # Global Scope
# greeting = "Hi!"

# def say_hello():
#     print(greeting + " from inside the function")

# say_hello()
# print(greeting + " from outside the function")

# #=======================================#

# # Importing and Using Modules

# Import an entire module
# import math
# print("From an entire module, result: ", math.sqrt(16))

# # Import specific functions
# from math import sqrt
# print("From specific function, result: ",  sqrt(16))

# # Using aliases
# import math as m  
# print("From use aliases, result: ", m.sqrt(16))

# Creating Custom Modules

