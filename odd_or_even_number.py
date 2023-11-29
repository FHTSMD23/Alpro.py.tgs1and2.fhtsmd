# Membaca input berupa angka dari user
angka = float(input("Masukkan angka: "))

# Menentukan apakah angka yang dimasukan adalah genap atau ganjil
if angka % 2 == 0:
    print(" ")
    print(f"{angka} adalah angka genap.")
else:
    print(" ")
    print(f"{angka} adalah angka ganjil.")