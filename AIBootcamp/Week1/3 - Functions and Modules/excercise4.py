# Create module for string operation, 
# including functions to reverse a string, count vowels, 
# and check for palindromes. Import it into a script and test the functions

# test_string_operations.py

# Mengimpor modul custom
import string_operations

# Menguji fungsi reverse_string
string_to_reverse = "hello"
reversed_string = string_operations.reverse_string(string_to_reverse)
print(f"Original String: {string_to_reverse}")
print(f"Reversed String: {reversed_string}")

# Menguji fungsi count_vowels
string_for_vowel_count = "This is a test string."
vowel_count = string_operations.count_vowels(string_for_vowel_count)
print(f"String: '{string_for_vowel_count}'")
print(f"Number of Vowels: {vowel_count}")

# Menguji fungsi is_palindrome
string_to_check = "A man, a plan, a canal, Panama"
is_palindrome = string_operations.is_palindrome(string_to_check)
print(f"String: '{string_to_check}'")
print(f"Is palindrome: {is_palindrome}")
