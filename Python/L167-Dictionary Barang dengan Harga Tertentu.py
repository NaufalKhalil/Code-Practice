data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_input_int():
    while True:
        batas_harga = (input("Masukkan batas harga : "))
        try:
            batas_harga = int(batas_harga)
            return batas_harga
        except ValueError:
            print("[Error] Masukkan sebuah nilai/angka!")

def d_sortir_barang_dengan_batas_harga(batas_harga, data):
    hasil_data = {}
    jumlah_barang = 0
    for key, value in data.items():
        if value <= batas_harga:
            hasil_data[key] = value
            jumlah_barang += 1
    return hasil_data, jumlah_barang

def d_tampilkan(batas_harga, data, jumlah_barang):
    print(f"Barang dengan harga <= Rp.{batas_harga}")
    print()
    for key, value in data.items():
        print(f"-> {key} : Rp.{value}")
    print()
    print(f"Jumlah barang : {jumlah_barang}")

batas_harga = d_input_int()
print()
hasil_data, jumlah_barang = d_sortir_barang_dengan_batas_harga(batas_harga, data)
d_tampilkan(batas_harga, hasil_data, jumlah_barang)