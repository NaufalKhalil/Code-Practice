angka = []
# deklarasi julah_kemunculan_sebelumnya yang belum ada karena masih putaran ke 0
jumlah_kemunculan_sebelumnya = 0

# masukkan input user ke dalam array angka
for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

# perulangan untuk array
for i in range(len(angka)):
    
    # deklarasi cari adalah angka array sekarang
    cari = angka[i]

    # reset jumlah kemunculan apabila perulangan "j" sudah selesai
    jumlah_kemunculan = 0    

    # perulangan untuk jumlah angka yang di cari
    for j in range(len(angka)):
        if cari == angka[j] :
            jumlah_kemunculan += 1
    
    if jumlah_kemunculan > jumlah_kemunculan_sebelumnya :
        jumlah_kemunculan_sebelumnya = jumlah_kemunculan
        angka_modus = angka[i]

for i in range(len(angka)):



    
    
print("-"*16)
print(f"Angka paling sering muncul = {angka_modus}")
print(f"Jumlah kemunculan = {jumlah_kemunculan_sebelumnya}")