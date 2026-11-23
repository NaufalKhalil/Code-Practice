def tampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]}) - Rp.{data[i][2]}.")

produk = [
    ["Gaming Mouse", "gaming", 250000],
    ["Office Keyboard", "office", 300000],
    ["Webcam HD", "aksesoris", 450000]
]

produk_diskon = [
    ["Flashdisk", "storage", 90000],
    ["SSD 1TB", "storage", 1200000]
]

print("Produk utama :")
tampilkan_produk(produk)
print()
print("Produk diskon :")
tampilkan_produk(produk_diskon)