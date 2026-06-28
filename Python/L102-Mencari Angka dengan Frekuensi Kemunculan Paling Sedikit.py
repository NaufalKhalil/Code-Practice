angka = []

angka_sortir = []
jumlah_muncul = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sortir:
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total)

for i in range(len(angka_sortir)):

    for j in range(len(angka_sortir) - 1):

        if jumlah_muncul[j] < jumlah_muncul[j + 1]:
            jumlah_muncul[j], jumlah_muncul[j + 1] = jumlah_muncul[j + 1], jumlah_muncul[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]

n = len(jumlah_muncul) - 1

kemunculan_terkecil = jumlah_muncul[n]

print("-"*24)

print(f"Jumlah kemunculan terkecil = {kemunculan_terkecil}")

print("Angka :")

for i in range(len(angka_sortir)):
    if jumlah_muncul[i] == kemunculan_terkecil:
        print(angka_sortir[i])