#OPERASI ARITMATIKA
a = 12  #Nilai variabel a
b = 5   #Nilai variabel b
hasil = a+b     #operasi penjumlahan
print(hasil)
hasil = a-b     #operasi pengurangan
print(hasil)
hasil =a*b      #operasi perkalian
print(hasil)
hasil = a/b     #operasi pembagian
print(hasil)
hasil = a**b    #operasi eksponen(pangkat)a pangkat b
print(hasil)
hasil = a%b     #operasi modulus (sisa dari pembagian)
print(hasil)
hasil = a//b    #operasi floor division (pembulatan)
print(hasil)

#KOVERSI SATUAN TEMPERATURE
#Konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukan suhu dalam celcius : ")) #untuk menampilkan hasil dalam bentuk data float
print("suhu adalah",celcius,"Celcius") #suhu adalah untuk kata pertama dilanjutkan inputan celcius dan diakhiri kata celcius
# reamur
reamur = (4/5) * celcius    #Dalam reamur dikalikan dengan celcius
print("suhu dalam reamur adalah" ,reamur,"Reamur")
#fahrenheit   
fahrenheit = ((9/5) * celcius) + 32     #dalam fahrenheit dikalikan dengan celcius lalu ditambah 32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")
#Kelvin
kelvin = celcius + 273      #dalam kelvin celcius ditambah dengan 273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")

#OPERASI KOMPERASI
#Setiap hasil dari komperasi adalah booelan
a = 10
b = 5

hasil = a > b
print(a, ">", b, "=", hasil) #a lebih besar dari b          

hasil = a < b
print(a, "<", b, "=", hasil) #a lebih kecil dari b 
hasil = a >= b
print(a, ">=", b, "=", hasil) #a lebih besar sama dengan b 
hasil = a <= b
print(a, "<=", b, "=", hasil) #a lebih kecil sama dengan b      

hasil = a == b
print(a, "==", b, "=", hasil) #untuk membandingkan kedua variabel (==)     
hasil = a != b
print(a, "!=", b, "=", hasil) #tidak sama dengan (variabelnya tidak sama sama sekali)

# Dimensi bangunan (balok)
panjang = 12
lebar = 5
tinggi = 8

# a. Perhitungan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
volume = panjang * lebar * tinggi
keliling = 4 * (panjang + lebar + tinggi)

# b & c. Evaluasi Kondisi
is_luas_gt_50 = luas_permukaan > 50
is_volume_480 = volume == 480

# Output hasil
print(f"a. Luas Permukaan : {luas_permukaan}")
print(f"   Volume         : {volume}")
print(f"   Keliling       : {keliling}")
print(f"b. Apakah luas > 50? {is_luas_gt_50} (Ya)")
print(f"c. Apakah volume == 480? {is_volume_480} (Ya)")