angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)


print(f"Rata-rata = {rata_rata}")
print("Angka di atas rata-rata :")

for i in range(len(angka)):
    if angka[i] > rata_rata :
        print(angka[i])