data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_termurah(data):
    for key, value in data.items():
        termurah = value
        nama_barang = key
        break

    for key, value in data.items():
        if termurah > value:
            termurah = value
            nama_barang = key
    return nama_barang, termurah 

nama, harga = d_termurah(data)
print("Barang Termurah :")
print(f"{nama} = Rp.{harga}")