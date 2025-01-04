# Program to Calculate the Factorial of a Number Using a While Loop

while True:
    # Meminta input bilangan dari pengguna
    try:
        num = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue  # Kembali ke awal perulangan jika input tidak valid
    
    # Validasi input: Faktorial hanya didefinisikan untuk bilangan non-negatif
    if num < 0:
        print("Factorial is not defined for negative numbers. Please try again.")
    else:
        break  # Keluar dari perulangan jika input valid

# Inisialisasi hasil faktorial dan variabel pengendali perulangan
factorial = 1
i = num

# Menampilkan langkah perhitungan
print(f"Calculating {num}!:")

while i > 0:
    print(f"{i}", end="")  # Menampilkan nilai i
    factorial *= i         # Kalikan hasil faktorial dengan nilai i
    i -= 1                 # Kurangi i dengan 1 pada setiap iterasi

    if i > 0:
        print(" * ", end="")  # Tambahkan simbol perkalian jika masih ada angka berikutnya
    else:
        print(" = ", end="")  # Tambahkan simbol '=' di akhir

# Menampilkan hasil faktorial
print(factorial)
