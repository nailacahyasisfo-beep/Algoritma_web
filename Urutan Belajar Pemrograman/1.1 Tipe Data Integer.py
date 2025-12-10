# Contoh penggunaan tipe data integer

angka1 = 10
angka2 = 25
angka3 = -7   # integer juga bisa bernilai negatif

print("Angka 1 :", angka1)
print("Angka 2 :", angka2)
print("Angka 3 :", angka3)

# Operasi aritmatika sederhana
jumlah = angka1 + angka2
selisih = angka2 - angka1
perkalian = angka1 * angka3
pembagian = angka2 // angka1   # pembagian bulat (integer division)

print("\nHasil Operasi:")
print("Jumlah       :", jumlah)
print("Selisih      :", selisih)
print("Perkalian    :", perkalian)
print("Pembagian    :", pembagian)

#HASIL MODIFIKASI

# Program sederhana untuk penggunaan tipe data integer

print("=== Program Operasi Integer ===")

# Input integer dari user
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua   : "))

print("\nAngka yang dimasukkan:")
print("Angka 1 :", a)
print("Angka 2 :", b)

# Operasi aritmatika
jumlah = a + b
selisih = a - b
perkalian = a * b

# Menghindari pembagian oleh nol
if b != 0:
    pembagian = a // b
else:
    pembagian = "Tidak bisa membagi dengan nol!"

print("\n=== Hasil Operasi ===")
print("Penjumlahan :", jumlah)
print("Selisih     :", selisih)
print("Perkalian   :", perkalian)
print("Pembagian   :", pembagian)
