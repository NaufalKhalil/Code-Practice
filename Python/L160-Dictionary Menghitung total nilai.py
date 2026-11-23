data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000
}

def d_kalkulasi_harga(data):
    total = 0
    for value in data.values():
        total += value
    return total

def d_tampilkan(data, total_harga):
    for key, value in data.items():
        print(f"- {key} : {value}")
    print("-" * 16)
    print(f"Total Harga = Rp{total_harga}")

print("Belanja anda hari ini :")
hasil = d_kalkulasi_harga(data)
d_tampilkan(data, hasil)