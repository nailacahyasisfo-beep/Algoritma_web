# Contoh Algoritma Selection Sort

# Data awal
data = [25, 10, 5, 30, 15]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Selection Sort
n = len(data)
for i in range(n - 1):
    # Anggap indeks i adalah nilai terkecil
    min_index = i
    
    # Mencari nilai terkecil di sisa array
    for j in range(i + 1, n):
        if data[j] < data[min_index]:
            min_index = j
    
    # Tukar posisi jika ditemukan nilai lebih kecil
    data[i], data[min_index] = data[min_index], data[i]
    
    print(f"Iterasi ke-{i+1}: {data}")

print("\nData setelah diurutkan:")
print(data)


#HASIL MODIFIKASI

# Algoritma Selection Sort (Versi Modifikasi)

# Data awal
data = [25, 10, 5, 30, 15]

print("Data sebelum diurutkan:")
print(data)
print("----------------------------------")

# Algoritma Selection Sort
n = len(data)
for i in range(n - 1):
    min_index = i
    print(f"\nIterasi ke-{i+1}:")
    print(f"Mulai dari indeks {i}, nilai awal minimum = {data[min_index]}")

    # Mencari nilai terkecil di sisa list
    for j in range(i + 1, n):
        print(f"  Membandingkan dengan {data[j]}")
        if data[j] < data[min_index]:
            min_index = j
            print(f"  -> Nilai minimum baru ditemukan: {data[min_index]} (indeks {min_index})")

    # Tukar posisi jika perlu
    if min_index != i:
        print(f"Menukar {data[i]} dengan {data[min_index]}")
        data[i], data[min_index] = data[min_index], data[i]
    else:
        print("Tidak ada pertukaran (nilai sudah minimum).")

    print("Hasil sementara:", data)

print("\n----------------------------------")
print("Data setelah diurutkan:")
print(data)
