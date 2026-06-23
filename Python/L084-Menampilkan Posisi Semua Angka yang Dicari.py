angka = []
total = 0

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

cari = int(input("Cari angka : "))

for i in range(len(angka)):
    if angka[i] == cari :
        total += 1

print("-"*16)
print(f"Angka {cari} muncul sebanyak {total}")
print()
print("Muncul pada :")

for i in range(len(angka)):
    if angka[i] == cari :
        print(f"Angka ke = {i + 1}, Posisi = {i}")