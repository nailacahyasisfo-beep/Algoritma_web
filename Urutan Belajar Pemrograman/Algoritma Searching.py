# Algoritma Linear Search dalam Python

def linear_search(data, target):
    print("Mencari:", target)
    for i in range(len(data)):
        print(f"Memeriksa indeks {i} -> {data[i]}")
        if data[i] == target:
            return i   # mengembalikan posisi jika ditemukan
    return -1          # -1 berarti tidak ditemukan


# Contoh data
angka = [12, 7, 25, 30, 18, 50]

# Data yang ingin dicari
dicari = 30

# Proses pencarian
hasil = linear_search(angka, dicari)

# Menampilkan hasil
print("\nHasil Pencarian:")
if hasil != -1:
    print(f"Angka {dicari} ditemukan pada indeks ke-{hasil}.")
else:
    print(f"Angka {dicari} TIDAK ditemukan dalam list.")


#HASIL MODIFIKASI

# Algoritma Linear Search versi modifikasi
def linear_search(data, target):
    langkah = 0   # menghitung jumlah langkah

    print("=== Proses Pencarian ===")
    print("Mencari nilai:", target, "\n")

    for i in range(len(data)):
        langkah += 1
        print(f"Langkah {langkah}: Memeriksa indeks {i} -> {data[i]}")

        if data[i] == target:
            print("\nData ditemukan!")
            return i, langkah   # kembalikan indeks & jumlah langkah

    print("\nData tidak ditemukan!")
    return -1, langkah          # jika tidak ada


# Contoh data
angka = [12, 7, 25, 30, 18, 50]

# Input target yang ingin dicari
dicari = 30

# Proses pencarian
posisi, langkah_total = linear_search(angka, dicari)

# Menampilkan hasil
print("\n=== Hasil Akhir ===")
print("List data:", angka)
print("Target    :", dicari)
print("Langkah   :", langkah_total)

if posisi != -1:
    print(f"Hasil     : Ditemukan pada indeks ke-{posisi}")
else:
    print("Hasil     : TIDAK ditemukan dalam list")
