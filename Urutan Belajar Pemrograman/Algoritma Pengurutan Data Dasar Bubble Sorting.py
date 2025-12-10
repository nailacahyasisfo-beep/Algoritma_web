# Contoh Algoritma Bubble Sort Sederhana

# Data awal
data = [5, 2, 9, 1, 7]

print("Data sebelum diurutkan:")
print(data)

# Algoritma Bubble Sort
n = len(data)
for i in range(n - 1):
    for j in range(n - i - 1):
        if data[j] > data[j + 1]:
            # Tukar posisi
            data[j], data[j + 1] = data[j + 1], data[j]

print("Data setelah diurutkan:")
print(data)


#HASIL MODIFIKASI

# Modifikasi Algoritma Bubble Sort

# Input data dari user
data = []
jumlah = int(input("Masukkan jumlah data: "))

for i in range(jumlah):
    nilai = int(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

print("\nData sebelum diurutkan:")
print(data)

# Algoritma Bubble Sort
n = len(data)
for i in range(n - 1):
    print(f"\n--- Iterasi ke-{i+1} ---")
    for j in range(n - i - 1):
        print(f"Membandingkan {data[j]} dan {data[j+1]}")
        if data[j] > data[j + 1]:
            print("  → Tukar posisi")
            data[j], data[j + 1] = data[j + 1], data[j]
        else:
            print("  → Tidak ditukar")
    print("Hasil sementara:", data)

print("\nData setelah diurutkan:")
print(data)
