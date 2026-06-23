angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

print("-"*16)
print(f"Rata-rata : {rata_rata}")

for i in range(len(angka)):
    jarak = rata_rata - angka[i]

    jarak = abs(jarak) 

    if i == 0 :
        jarak_terdekat = jarak
        angka_terdekat = angka[0]
    elif jarak_terdekat > jarak :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]

print(f"Angka terdekat = {angka_terdekat}")