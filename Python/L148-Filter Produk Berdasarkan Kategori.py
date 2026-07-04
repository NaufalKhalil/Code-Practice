produk = [
    ["Gaming Mouse", "gaming"],
    ["Mechanical Keyboard", "gaming"],
    ["Office Keyboard", "office"],
    ["Gaming Chair", "gaming"],
    ["Webcam HD", "aksesoris"],
    ["Mouse Pad XXL", "aksesoris"],
    ["Office Chair", "office"]
]

kategori = input("Cari kategori produk : ")
kategori = kategori.lower()

print("-" * 20)
print(f"Daftar produk kategori {kategori} :")

total = 0

for i in range(len(produk)):
    if kategori == produk[i][1]:
        total += 1
        print(f"{total}. {produk[i][0]}")

print()
if total > 0 :
    print(f"Total produk ditemukan : {total}")
else :
    print("Produk tidak ditemukan!")
