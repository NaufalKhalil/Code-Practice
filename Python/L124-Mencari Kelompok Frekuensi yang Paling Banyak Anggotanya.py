angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 20):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_total_besar = 0

for i in range(len(frekuensi_sort)):
  
    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total_besar < f_total:
        f_total_besar = f_total

print("Tahta paling ramai :")

jumlah_anggota = 0

for i in range(len(angka_sort)):

    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total == f_total_besar:
        print(angka_sort[i])
        jumlah_anggota += 1 

print(f"Jumlah anggota = {jumlah_anggota} ")