angka = []
total = 0

for i in range(0, 8):
    input_angka = int(input(f"Masukkan Angka ke-{i + 1} : "))
    angka.append(input_angka)

print("-"*16)

cari = int(input("Cari angka : "))

for i in range(len(angka)):
    if cari == angka[i]:
        total += 1

print(f"Angka {cari} muncul sebanyak {total}") 