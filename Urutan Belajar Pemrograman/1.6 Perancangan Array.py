# Program Perancangan Array Sederhana

# Membuat array (list) berisi beberapa nilai
nilai = [80, 75, 90, 65, 85]

print("Isi array:")
print(nilai)

# Menampilkan elemen array satu per satu
print("\nMenampilkan elemen array:")
for i in range(len(nilai)):
    print(f"Index {i} = {nilai[i]}")

# Menambahkan elemen ke dalam array
nilai.append(95)
print("\nArray setelah ditambah satu nilai:")
print(nilai)

# Mengubah elemen array
nilai[2] = 100
print("\nArray setelah nilai index 2 diubah menjadi 100:")
print(nilai)

# Menghapus elemen dari array
nilai.remove(65)
print("\nArray setelah nilai 65 dihapus:")
print(nilai)

# Menampilkan jumlah elemen
print("\nJumlah elemen dalam array:", len(nilai))

#HASIL MODIFIKASI

# ==========================================================
#   PROGRAM PERANCANGAN ARRAY – DATA MAHASISWA (MODIFIKASI)
# ==========================================================

# Array berisi data mahasiswa
mahasiswa = [
    ["Andi", "231001", "Informatika", "FTI"],
    ["Budi", "231002", "Sistem Informasi", "FTI"],
    ["Cici", "231003", "Manajemen", "FEB"],
    ["Dinda", "231004", "Teknik Sipil", "FT"],
]

# -----------------------------
# Fungsi menampilkan data array
# -----------------------------
def tampilkan_data():
    print("\n=== DATA MAHASISWA ===")
    for i in range(len(mahasiswa)):
        print(f"\nIndex {i}:")
        print(f"  Nama     : {mahasiswa[i][0]}")
        print(f"  NIM      : {mahasiswa[i][1]}")
        print(f"  Prodi    : {mahasiswa[i][2]}")
        print(f"  Fakultas : {mahasiswa[i][3]}")
    print("\nTotal data:", len(mahasiswa))


# -----------------------
# Fungsi menambah data
# -----------------------
def tambah_data():
    print("\n=== TAMBAH DATA BARU ===")
    nama = input("Masukkan Nama     : ")
    nim = input("Masukkan NIM      : ")
    prodi = input("Masukkan Prodi    : ")
    fakultas = input("Masukkan Fakultas : ")

    mahasiswa.append([nama, nim, prodi, fakultas])
    print("\nData berhasil ditambahkan!")


# -----------------------
# Fungsi mengubah data
# -----------------------
def ubah_data():
    tampilkan_data()
    index = int(input("\nMasukkan index data yang ingin diubah: "))

    if 0 <= index < len(mahasiswa):
        print("\nMasukkan data baru:")
        mahasiswa[index][0] = input("Nama baru     : ")
        mahasiswa[index][1] = input("NIM baru      : ")
        mahasiswa[index][2] = input("Prodi baru    : ")
        mahasiswa[index][3] = input("Fakultas baru : ")

        print("\nData berhasil diubah!")
    else:
        print("Index tidak valid!")


# -----------------------
# Fungsi menghapus data
# -----------------------
def hapus_data():
    tampilkan_data()
    index = int(input("\nMasukkan index yang ingin dihapus: "))

    if 0 <= index < len(mahasiswa):
        mahasiswa.remove(mahasiswa[index])
        print("\nData berhasil dihapus!")
    else:
        print("Index tidak valid!")


# -----------------------
# Menu utama program
# -----------------------
while True:
    print("\n====================================")
    print("      PROGRAM PERANCANGAN ARRAY     ")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.")
