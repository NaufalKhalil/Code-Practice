angka = []

angka_sorting = []
modus_sorting = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    
    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        modus_sorting.append(total)

for i in range(len(angka_sorting)):
    
    for j in range(len(angka_sorting) - 1):
        
        if modus_sorting[j] < modus_sorting[j + 1]:
            modus_sorting[j], modus_sorting[j + 1] = modus_sorting[j + 1], modus_sorting[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

print("-"*24)

for i in range(len(modus_sorting) - 1):

    print(f"{angka_sorting[i]} dan {angka_sorting[i + 1]} selisih modus = {modus_sorting[i] - modus_sorting[i + 1]} ")