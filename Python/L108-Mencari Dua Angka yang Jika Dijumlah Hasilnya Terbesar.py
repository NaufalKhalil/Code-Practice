angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Pasangan terbesar : {angka[0]} dan {angka[1]}")
print(f"Jumlah = {angka[0] + angka[1]}")