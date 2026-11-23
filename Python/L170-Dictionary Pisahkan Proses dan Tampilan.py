data = {
    "Buku": 15000,
    "Pensil": 3000,
    "Penghapus": 2000,
    "Pulpen": 5000,
    "Tas": 120000,
    "Penggaris": 4000,
    "Spidol Hitam": 7000,
    "Spidol Warna 12": 25000,
    "Crayon Pas": 45000,
    "Buku Gambar A4": 8000,
    "Buku Gambar A3": 15000,
    "Rautan Putar": 35000,
    "Rautan Kantong": 3000,
    "Kotak Pensil Kain": 18000,
    "Kotak Pensil Besi": 27000,
    "Tipe-X Kertas": 9000,
    "Tipe-X Cair": 6000,
    "Binder Note A5": 32000,
    "Binder Note B5": 40000,
    "Isi Binder A5": 8000,
    "Isi Binder B5": 10000,
    "Gunting Kertas": 12000,
    "Cutter Besar": 15000,
    "Cutter Kecil": 7000,
    "Isi Cutter": 5000,
    "Staples Kecil": 11000,
    "Isi Staples": 3000,
    "Lem Kertas Cair": 4000,
    "Lem Stik (Glue Stick)": 8000,
    "Stabilo Boss": 14000,
    "Sticky Notes Neon": 12000,
    "Post-it Penanda": 7000,
    "Jangka Matematika": 16000,
    "Busur Derajat": 3000,
    "Penggaris Segitiga": 8000,
    "Papan Ujian Akrilik": 19000,
    "Papan Ujian Kayu": 12000,
    "Kalkulator Ilmiah": 165000,
    "Kalkulator Toko": 55000,
    "Double Tape": 6000,
    "Solasi Bening": 4000,
    "Map Plastik Kancing": 5000,
    "Map Snelhechter": 7000,
    "Dompet Dokumen": 22000,
    "Kertas HVS A4 Rim": 53000,
    "Kertas F4 Rim": 58000,
    "Notebook Hardcover": 29000,
    "Kamus Bahasa Inggris": 85000,
    "Kamus Bahasa Indonesia": 75000,
    "Tinta Printer Hitam": 95000,
    "Kertas Origami": 6000,
    "Klip Kertas Botol": 9000,
    "Pin Styrofoam": 5000,
    "Pembersih Papan Tulis": 13000,
    "Id Card Holder": 4000,
    "Stempel Otomatis": 38000
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
    for key, value in data.items():
        if min_harga <= value <= max_harga :
            hasil_data[key] = value
    return hasil_data

def d_statistik(data):
    jumlah_barang = 0
    total_harga = 0
    for value in data.values():
        jumlah_barang += 1
        total_harga += value
    return jumlah_barang, total_harga

def d_tampilkan(min_harga, max_harga, data, jumlah_barang, total_harga):
    print(f"Barang dengan harga Rp.{min_harga} - Rp.{max_harga}")
    print()
    for key, value in data.items():
        print(f"-> {key} : Rp.{value}")
    print()
    print(f"Jumlah barang : {jumlah_barang}")
    print(f"Total harga : Rp.{total_harga}")

min_harga = d_input_int("Masukkan harga minimum : ", 0)
max_harga = d_input_int("Masukkan harga maksimum : ", min_harga)
print()
hasil_data = d_sortir_barang_dengan_batas_harga(min_harga, max_harga, data)
jumlah_barang, total_harga = d_statistik(hasil_data)
d_tampilkan(min_harga, max_harga, hasil_data, jumlah_barang, total_harga)
