def tampilkan_produk(data):
    print("===== DAFTAR PRODUK =====")
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} - Rp.{data[i][1]}.")
    print()

def hitung_total(data, pilih_produk, jumlah_produk):
    total = 0
    pilih_produk -= 1
    for i in range(jumlah_produk):
        total += data[pilih_produk][1]
    return total

produk = [
    ["Gaming Mouse", 250000],
    ["Office Keyboard", 300000],
    ["Webcam HD", 450000],
    ["Mouse Pad XXL", 120000],
    ["Gaming Chair", 2500000]
]

tampilkan_produk(produk)

pilih_produk = 0
jumlah_produk = 0

while pilih_produk <= 0 or pilih_produk > len(produk):
    pilih_produk = int(input("Pilih Produk : "))

while jumlah_produk <= 0:
    jumlah_produk = int(input("Jumlah Produk : "))

hasil = hitung_total(produk, pilih_produk, jumlah_produk)

print()
print(f"Total belajaan : Rp.{hasil}")