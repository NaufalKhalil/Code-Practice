angka = [10, 21, 30, 45, 50, 61]
jumlah = 0

for i in range(len(angka)):
    if angka[i] % 2 == 0 :
        jumlah += 1
print(jumlah)