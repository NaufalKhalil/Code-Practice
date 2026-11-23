data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_total_harga_dan_jumlah_barang(data):
    total = 0
    jumlah_barang = 0
    for _, value in data.items():
        total += value
        jumlah_barang += 1
    return total, jumlah_barang

def d_rata_rata(total, jumlah_barang):
    rata_rata = total / jumlah_barang
    return round(rata_rata, 2)

def d_tampilkan(total, jumlah_barang, rata_rata):
    print(f"-> Jumlah Barang    : {jumlah_barang}")
    print(f"-> Total Harga      : Rp.{total}")
    print(f"-> Rata-rata        : Rp.{rata_rata}")

total, jumlah_barang = d_total_harga_dan_jumlah_barang(data)
rata_rata = d_rata_rata(total, jumlah_barang)
d_tampilkan(total, jumlah_barang, rata_rata)