# Contoh konsep struktur menggunakan class

class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

# Membuat objek (data mahasiswa)
mhs1 = Mahasiswa("Andi", "2023001", 19)

# Menampilkan data
print("Data Mahasiswa:")
print("Nama :", mhs1.nama)
print("NIM  :", mhs1.nim)
print("Umur :", mhs1.umur)

#HASIL MODIFIKASI

# Program konsep struktur menggunakan class

class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

print("=== Program Data Mahasiswa ===")

# Input data mahasiswa dari user
nama = input("Masukkan nama mahasiswa : ")
nim = input("Masukkan NIM mahasiswa  : ")
umur = int(input("Masukkan umur mahasiswa : "))

# Membuat objek
mhs = Mahasiswa(nama, nim, umur)

# Menampilkan data mahasiswa
print("\n=== Data Mahasiswa ===")
print("Nama :", mhs.nama)
print("NIM  :", mhs.nim)
print("Umur :", mhs.umur)
