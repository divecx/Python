#1. write a program to reverse a list
#and remove duplicate using a set

# # Fungsi untuk membalik list dan menghapus duplikat
# def reverse_and_remove_duplicates(input_list):
#     # Menggunakan set untuk menghapus elemen duplikat
#     unique_items = set(input_list)
#     # Mengembalikan list yang dibalik
#     return list(unique_items)[::-1]

# # Contoh daftar (list) awal
# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# # Memanggil fungsi untuk memproses list
# result_list = reverse_and_remove_duplicates(original_list)

# # Menampilkan hasil
# print("List asli:", original_list)  # Menampilkan list asli
# print("List hasil (dibalik & tanpa duplikat):", result_list)  # Menampilkan list hasil

# ====================================== #

#2. create a program that stores student grades
#in dictionary and calculates the average grade

# Membuat dictionary untuk menyimpan nama siswa dan nilainya
student_grades = {}

# Memasukkan data siswa dan nilai
print("Masukkan data siswa dan nilai (ketik 'selesai' untuk berhenti):")
while True:
    # Meminta input nama siswa
    name = input("Nama siswa: ")
    if name.lower() == 'selesai':
        break
    try:
        # Meminta input nilai siswa
        grade = float(input(f"Nilai {name}: "))
        # Menambahkan ke dictionary
        student_grades[name] = grade
    except ValueError:
        print("Nilai harus berupa angka. Coba lagi.")

# Menampilkan data siswa dan nilai
print("\nData siswa dan nilai:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

# Menghitung rata-rata nilai
if student_grades:  # Mengecek apakah ada data siswa
    average_grade = sum(student_grades.values()) / len(student_grades)
    print(f"\nRata-rata nilai: {average_grade:.2f}")
else:
    print("\nTidak ada data siswa yang dimasukkan.")