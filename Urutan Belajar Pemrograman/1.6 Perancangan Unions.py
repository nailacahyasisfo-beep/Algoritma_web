# Perancangan union sederhana
class UnionSederhana:
    def __init__(self):
        self.value = None      # hanya satu nilai aktif
        self.jenis = None      # menyimpan tipe data terakhir

    def set_int(self, angka):
        self.value = int(angka)
        self.jenis = "Integer"

    def set_float(self, angka):
        self.value = float(angka)
        self.jenis = "Float"

    def set_char(self, huruf):
        if len(huruf) == 1:
            self.value = huruf
            self.jenis = "Character"
        else:
            raise ValueError("Karakter harus 1 huruf!")

    def tampilkan(self):
        print("Jenis Data :", self.jenis)
        print("Nilai      :", self.value)
        print("------------------------")


# Menggunakan union
data = UnionSederhana()

data.set_int(25)
data.tampilkan()

data.set_float(3.14)
data.tampilkan()

data.set_char('A')
data.tampilkan()

#HASIL MODIFIKASI

# Perancangan union sederhana (versi modifikasi)
class UnionSederhana:
    def __init__(self):
        self.value = None      # hanya satu nilai aktif
        self.jenis = None      # tipe data terbaru

    def info_perubahan(self):
        print(f"[INFO] Nilai union diubah menjadi {self.jenis}\n")

    def set_int(self, angka):
        self.value = int(angka)
        self.jenis = "Integer"
        self.info_perubahan()

    def set_float(self, angka):
        self.value = float(angka)
        self.jenis = "Float"
        self.info_perubahan()

    def set_char(self, huruf):
        if len(huruf) == 1:
            self.value = huruf
            self.jenis = "Character"
            self.info_perubahan()
        else:
            raise ValueError("Karakter harus 1 huruf!")

    # Menampilkan isi union
    def tampilkan(self):
        print("Jenis Data :", self.jenis)
        print("Nilai      :", self.value)
        print("------------------------")

    # Mereset kembali union ke keadaan awal
    def reset(self):
        self.value = None
        self.jenis = None
        print("[RESET] Union kembali kosong.\n")


# Penggunaan union
data = UnionSederhana()

data.set_int(25)
data.tampilkan()

data.set_float(3.14)
data.tampilkan()

data.set_char('A')
data.tampilkan()

# Melakukan reset union
data.reset()
