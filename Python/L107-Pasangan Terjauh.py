angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for j in range(len(angka)):

    for i in range(len(angka) - 1):

        if angka[i] < angka[i + 1]:
            angka[i], angka[i + 1] = angka[i + 1], angka[i]

n = len(angka)

print(f"Pasangan terjauh = {angka[0]} dan {angka[n - 1]}, dengan selisih = {angka[0] - angka[n - 1]}")