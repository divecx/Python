# Pythonic Code
# [expression for item in iterable if condition]

# Create a list of squares
squares = [x**2 for x in range(10)]
# print(squares)

# Filter Even Numbers
evens = [x for x in range(100) if x % 2 == 0]
# print(evens)

#===============================================#
# Lambda Functions
# lambda agruments: expression

add = lambda x, y: x + y
# print(add(3,5))

#===============================================#
# map() Applies a function to each item in an iterable

# numbers = [1, 2, 3, 4]

# squares = map(lambda x: x**2, numbers)
# print(list(squares))

# filter() filters items based on a condition
# numbers = [1, 2, 3, 4]
# evenList = filter(lambda x: x % 2 == 0, numbers)
# print(list(evenList))

# reduce() reduces an iterable to a single number
# from functools import reduce
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x,y: x * y, numbers)
# print(product)

#===============================================#
# Python os Module : provides functions to interact with the operating system
# import os

# print(os.getcwd())
# os.mkdir("test_dir")
# os.remove("file.txt")

# sys Module : provides access to tsystem-specific parameters and function
# import sys

# print(sys.argv)
# print(sys.version)
