text = input("Masukkan Text : ")

f_huruf = []
huruf_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in huruf_disortir:
        f_huruf.append(total)
        huruf_disortir.append(text[i])

for i in range(len(f_huruf)):
    for j in range(len(f_huruf) - 1):
        if f_huruf[j] < f_huruf[j + 1]:
            f_huruf[j], f_huruf[j + 1] = f_huruf[j + 1], f_huruf[j]
            huruf_disortir[j], huruf_disortir[j + 1] = huruf_disortir[j + 1], huruf_disortir[j]

f_sudah = []

for i in range(len(f_huruf)):
    
    if f_huruf[i] not in f_sudah:
        print(f"Frekuensi {f_huruf[i]} :")
        f_sudah.append(f_huruf[i])

        for j in range(len(f_huruf)):
            if f_huruf[i] == f_huruf[j]:
                print(huruf_disortir[j])