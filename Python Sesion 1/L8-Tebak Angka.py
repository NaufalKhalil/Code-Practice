angka_rahasia = 7
kesempatan = 3

for perulangan in range (1, kesempatan + 1):

    angka = int(input("Angka tebakan anda :"))

    if angka == angka_rahasia :
        print("Tebakan anda benar!")
        break
    else :

        if angka > angka_rahasia :
            print("Tebakan anda salah!, Angka tebakan anda terlalu besar.")
        else :
            print("Tebakan anda salah!, Angka tebakan anda terlalu kecil.")
        
        sisa = kesempatan - perulangan
        print(f"Sisa kesempatan untuk menebak = {sisa}")
        
        if sisa == 0:
            print("Game Over!")
    


