# Simulasi konsep UNION dalam Python

class UnionData:
    def __init__(self):
        self.value = None   # hanya satu nilai aktif

    def set_int(self, angka):
        self.value = int(angka)

    def set_float(self, number):
        self.value = float(number)

    def set_char(self, huruf):
        if len(huruf) == 1:
            self.value = huruf
        else:
            raise ValueError("Char harus 1 karakter saja.")

    def get_value(self):
        return self.value


# Menggunakan "union"
data = UnionData()

data.set_int(10)
print("Nilai sebagai int   :", data.get_value())

data.set_float(3.14)
print("Nilai sebagai float :", data.get_value())

data.set_char('A')
print("Nilai sebagai char  :", data.get_value())

#HASIL MODIFIKASI

# Simulasi konsep UNION dalam Python (Modifikasi)

class UnionData:
    def __init__(self):
        self.value = None       # nilai yang aktif
        self.active_type = None # tipe data yang sedang aktif

    def set_int(self, angka):
        self.value = int(angka)
        self.active_type = "Integer"

    def set_float(self, number):
        self.value = float(number)
        self.active_type = "Float"

    def set_char(self, huruf):
        if len(huruf) == 1:
            self.value = huruf
            self.active_type = "Char"
        else:
            raise ValueError("Char harus 1 karakter saja.")

    def reset(self):
        self.value = None
        self.active_type = None

    def get_value(self):
        return self.value

    def get_type(self):
        return self.active_type


# ===============================
# Contoh penggunaan UNION
# ===============================

data = UnionData()

data.set_int(10)
print("Nilai       :", data.get_value())
print("Tipe aktif  :", data.get_type())
print()

data.set_float(6.28)
print("Nilai       :", data.get_value())
print("Tipe aktif  :", data.get_type())
print()

data.set_char('Z')
print("Nilai       :", data.get_value())
print("Tipe aktif  :", data.get_type())
print()

# Reset union
data.reset()
print("Setelah reset -> Nilai:", data.get_value(), ", Tipe:", data.get_type())
