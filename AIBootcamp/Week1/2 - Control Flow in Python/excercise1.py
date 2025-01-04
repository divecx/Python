# Exercise 2: Check if a Number is Prime

# Meminta input angka dari pengguna
num = int(input("Enter a number: "))

# Memeriksa apakah angka lebih besar dari 1 (hanya angka > 1 yang bisa jadi bilangan prima)
if num > 1:
    # Perulangan untuk mencari faktor dari 2 hingga akar kuadrat dari angka
    for i in range(2, int(num**0.5) + 1):
        # Jika ditemukan pembagi, angka bukan bilangan prima
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        # Jika tidak ada pembagi ditemukan, angka adalah bilangan prima
        print(f"{num} is a prime number")
else:
    # Jika angka kurang dari atau sama dengan 1, bukan bilangan prima
    print(f"{num} is not a prime number")
