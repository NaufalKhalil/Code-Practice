angka = []

angka_sorting = []
jumlah_modus = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j] :
            total += 1

    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        jumlah_modus.append(total)

for i in range(len(angka_sorting)):
    
    for j in range(len(angka_sorting) - 1):
        
        if jumlah_modus[j] < jumlah_modus[j + 1]:
            jumlah_modus[j], jumlah_modus[j + 1] = jumlah_modus[j + 1], jumlah_modus[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

posisi_terakhir = len(angka_sorting) - 1
modus_terbesar = jumlah_modus[0]
modus_terkecil = jumlah_modus[posisi_terakhir]
selisih = modus_terbesar - modus_terkecil

print("-"*24)

print(f"Modus terbesar = {modus_terbesar}")
print("Angka :")

for i in range(len(angka_sorting)):
    if jumlah_modus[i] == modus_terbesar:
        print(angka_sorting[i])

print("-"*24)

print(f"Modus terkecil = {modus_terkecil}")
print("Angka :")

for i in range(len(angka_sorting)):
    if jumlah_modus[i] == modus_terkecil:
        print(angka_sorting[i])

print("-"*24)

print(f"Selisih = {selisih}")
