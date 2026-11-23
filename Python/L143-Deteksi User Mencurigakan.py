login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)
print("Persentase aktivitas :")

flag = False

for i in range(len(f_login)):

    persentase = (f_login[i] / len(login)) * 100
    persentase = round(persentase, 1)

    if persentase > 50 :
        print(f"{login_sortir[i]} = {persentase}%")
        flag = True
    
if flag == False :
    print("Tidak ada user mencurigakan")