angka = []

for i in range(0, 10):
    input_user = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_user)

# sorting terbesar → terkecil
for i in range(len(angka)):
    for j in range(len(angka)-1):

        if angka[j] < angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]

print("-"*24)
print(angka)

# cari selisih terkecil
for i in range(len(angka)-1):

    selisih = abs(angka[i] - angka[i+1])

    if i == 0:
        selisih_update = selisih
    elif selisih < selisih_update:
        selisih_update = selisih

print("-"*24)
print("Pasangan terdekat :")

for i in range(len(angka)-1):

    selisih = abs(angka[i] - angka[i+1])

    if selisih == selisih_update:
        print(f"{angka[i]} dan {angka[i+1]}")

print(f"Selisih = {selisih_update}")