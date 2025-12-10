# Contoh array (list) tiga dimensi

array3D = [
    [   # Lapisan 1
        [1, 2, 3],
        [4, 5, 6]
    ],
    [   # Lapisan 2
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Isi Array 3 Dimensi:")
for lapisan in array3D:
    print(lapisan)

# Mengakses elemen tertentu
print("\nAkses Elemen:")
print("Elemen di lapisan 1, baris 2, kolom 3 =", array3D[0][1][2])  # 6
print("Elemen di lapisan 2, baris 1, kolom 1 =", array3D[1][0][0])  # 7

# Mengubah elemen
array3D[1][1][1] = 99  # ubah elemen di lapisan 2, baris 2, kolom 2

print("\nSetelah diubah (lapisan 2, baris 2, kolom 2 → 99):")
for lapisan in array3D:
    print(lapisan)

#HASIL MODIFIKASI

# Program Array 3 Dimensi dengan Input User

print("=== Program Array 3 Dimensi ===")

# Input ukuran array
lapisan = int(input("Masukkan jumlah lapisan : "))
baris = int(input("Masukkan jumlah baris    : "))
kolom = int(input("Masukkan jumlah kolom    : "))

# Membuat array 3D kosong
array3D = []

# Mengisi data array
print("\nMasukkan nilai array:")
for l in range(lapisan):
    layer = []
    for b in range(baris):
        row = []
        for k in range(kolom):
            nilai = int(input(f"Nilai untuk [Lapisan {l+1}][Baris {b+1}][Kolom {k+1}]: "))
            row.append(nilai)
        layer.append(row)
    array3D.append(layer)

# Menampilkan array 3 dimensi
print("\n=== Isi Array 3 Dimensi ===")
for l in range(lapisan):
    print(f"Lapisan {l+1}:")
    for b in range(baris):
        print(array3D[l][b])

# Mengakses elemen tertentu
print("\n=== Akses Elemen ===")
x = int(input("Masukkan lapisan yang ingin diakses : "))
y = int(input("Masukkan baris yang ingin diakses   : "))
z = int(input("Masukkan kolom yang ingin diakses   : "))

if 1 <= x <= lapisan and 1 <= y <= baris a
