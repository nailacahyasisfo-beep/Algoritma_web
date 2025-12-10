# Algoritma Merge Sort Sederhana

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2   # titik tengah
        kiri = data[:mid]      # bagian kiri
        kanan = data[mid:]     # bagian kanan

        print("Membagi:", data)
        
        # Rekursif: pecah kedua bagian
        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0

        # Menggabungkan kembali dua bagian
        print("Menggabungkan:", kiri, "dan", kanan)

        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        # Jika masih ada sisa elemen kiri
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        # Jika masih ada sisa elemen kanan
        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

        print("Hasil sementara:", data)


# Data awal
data = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum diurutkan:")
print(data)

# Proses merge sort
merge_sort(data)

print("\nData setelah diurutkan:")
print(data)

#HASIL MODIFIKASI

# Algoritma Merge Sort (Versi Modifikasi)

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2    # cari titik tengah
        kiri = data[:mid]       # bagian kiri
        kanan = data[mid:]      # bagian kanan

        print(f"\nMembagi  : {data}")
        print(f" -> Kiri  : {kiri}")
        print(f" -> Kanan : {kanan}")

        # Rekursif untuk membagi lagi
        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0

        # Proses menggabungkan dua bagian
        print(f"Menggabungkan {kiri} + {kanan}")

        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        # Tambahkan sisa elemen dari kiri
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        # Tambahkan sisa elemen dari kanan
        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

        print("Hasil sementara:", data)


# Data awal
data = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum diurutkan:")
print(data)

# Proses merge sort
merge_sort(data)

print("\nData setelah diurutkan:")
print(data)
