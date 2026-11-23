angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

    if i == 0 :
        terbesar = input_angka
    elif input_angka > terbesar :
        terbesar = input_angka
    
    if i == 0 :
        terkecil = input_angka
    elif input_angka < terkecil  :
        terkecil = input_angka
    
print(f"Nilai terbesar = {terbesar}")
print(f"Nilai terkecil = {terkecil}")
print(f"Rata-rata = {total / len(angka)}")