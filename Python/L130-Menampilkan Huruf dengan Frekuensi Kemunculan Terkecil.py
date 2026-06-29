text = input("Masukkan Text : ")

sudah_tampil = []
total_kecil = len(text)

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total < total_kecil:
        total_kecil = total

print(f"Frekuensi terkecil = {total_kecil}")
print("huruf :")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == total_kecil:
        if text[i] not in sudah_tampil:
            print(text[i])
            sudah_tampil.append(text[i])