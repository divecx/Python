# string_operations.py

# Fungsi untuk membalik sebuah string
def reverse_string(s):
    return s[::-1]

# Fungsi untuk menghitung jumlah huruf vokal dalam sebuah string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Fungsi untuk memeriksa apakah sebuah string adalah palindrom
def is_palindrome(s):
    # Menghilangkan karakter non-alfanumerik dan menjadikan huruf kecil
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
