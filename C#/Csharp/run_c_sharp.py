import os
import re

# Mendapatkan path folder tempat script Python ini berada secara otomatis
FOLDER_PROYEK = os.path.dirname(os.path.abspath(__file__))


def dapatkan_daftar_file_cs():
    # Mencari file .cs langsung di folder proyek C#
    files = [f for f in os.listdir(FOLDER_PROYEK) if f.endswith('.cs') and f.startswith('L')]
    files.sort()
    return files


def nomor_level(nama_file):
    # Ambil angka setelah huruf L, contoh: "L015-xxx.cs" -> 15
    cocok = re.match(r'L(\d+)', nama_file)
    return int(cocok.group(1)) if cocok else -1


def file_nomor_tertinggi(files):
    return max(files, key=nomor_level)


def file_terakhir_dimodifikasi(files):
    return max(files, key=lambda f: os.path.getmtime(os.path.join(FOLDER_PROYEK, f)))


def update_csproj(nama_file):
    csproj_file = os.path.join(FOLDER_PROYEK, 'C#.csproj')

    if not os.path.exists(csproj_file):
        print(f"[Error] File {csproj_file} tidak ditemukan!")
        return False

    isi_baru = f"""<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="{nama_file}" />
  </ItemGroup>

</Project>
"""
    with open(csproj_file, 'w', encoding='utf-8') as f:
        f.write(isi_baru)
    return True


def jalankan_file(file_terpilih):
    print(f"\n[Proses] Mengatur proyek untuk: {file_terpilih}")

    if update_csproj(file_terpilih):
        print("[Proses] Menjalankan dotnet run...\n")
        print("-" * 40)
        print()
        print()

        # Berpindah folder ke lokasi proyek C# sebelum menjalankan dotnet run
        perintah = f'cd /d "{FOLDER_PROYEK}" && dotnet run' if os.name == 'nt' else f'cd "{FOLDER_PROYEK}" && dotnet run'
        os.system(perintah)

        print()
        print()
        print("-" * 40)
        input("\nTekan Enter untuk kembali ke menu...")


def main():
    while True:
        # Daftar dimuat ulang tiap menu tampil, jadi file baru langsung terdeteksi
        files = dapatkan_daftar_file_cs()

        if not files:
            print(f"Tidak ada file latihan C# (.cs) yang ditemukan di: {FOLDER_PROYEK}")
            return

        tertinggi = file_nomor_tertinggi(files)
        dimodifikasi = file_terakhir_dimodifikasi(files)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== MENU PEMILIH FILE C# =====")
        for i, file in enumerate(files, 1):
            penanda = ""
            if file == tertinggi:
                penanda += "  <- level terbaru (Enter)"
            if file == dimodifikasi:
                penanda += "  <- terakhir diedit (m)"
            print(f"{i}. {file}{penanda}")
        print("0. Keluar")
        print("--------------------------------")

        masukan = input("Pilih nomor (Enter = level terbaru, m = terakhir diedit): ").strip().lower()

        # Enter saja -> jalankan file dengan nomor L tertinggi
        if masukan == "":
            jalankan_file(tertinggi)
            continue

        # m -> jalankan file yang terakhir dimodifikasi
        if masukan == "m":
            jalankan_file(dimodifikasi)
            continue

        try:
            pilihan = int(masukan)
        except ValueError:
            input("Masukkan angka yang valid! Tekan Enter untuk coba lagi...")
            continue

        if pilihan == 0:
            print("Keluar dari pembantu Python.")
            break
        elif 1 <= pilihan <= len(files):
            jalankan_file(files[pilihan - 1])
        else:
            input("Nomor tidak valid! Tekan Enter untuk coba lagi...")


if __name__ == "__main__":
    main()
