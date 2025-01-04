# Menu-Driven Calculator Program

# Fungsi untuk operasi penjumlahan
def add(a, b):
    return a + b

# Fungsi untuk operasi pengurangan
def subtract(a, b):
    return a - b

# Fungsi untuk operasi perkalian
def multiply(a, b):
    return a * b

# Fungsi untuk operasi pembagian
def divide(a, b):
    if b != 0:
        return a / b  # Jika pembagi tidak nol, lakukan pembagian
    else:
        return "Division by zero is not allowed"  # Jika pembagi nol, kembalikan pesan error

# Perulangan utama program (looping menu)
while True:
    # Menampilkan menu pilihan ke pengguna
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    # Meminta pengguna memilih operasi
    choice = input("Enter your choice (1-5): ")
    
    # Jika pengguna memilih opsi keluar (5)
    if choice == "5":
        print("Exiting Program. Goodbye!")
        break  # Menghentikan perulangan dan keluar dari program
    
    # Validasi jika pilihan tidak valid
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please select a valid option (1-5).")
        continue  # Kembali ke awal perulangan untuk meminta pilihan lagi
    
    # Meminta input angka dari pengguna
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue  # Kembali ke awal perulangan jika input tidak valid
    
    # Menjalankan operasi berdasarkan pilihan pengguna
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))  # Memanggil fungsi divide untuk pembagian
