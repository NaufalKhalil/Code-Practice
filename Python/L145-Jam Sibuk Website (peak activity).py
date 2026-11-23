jam_login = (input("Masukkan Jam login User = "))
jam_login = jam_login.split()

f_jam_login = []
a_jam_login = []

for i in range(len(jam_login)):

    total = 0

    for j in range(len(jam_login)):
        if jam_login[i] == jam_login[j]:
            total += 1
        
    if jam_login[i] not in a_jam_login:
        f_jam_login.append(total)
        a_jam_login.append(jam_login[i])

for i in range(len(f_jam_login)):
    for j in range(len(f_jam_login) - 1):
        if f_jam_login[j] < f_jam_login[j + 1]:
            f_jam_login[j], f_jam_login[j + 1] = f_jam_login[j + 1], f_jam_login[j]
            a_jam_login[j], a_jam_login[j + 1] = a_jam_login[j + 1], a_jam_login[j]

print()
print("Jam tersibuk :")

for i in range(len(f_jam_login)):
    if f_jam_login[i] == f_jam_login[0]:
        print(f"{a_jam_login[i]} = {f_jam_login[i]} login")