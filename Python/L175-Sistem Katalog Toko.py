import os, time

data_produk = {
    "Buku tulis": {
        "Harga": 15000,
        "Stok": 85,
        "Merek": "SIDU",
        "Kategori": [
            "Alat tulis",
            "Peralatan Sekolah",
            "Buku"
        ],
        "Detail": {
            "Warna": [
                "Merah",
                "Biru",
                "Hijau",
                "Hitam"
            ],
            "Jumlah_Halaman": 58,
            "Ukuran": "A5"
        }
    },
    "Pensil 2B": {
        "Harga": 3000,
        "Stok": 120,
        "Merek": "Faber-Castell",
        "Kategori": [
            "Alat tulis",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Hitam"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Standar"
        }
    },
    "Pulpen Gel": {
        "Harga": 5000,
        "Stok": 95,
        "Merek": "Pilot",
        "Kategori": [
            "Alat tulis",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Biru",
                "Merah"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "0.5mm"
        }
    },
    "Penghapus": {
        "Harga": 2000,
        "Stok": 150,
        "Merek": "Joyko",
        "Kategori": [
            "Alat tulis",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Putih",
                "Hitam"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Kecil"
        }
    },
    "Penggaris 30cm": {
        "Harga": 4000,
        "Stok": 60,
        "Merek": "Butterfly",
        "Kategori": [
            "Alat tulis",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Bening",
                "Kuning"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "30cm"
        }
    },
    "Tipe-X Kertas": {
        "Harga": 8000,
        "Stok": 45,
        "Merek": "Correction Pen",
        "Kategori": [
            "Alat tulis",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "12 meter"
        }
    },
    "Rautan Pensil": {
        "Harga": 5000,
        "Stok": 70,
        "Merek": "Kenko",
        "Kategori": [
            "Alat tulis",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Merah",
                "Biru",
                "Hijau"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Putar"
        }
    },
    "Spidol Boardmarker": {
        "Harga": 9000,
        "Stok": 110,
        "Merek": "Snowman",
        "Kategori": [
            "Alat tulis",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Biru",
                "Merah"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Chisel Tip"
        }
    },
    "Stabilo Boss": {
        "Harga": 12000,
        "Stok": 40,
        "Merek": "Stabilo",
        "Kategori": [
            "Alat tulis",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Kuning",
                "Hijau",
                "Pink",
                "Oranye"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Original"
        }
    },
    "Buku Gambar": {
        "Harga": 8000,
        "Stok": 55,
        "Merek": "Sinar Dunia",
        "Kategori": [
            "Buku",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Putih"
            ],
            "Jumlah_Halaman": 20,
            "Ukuran": "A4"
        }
    },
    "Binder Loose Leaf": {
        "Harga": 25000,
        "Stok": 30,
        "Merek": "Bantex",
        "Kategori": [
            "Buku",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Biru",
                "Abu-abu"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "A5"
        }
    },
    "Kertas HVS A4": {
        "Harga": 45000,
        "Stok": 200,
        "Merek": "PaperOne",
        "Kategori": [
            "Office",
            "Kertas"
        ],
        "Detail": {
            "Warna": [
                "Putih"
            ],
            "Jumlah_Halaman": 500,
            "Ukuran": "70gr"
        }
    },
    "Sticky Notes": {
        "Harga": 7000,
        "Stok": 140,
        "Merek": "Post-it",
        "Kategori": [
            "Office",
            "Alat tulis"
        ],
        "Detail": {
            "Warna": [
                "Kuning",
                "Pink",
                "Hijau"
            ],
            "Jumlah_Halaman": 100,
            "Ukuran": "3x3 inci"
        }
    },
    "Map Dokumen": {
        "Harga": 5000,
        "Stok": 85,
        "Merek": "Biola",
        "Kategori": [
            "Office",
            "Penyimpanan"
        ],
        "Detail": {
            "Warna": [
                "Merah",
                "Kuning",
                "Hijau",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "F4"
        }
    },
    "Gunting Kantor": {
        "Harga": 12000,
        "Stok": 50,
        "Merek": "Kenko",
        "Kategori": [
            "Office",
            "Peralatan"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Merah"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Sedang"
        }
    },
    "Cutter": {
        "Harga": 9000,
        "Stok": 65,
        "Merek": "SDI",
        "Kategori": [
            "Office",
            "Peralatan"
        ],
        "Detail": {
            "Warna": [
                "Merah",
                "Kuning",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Kecil"
        }
    },
    "Stapler": {
        "Harga": 15000,
        "Stok": 35,
        "Merek": "Max",
        "Kategori": [
            "Office",
            "Peralatan"
        ],
        "Detail": {
            "Warna": [
                "Abu-abu",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "No.10"
        }
    },
    "Isi Staples": {
        "Harga": 3000,
        "Stok": 180,
        "Merek": "Max",
        "Kategori": [
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Silver"
            ],
            "Jumlah_Halaman": 20,
            "Ukuran": "No.10"
        }
    },
    "Paper Clip": {
        "Harga": 4000,
        "Stok": 220,
        "Merek": "Joyko",
        "Kategori": [
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Silver",
                "Warna-warni"
            ],
            "Jumlah_Halaman": 100,
            "Ukuran": "Kecil"
        }
    },
    "Double Tape": {
        "Harga": 6000,
        "Stok": 90,
        "Merek": "Nachiti",
        "Kategori": [
            "Office",
            "Perekat"
        ],
        "Detail": {
            "Warna": [
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "1 inci"
        }
    },
    "Lakban Hitam": {
        "Harga": 12000,
        "Stok": 75,
        "Merek": "Daimaru",
        "Kategori": [
            "Office",
            "Perekat"
        ],
        "Detail": {
            "Warna": [
                "Hitam"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "2 inci"
        }
    },
    "Kalkulator Ilmiah": {
        "Harga": 150000,
        "Stok": 15,
        "Merek": "Casio",
        "Kategori": [
            "Elektronik",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Abu-abu"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "FX-991EX"
        }
    },
    "Flashdisk 64GB": {
        "Harga": 85000,
        "Stok": 40,
        "Merek": "SanDisk",
        "Kategori": [
            "Elektronik",
            "Penyimpanan"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Merah"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "USB 3.0"
        }
    },
    "Mouse Wireless": {
        "Harga": 120000,
        "Stok": 28,
        "Merek": "Logitech",
        "Kategori": [
            "Elektronik",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Putih",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "M170"
        }
    },
    "Keyboard Eksternal": {
        "Harga": 175000,
        "Stok": 12,
        "Merek": "Logitech",
        "Kategori": [
            "Elektronik",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "K120"
        }
    },
    "Kabel Data Type-C": {
        "Harga": 35000,
        "Stok": 110,
        "Merek": "Anker",
        "Kategori": [
            "Elektronik"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "1 meter"
        }
    },
    "Earphone Wired": {
        "Harga": 50000,
        "Stok": 65,
        "Merek": "JBL",
        "Kategori": [
            "Elektronik"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "C100SI"
        }
    },
    "Desk Mat / Mousepad": {
        "Harga": 45000,
        "Stok": 40,
        "Merek": "Polos",
        "Kategori": [
            "Aksesoris",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Navy",
                "Hijau"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "80x30cm"
        }
    },
    "Lampu Meja Belajar": {
        "Harga": 75000,
        "Stok": 22,
        "Merek": "Philips",
        "Kategori": [
            "Elektronik",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Putih",
                "Pink"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "LED USB"
        }
    },
    "Stand Laptop": {
        "Harga": 60000,
        "Stok": 18,
        "Merek": "Aluminium",
        "Kategori": [
            "Aksesoris",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Silver",
                "Abu-abu"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Adjustable"
        }
    },
    "Powerbank 10000mAh": {
        "Harga": 135000,
        "Stok": 25,
        "Merek": "Baseus",
        "Kategori": [
            "Elektronik"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Fast Charge"
        }
    },
    "Tas Ransel Sekolah": {
        "Harga": 185000,
        "Stok": 14,
        "Merek": "Exsport",
        "Kategori": [
            "Peralatan Sekolah",
            "Tas"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Maroon",
                "Navy"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "20 Liter"
        }
    },
    "Kotak Pensil Kain": {
        "Harga": 25000,
        "Stok": 55,
        "Merek": "Eiger",
        "Kategori": [
            "Peralatan Sekolah",
            "Penyimpanan"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Hijau Army"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Resleting"
        }
    },
    "Botol Minum Tumbler": {
        "Harga": 65000,
        "Stok": 48,
        "Merek": "LocknLock",
        "Kategori": [
            "Peralatan Sekolah",
            "Gaya Hidup"
        ],
        "Detail": {
            "Warna": [
                "Biru",
                "Hijau",
                "Tosca"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "600ml"
        }
    },
    "Kotak Makan": {
        "Harga": 40000,
        "Stok": 36,
        "Merek": "Yooyee",
        "Kategori": [
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Pink",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "3 Sekat"
        }
    },
    "Payung Lipat": {
        "Harga": 55000,
        "Stok": 29,
        "Merek": "Joju",
        "Kategori": [
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Biru",
                "Hijau"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Otomatis"
        }
    },
    "Jas Hujan Ponco": {
        "Harga": 45000,
        "Stok": 42,
        "Merek": "Elephant",
        "Kategori": [
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Biru",
                "Hijau"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "All Size"
        }
    },
    "Kaos Kaki Hitam": {
        "Harga": 10000,
        "Stok": 130,
        "Merek": "Specs",
        "Kategori": [
            "Peralatan Sekolah",
            "Pakaian"
        ],
        "Detail": {
            "Warna": [
                "Hitam",
                "Putih"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Sedang"
        }
    },
    "Buku Agenda": {
        "Harga": 35000,
        "Stok": 47,
        "Merek": "Gramedia",
        "Kategori": [
            "Buku",
            "Office"
        ],
        "Detail": {
            "Warna": [
                "Cokelat",
                "Hitam"
            ],
            "Jumlah_Halaman": 100,
            "Ukuran": "A5 Premium"
        }
    },
    "Kertas Manila": {
        "Harga": 3000,
        "Stok": 90,
        "Merek": "Lokal",
        "Kategori": [
            "Kertas",
            "Peralatan Sekolah"
        ],
        "Detail": {
            "Warna": [
                "Putih",
                "Kuning",
                "Biru"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Besar"
        }
    },
    "Gantungan Kunci Tas": {
        "Harga": 7000,
        "Stok": 115,
        "Merek": "Handmade",
        "Kategori": [
            "Aksesoris"
        ],
        "Detail": {
            "Warna": [
                "Warna-warni"
            ],
            "Jumlah_Halaman": 1,
            "Ukuran": "Karakter"
        }
    },
    "Crayon 24 Warna": {
        "Harga": 35000,
        "Stok": 38,
        "Merek": "Titi",
        "Kategori": [
            "Alat tulis",
            "Kreativitas"
        ],
        "Detail": {
            "Warna": [
                "24 Warna"
            ],
            "Jumlah_Halaman": 24,
            "Ukuran": "Set"
        }
    },
    "Cat Air / Watercolor": {
        "Harga": 55000,
        "Stok": 22,
        "Merek": "Pentel",
        "Kategori": [
            "Alat tulis",
            "Kreativitas"
        ],
        "Detail": {
            "Warna": [
                "12 Warna"
            ],
            "Jumlah_Halaman": 12,
            "Ukuran": "Tube"
        }
    },
    "Kuas Lukis Set": {
        "Harga": 20000,
        "Stok": 45,
        "Merek": "Lyra",
        "Kategori": [
            "Alat tulis",
            "Kreativitas"
        ],
        "Detail": {
            "Warna": [
                "Set 5pcs"
            ],
            "Jumlah_Halaman": 5,
            "Ukuran": "Assorted"
        }
    }
}

global_input_text_int = "=> : "
global_input_text_accept = "[y/n] => : "

opsi_menu_utama = ["1", "2", "3", "4", "5", "6", "7"]

global_error_text_int = "[ERROR] Masukkan opsi sesuai dengan angka yang tersedia!"
global_error_text_accept = "[ERROR] Masukkan opsi yang tersedia!"

def d_clear_terminal():
    os.system('cls')    

def d_menu_utama():
    print("===== SISTEM INVENTORI TOKO =====")
    print("1. Cari barang")
    print("2. Statistik inventori")
    print("3. Tambah barang")
    print("4. Edit barang")
    print("5. Keluar")

def d_menu_filter_barang():
    print("===== FILTER BARANG =====")
    print("-> Filter harga barang")
    print("-> Filter stock barang")
    print("-> Filter barang berdasarkan kategori")
    print("-> Filter barang berdasarkan merek")

def d_menu_filter_harga_barang():
    print("===== FILTER BARANG =====")
    print("1. Filter harga barang dari yang [Termahal] - [Termurah]")
    print("2. Filter harga barang dari yang [Termurah] - [Termahal]")

def d_menu_filter_stock_barang():
    print("===== FILTER BARANG =====")
    print("1. Filter stock barang dari yang [Terbesar] - [Terkecil]")
    print("2. Filter stock barang dari yang [Terkecil] - [Terbesar]")

def d_menu_filter_kategori_barang(data_produk):
    print("===== FILTER BARANG =====")
    print("[INFO] Kategori barang yang tersedia :")
    for nama_produk, deskripsi_produk, in data_produk.items():
        print(f"1. {nama_produk}")
        for harga, stock, merek, kategori, detail_produk in deskripsi_produk.items():
            print(f" - Harga    : Rp{harga:,}".replace(",", "."))
            print(f" - Stock    : {stock}")
            print(f" - Merek    : {merek}")
            print(f" - Kategori : ", *kategori)
            print(f" - Detail   :")
            for warna, jumlah_halaman, 
            print(f"   - Warna      : ", *)



def d_input_user(input_text, opsi, error_text):
    print()
    while True:   
        input_user = input(input_text)
        if input_user in opsi:
            return input_user
        else:
            print(error_text)


while True:
    d_menu_utama()
    input_user = d_input_user(global_input_text_int, opsi_menu_utama, global_error_text_int )
    d_clear_terminal()

    if input_user == "1":
        cari = input("Cari :")

