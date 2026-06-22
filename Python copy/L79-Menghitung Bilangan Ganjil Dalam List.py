angka = []
ganjil = 0

for i in range(1, 5 + 1):
    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)
    if input_angka % 2 == 1 :
        ganjil += 1
print(f"Jumlah bilangan ganjil : {ganjil}")