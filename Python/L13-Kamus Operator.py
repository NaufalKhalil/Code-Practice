import sys
import operator

while True :
    while True :

        menu = {
            1 : ("+", "Penjumlahan", operator.add),
            2 : ("-", "Pengurangan", operator.sub),
            3 : ("*", "Perkalian", operator.mul),
            4 : ("/", "Pembagian", operator.truediv),
            5 : ("**", "Perpangkatan", operator.pow),
            6 : ("", "Keluar")
        }

        garis = "-"*16

        for key, value in menu.items():

            print(f"[{key}] {value[1]}")

        print(garis)

        operasi = int(input("Anda mau melakukan apa? :"))

        if operasi == 6:
                    print("Terima kasih sudah menggunakan kalkulator")
                    sys.exit()

                if operasi >= 1 and operasi <= 5:
                    break
                else:
                    print("Masukan angka menu yang valid!")

    angka_1 = int(input("Masukan angka pertama :"))
    angka_2 = int(input("Masukan angka kedua :"))

    if operasi == 4 :
            while angka_2 == 0:
                print("Error!, Angka kedua dalam pembagian tidak boleh 0")
                angka_2 = int(input("Masukan angka kedua :"))

        hasil_teks = mesin_operasi(operasi, angka_1, angka_2)

        print(hasil_teks)