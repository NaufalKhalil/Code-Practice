text = input("Masukkan Text : ")

text = text.split() 

frekuensi_text = []
text_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in text_disortir:
        frekuensi_text.append(total)
        text_disortir.append(text[i])

for i in range(len(frekuensi_text)):
    for j in range(len(frekuensi_text) - 1):
        if frekuensi_text[j] < frekuensi_text[j + 1]:
            frekuensi_text[j], frekuensi_text[j + 1] = frekuensi_text[j + 1], frekuensi_text[j]
            text_disortir[j], text_disortir[j + 1] = text_disortir[j + 1], text_disortir[j]

print("-" * 24)
print("Rangking :")

for i in range(len(frekuensi_text)):
    print(f"{text_disortir[i]} = {frekuensi_text[i]}")