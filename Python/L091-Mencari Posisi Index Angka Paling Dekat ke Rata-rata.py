angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

for i in range(len(angka)):

    jarak = rata_rata - angka[i]

    jarak = abs(jarak)

    if i == 0 :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]
        posisi = i
    elif jarak < jarak_terdekat :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]
        posisi = i

print("-"*16)
print(f"Rata-rata = {rata_rata}")
print(f"Angka terdekat = {angka_terdekat}")
print(f"Angka ke = {posisi + 1}")
print(f"Posisi index ke = {posisi}")