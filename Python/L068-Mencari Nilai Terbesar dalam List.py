angka = [10, 45, 23, 99, 12]

terbesar = angka[0]

for i in range(len(angka)):
    if angka[i] > terbesar:
        terbesar = angka[i]
print(terbesar)