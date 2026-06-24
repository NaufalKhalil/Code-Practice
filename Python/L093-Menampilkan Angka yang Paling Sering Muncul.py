angka = []
jumlah_modus = 0

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i +1} = "))
    angka.append(input_angka)
    

for j in range(len(angka)):    

    for i in range(len(angka)):
        if angka[j] == angka[i]:
            jumlah_modus += 1
 
            