angka = []

jumlah_input = int(input("Berapa data? : "))

for i in range(jumlah_input):

    angka_input = int(input("Masukkan angka : "))
    angka.append(angka_input)

    if i == 0 :
        terbesar = angka[0]

    elif angka[i] > terbesar :
        terbesar = angka[i]

print(f"Nilai Terbesar : {terbesar}")