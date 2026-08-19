data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000
}

def d_input_int(text, nilai_minimum):
    while True:
        batas_harga = (input(text))
        try:
            batas_harga = int(batas_harga)
            if batas_harga >= nilai_minimum:
                return batas_harga
            else:
                print("[Error] Nilai/angka Maksimum tidak boleh kurang dari nilai Minimum ")
        except ValueError:
            print("[Error] Masukkan sebuah nilai/angka!")

def d_sortir_barang_dengan_batas_harga(min_harga, max_harga, data):
    hasil_data = {}
    jumlah_barang = 0
    for key, value in data.items():
        if min_harga <= value <= max_harga :
            hasil_data[key] = value
            jumlah_barang += 1
    return hasil_data, jumlah_barang

def d_tampilkan(min_harga, max_harga, data, jumlah_barang):
    print(f"Barang dengan harga Rp.{min_harga} - Rp.{max_harga}")
    print()
    total_harga = 0
    for key, value in data.items():
        print(f"-> {key} : Rp.{value}")
        total_harga += value
    print()
    print(f"Jumlah barang : {jumlah_barang}")
    print(f"Total harga : Rp.{total_harga}")

min_harga = d_input_int("Masukkan harga minimum : ", 0)
max_harga = d_input_int("Masukkan harga maksimum : ", min_harga)
print()
hasil_data, jumlah_barang = d_sortir_barang_dengan_batas_harga(min_harga, max_harga, data)
d_tampilkan(min_harga, max_harga, hasil_data, jumlah_barang)