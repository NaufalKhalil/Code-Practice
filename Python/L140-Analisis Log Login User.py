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
print("User aktif :")

for i in range(len(f_login)):
    print(f"{login_sortir[i]} = {f_login[i]} kali login")