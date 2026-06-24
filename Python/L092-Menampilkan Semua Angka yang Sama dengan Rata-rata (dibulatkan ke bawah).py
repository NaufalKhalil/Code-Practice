angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)
    total += input_angka

rata_rata = int(total / len(angka))

print("-"*16)
print(f"Rata-rata = {rata_rata}")
print("Di temukan pada :")

for i in range(len(angka)):

    if angka[i] == rata_rata :
        print(f"Angka ke = {i + 1}, Posisi = {i}")