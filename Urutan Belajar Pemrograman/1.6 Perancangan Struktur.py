# Perancangan struktur sederhana untuk data barang
class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

# Membuat objek (data barang)
barang1 = Barang("BRG001", "Pulpen", 3000)
barang2 = Barang("BRG002", "Buku Tulis", 5000)

# Menampilkan data
print("Data Barang 1:")
print("Kode  :", barang1.kode)
print("Nama  :", barang1.nama)
print("Harga :", barang1.harga)

print("\nData Barang 2:")
print("Kode  :", barang2.kode)
print("Nama  :", barang2.nama)
print("Harga :", barang2.harga)

#HASIL MODIFIKASI

# Perancangan struktur sederhana untuk data barang
class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    # Method untuk menampilkan data barang
    def tampilkan(self):
        print("Kode  :", self.kode)
        print("Nama  :", self.nama)
        print("Harga :", self.harga)
        print("------------------------")

    # Method untuk mengubah harga barang
    def ubah_harga(self, harga_baru):
        self.harga = harga_baru


# Membuat objek (data barang)
barang1 = Barang("BRG001", "Pulpen", 3000)
barang2 = Barang("BRG002", "Buku Tulis", 5000)

print("Data Barang Awal:")
barang1.tampilkan()
barang2.tampilkan()

# Mengubah harga salah satu barang
barang1.ubah_harga(4000)

print("Setelah Harga Pulpen Diubah:")
barang1.tampilkan()
