produk = [
    "Mouse",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Webcam",
    "Monitor",
    "Keyboard",
    "Mouse"
]

array_produk = []
array_jumlah = []

for i in range(len(produk)):

    total = 0

    for j in range(len(produk)):
        if produk[i] == produk[j]:
            total += 1

    if produk[i] not in array_produk:
        array_produk.append(produk[i])
        array_jumlah.append(total)

for i in range(len(array_jumlah)):
    for j in range(len(array_jumlah) - 1):
        if array_jumlah[j] < array_jumlah[j + 1]:
            array_jumlah[j], array_jumlah[j + 1] = array_jumlah[j + 1], array_jumlah[j]
            array_produk[j], array_produk[j + 1] = array_produk[j + 1], array_produk[j]
print("===[ Statistik Penjualan ]===")
print()

for i in range(len(array_jumlah)):
    print(f"- {array_produk[i]} : {array_jumlah[i]} kali")

print()
print("=> Produk terlaris :")

for i in range(len(array_jumlah)):
    if array_jumlah[i] >= array_jumlah[0]:
        print(f"- {array_produk[i]}, dengan jumlah penjualan : {array_jumlah[0]} kali")
