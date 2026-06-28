angka = []
jumlah_modus_sebelumnya = 0


for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    jumlah_modus = 0

    for j in range(len(angka)):

        if angka[i] == angka[j] :
            jumlah_modus += 1

    if jumlah_modus > jumlah_modus_sebelumnya :
        jumlah_modus_sebelumnya = jumlah_modus

print(f"Jumlah kemunculan terbesar = {jumlah_modus_sebelumnya}")
print("Angka :")

angka_yang_sudah_ditampilkan = []

for i in range(len(angka)):

    jumlah_kemunculan = 0

    for j in range(len(angka)):

        if angka[i] == angka[j] :    
            jumlah_kemunculan += 1

    if jumlah_modus_sebelumnya == jumlah_kemunculan and angka[i] not in angka_yang_sudah_ditampilkan :
        print(angka[i])
        angka_yang_sudah_ditampilkan.append(angka[i])
        
