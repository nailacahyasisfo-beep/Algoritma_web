# Algoritma Quick Sort Sederhana

def quick_sort(data):
    if len(data) <= 1:
        return data  # sudah terurut jika 1 elemen

    pivot = data[0]  # pilih elemen pertama sebagai pivot
    kiri = [x for x in data[1:] if x <= pivot]   # elemen ≤ pivot
    kanan = [x for x in data[1:] if x > pivot]   # elemen > pivot

    print(f"Pivot: {pivot} | Kiri: {kiri} | Kanan: {kanan}")

    # rekursif untuk mengurutkan kiri dan kanan
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)


# Data awal
data = [25, 10, 5, 30, 15]

print("Data sebelum diurutkan:")
print(data)

# Proses Quick Sort
hasil = quick_sort(data)

print("\nData setelah diurutkan:")
print(hasil)

#HASIL MODIFIKASI

# Algoritma Quick Sort (Versi Modifikasi)

def quick_sort(data, depth=0):
    indent = "  " * depth   # indentation untuk melihat level rekursi

    if len(data) <= 1:
        print(f"{indent}Return (sudah terurut): {data}")
        return data

    pivot = data[0]  # memilih pivot
    kiri = [x for x in data[1:] if x <= pivot]
    kanan = [x for x in data[1:] if x > pivot]

    print(f"{indent}Data   : {data}")
    print(f"{indent}Pivot  : {pivot}")
    print(f"{indent}Kiri   : {kiri}")
    print(f"{indent}Kanan  : {kanan}\n")

    # rekursif (dengan depth ditambah)
    hasil_kiri = quick_sort(kiri, depth + 1)
    hasil_kanan = quick_sort(kanan, depth + 1)

    # gabungkan hasilnya
    gabungan = hasil_kiri + [pivot] + hasil_kanan
    print(f"{indent}Gabung : {gabungan}")

    return gabungan


# Data awal
data = [25, 10, 5, 30, 15]

print("Data sebelum diurutkan:")
print(data)

# Proses Quick Sort
print("\nProses Quick Sort:")
hasil = quick_sort(data)

print("\nData setelah diurutkan:")
print(hasil)
