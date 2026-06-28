angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Tiga angka terbesar jika di jumlahkan : {angka[0]}, {angka[1]}, dan {angka[2]}")
print(f"Dengan hasil penjumlahan = {angka[0] + angka[1] + angka[2]}")
