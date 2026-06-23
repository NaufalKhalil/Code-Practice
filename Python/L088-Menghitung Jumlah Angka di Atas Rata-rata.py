angka = []
total = 0
di_atas_rata_rata = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

for i in range(len(angka)):
    if angka[i] > rata_rata :
        di_atas_rata_rata += 1

print(f"Rata-rata = {rata_rata}")
print(f"Jumlah angka di atas rata-rata = {di_atas_rata_rata}")