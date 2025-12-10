# Contoh array (list) satu dimensi

buah = ["Apel", "Jeruk", "Mangga", "Pisang"]

print("Daftar Buah:")
print(buah)

# Mengakses elemen array
print("\nElemen pertama :", buah[0])
print("Elemen kedua   :", buah[1])

# Mengubah elemen array
buah[2] = "Anggur"
print("\nSetelah diubah:")
print(buah)

# Menambah elemen baru
buah.append("Melon")
print("\nSetelah menambah elemen:")
print(buah)

# Menghitung jumlah elemen
print("\nJumlah elemen dalam array:", len(buah))

#HASIL MODIFIKASI

# Program array (list) satu dimensi dengan input user

print("=== Program Array Buah ===")

# Membuat array kosong
buah = []

# Input jumlah data
jumlah = int(input("Masukkan jumlah buah yang ingin ditambahkan: "))

# Input elemen-elemen array
for i in range(jumlah):
    nama = input(f"Masukkan nama buah ke-{i+1}: ")
    buah.append(nama)

print("\nDaftar Buah:")
print(buah)

# Mengakses elemen array
if len(buah) >= 2:
    print("\nElemen pertama :", buah[0])
    print("Elemen kedua   :", buah[1])

# Mengubah elemen tertentu
index_ubah = int(input("\nMasukkan indeks buah yang ingin diubah (mulai dari 0): "))
if 0 <= index_ubah < len(buah):
    buah_baru = input("Masukkan nama buah baru: ")
    buah[i]()
