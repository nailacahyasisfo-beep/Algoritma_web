# Contoh Algoritma Insertion Sort

# Data awal
data = [8, 3, 5, 2, 9]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Insertion Sort
for i in range(1, len(data)):
    key = data[i]      # elemen yang akan ditempatkan
    j = i - 1

    print(f"\nMemasukkan {key} ke posisi yang tepat")

    # Geser elemen yang lebih besar ke kanan
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    # Tempatkan elemen (key) di posisi yang benar
    data[j + 1] = key

    print("Hasil sementara:", data)

print("\nData setelah diurutkan:")
print(data)


#HASIL MODIFIKASI

# Modifikasi Algoritma Insertion Sort

# Data awal
data = [8, 3, 5, 2, 9]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Insertion Sort
for i in range(1, len(data)):
    key = data[i]       
    j = i - 1

    print(f"\nIterasi ke-{i}")
    print(f"Key yang dipilih : {key}")

    # Geser elemen yang lebih besar ke kanan
    while j >= 0 and data[j] > key:
        print(f"  {data[j]} lebih besar dari {key}, geser ke kanan")
        data[j + 1] = data[j]
        j -= 1

    # Tempatkan elemen key pada posisi yang tepat
    data[j + 1] = key

    print("Hasil sementara :", data)

print("\nData setelah diurutkan:")
print(data)
