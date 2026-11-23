import os, time

mahasiswa = [
    [" andi saputra ", 85],
    ["BUDI santoso", 72],
    ["citra lestari", 91],
    ["Dinda Pratiwi", 68],
    ["eko nugroho", 77],
    ["FARAH amelia", 95],
    ["galih Wibowo", 80],
    ["Kartika Prasetyo", 75],
    ["oki lestari", 94],
    ["joko wibowo", 61],
    ["JOKO SAPUTRI", 92],
    ["FAJAR PRASETYO", 94],
    [" vino HIDAYAT ", 97],
    ["PUTRI PRASETYO", 87],
    ["SITI SARI", 73],
    ["siti kusuma", 84],
    ["Kartika Pratiwi", 98],
    [" putri UTAMI ", 94],
    ["kartika santoso", 95],
    ["RIAN PRATIWI", 64],
    ["Indah Hidayat", 65],
    [" oki KUSUMA ", 77],
    ["WATI PRATIWI", 83],
    ["Taufik Saputri", 64],
    ["FAJAR RAMADHAN", 70],
    ["Wati Santoso", 100],
    ["Bambang Hidayat", 63],
    ["Oki Utami", 85],
    ["PUTRI WIJAYA", 96],
    [" siti SAPUTRI ", 85],
    ["Wati Lestari", 68],
    [" oki SARI ", 97],
    ["UTAMI PRATIWI", 68],
    ["zaki amelia", 63],
    ["KARTIKA LESTARI", 87],
    [" fajar WIJAYA ", 84],
    ["Fajar Nugroho", 95],
    ["Hadi Kusuma", 81],
    [" kartika KURNIAWAN ", 70],
    ["Wati Prasetyo", 92],
    ["mega saputra", 100],
    ["RIAN SAPUTRA", 69],
    ["taufik ramadhan", 98],
    ["siti amelia", 67],
    ["TAUFIK KURNIAWAN", 63],
    ["oki wijaya", 91],
    ["JOKO LESTARI", 90],
    ["Bambang Ramadhan", 93],
    ["FAJAR WIBOWO", 94],
    [" nugraha KURNIAWAN ", 83]
]

# ===== tampilan menu =====

def d_tampilkan_menu_utama():
    print("===== SISTEM DATA MAHASISWA =====")
    print("1. Lihat Data")
    print("2. Rapikan Semua Nama")
    print("3. Cari Mahasiswa")
    print("4. Ganti Nama Mahasiswa")
    print("5. Statistik Nilai")
    print("6. Keluar")
    print("-" * 23)

def d_tampilkan_menu_edit():
    print("-" * 23)
    print("1. Edit Nama")
    print("2. Edit Nilai")
    print("3. Hapus Mahasiswa Dari Data")
    print("4. Tambahkan Data Baru")
    print("5. Keluar")
    print("-" * 23)

def d_tampilkan_daftar(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} = {data[i][1]}", flush=True)
        time.sleep(0.02)

def d_tampilkan_daftar_tanpa_nomor(data):
    for i in range(len(data)):
        print(f"- {data[i][0]} = {data[i][1]}", flush=True)
        time.sleep(0.02)

def d_tampilkan_statistik(data):
    total = len(data)

    if total == 0:
        print("[Info] Data mahasiswa masih kosong!")
        return

    jumlah_nilai = 0
    tertinggi = data[0][1]
    terendah = data[0][1]

    for i in range(len(data)):
        nilai = data[i][1]
        jumlah_nilai += nilai

        if nilai > tertinggi:
            tertinggi = nilai

        if nilai < terendah:
            terendah = nilai

    nama_tertinggi = []
    nama_terendah = []

    for i in range(len(data)):
        if data[i][1] == tertinggi:
            nama_tertinggi.append(data[i][0])
        if data[i][1] == terendah:
            nama_terendah.append(data[i][0])

    rata_rata = jumlah_nilai / total
    daftar_tertinggi = ", ".join(nama_tertinggi)
    daftar_terendah = ", ".join(nama_terendah)

    print(f"Jumlah Mahasiswa   : {total}")
    print(f"Rata-rata Nilai    : {rata_rata:.2f}")
    print(f"Nilai Tertinggi    : {tertinggi} ({daftar_tertinggi})")
    print(f"Nilai Terendah     : {terendah} ({daftar_terendah})")

# ===== fungsi logika =====

def d_merapikan_nama(data):
    hasil = []
    for i in range(len(data)):
        nama = data[i][0]
        nama = nama.split()
        nama = " ".join(nama)
        nama = nama.title()
        hasil.append([nama, data[i][1]])
    return hasil

def d_cari_data(data, cari):
    hasil = []

    if cari.isdigit():
        cari = int(cari)
        for i in range(len(data)):
            if cari == data[i][1]:
                hasil.append(data[i])
        return hasil
    else:
        cari = cari.title()
        for i in range(len(data)):
            if cari in data[i][0]:
                hasil.append(data[i])
        return hasil

def d_validasi_index_data(data):
    while True:
        cari = input("=> Masukkan nomor mahasiswa :")

        try:
            cari = int(cari)
            cari -= 1
            if cari < 0:
                print("[Error] Anda harus memasukkan nomor/angka tanpa simbol apapun!")
            elif 0 <= cari < len(data):
                return cari
            else:
                print(f"[Error] Mahasiswa dengan posisi nomor {cari + 1} tidak ditemukan/diluar jangkauan data!")

        except ValueError:
            print("[Error] Anda harus memasukkan sebuah nomor dari posisi nama mahasiswa!")

def d_edit_nama(data, posisi):
    ganti = input(f"=> Mengganti nama : {data[posisi][0]}, Menjadi : ")
    pesan = f"[y/n] Mengganti nama : {data[posisi][0]}, Menjadi : {ganti} :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data[posisi][0] = ganti
        print("[Info] Nama mahasiswa telah diperbarui!")
        time.sleep(1.5)
        return None
    else:
        print("[Info] Membatalkan perubahan nama...")
        time.sleep(1.5)
        return None

def d_edit_nilai(data, posisi):
    while True:
        try:
            ganti = int(input(f"=> Mengganti nilai : {data[posisi][1]}, Menjadi : "))
            break
        except ValueError:
            print("[Error] Anda wajib memasukkan sebuah nilai berupa angka!")

    pesan = f"[y/n] Mengganti nilai : {data[posisi][1]}, Menjadi : {ganti} :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data[posisi][1] = ganti
        print("[Info] Nilai mahasiswa telah diperbarui!")
        time.sleep(1.5)
        return None
    else:
        print("[Info] Membatalkan perubahan nilai...")
        time.sleep(1.5)
        return None

def d_hapus_data(data, posisi):
    pesan = f"[y/n] Menghapus data mahasiswa bernama : {data[posisi][0]}, dari daftar :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        del data[posisi]
        print("[Info] Data mahasiswa telah dihapus!")
        time.sleep(1.5)
        return "hapus"
    else:
        print("[Info] Membatalkan penghapusan data...")
        time.sleep(1.5)
        return None

def d_tambah_data(data, posisi):
    d_clear_terminal()
    print("===== TAMBAH DATA MAHASISWA BARU =====")
    nama_baru = input("=> Masukkan nama mahasiswa baru : ")
    while True:
        try:
            nilai_baru = int(input("=> Masukkan nilai mahasiswa baru : "))
            break
        except ValueError:
            print("[Error] Anda wajib memasukkan sebuah nilai berupa angka!")

    pesan = f"[y/n] Menambahkan mahasiswa baru : {nama_baru} = {nilai_baru}, ke dalam daftar :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data.append([nama_baru, nilai_baru])
        print("[Info] Data mahasiswa baru telah ditambahkan!")
        time.sleep(1.5)
        return "tambah"
    else:
        print("[Info] Membatalkan penambahan data...")
        time.sleep(1.5)
        return None

def d_edit_data(data, opsi, posisi):

    if opsi == "1":
        return d_edit_nama(data, posisi)

    elif opsi == "2":
        return d_edit_nilai(data, posisi)

    elif opsi == "3":
        return d_hapus_data(data, posisi)

    elif opsi == "4":
        return d_tambah_data(data, posisi)

def d_opsi_utama(pilihan, tampilan_menu):
    d_clear_terminal()
    tampilan_menu()
    while True:
        try:
            opsi = int(input("=> :"))
            if opsi in pilihan:
                d_clear_terminal()
                return opsi
            else:
                print("[Error] Masukkan perintah yang valid!")
        except ValueError:
            print("[Error] Masukkan perintah yang valid!")

def d_program_selesai():
    print()
    input("=> Enter untuk kembali :")

def d_clear_terminal():
    os.system("cls")

def d_loading(durasi, pesan, selesai):
    jeda = durasi / 100
    bar_loading = "#"

    print(f"{pesan}")

    for i in range(1, 100 + 1):
        jumlah_bar = i // 10
        print(f"\r{bar_loading * jumlah_bar}[{i}]%", end="", flush=True)
        time.sleep(jeda)

    print(f"\n{selesai}")

def d_opsi_sub(pilihan, pesan):
    print()
    while True:
        opsi = input(f"{pesan}")
        if opsi in pilihan:
            return opsi
        else:
            print("[Error] Masukkan perintah yang valid!")

opsi_utama = [1, 2, 3, 4, 5, 6]
opsi_accept = ["y", "n", "Y", "N"]
opsi_edit = ["1", "2", "3", "4", "5"]

while True:

    opsi = d_opsi_utama(opsi_utama, d_tampilkan_menu_utama)

    if opsi == 1:
        print("===== DAFTAR NILAI MAHASISWA =====")
        d_tampilkan_daftar(mahasiswa)
        d_program_selesai()

    elif opsi == 2:
        print("===== PREVIEW PERUBAHAN NAMA =====")
        hasil = d_merapikan_nama(mahasiswa)
        d_tampilkan_daftar(hasil)
        opsi = d_opsi_sub(opsi_accept, "[y/n] Setujui perubahan/perbaikan nama pada data asli :")
        if opsi.lower() == "y":
            d_loading(5, "[Info] Sedang melakukan perubahan pada data asli...", "[Info] Data asli telah diperbarui!")
            mahasiswa = hasil
            d_program_selesai()
        else:
            print("[Info] Membatalkan perubahan nama...")
            time.sleep(3)

    elif opsi == 3:
        cari = input("Cari nama/nilai :")
        hasil = d_merapikan_nama(mahasiswa)
        hasil = d_cari_data(hasil, cari)
        if len(hasil) == 0:
            print("Nama/Nilai yang anda cari tidak ditemukan!")
            d_program_selesai()
        else:
            d_tampilkan_daftar_tanpa_nomor(hasil)
            d_program_selesai()

    elif opsi == 4:
        print("===== EDIT DATA MAHASISWA =====")
        posisi = d_validasi_index_data(mahasiswa)

        while True:
            d_clear_terminal()
            print("===== EDIT DATA MAHASISWA =====")
            d_tampilkan_daftar_tanpa_nomor([mahasiswa[posisi]])
            print()
            d_tampilkan_menu_edit()
            sub_opsi = d_opsi_sub(opsi_edit, "=> :")

            if sub_opsi == "5":
                break

            status = d_edit_data(mahasiswa, sub_opsi, posisi)
            if status == "hapus" or status == "tambah":
                break

        d_program_selesai()

    elif opsi == 5:
        print("===== STATISTIK NILAI MAHASISWA =====")
        hasil = d_merapikan_nama(mahasiswa)
        d_tampilkan_statistik(hasil)
        d_program_selesai()

    elif opsi == 6:
        d_clear_terminal()
        print("Terima kasih telah menggunakan Sistem Data Mahasiswa!")
        break