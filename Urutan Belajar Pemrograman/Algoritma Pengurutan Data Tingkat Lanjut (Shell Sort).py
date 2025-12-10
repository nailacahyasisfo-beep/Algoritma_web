# Contoh Algoritma Shell Sort Sederhana

# Data awal
data = [12, 34, 54, 2, 3]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Shell Sort
n = len(data)
gap = n // 2     # langkah awal gap

while gap > 0:
    print(f"\nGap saat ini: {gap}")

    # Melakukan insertion sort dengan jarak (gap)
    for i in range(gap, n):
        temp = data[i]
        j = i

        # Pindah selama elemen sebelumnya lebih besar
        while j >= gap and data[j - gap] > temp:
            data[j] = data[j - gap]
            j -= gap

        data[j] = temp

    print("Hasil sementara:", data)

    # Mengurangi gap
    gap //= 2

print("\nData setelah diurutkan:")
print(data)

#HASIL MODIFIKASI

# Algoritma Shell Sort Sederhana (Modifikasi)

# Data awal
data = [12, 34, 54, 2, 3]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Shell Sort
n = len(data)
gap = n // 2     # langkah awal gap

iterasi = 1

while gap > 0:
    print(f"\n=== Gap {gap} ===")

    # Melakukan proses dengan jarak (gap)
    for i in range(gap, n):
        temp = data[i]
        j = i

        print(f"\nMemasukkan nilai {temp} pada posisi yang tepat...")

        # Pergerakan elemen dengan jarak gap
        while j >= gap and data[j - gap] > temp:
            print(f"  Geser {data[j - gap]} ke posisi {j}")
            data[j] = data[j - gap]
            j -= gap

        data[j] = temp
        print("  Hasil sementara:", data)

    print(f"Data setelah gap {gap}: {data}")
    gap //= 2   # perkecil gap

print("\n=== Data setelah diurutkan ===")
print(data)
