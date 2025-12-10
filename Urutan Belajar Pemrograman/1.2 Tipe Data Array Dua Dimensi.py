# Contoh array (list) dua dimensi

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Isi Array 2 Dimensi:")
for baris in matriks:
    print(baris)

# Mengakses elemen tertentu
print("\nElemen di baris 1 kolom 2 :", matriks[0][1])  # 2
print("Elemen di baris 3 kolom 1 :", matriks[2][0])  # 7

# Mengubah elemen
matriks[1][1] = 99
print("\nSetelah diubah (baris 2 kolom 2 menjadi 99):")
for baris in matriks:
    print(baris)

#HASIL MODIFIKASI

# Program array (list) dua dimensi dengan input user

print("=== Program Array 2 Dimensi ===")

# Input jumlah baris dan kolom
baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("Masukkan jumlah kolom : "))

# Membuat matriks kosong
matriks = []

# Input nilai matriks
print("\nMasukkan elemen-elemen matriks:")
for i in range(baris):
    row = []
    for j in range(kolom):
        nilai = int(input(f"Masukkan nilai untuk baris {i+1}, kolom {j+1}: "))
        row.append(nilai)
    matriks.append(row)

# Menampilkan matriks
print("\nIsi Matriks:")
for r in matriks:
    print(r)

# Mengakses elemen tertentu
print("\n=== Akses Elemen ===")
x = int(input("Masukkan baris yang ingin diakses (mulai dari 1): "))
y = int(input("Masukkan kolom yang ingin diakses (mulai dari 1): "))

if 1 <= x <= baris and 1 <= y <= kolom:
    print("Nilai pada posisi tersebut adalah:", matriks[x-1][y-1])
else:
    print("Posisi tidak valid!")

# Mengubah elemen tertentu
print("\n=== Ubah Elemen Matriks ===")
u_baris = int(input("Masukkan baris yang ingin diubah: "))
u_kolom = int(input("Masukkan kolom yang ingin diubah: "))

if 1 <= u_baris <= baris and 1 <= u_kolom <= kolom:
    nilai_baru = int(input("Masukkan nilai baru: "))
    matriks[u_baris-1][u_kolom-1] = nilai_baru
else:
    print("Posisi tidak valid!")

# Menampilkan matriks setelah diubah
print("\nMatriks Setelah Diubah:")
for r in matriks:
    print(r)
