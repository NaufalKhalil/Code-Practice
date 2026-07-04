def menu():
    print()
    print("===== MENU =====")
    print("1. Halo")
    print("2. Tentang")
    print("3. Keluar")

def opsi_1():
    print()
    print("Halo, selamat datang di aplikasi inventaris!")

def opsi_2():
    print()
    print("Aplikasi ini dibuat untuk belajar Python Function.")

flag = True

while True:
    
    if flag == True :
        menu()

    input_user = input("=> :")

    if input_user == "1":
        opsi_1()
        flag = True
    elif input_user == "2":
        opsi_2()
        flag = True
    elif input_user == "3":
        break
    else:
        flag = False
        print("Perintah tidak valid!")