text = input("Masukkan Text : ")

sudah_tampil = []
total_besar = 0

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > total_besar:
        total_besar = total

print("Raja huruf :")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == total_besar:
        if text[i] not in sudah_tampil:
            print(text[i])
            sudah_tampil.append(text[i])