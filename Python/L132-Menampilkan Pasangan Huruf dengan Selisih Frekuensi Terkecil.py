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

selisih_terkecil = len(text)
flag = False

for i in range(len(f_huruf) - 1):

    selisih = abs(f_huruf[i] - f_huruf[i + 1])

    if selisih < selisih_terkecil and selisih != 0 :
        selisih_terkecil = selisih
        flag = True

if flag == True :

    print("Pasangan :")

    for i in range(len(f_huruf) - 1):
        
        selisih = abs(f_huruf[i] - f_huruf[i + 1])

        if selisih_terkecil == selisih :
            print(f"{huruf_disortir[i]} dan {huruf_disortir[i + 1]}")
    
    print()
    print(f"Selisih = {selisih_terkecil}")

else :
    print("Tidak ada selisih terkecil")