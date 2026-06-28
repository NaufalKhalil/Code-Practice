angka = []

angka_sortir = []
jumlah_muncul = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total_muncul = 0

    for j in range(len(angka)):
        if angka[j] == angka[i]:
            total_muncul += 1

    if angka[i] not in angka_sortir :
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total_muncul)

for i in range(len(jumlah_muncul)):

    for j in range(len(jumlah_muncul) - 1 ):

        if jumlah_muncul[j] < jumlah_muncul[j + 1]:
            jumlah_muncul[j], jumlah_muncul[j + 1] = jumlah_muncul[j + 1], jumlah_muncul[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]
        
print("-"*16)

for i in range(len(angka_sortir)):
    print(f"{angka_sortir[i]} muncul {jumlah_muncul[i]} kali")