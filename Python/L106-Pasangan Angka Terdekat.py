angka = []

for i in range(0, 10):
    input_user = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_user)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print("-"*24)
print(angka)


for i in range(len(angka) - 1):

    selisih = abs(angka[i] - angka[i + 1])

    if i == 0 :
        
        for j in range(len(angka)):
            selisih_update = angka

        selisih_update = angka_terakhir
    elif 0 < selisih < selisih_update :
        selisih_update = selisih 

for i in range(len(angka) - 1):
    if selisih_update == abs(angka[i] - angka[i + 1]):
        print(f"{angka[i]} dan {angka[i + 1]} dengan selisih = {selisih_update}")