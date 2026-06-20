import sys
import operator
import os
import time

menu = {
    1 : ("+", "Penjumlahan", operator.add),
    2 : ("-", "Pengurangan", operator.sub),
    3 : ("*", "Perkalian", operator.mul),
    4 : ("/", "Pembagian", operator.truediv),
    5 : ("**", "Perpangkatan", operator.pow),
    6 : ("", "Keluar")
}

garis = "-"*16

def mesin_hitung(opsi, angka_1, angka_2):
    simbol = menu[opsi][0]
    nama_operasi = menu[opsi][1]
    operasi = menu[opsi][2]

    hasil = operasi(angka_1, angka_2)

    print(garis)

    print(f"Hasil {nama_operasi} dari {angka_1} {simbol} {angka_2} = {hasil}")

while True :

    while True :

        print(garis)

        print("Kalkulator Menu :")

        print(garis)

        for key, value in menu.items():
            if key == 6 :
                continue
            print(f"[{key}] {value[1]}")

        print(garis)    

        print(f"[{6}] {value[1]}")

        print(garis)    

        opsi = int(input("Anda mau melakukan apa? :"))

        if opsi == 6 :
            time.sleep(0.5)
            print("Keluar dari Kakulator...")
            sys.exit()
        elif opsi > 6 or opsi <= 0 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Masukan angka menu yang valid!")
            time.sleep(0.5)
        elif opsi >= 1 and opsi <= 5:
            break

    angka_1 = int(input("Masukan angka pertama :"))
    angka_2 = int(input("Masukan angka kedua :"))

    if opsi == 4 :
        while angka_2 == 0:
            print("Error!, Angka kedua dalam pembagian tidak boleh 0")
            angka_2 = int(input("Masukan angka kedua :"))

    mesin_hitung(opsi, angka_1, angka_2)
    