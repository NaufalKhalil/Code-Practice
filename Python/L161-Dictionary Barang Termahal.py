data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_termahal(data):
    termahal = 0
    for key, value in data.items():
        if termahal < value:
            termahal = value
            nama_barang = key
    return nama_barang, termahal 

nama, harga = d_termahal(data)
print("Barang Termahal :")
print(f"{nama} = Rp.{harga}")