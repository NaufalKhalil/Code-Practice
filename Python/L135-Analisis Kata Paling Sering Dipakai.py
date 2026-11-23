text = input("Masukkan text :")

kata = text.split()

total_terbesar = 0


for i in range(len(kata)):
    
    total = 0
        
    for j in range(len(kata)):
        if kata[i] == kata[j]:
            total += 1

    if total_terbesar < total:
        total_terbesar = total

sudah_tampil = []

for i in range(len(kata)):
    
    total = 0

    for j in range(len(kata)):
        if kata[i] == kata[j]:
            total += 1
        
    if total == total_terbesar and kata[i] not in sudah_tampil:
        print(f"{kata[i]} = {total_terbesar}")
        sudah_tampil.append(kata[i])