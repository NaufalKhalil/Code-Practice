produk = [
    "Gaming Mouse",
    "Mechanical Keyboard",
    "Gaming Headset",
    "Mouse Pad XXL",
    "Webcam HD",
    "Gaming Chair",
    "Office Keyboard",
    "Wireless Mouse"
]

cari = input("Cari Produk : ")
print()

total_pencarian = 0

for i in range(len(produk)):
    if cari in produk[i]:
        total_pencarian += 1
        print(f"{total_pencarian}. {produk[i]}")

print()
if total_pencarian > 0 :
    print(f"Total produk ditemukan : {total_pencarian}")
else :
    print("Produk tidak ditemukan.")