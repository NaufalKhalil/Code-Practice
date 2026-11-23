data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_termahal(data):
    for key, value in data.items():
        nama_barang = key
        harga_barang = value
        break

    for key, value in data.items():
        if harga_barang < value:
            nama_barang = key
            harga_barang = value

    return nama_barang, harga_barang

def d_termurah(data):
    for key, value in data.items():
        nama_barang = key
        harga_barang = value
        break

    for key, value in data.items():
        if harga_barang > value:
            nama_barang = key
            harga_barang = value

    return nama_barang, harga_barang

def d_selisih_harga(harga_max, harga_min):
    selisih = harga_max - harga_min
    return selisih

def d_tampilkan(nama_max, nama_min, harga_max, harga_min, selisih_harga):
    print("Barang Termahal :")
    print(f"-> {nama_max} : Rp.{harga_max}")
    print()
    print("Barang Termurah : ")
    print(f"-> {nama_min} : Rp.{harga_min}")
    print()
    print(f"Selisih harga = Rp.{selisih_harga}")

nama_barang_termahal, harga_barang_termahal = d_termahal(data)     
nama_barang_termurah, harga_barang_termurah = d_termurah(data)
selisih_harga = d_selisih_harga(harga_barang_termahal, harga_barang_termurah)

d_tampilkan(nama_barang_termahal, nama_barang_termurah, harga_barang_termahal, harga_barang_termurah, selisih_harga)