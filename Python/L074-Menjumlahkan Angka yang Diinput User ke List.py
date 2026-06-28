angka = []
total = 0
jumlah_input = int(input("Berapa data? : "))

for i in range(jumlah_input):
    angka_input = int(input("Masukkan angka : "))
    angka.append(angka_input)
    total += angka[i]
print(f"Total : {total}")