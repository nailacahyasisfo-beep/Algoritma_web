class ContohStatik:
    # Variabel statis (dimiliki semua objek)
    hitung_objek = 0

    def __init__(self, nama):
        self.nama = nama
        ContohStatik.hitung_objek += 1   # setiap objek dibuat, nilai static bertambah


# Membuat objek
obj1 = ContohStatik("A")
obj2 = ContohStatik("B")
obj3 = ContohStatik("C")

# Menampilkan nilai variabel statis
print("Jumlah objek yang dibuat:", ContohStatik.hitung_objek)

#HASIL MODIFIKASI

class ContohStatik:
    # Variabel statis (dimiliki oleh semua objek)
    hitung_objek = 0

    def __init__(self, nama):
        self.nama = nama
        ContohStatik.hitung_objek += 1   # setiap objek dibuat, nilai static bertambah

    def info(self):
        print(f"Nama objek : {self.nama}")
        print(f"Total objek (static) : {ContohStatik.hitung_objek}")
        print("--------------------------")


# Membuat objek
obj1 = ContohStatik("Objek Pertama")
obj2 = ContohStatik("Objek Kedua")
obj3 = ContohStatik("Objek Ketiga")

# Menampilkan info tiap objek
obj1.info()
obj2.info()
obj3.info()

# Menampilkan nilai variabel statis langsung dari class
print("Jumlah total objek yang dibuat:", ContohStatik.hitung_objek)
