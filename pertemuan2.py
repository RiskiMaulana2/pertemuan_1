#a=10, a adalah variabel dengan nilai m10
# tipe data : Angka satuan yang tidak ada komanya (integer)
data_integer=12
print("data:",data_integer)
print("-beritpe",type(data_integer))
#tipe data : angka dengan koma (float)
data_float=2.5
print("data:",data_float)
print("-bertipe",type(data_float))
#tipe data : kumpulan karakter (string)
data_string="riski maulana achmad"
print("data:",data_string)
print("-bertipe",type(data_string))
#tipe data : biner true/false (boolean)
data_bool=False
print("data:",data_bool)
print("-bertipe",type(data_bool))


# INTEGER ke tipe data lain
data_int=12
data_float=float(data_int)
data_str=str(data_int)
data_bool=bool(data_int)# akan false ketika nilai integer 0
print(data_float)
print(data_str)
print(data_bool)

#float ke tipe data lain
data_float=9.3
data_int=int(data_float)
data_str=str(data_float)
data_bool=bool(data_float)
print(data_int)
print(data_str)
print(data_bool)

#string ke tipe data lain
data_str="10"
data_int=int(data_str)
data_float=float(data_str)
data_bool=bool(data_str)
print(data_int)
print(data_float)
print(data_bool)
print(type(data_float))


# Deklarasi variabel dengan tipe data dan nilainya
nama = "Riski Maulana Achmad"    # Tipe data: string
umur = 20                        # Tipe data: integer
berat = 55                       # Tipe data: float

# Menampilkan output sesuai format
print(f"Nama  : {nama}")
print(f"Umur  : {umur} tahun")
print(f"Berat : {berat} Kg")


# Inisialisasi variabel awal
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
hasil_1 = int(angka_string)

# 2. Konversi angka_float menjadi integer
hasil_2 = int(angka_float)

# 3. Konversi angka_integer menjadi float
hasil_3 = float(angka_integer)

# 4. Konversi angka_integer menjadi string
hasil_4 = str(angka_integer)

# Menampilkan hasil (opsional untuk mengecek)
print(hasil_1, type(hasil_1))  # Output: 123 <class 'int'>
print(hasil_2, type(hasil_2))  # Output: 45 <class 'int'> (desimal akan dihilangkan)
print(hasil_3, type(hasil_3))  # Output: 89.0 <class 'float'>
print(hasil_4, type(hasil_4))  # Output: '89' <class 'str'>




# c. Meminta input nama (string)
nama = input("Masukkan nama Anda: ")

# a. Meminta input usia (integer)
usia = int(input("Masukkan usia Anda: "))

# b. Meminta input tinggi badan (float)
tinggi_badan = float(input("Masukkan tinggi badan Anda (cm): "))

# Menampilkan hasil input (opsional)
print("Halo", nama, "usia Anda adalah", usia, "tahun dan tinggi Anda", tinggi_badan, "cm.")

