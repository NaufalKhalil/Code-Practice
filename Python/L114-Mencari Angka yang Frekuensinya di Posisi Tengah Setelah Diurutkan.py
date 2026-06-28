angka = []

angka_sorting = []
frekuensi_sorting = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    
    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        frekuensi_sorting.append(total)

for i in range(len(frekuensi_sorting)):
    for j in range(len(frekuensi_sorting) - 1):
        if frekuensi_sorting[j] < frekuensi_sorting[j + 1]:
            frekuensi_sorting[j], frekuensi_sorting[j + 1] = frekuensi_sorting[j + 1], frekuensi_sorting[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

median_frekuensi = len(frekuensi_sorting) // 2

print(f"Frekuensi tengah = {frekuensi_sorting[median_frekuensi - 1]}")

for i in range(len(angka_sorting)):
    if frekuensi_sorting[median_frekuensi - 1] == frekuensi_sorting[i]:
        print(angka_sorting[i])