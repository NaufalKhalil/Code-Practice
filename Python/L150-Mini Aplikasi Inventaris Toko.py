produk = [

    ["gaming mouse", "gaming", 250_000],
    ["mechanical keyboard", "gaming", 850_000],
    ["gaming chair", "gaming", 2_500_000],
    ["gaming headset", "gaming", 450_000],
    ["gamepad wireless", "gaming", 350_000],
    ["cooling pad laptop", "gaming", 180_000],

    ["office keyboard", "office", 300_000],
    ["office chair", "office", 1_500_000],
    ["office mouse", "office", 150_000],
    ["meja kerja minimalis", "office", 1_200_000],
    ["shredder kertas mini", "office", 350_000],
    ["papan jalan jepit", "office", 25_000],

    ["webcam hd", "aksesoris", 450_000],
    ["mouse pad xxl", "aksesoris", 120_000],
    ["usb hub type-c", "aksesoris", 150_000],
    ["kabel hdmi 2m", "aksesoris", 65_000],
    ["pouch organizer", "aksesoris", 80_000],
    ["cleaning kit lcd", "aksesoris", 30_000],

    ["desk lamp led", "belajar", 125_000],
    ["laptop stand", "belajar", 150_000],
    ["buku catatan a5", "belajar", 35_000],
    ["kalkulator ilmiah", "belajar", 220_000],
    ["rak buku meja", "belajar", 90_000],
    ["highlighter set", "belajar", 30_000]
]


flag = True

while flag == True:
    print()
    print("===== INVENTARIS TOKO =====")
    print("1. Lihat semua produk")
    print("2. Cari produk")
    print("3. Filter kategori")
    print("4. Produk termurah")
    print("5. Produk termahal")
    print("6. Keluar")
    print("---------------------------")

    input_user = input(f"=> Pilih Menu : ")

    print()
    print("---------------------------")

    if input_user == "1":
        print("=> Menampilkan semua produk :")
        for i in range(len(produk)):
            print(f"{i + 1}. {produk[i][0]} ({produk[i][1]}) - {produk[i][2]}")
    elif input_user == "2":
        cari = input("Cari produk :")
        cari = cari.lower()
        print()

        total = 0
        for i in range(len(produk)):
            if cari == produk[i][1] or cari in produk[i][0]:
                total += 1
                print(f"{total}. {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
        print()
        if total > 0:
            print(f"=> Sebanyak {total} Produk ditemukan.")
        else:
            print("Produk tidak ditemukan")
    
    elif input_user == "3":
        cari = input("Cari Kategori :")
        cari = cari.lower()
        print()

        total = 0
        for i in range(len(produk)):
            if cari == produk[i][1]:
                total += 1
                print(f"{total}. {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
        print()

        if total > 0:
            print(f"=> Sebanyak {total} Produk dengan kategori {cari} ditemukan.")
        else:
            print(f"Produk dengan kategori {cari} tidak ditemukan")
    
    elif input_user == "4":
        for i in range(len(produk)):
            if i == 0 :
                termurah = produk[i][2]
            elif termurah > produk[i][2]:
                termurah = produk[i][2]
        
        print("Produk termurah :")

        for i in range(len(produk)):
            if termurah == produk[i][2]:
                print(f"- {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
    
    elif input_user == "5":
        for i in range(len(produk)):
            if i == 0 :
                termahal = produk[i][2]
            elif termahal < produk[i][2]:
                termahal = produk[i][2]
        
        print("Produk termahal :")

        for i in range(len(produk)):
            if termahal == produk[i][2]:
                print(f"- {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
    
    elif input_user == "6":
        flag = False
    
    else:
        print("[Error] Masukkan perintah yang valid!")