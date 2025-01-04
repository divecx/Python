# # Example 1: Checking a condition
# num = 27
# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative Number")
    
# # Example 2: Nested conditions
# age = 18 
# if age > 18:
#     if age < 30:
#         print("Young Adult")
#     else:
#         print("Adult")

# #=======================================#

# # Example 3: Syntax for for-loop
# for item in sequence:
#     #Code block

# # Loop through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
    
# # Loop with range
# for i in range(5): #[0,1,2,3,4]
#     print(i)

# # Example 4: Syntax while loop
# while condition:
#     #Code block

# # Count down from 5
# count = 5
# while count > 0:
#     print(count)
#     count -= 1 # count = count -1 
# print("Outside while loop")

# #=======================================#

# # Example 4: Break for Control FLow (terminates the loop prematurely when a condition is met)
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
    
# print("Break")
    
# # Example 4: Continue for Control FLow (skips the current iteration and proceeds to the next) 
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
    
# print("Outside for loop")

# # Example 5
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)