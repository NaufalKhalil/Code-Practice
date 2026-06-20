import sys

def mesin_operasi(operasi, angka_1, angka_2):
    if operasi == 1 :
        return angka_1 + angka_2
    elif operasi == 2 :
        return angka_1 - angka_2
    elif operasi == 3 :
        return angka_1 * angka_2
    elif operasi == 4 :
        return angka_1 / angka_2
    elif operasi == 5 :
        return angka_1 ** angka_2

while True :

    while True :
        print("-"*16)
        print("[1] Penjumlahan")
        print("[2] Pengurangan")
        print("[3] Perkalian")
        print("[4] Pembagian")
        print("[5] Perpangkatan")
        print("-"*16)
        print("[6] Keluar")
        print("-"*16)

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

    hasil_angka = mesin_operasi(operasi, angka_1, angka_2)

    if operasi == 1:
        print(f"hasil penjumlahan : {angka_1} + {angka_2} = {hasil_angka}")
    elif operasi == 2:
        print(f"hasil pengurangan : {angka_1} - {angka_2} = {hasil_angka}")
    elif operasi == 3:
        print(f"hasil perkalian : {angka_1} * {angka_2} = {hasil_angka}")
    elif operasi == 4:
        print(f"hasil pembagian : {angka_1} / {angka_2} = {hasil_angka}")
    elif operasi == 5:
        print(f"hasil perpangkatan : {angka_1} ** {angka_2} = {hasil_angka}")