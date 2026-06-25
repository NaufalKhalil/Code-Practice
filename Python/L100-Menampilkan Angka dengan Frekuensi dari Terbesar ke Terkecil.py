angka = []

angka_sortir = []
jumlah_muncul = []

angka_sortir_terbanyak = []
jumlah_muncul_terbanyak = []

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

print("-"*16)


