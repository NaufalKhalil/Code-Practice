text = input("Masukkan Text : ")
sudah_tampil = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > 1:
        if text[i] not in sudah_tampil:
            print(f"{text[i]} = {total}")
            sudah_tampil.append(text[i])