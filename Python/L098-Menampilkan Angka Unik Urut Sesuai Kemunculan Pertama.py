angka = []
angka_tampil = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

print("Angka Unik")

for i in range(len(angka)):
    if angka[i] not in angka_tampil:
        angka_tampil.append(angka[i])
        print(angka[i])