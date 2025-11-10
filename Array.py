#array
# Program array dua dimensi: data nilai siswa

# Membuat array 2D (list di dalam list)
nilai_siswa = [
    ["Reka", 81, 70, 85],
    ["Bayu", 85, 78, 92],
    ["Segara", 80, 95, 95],
    ["Cahya", 83, 92, 77]
]

# Menampilkan semua data
print("=== Data Nilai Siswa ===")
for data in nilai_siswa:
    print(f"Nama: {data[0]}, Nilai 1: {data[1]}, Nilai 2: {data[2]}, Nilai 3: {data[3]}")

# Menghitung rata-rata tiap siswa
print("\n=== Rata-Rata Nilai ===")
for data in nilai_siswa:
    nama = data[0]
    rata = (data[1] + data[2] + data[3]) / 3
    print(f"{nama}: {rata:.2f}")





# Membuat dictionary
my_dict = {'nama': 'naila', 'usia': 19, 'kota': 'polewali mandar'}

# Mengakses value berdasarkan key
print(my_dict['nama'])  # Output: naila

# Menambah pasangan key-value
my_dict['pekerjaan'] = 'mahasiswa'
print(my_dict)  # Output: {'nama': 'cyntia', 'usia': 19, 'kota': 'polewali mandar', 'pekerjaan': 'mahasiswa'
# Mengubah value
my_dict['usia'] = 19
print(my_dict)  # Output: {'nama': 'naila', 'usia': '19, 'kota': 'polewali mandar', 'pekerjaan': 'mahasiswa'}

# Menghapus pasangan
del my_dict['kota']
print(my_dict)  # Output: {'nama': 'naila', 'usia': 19, 'pekerjaan': 'mamasa'}

# Iterasi
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# nama: naila
# usia: 19
# pekerjaan: mahasiswa