angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

x = (len(angka) // 2) - 1
median = (angka[x] + angka[x + 1]) / 2

print(f"Median = {median}")