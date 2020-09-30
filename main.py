#Import Module
import math
from os import system
import time
import sys
#Define The Variable Of Program
#Function Of Add
def tambah(x,y):
    return x + y
#Function Of Subtract
def kurang(x,y):
    return x - y
#Function Of Multiply
def kali(x,y):
    return x * y
#Function Of Divide
def bagi(x,y):
    return x / y
def sgt(x,y):
    return 0.5 * x * y
def pemangkatan(x,y):
    return x ** y
def pem_bulat(x,y):
    return x // y
def pembanding(x,y):
    a = x > y
    b = x < y
    c = x == y
    d = x != y
    print("""
        Keterangan 
        True Adalah Benar
        False Adalah Salah""")
    print("\n\tNilai",x, "> (Lebih Besar","Daripada)",y,a,"\n",
          "\tNilai",x,"< (Lebih Kecil Daripada)",y,b,"\n",
          "\tNilai",x,"== (Sama Dengan)",y,c,"\n"
          "\tNilai",x,"!= (Tidak Sama Dengan)",y,d)
#Function Main() Of The Program
def sgta():
    c = float(input("Masukkan Nilai Alas Segitiga; "))
    d = float(input("Masukkan Nilai Tinggi Segitiga; "))
    print(c, ":" ,d, "=" ,sgt(c,d))
def ll():
    phi = 3.14
    r = float(input("Masukkan Jari Jari Lingkaran; "))
    hasil = phi * r * r
    print ("Hasil Dari Jari-Jari Lingkaran",r,"Adalah",hasil)
def bujur_sangkar():
    t = int(input("Masukkan Nilai Sisi; "))
    h = t ** 2
    print("Hasil Dari Perhitungan Luas Sisi Bujur Sangkar",t,"Adalah",h)

def main2():
    time.sleep(0.5)
    print ("Penghitungan Luas -\n"
            "1. Luas Segitiga\n"
            "2. Luas Lingkaran\n"
            "3. Luas Bujur Sangkar\n")
    tnya = input("Masukkan Pilihan Anda; ")
    if tnya in ('1','2','3'):
        if tnya == '1':
            sgta()
        elif tnya == '2':
            ll()
        elif tnya == '3':
            bujur_sangkar()
    else:
        print("Input Salah")
        main2()
def main():
    print ("Program Kalkulator Sederhana -\n"\
            "1. Pertambahan \n"\
            "2. Pengurangan \n"\
            "3. Perkalian\n"\
            "4. Pembagian\n"
            "5. Pemangkatan\n"
            "6. Pembagian Bulat\n"
            "7. Pembanding")
    #Take Choie From USer
    tanya = input("Masukan Pilihan Anda: ")
    #Check If Choice Is One Of The Four Options 
    if tanya in ('1','2','3','4','5','6','7'):
        a = int(input("Masukkan Nilai Pertama; "))
        b = int(input("Masukkan Nilai Kedua; "))

        if tanya == '1':
            print (a, "+" ,b, "=" ,tambah(a,b))
        elif tanya == '2':
            print (a, "-" ,b, "=" ,kurang(a,b))
        elif tanya == '3':
            print (a, "x" ,b, "=" ,kali(a,b))
        elif tanya == '4':
            print (a, ":" ,b, "=" ,bagi(a,b))
        elif tanya == '5':
            print (a, ":" ,b, "=" ,pemangkatan(a,b))
        elif tanya == '6':
            print (a, ":" ,b, "=" ,pem_bulat(a,b))
        elif tanya == '7':
            pembanding(a,b)
    else:
        print("Invalid Input")
    

#Start Of The Program

print ("Program Sederhana\n"\
        "1. Kakulator\n"\
        "2. Print Sesuatu\n"
        "3. Penghitungan Luas\n")
try:
    tanya2 = input("Masukan  Pilihan Anda: ")
    if tanya2 in ('1','2','3'):
        if tanya2 == '1':
            system('cls')
            main()
        elif tanya2 == '2':
            system('cls')
            c = input("Masukkan Nama Mu: ")
            print ("Haii:",c)
        elif tanya2 == '3':
            main2()
        else:
            print("Input Salah ")
except KeyboardInterrupt:
    print("\nCTRL-C Di Aktifkan")
    time.sleep(1)
    sys.exit("Exitng")
    



################################Created By Azzarnuji Nur Ukhrowi#########################