angka = []
posisi = 0

for i in range(0 , 5):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = angka[0]
    elif input_angka > terbesar:
        terbesar = angka[i]
        posisi = i

print(f"Nilai terbesar = {terbesar}")
print(f"Angka ke = {posisi + 1}, Posisi ke = {posisi} pada array")