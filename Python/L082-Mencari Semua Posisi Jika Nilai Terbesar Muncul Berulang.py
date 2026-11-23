angka = []

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = angka[i]
    
    elif input_angka > terbesar :
        terbesar = input_angka


print()

print(f"Nilai terbesar = {terbesar}")

print("Muncul pada :")

for i in range(len(angka)):
    if angka[i] == terbesar :
        print(f"Angka ke = {i + 1}, Posisi ke = {i} ")
