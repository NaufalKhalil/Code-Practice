angka = [10, 21, 30, 45, 50, 61]
total = 0
for i in range(len(angka)):
    if angka[i] % 2 == 1:
        ganjil += 1
print(f"Jumlah angka ganjil: {ganjil}")