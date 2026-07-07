import os, time

buku = [
    ["Laskar Pelangi", "Andrea Hirata", 2005, 5],
    ["Atomic Habits", "James Clear", 2018, 3],
    ["Clean Code", "Robert C. Martin", 2008, 2],
    ["Filosofi Teras", "Henry Manampiring", 2018, 4],
    ["Bumi", "Tere Liye", 2014, 6],
    ["Sapiens", "Yuval Noah Harari", 2011, 3],
    ["The Psychology of Money", "Morgan Housel", 2020, 5],
    ["Laut Bercerita", "Leila S. Chudori", 2017, 2],
    ["Rich Dad Poor Dad", "Robert T. Kiyosaki", 1997, 4],
    ["Start With Why", "Simon Sinek", 2009, 3],
    ["Gadis Kretek", "Ratih Kumala", 2012, 4],
    ["Bumi Manusia", "Pramoedya Ananta Toer", 1980, 5],
    ["Cantik Itu Luka", "Eka Kurniawan", 2002, 3],
    ["Negeri 5 Menara", "Ahmad Fuadi", 2009, 6],
    ["Perahu Kertas", "Dee Lestari", 2009, 4],
    ["Pulang", "Leila S. Chudori", 2012, 2],
    ["Hujan", "Tere Liye", 2016, 7],
    ["Ronggeng Dukuh Paruk", "Ahmad Tohari", 1982, 3],
    ["Dilan 1990", "Pidi Baiq", 2014, 8],
    ["Ayat-Ayat Cinta", "Habiburrahman El Shirazy", 2004, 5],
    ["Supernova: Ksatria, Puteri, dan Bintang Jatuh", "Dee Lestari", 2001, 3],
    ["5 cm", "Donny Dhirgantoro", 2005, 6],
    ["Tenggelamnya Kapal Van der Wijck", "HAMKA", 1938, 4],
    ["The Alchemist", "Paulo Coelho", 1988, 5],
    ["Thinking, Fast and Slow", "Daniel Kahneman", 2011, 2],
    ["Good to Great", "Jim Collins", 2001, 4],
    ["The Lean Startup", "Eric Ries", 2011, 3],
    ["Zero to One", "Peter Thiel", 2014, 5],
    ["Deep Work", "Cal Newport", 2016, 4],
    ["Grit", "Angela Duckworth", 2016, 3],
    ["Ikigai", "Héctor García", 2016, 6],
    ["The 7 Habits of Highly Effective People", "Stephen R. Covey", 1989, 4],
    ["Man's Search for Meaning", "Viktor E. Frankl", 1946, 3],
    ["Educated", "Tara Westover", 2018, 2],
    ["Becoming", "Michelle Obama", 2018, 4],
    ["Shoe Dog", "Phil Knight", 2016, 5],
    ["The Subtle Art of Not Giving a F*ck", "Mark Manson", 2016, 6],
    ["Quiet", "Susan Cain", 2012, 3],
    ["Outliers", "Malcolm Gladwell", 2008, 4],
    ["Principles", "Ray Dalio", 2017, 3],
    ["The Intelligent Investor", "Benjamin Graham", 1949, 2],
    ["Zero Limits", "Joe Vitale", 2007, 3],
    ["The Power of Habit", "Charles Duhigg", 2012, 5],
    ["Drive", "Daniel H. Pink", 2009, 4],
    ["Mindset", "Carol S. Dweck", 2006, 5],
    ["Hyperfocus", "Chris Bailey", 2018, 3],
    ["Factfulness", "Hans Rosling", 2018, 4],
    ["Originals", "Adam Grant", 2016, 3],
    ["Almond", "Sohn Won-pyung", 2017, 5],
    ["Kim Ji-young, Born 1982", "Cho Nam-joo", 2016, 4]
]

def d_clear():
    os.system("cls")

def d_tampilkan_menu_utama():
    print("========== PERPUSTAKAAN ==========")
    print("1. Lihat Semua Buku")
    print("2. Cari Buku")
    print("3. Tambah Buku")
    print("4. Edit Buku")
    print("5. Pinjam Buku")
    print("6. Kembalikan Buku")
    print("7. Statistik")
    print("8. Keluar")

def d_tampilkan_menu_edit_buku():
    print("========== EDIT BUKU ==========")
    print("1. Edit nama buku ")
    print("2. Edit penulis buku")
    print("3. Edit tahun buku")
    print("4. Edit stock buku")
    print("5. Hapus buku dari daftar")
    print("6. Cancel edit, Kembali ke menu utama")

def d_tampilkan_daftar_nomor(data):
    for i in range(len(data)):
        print(f"{i + 1}.[ {data[i][0]} ]")
        print(f"-> Penulis      : {data[i][1]}")
        print(f"-> Tahun terbit : {data[i][2]}")
        print(f"-> Stock buku   : {data[i][3]}")
        print("-" * 32)

def d_tampilkan_daftar_tanpa_nomor(data):
    for i in range(len(data)):
        print(f"=> [ {data[i][0]} ]")
        print(f"-> Penulis      : {data[i][1]}")
        print(f"-> Tahun terbit : {data[i][2]}")
        print(f"-> Stock buku   : {data[i][3]}")
        print()

def d_edit_buku(data, nomor_buku, index, edit):
    nomor_buku -= 1
    data[nomor_buku][index] = edit

def d_cegah_input_kosong(pesan_input, pesan_error):
    while True:
        input_user = input(pesan_input)
        if not input_user.strip():
            print(pesan_error)
        else:
            return input_user

def d_cari(data, cari, index):
    hasil = []
    
    if index == 0 or index == 1:
        for i in range(len(data)):
            if cari in data[i][index]:
                hasil.append(data[i])
    elif index == 2 or index == 3:
        for i in range(len(data)):
            if cari == data[i][index]:
                hasil.append(data[i])
    return hasil

def d_int_or_string(input_user):
    if input_user.isdigit():
        input_user = int(input_user)
    return input_user

def d_program_selesai():
    input("=> Tekan [Enter] untuk kembali : ")
    d_clear()

def d_pesan_opsi_not_valid():
    print("[ERROR] Input tidak valid!")

def d_acc_opsi(pesan):
    opsi = input(f"[y/n] {pesan}").lower()
    if opsi == "y":
        opsi = True
    elif opsi == "n":
        opsi = False

while True:
    
    d_tampilkan_menu_utama()

    opsi = input("=> : ")

    if opsi == "1":
        d_clear()
        print("========== DAFTAR BUKU ==========")
        d_tampilkan_daftar_nomor(buku)
        d_program_selesai()
    
    elif opsi == "2":
        d_clear()
        cari = d_cegah_input_kosong("=> Cari : ", "[INFO] Input kosong!")
        print("=" * 32)
        cari = d_int_or_string(cari)
        hasil_pencarian_ada = False
        if isinstance(cari, str):
            index = 0
            hasil = d_cari(buku, cari, index)
            if len(hasil) != 0:
                hasil_pencarian_ada = True
                print(f"===> Nama buku : {cari}")
                print("-" * 32)
                d_tampilkan_daftar_tanpa_nomor(hasil)
            
            index = 1
            hasil = d_cari(buku, cari, index)
            if len(hasil) != 0:
                hasil_pencarian_ada = True
                print(f"===> Nama penulis buku : {cari}")
                print("-" * 32)
                d_tampilkan_daftar_tanpa_nomor(hasil)

        elif isinstance(cari, int):
            index = 2
            hasil = d_cari(buku, cari, index)
            if len(hasil) != 0:
                hasil_pencarian_ada = True
                print(f"===> Buku dengan tahun terbit : {cari}")
                print("-" * 32)
                d_tampilkan_daftar_tanpa_nomor(hasil)

            index = 3
            hasil = d_cari(buku, cari, index)
            if len(hasil) != 0:
                hasil_pencarian_ada = True
                print(f"===> Buku dengan jumlah stock : {cari}")
                print("-" * 32)
                d_tampilkan_daftar_tanpa_nomor(hasil)
        if hasil_pencarian_ada == False:
            print(f'[INFO] Hasil pencarian untuk "{cari}" tidak ditemukan pada pustaka data (Judul, Penulis, Tahun, Stok).')
        d_program_selesai()
    elif opsi == "3":
        None    

    elif opsi == "4":
        d_clear()
        print("========== DAFTAR BUKU ==========")
        d_tampilkan_daftar_nomor(buku)
        
        while True:
            while True:
                try:
                    nomor_buku = int(input("=> Masukkan nomor buku : "))
                    break
                except ValueError:
                    print("[Error] Anda tidak memasukkan sebuah angka!")
            

            if nomor_buku > len(buku) or nomor_buku < 1:
                print(f"[ERROR] Tidak ditemukan buku dengan nomor {nomor_buku}")
            else:
                break
        
        d_clear()
        d_tampilkan_menu_edit_buku()

        while True:
            opsi = input("=> : ")
            pesan = "[INFO] Input kosong!"    

            if opsi == "1": #edit nama
                edit = input(f'=> Ubah judul buku dari "{buku[nomor_buku - 1][0]}", Menjadi : ')
                hasil = d_edit_buku(buku, nomor_buku, 0, edit)
                d_acc_opsi("")
            elif opsi == "2": #edit penulis
                input_user = input(f'=> Ubah penulis buku dari "{buku[nomor_buku - 1][1]}", Menjadi : ')
                rename = d_int_or_string(input_user, pesan)
            elif opsi == "3": #edit tahun
                input_user = f'=> ubah tahun terbit buku dari "{buku[nomor_buku - 1][2]}", Menjadi : '
                rename = d_int_or_string(input_user, pesan)
            elif opsi == "4": #edit stock
                input_user = f'=> ubah jumlah stock buku dari "{buku[nomor_buku - 1][3]}", Menjadi : '
                rename = d_int_or_string(input_user, pesan)
            elif opsi == "5": #hapus buku
                None
            elif opsi == "6": #cancel
                break
            else:
                d_pesan_opsi_not_valid()








