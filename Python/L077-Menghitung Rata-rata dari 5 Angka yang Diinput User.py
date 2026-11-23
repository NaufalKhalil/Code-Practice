angka = []
total = 0

for i in range(1, 5 + 1):
    input_angka = int(input(f"Masukkan angka ke-{i} : "))
    angka.append(input_angka)

    total += input_angka

print(f"Jumlah = {total}")
print(f"Rata - rata = {total / len(angka)}")

