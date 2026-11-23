angka = []
posisi = 0

for i in range(0 , 5):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terkecil = angka[0]
    elif input_angka < terkecil:
        terkecil = angka[i]
        posisi = i

print(f"Nilai terkecil = {terkecil}")
print(f"Angka ke = {posisi + 1}, Posisi ke = {posisi} pada array")