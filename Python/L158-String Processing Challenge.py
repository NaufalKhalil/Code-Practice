import os

def clear_terminal():
    os.system("cls")

mahasiswa = [
    ["  andi saputra  ", 85],
    ["BUDI santoso", 72],
    ["citra   lestari", 91],
    ["Dinda Pratiwi", 68],
    ["eko   nugroho", 77],
    ["FARAH amelia", 95],
    ["galih Wibowo", 80]
]

def d_tampilkan_menu_utama():
    print("===== SISTEM DATA MAHASISWA =====")
    print("1. Lihat Data")
    print("2. Rapikan Semua Nama")
    print("3. Cari Mahasiswa")
    print("4. Ganti Nama/Nilai Mahasiswa")
    print("5. Statistik Mahasiswa")
    print("6. Keluar")
    print()

def d_tampilakan_statistik(
    data, nama_terpanjang, nama_terpendek, rata_rata_panjang_nama,
    nilai_tertinggi, nilai_terendah, rata_rata_nilai):
    
    print("===== STATISTIK MAHASISWA =====")
    print(f"-> Jumlah mahasiswa         : {len(data)}")
    print(f"-> Nama terpanjang          : {nama_terpanjang}")
    print(f"-> Nama terpendek           : {nama_terpendek}")
    print(f"-> Rata-rata panjang nama   : {rata_rata_panjang_nama}")
    print(f"-> Nilai tertinggi          : {nilai_tertinggi}")
    print(f"-> Nilai terendah           : {nilai_terendah}")
    print(f"-> Rata-rata nilai          : {rata_rata_nilai}")
    print()

def d_tampilkan_menu_edit_nama_atau_nilai():
    print("===== EDIT {nama}")
    print("1. Edit Nama Mahasiswa")
    print("2. Edit Nilai Mahasiswa")

def d_tampilkan_nama(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} = {data[i][1]}")

def d_tampilkan_nama_tanpa_nomor(data, cari):
    for i in range(len(data)):
        if cari == data[i]:
            print(f"- {data[i][0]} = {data[i][1]}")

def d_cari_nama(data, cari):
    ketemu = []
    for i in range(len(data)):
        if cari == data[i][0]:
            ketemu.append(data[i])

def d_merapikan_nama(data):
    data_hasil = []

    for i in range(len(data)):
        nama_ = data[i][0]
        nama_ = nama_.split()
        nama_ = " ".join(nama_)
        nama_ = nama_.title()

        data_hasil.append([nama_, data[i][1]])
    
    return data_hasil

def d_validasi_edit(data, cari):
    valid = False
    cari -= 1
    if 0 <= cari <= len(data):
        valid = True
    return valid

def d_edit_nama_dan_nilai(data, opsi, index, value):
    index -= 1
    if opsi == 1:
        data[index][0] = value
    elif opsi == 2:
        data[index][1] = value

while True:

    d_tampilkan_menu_utama()

    try:
        opsi_utama = int(input("=> : "))
        if opsi_utama < 1 or opsi_utama > 6:
            raise ValueError("[Error] Pilih angka yang tersedia di menu!")
        break
    except ValueError:
        raise ValueError("[Error] Pilih angka yang tersedia di menu!")

    clear_terminal()






    






