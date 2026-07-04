import os

def clear():
    os.system("cls")

array_produk = [

    ["Gaming Mouse", "Gaming", 250000, 10],
    ["Mechanical Keyboard", "Gaming", 850000, 5],
    ["Gaming Chair", "Gaming", 2500000, 2],
    ["Gaming Headset", "Gaming", 600000, 12],
    ["Monitor Gaming 24 Inc", "Gaming", 1800000, 4],
    ["Mousepad RGB", "Gaming", 120000, 20],
    
    ["Wireless Office Mouse", "Office", 180000, 14],
    ["Laptop Stand Aluminium", "Office", 220000, 9],
    ["Desk Mat Felt", "Office", 130000, 0],
    ["Ergonomic Footrest", "Office", 250000, 7],
    ["Office Keyboard", "Office", 300000, 8],
    ["Office Chair", "Office", 1500000, 3],

    ["Microphone Kondensor", "Aksesoris", 550000, 0],
    ["Ring Light LED", "Aksesoris", 175000, 13],
    ["Kabel HDMI 4K", "Aksesoris", 85000, 25],
    ["External SSD 1TB", "Aksesoris", 1250000, 8],
    ["Speaker Bluetooth", "Aksesoris", 350000, 10],
    ["Cooling Pad Laptop", "Aksesoris", 140000, 18],
    ["Webcam HD", "Aksesoris", 450000, 7],
    ["USB Hub", "Aksesoris", 150000, 15]

]

#def tampilkan menu

def d_tampilkan_menu():
    print("===== MENU UTAMA =====")
    print("1. Lihat Semua Produk")
    print("2. Cari")
    print("3. Edit Produk")
    print("4. Keluar")
    print()

def d_menampilkan_sub_menu_cari():
    print("===== MENU CARI =====")
    print("1. Cari produk")
    print("2. Cari Kategori")
    print("3. Cari Harga")
    print("4. Cari Stock")
    print("5. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_sub_menu_harga():
    print("===== MENU HARGA PRODUK =====")
    print("1. Cari Produk dengan harga tertentu")
    print("2. Cari produk dengan harga tertinggi")
    print("3. Cari Produk dengan harga terendah")
    print("4. Total inventaris gudang")
    print("5. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_sub_menu_stock():
    print("===== MENU STOCK PRODUK =====")
    print("1. Cari Produk dengan stock tertentu")
    print("2. Cari Produk dengan stock tertinggi")
    print("3. Cari Produk dengan stock terendah/kosong")
    print("4. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_menu_edit_produk():
    print("===== MENU EDIT PRODUK =====")
    print("1. Edit Nama Produk")
    print("2. Edit Kategori Produk")
    print("3. Edit Harga Produk")
    print("4. Edit Stock Produk")
    print("5. Batalkan Edit Produk")
    print()


#def tampilkan hasil dari fungsi

def d_menampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]})")
        print(f"   -> Harga: Rp.{data[i][2]}.")
        print(f"   -> Stock: {data[i][3]}")
        print()

def d_menampilkan_produk_tanpa_nomor(data):
    for i in range(len(data)):
        print(f"==> {data[i][0]} ({data[i][1]})")
        print(f" -> Harga: Rp.{data[i][2]}.")
        print(f" -> Stock: {data[i][3]}")
        print()

#def cari

def d_validasi_array(data, cari):
    cari += 1
    valid = False
    if cari <= len(data) and cari >= 0:
        valid = True
        return valid
    else :
        return valid
    
def d_cari_array(data, cari):
    array_ketemu = []
    array_ketemu.append(data[cari])
    return array_ketemu

def d_cari_produk(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari in data[i][0]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_kategori(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][1]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_harga(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][2]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_stock(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][3]:
            array_ketemu.append(data[i])
    return array_ketemu

#def fungsi max, min, total all inventaris

#harga max/min
def d_cari_harga_max(data):
    for i in range(len(data)):
        if i == 0 :
            harga_max = data[i][2]
        elif harga_max < data[i][2]:
            harga_max = data[i][2]
    return harga_max

def d_cari_harga_min(data):
    for i in range(len(data)):
        if i == 0 :
            harga_min = data[i][2]
        elif harga_min > data[i][2]:
            harga_min = data[i][2]
    return harga_min

#stock max/min
def d_cari_stock_max(data):
    for i in range(len(data)):
        if i == 0 :
            stock_max = data[i][3]
        elif stock_max < data[i][3]:
            stock_max = data[i][3]
    return stock_max

def d_cari_stock_min(data):
    for i in range(len(data)):
        if i == 0 :
            stock_min = data[i][3]
        elif stock_min > data[i][3]:
            stock_min = data[i][3]
    return stock_min

#def edit
def d_edit_nama(data, posisi, nama):
    data[posisi][0] = nama

def d_edit_kategori(data, posisi, kategori):
    data[posisi][1] = kategori

def d_edit_harga(data, posisi, harga):
    data[posisi][2] = harga

def d_edit_stock(data, posisi, stock):
    data[posisi][3] = stock

#total invetaris
def d_total_nilai_gudang(data):
    total = 0
    for i in range(len(data)):
        total += (data[i][2] * data[i][3])
    return total

def d_total_stock_gudang(data):
    total = 0
    for i in range(len(data)):
        total += data[i][3]
    return total

menu_tampil = True

while True:

    #mencegah menu tercetak ketika perintah invalid
    if menu_tampil == True:
        clear()
        d_tampilkan_menu()
    menu_tampil = False

    opsi = input("=> Pilih Menu : ")
    
    #eksekusi perintah
    if opsi == "1":
        clear()
        print("===== SEMUA PRODUK =====")
        print()
        d_menampilkan_produk(array_produk)

        program_selesai = input("Tekan (Enter) untuk kembali ke menu utama ->")
        menu_tampil = True
        clear()
        
    elif opsi == "2":

        clear()
        menu_tampil = True

        while True:

            if menu_tampil == True:
                d_menampilkan_sub_menu_cari()
            menu_tampil = False

            sub_opsi_2 = input("=> Pilih Menu : ")

            if sub_opsi_2 == "1": #cari produk

                clear()
                cari = input("Cari Nama Produk : ")
                print()

                hasil = d_cari_produk(array_produk, cari)
                if len(hasil) == 0 :
                    print(f"Produk dengan nama : {cari}, Tidak ditemukan!")
                else :
                    d_menampilkan_produk_tanpa_nomor(hasil)

                program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                clear()
                menu_tampil = True

            elif sub_opsi_2 == "2": #cari kategori
                
                clear()
                cari = input("Cari Kategori Produk : ")
                print()

                hasil = d_cari_kategori(array_produk, cari)
                if len(hasil) == 0 :
                    print(f"Produk dengan kategori : {cari}, Tidak ditemukan!")
                else :
                    d_menampilkan_produk_tanpa_nomor(hasil)

                program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                clear()
                menu_tampil = True

            elif sub_opsi_2 == "3": #cari harga

                menu_tampil = True
                clear()
                
                while True:  

                    if menu_tampil == True:
                        d_menampilkan_sub_sub_menu_harga()
                    menu_tampil = False

                    sub_sub_opsi_3 = input("=> Pilih Menu : ")

                    if sub_sub_opsi_3 == "1":

                        clear()
                        cari = int(input("Cari Harga Produk : "))
                        print()

                        hasil = d_cari_harga(array_produk, cari)
                        if len(hasil) == 0 :
                            print(f"Produk dengan harga : {cari}, Tidak ditemukan!")
                        else :
                            d_menampilkan_produk_tanpa_nomor(hasil)

                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "2":

                        clear()
                        print("===== PRODUK DENGAN HARGA TERTINGGI =====")
                        
                        hasil = d_cari_harga_max(array_produk)
                        hasil = d_cari_harga(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True
                        
                    elif sub_sub_opsi_3 == "3":

                        clear()
                        print("===== PRODUK DENGAN HARGA TERENDAH/KOSONG =====")
                        
                        hasil = d_cari_harga_min(array_produk)
                        hasil = d_cari_harga(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "4":

                        clear()
                        print("===== TOTAL INVENTARIS GUDANG =====")
                        
                        hasil = d_total_nilai_gudang(array_produk)
                        print(f"-> Harga Total Gudang    : {hasil}")
                        
                        hasil = d_total_stock_gudang(array_produk)
                        print(f"-> Stock Barang Tersedia : {hasil}")

                        print(f"-> Jumlah Jenis Barang   : {len(array_produk)}")

                        hasil = d_cari_stock(array_produk, 0)
                        if len(hasil) != 0:
                            print()
                            print("[Peringatan]")
                            print(f"-> Terdapat {len(hasil)} Produk dengan stock kosong! ")

                        print()
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "5":

                        clear()
                        menu_tampil = True
                        break

                    else:
                        menu_tampil = False
                        print("[Error] Masukkan perintah yang valid!")
                        

            elif sub_opsi_2 == "4": #cari stock
                
                menu_tampil = True
                clear()

                while True:  

                    if menu_tampil == True:
                        d_menampilkan_sub_sub_menu_stock()
                    menu_tampil = False

                    sub_sub_opsi_3 = input("=> Pilih Menu : ")

                    if sub_sub_opsi_3 == "1":

                        clear()
                        cari = int(input("Cari Stock Produk : "))
                        print()

                        hasil = d_cari_stock(array_produk, cari)
                        if len(hasil) == 0 :
                            print(f"Produk dengan stock : {cari}, Tidak ditemukan!")
                        else :
                            d_menampilkan_produk_tanpa_nomor(hasil)

                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "2":

                        clear()
                        print("===== PRODUK DENGAN STOCK BARANG TERTINGGI =====")
                        
                        hasil = d_cari_stock_max(array_produk)
                        hasil = d_cari_stock(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True
                        
                    elif sub_sub_opsi_3 == "3":

                        clear()
                        print("===== PRODUK DENGAN STOCK BARANG TERENDAH/KOSONG =====")
                        
                        hasil = d_cari_stock_min(array_produk)
                        hasil = d_cari_stock(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "4":

                        clear()
                        menu_tampil = True
                        break

                    else :
                        print("[Error] Masukkan perintah yang valid!")

                clear()

            elif sub_opsi_2 == "5": #kembali ke menu utama
                clear()
                menu_tampil = True
                break

            else:
                print("[Error] Masukkan perintah yang valid!")
        
        clear()

    elif opsi == "3":

        menu_tampil = True
        clear()

        while True:
            
            print()
            if menu_tampil == True :
                print("===== EDIT PRODUK =====")
                d_menampilkan_produk(array_produk)
            menu_tampil = False

            
            sub_opsi_3 = int(input("=> Masukkan Nomor Barang, 0 = Kembali Ke Menu Utama : "))
            sub_opsi_3 -= 1
            valid = d_validasi_array(array_produk, sub_opsi_3)

            if sub_opsi_3 == -1:
                break
            elif valid == False:
                print(f"Produk dengan nomor barang {sub_opsi_3 + 1}, Tidak ditemukan... Nomor barang di luar jangkauan data.")
                menu_tampil = False
            else:
                
                hasil = d_cari_array(array_produk, sub_opsi_3)

                clear()
                print("===== EDIT PRODUK =====")
                print(f">>> Nomor Produk : {sub_opsi_3 + 1} <<<")
                print()
                d_menampilkan_produk_tanpa_nomor(hasil)
                print()

                menu_tampil = True

                while True:

                    if menu_tampil == True:
                        d_menampilkan_sub_menu_edit_produk()
                        menu_tampil = False

                    sub_sub_opsi_ada = input("=> Pilih Menu : ")

                    clear()
                    if sub_sub_opsi_ada == "1":
                        isi = input(f"=> Ganti Nama Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : ")
                        d_edit_nama(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "2":
                        isi = input(f"=> Ganti Kategori Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : ")
                        d_edit_kategori(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "3":
                        isi = int(input(f"=> Ganti Harga Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : "))
                        d_edit_harga(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "4":
                        isi = int(input(f"=> Ganti Stock Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : "))
                        d_edit_stock(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "5":
                        menu_tampil = True
                        break
                    else :
                        print("[Error] Masukkan perintah yang valid!")
                        menu_tampil = False

        menu_tampil = True

    elif opsi == "4":
        
        print("[Info] Keluar dari program...")
        break
    
    else:
        print("[Error] Masukkan perintah yang valid!")