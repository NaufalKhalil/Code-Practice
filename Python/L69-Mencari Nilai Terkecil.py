angka = [10, 45, 23, 99, 12]
terkecil = angka[0]

for i in range(len(angka)):
    if  angka[i] < terkecil:
        terkecil = angka[i]
print(terkecil)