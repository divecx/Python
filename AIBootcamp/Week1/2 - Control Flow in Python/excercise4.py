# Program to Find the Largest Number in a List Using a For Loop

while True:
    # Meminta pengguna memasukkan daftar angka
    numbers = input("Enter numbers separated by spaces: ").split()

    try:
        # Mengonversi setiap elemen dalam daftar menjadi bilangan bulat
        numbers = [int(num) for num in numbers]
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        continue  # Kembali ke awal perulangan jika input tidak valid

    # Memastikan daftar tidak kosong
    if len(numbers) == 0:
        print("The list is empty. Please provide valid numbers.")
        continue  # Kembali ke awal perulangan jika daftar kosong

    # Jika input valid, keluar dari perulangan
    break

# Inisialisasi angka terbesar dengan elemen pertama dalam daftar
largest = numbers[0]

# Perulangan untuk membandingkan setiap elemen dalam daftar
for num in numbers:
    if num > largest:
        largest = num  # Update angka terbesar jika ditemukan angka yang lebih besar

# Menampilkan angka terbesar
print(f"The largest number in the list is: {largest}")
