# Contoh penggunaan tipe data float

nilai1 = 3.14
nilai2 = 2.5
nilai3 = -7.8   # float juga bisa bernilai negatif

print("Nilai 1 :", nilai1)
print("Nilai 2 :", nilai2)
print("Nilai 3 :", nilai3)

# Operasi aritmatika sederhana
jumlah = nilai1 + nilai2
selisih = nilai2 - nilai1
perkalian = nilai1 * nilai3
pembagian = nilai1 / nilai2   # pembagian float

print("\nHasil Operasi:")
print("Jumlah       :", jumlah)
print("Selisih      :", selisih)
print("Perkalian    :", perkalian)
print("Pembagian    :", pembagian)

#HASIL MODIFIKASI

# Program sederhana penggunaan tipe data float

print("=== Program Operasi Float ===")

# Input float dari user
a = float(input("Masukkan nilai pertama : "))
b = float(input("Masukkan nilai kedua   : "))

print("\nNilai yang dimasukkan:")
print("Nilai 1 :", a)
print("Nilai 2 :", b)

# Operasi aritmatika
jumlah = a + b
selisih = a - b
perkalian = a * b

# Menghindari pembagian dengan nol
if b != 0:
    pembagian = a / b
else:
    pembagian = "Tidak bisa membagi dengan nol!"

print("\n=== Hasil Operasi ===")
print("Penjumlahan :", jumlah)
print("Selisih     :", selisih)
print("Perkalian   :", perkalian)
print("Pembagian   :", pembagian)
