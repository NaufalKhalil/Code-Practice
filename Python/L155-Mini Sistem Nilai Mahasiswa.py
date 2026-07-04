mahasiswa = [
    ["Andi", 85],
    ["Budi", 72],
    ["Citra", 91],
    ["Dinda", 68],
    ["Eko", 77],
    ["Farah", 95],
    ["Galih", 80]
]


#menampilkan menu
def tampilkan_menu():
    print()
    print("===== SISTEM NILAI =====")
    print("1. Lihat semua mahasiswa")
    print("2. Cari mahasiswa")
    print("3. Nilai tertinggi")
    print("4. Nilai terendah")
    print("5. Rata-rata nilai")
    print("6. Keluar")
    print()


#menampilkan semua mahasiswa
def tampilkan_semua_data(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} = {data[i][1]}")


#mengurutkan tertinggi - terendah
def mengurutkan_max_min(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    tertinggi = data[0][1]
    terendah = data[len(data) - 1][1]
    return data, tertinggi, terendah


#mencari nama mahasiswa
def mencari_nama(data, cari):
    ketemu = False
    for i in range(len(data)):
        if cari == data[i][0]:
            print(f"-> {data[i][0]} = {data[i][1]}")
            ketemu = True
    if ketemu == False:
        print(f"Mahasiswa dengan nama {cari}, Tidak ditemukan dalam daftar!")


#menampilkan nama mahasiswa dengan nilai tertentu
def menampilkan_nilai_tertentu(data, cari_nilai):
    for i in range(len(data)):
        if cari_nilai == data[i][1]:
            print(f"{i + 1}. {data[i][0]} = {data[i][1]}")


#mencari rata-rata
def mencari_rata_rata(data):
    total = 0
    for i in range(len(data)):
        total += data[i][1]
    rata_rata = total / len(data)
    rata_rata = round(rata_rata, 2)
    return rata_rata


tampil = True #mencegah menu tercetak ketika perintah invalid

while True :

    if tampil == True: #mencegah menu tercetak ketika perintah invalid
        tampilkan_menu()
    tampil = False

    opsi = input("=> Masukkan Perintah :")

    #eksekusi perintah
    if opsi == "1": #tampilkan semua
        print()
        print("===[Daftar Nilai Mahasiswa]===")

        hasil, _, _ = mengurutkan_max_min(mahasiswa)
        tampilkan_semua_data(hasil)

        input("Tekan (Enter) untuk kembali ke menu utama ->")
        tampil = True

    elif opsi == "2": #cari nama
        print()

        cari = input("Cari nama :")
        mencari_nama(mahasiswa, cari)

        input("Tekan (Enter) untuk kembali ke menu utama ->")
        tampil = True

    elif opsi == "3": #nilai tertinggi
        print()
        print("=> Mahasiswa dengan nilai tertinggi :")

        hasil, nilai_tertinggi, _ = mengurutkan_max_min(mahasiswa)
        menampilkan_nilai_tertentu(hasil, nilai_tertinggi)

        input("Tekan (Enter) untuk kembali ke menu utama ->")
        tampil = True

    elif opsi == "4": #nilai terendah
        print()
        print("=> Mahasiswa dengan nilai terendah :")

        hasil, _, nilai_terendah = mengurutkan_max_min(mahasiswa)
        menampilkan_nilai_tertentu(hasil, nilai_terendah)

        input("Tekan (Enter) untuk kembali ke menu utama ->")
        tampil = True

    elif opsi == "5": #nilai rata-rata semua mahasiswa
        print()
        hasil = mencari_rata_rata(mahasiswa)
        print(f"=> Rata-rata nilai seluruh Mahasiswa : {hasil}")

        input("Tekan (Enter) untuk kembali ke menu utama ->")
        tampil = True

    elif opsi == "6": #keluar dari program
        print("[Info] Keluar dari program...")
        break

    else: #perintah invalid!
        tampil = False
        print("[Error] Masukkan perintah yang valid!")