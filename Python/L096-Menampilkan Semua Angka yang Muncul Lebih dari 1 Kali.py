angka = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

print("Angka yang muncul lebih dari sekali :")

angka_sudah_ditampilkan = []

for i in range(len(angka)):
    
    total_modus = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total_modus += 1
    
    if total_modus > 1 and angka[i] not in angka_sudah_ditampilkan :
        print(angka[i])
        angka_sudah_ditampilkan.append(angka[i])
