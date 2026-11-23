text = input("Masukkan Text : ")

sudah_tampil = []
total_besar_1 = 0

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > total_besar_1:
        total_besar_1 = total

total_besar_2 = 0

flag = False

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total_besar_2 < total < total_besar_1:
        total_besar_2 = total
        flag = True

if flag == True :

    print(f"Frekuensi Terbesar ke dua = {total_besar_2}")
    print("huruf :")

    for i in range(len(text)):

        total = 0

        for j in range(len(text)):
            if text[i] == text[j]:
                total += 1

        if total == total_besar_2:
            if text[i] not in sudah_tampil:
                print(text[i])
                sudah_tampil.append(text[i])

else:
    print("Tidak ada Frekuensi Terbesar ke dua")