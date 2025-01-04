# Reading and Writing Text Files 

# 1. Opening Files 
# Use the built-in open() function to open a file 
# r|w|a|r+

# 2. Reading Files 
# .read()|.readline()|.readlines()

# 3. Writing to files 
# .write()|.writelines()

# with open("sample.txt", "r") as file:
#     # content = file.read()
#     # print(content)
    
#     file.write("Hello, World!")
#     file.writelines(["ALice", "Bob", "Cherry"])

# Using "with" statement for file management
# File is automatically close


# Basic Exception Handling for File Operations
# try-except Blocks
# common file handling exception: FileNotFoundError, PermissionError, IOError
try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File Not Found!")