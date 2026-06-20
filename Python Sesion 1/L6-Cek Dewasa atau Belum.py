umur = int(input("Masukan umur anda :"))
dewasa = "Anda sudah dewasa" 
non_dewasa = "Anda masih di bawah umur"
satu_abad = "Wah, umur Anda sudah satu abad atau lebih!"

if umur > 99 :
    print(f"Umur adalah : {umur}, {satu_abad}")
elif umur >= 18 :
    print(f"Umur adalah : {umur}, {dewasa}")
else :
    print(f"Umur adalah : {umur}, {non_dewasa}")


