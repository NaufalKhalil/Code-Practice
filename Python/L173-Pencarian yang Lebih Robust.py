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

def d_input():
    cari = input("Masukkan nama barang : ")
    cari = cari.strip()
    cari = cari.lower()
    return cari

def d_cari(cari, data):
    hasil = {}
    for key, value in data.items():
        if cari in key:
            hasil[key] = value
    return hasil

def d_tampilkan(hasil):
    if not hasil:
        print()
        print("Barang tidak ditemukan!")
    else:
        print()
        print("Barang ditemukan!")
        print()
        for key, value in hasil.items():
            print(f"-> Nama    : {key}")
            print(f"-> Harga   : Rp.{value}")
            print()

def d_convert_data(data):
    hasil_convert = {}
    for key, value in data.items():
        key = key.lower()
        key = key.strip()
        hasil_convert[key] = value
    return hasil_convert

cari = d_input()
data_convert = d_convert_data(data)
hasil = d_cari(cari, data_convert)
d_tampilkan(hasil)