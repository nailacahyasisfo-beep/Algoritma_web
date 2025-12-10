# Contoh menggunakan karakter (char) di Python

huruf1 = 'A'
huruf2 = 'b'
symbol = '#'

print("Huruf 1 :", huruf1)
print("Huruf 2 :", huruf2)
print("Symbol  :", symbol)

# Mengecek apakah huruf besar atau kecil
if huruf1.isupper():
    print(huruf1, "adalah huruf besar")

if huruf2.islower():
    print(huruf2, "adalah huruf kecil")


#HASIL MODIFIKASI

# Program pengecekan tipe karakter

# Input karakter dari user
karakter = input("Masukkan satu karakter: ")

# Pastikan hanya satu karakter yang dimasukkan
if len(karakter) != 1:
    print("Harus memasukkan tepat satu karakter!")
else:
    print("\nKarakter yang dimasukkan:", karakter)

    # Mengecek jenis karakter
    if karakter.isupper():
        print(karakter, "adalah huruf besar.")
    elif karakter.islower():
        print(karakter, "adalah huruf kecil.")
    elif karakter.isdigit():
        print(karakter, "adalah angka.")
    else:
        print(karakter, "adalah simbol atau karakter khusus.")
