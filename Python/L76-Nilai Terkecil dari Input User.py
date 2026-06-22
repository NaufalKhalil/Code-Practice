angka = []

jumlah_angka = int(input("Berapa data? : "))
    
for i in range(jumlah_angka):
    
    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)

    if i == 0 : 
        terkecil = angka[0]

    elif input_angka > angka[i]:
        terkecil = angka[i]

print(f"Nilai terkecil : {terkecil}")

    
