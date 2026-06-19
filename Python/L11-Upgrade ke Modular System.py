import sys

def mesin_operasi(operasi, angka_1, angka_2):
    if operasi == 1 :
        return(f"hasil penjumlahan : {angka_1} + {angka_2} = {angka_1 + angka_2}")
    elif operasi == 2 :
        return(f"hasil pengurangan : {angka_1} - {angka_2} = {angka_1 - angka_2}")
    elif operasi == 3 :
        return(f"hasil perkalian : {angka_1} * {angka_2} = {angka_1 * angka_2}")
    elif operasi == 4 :  
        return(f"hasil pembagian : {angka_1} / {angka_2} = {angka_1 / angka_2}")
    elif operasi == 5 :
        return(f"hasil perpangkatan : {angka_1} ** {angka_2} = {angka_1 ** angka_2}")

while True :

    while True :
        print("-----------------------")
        print("[1] Penjumlahan")
        print("[2] Pengurangan")
        print("[3] Perkalian")
        print("[4] Pembagian")
        print("[5] Perpangkatan")
        print("-----------------------")
        print("[6] Keluar")
        print("-----------------------")

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