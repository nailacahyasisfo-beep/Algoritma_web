#PERBEDAAN TUPLE DENGAN LIST

#Tuple dan list adalah tipe data sekuens yang menyimpan kumpulan item yang berurutan
#Tuple bersifat tidak dapat diubah (immutable), sehingga cocok untuk data yang tetap dan heterogen
#List bersifat dapat diubah (mutable) dan ideal untuk data yang dinamis dan homogen
#Penggunaan tuple bisa lebihh eksplisit dan mudah dibaca
#List () dapat mengkonversi literable apa pun menjadi sebuah daftar

#Contoh Tuple
data_mahasiswa = ("Naila", 19, "Sistem Informasi")
#Menampilkan semua isi Tuple
print("Data Mahasiswa:", data_mahasiswa)
#Mengakses elemen Tuple
print("Nama:", data_mahasiswa[0])
print("Umur:", data_mahasiswa[1])
print("Program Studi:", data_mahasiswa[2])
#Mencoba mengubah isi tuple (akan error karena tuple immutable)
#data_mahasiswa[1] = 21  # Jika dijalankan akan menghasilkan error
# Menghitung jumlah elemen dalam tuple
print("Jumlah elemen:", len(data_mahasiswa))

#CONTOH LIST
data_mahasiswa = ["Naila", 19, "Sistem Informasi"]
# Menampilkan semua isi list
print("Data Mahasiswa:", data_mahasiswa)
# Mengakses elemen list
print("Nama:", data_mahasiswa[0])
print("Umur:", data_mahasiswa[1])
print("Program Studi:", data_mahasiswa[2])
# Mengubah isi list (list bisa diubah)
data_mahasiswa[1] = 21  # Mengubah umur menjadi 21
# Menampilkan list setelah diubah
print("Data Mahasiswa setelah diubah:", data_mahasiswa)
# Menghitung jumlah elemen dalam list
print("Jumlah elemen:", len(data_mahasiswa))