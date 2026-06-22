angka = []
genap = 0

for i in range(1, 5 + 1):
    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)
    if input_angka % 2 == 0 :
        genap += 1
print(f"Jumlah bilangan genap : {genap}")