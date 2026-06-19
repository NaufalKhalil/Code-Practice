username = input("Username :")
password = input("Password :")
admin_username = "admin"
admin_password = "12345"

if username == admin_username and password == admin_password:
    print("Login Berhasil!")
else:
    print("Login Gagal!")
    if username != admin_username and password != admin_password:
        print("Username dan Password Salah")
    elif username != admin_username:
        print("Username Salah")
    elif password != admin_password:
        print("Password Salah")

