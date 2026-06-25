angka = []
angka_sortir = []
list_modus = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sortir :
        angka_sortir.append(angka[i])
        list_modus.append(total)

print("-"*24)

print(f"=> Jumlah angka unik = {len(angka_sortir)}")

for i in range(len(angka_sortir)):

    for j in range(len(angka_sortir) - 1):

        if list_modus[j] < list_modus[j + 1]:
            list_modus[j], list_modus[j + 1] = list_modus[j + 1], list_modus[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]

print()

print(f"Jumlah kemunculan = {list_modus[0]}")

print()
print("-"*24)
print("=> Angka paling sering muncul :")

for i in range(len(angka_sortir)):
    if list_modus[0] == list_modus[i]:
        print(f"{angka_sortir[i]}")

print()
print("-"*24)
print("=> Statistik :")

for i in range(len(angka_sortir)):
    print(f"{angka_sortir[i]} muncul {list_modus[i]}")