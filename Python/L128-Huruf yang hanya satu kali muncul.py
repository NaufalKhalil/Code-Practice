text = input("Masukkan Text : ")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == 1:
        print(text[i])