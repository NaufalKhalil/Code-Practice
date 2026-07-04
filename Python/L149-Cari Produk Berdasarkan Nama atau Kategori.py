produk = [
    ["gaming mouse", "gaming"],
    ["mechanical keyboard", "gaming"],
    ["office keyboard", "office"],
    ["gaming chair", "gaming"],
    ["webcam hd", "aksesoris"],
    ["mouse pad xxl", "aksesoris"],
    ["office chair", "office"]
]

cari = input("Cari : ")
cari = cari.lower()

total = 0

for i in range(len(produk)):
    if cari == produk[i][1]:
        total += 1
        print(f"{total}. {produk[i][0]} ({produk[i][1]})")
    elif cari in produk[i][0]:
        total += 1
        print(f"{total}. {produk[i][0]} ({produk[i][1]})")

if total > 0:
    print(f"Total ditemukan : {total}")
else:
    print("Data tidak di temukan")