def hitung_total(data):
    total = 0
    for i in range(len(data)):
        total += data[i][2]
    return total 

def tampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]}) - Rp.{data[i][2]}.")

produk = [
    ["Gaming Mouse", "gaming", 250000],
    ["Office Keyboard", "office", 300000],
    ["Webcam HD", "aksesoris", 450000]
]

tampilkan_produk(produk)
print("-"*18)
hasil = hitung_total(produk)
print(f"Total belanjaan : Rp.{hasil}")