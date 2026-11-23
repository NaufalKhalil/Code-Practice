"""
buat_cs.py
==========
Membuat file latihan C# baru dengan nomor otomatis + kerangka kode yang
biasa dipakai, lalu otomatis mengarahkan C#.csproj ke file baru tersebut.

Cara pakai:
  1. Letakkan script ini di folder latihan C# kamu (satu folder dengan
     file L001-..., L002-..., dst dan C#.csproj).
  2. Jalankan:  python buat_cs.py
  3. Ketik nama file (tanpa nomor & tanpa .cs), contoh:  For Loop
     -> terbuat  L018-For Loop.cs  (nomor = nomor terbesar yang ada + 1)
     -> C#.csproj otomatis menunjuk ke  L018-For Loop.cs
  4. Kosongkan input lalu Enter untuk selesai.

Nama class otomatis diambil dari nama file, contoh:
  L018-For Loop.cs  ->  class L018_For_Loop
"""

import os
import re

NAMESPACE = "Code_Practice"   # ganti di sini kalau namespace-nya berubah
AWALAN = "L"                  # awalan nomor file (L001, L002, ...)
DIGIT = 3                     # jumlah digit nomor (001, 002, ...)
NAMA_CSPROJ = "C#.csproj"     # ganti kalau nama file csproj-nya berbeda

TEMPLATE = """using System;

namespace {namespace}{{
    class {kelas}{{
        static void Main(string[] args){{

            

        }}
    }}
}}
"""

TEMPLATE_CSPROJ = """<Project Sdk="Microsoft.NET.Sdk">

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


def nomor_berikutnya(folder):
    """Cari nomor terbesar dari file Lxxx-*.cs di folder, lalu +1."""
    pola = re.compile(rf"^{AWALAN}(\d+)-", re.IGNORECASE)
    terbesar = 0
    for nama in os.listdir(folder):
        m = pola.match(nama)
        if m:
            terbesar = max(terbesar, int(m.group(1)))
    return terbesar + 1


def bersihkan_nama_file(nama):
    """Buang karakter yang tidak boleh ada di nama file Windows."""
    nama = re.sub(r'[\\/:*?"<>|]', "", nama)
    nama = re.sub(r"\s+", " ", nama).strip(" .")
    if nama.lower().endswith(".cs"):
        nama = nama[:-3].strip()
    return nama


def buat_nama_kelas(nama_file_tanpa_ext):
    """'L018-For Loop' -> 'L018_For_Loop' (hanya huruf, angka, underscore)."""
    kelas = re.sub(r"[^0-9A-Za-z]+", "_", nama_file_tanpa_ext).strip("_")
    return kelas


def update_csproj(folder, nama_file):
    """Arahkan C#.csproj ke file .cs yang baru dibuat."""
    path_csproj = os.path.join(folder, NAMA_CSPROJ)

    if not os.path.exists(path_csproj):
        print(f"⚠️   {NAMA_CSPROJ} tidak ditemukan, csproj tidak diperbarui.")
        return False

    with open(path_csproj, "w", encoding="utf-8") as f:
        f.write(TEMPLATE_CSPROJ.format(nama_file=nama_file))
    return True


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    print("=" * 60)
    print("  BUAT FILE LATIHAN C#")
    print("=" * 60)

    while True:
        nomor = nomor_berikutnya(folder)
        label = f"{AWALAN}{nomor:0{DIGIT}d}"

        try:
            masukan = input(f"\nNama file setelah {label}- (kosong = selesai): ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram dihentikan.")
            break

        nama = bersihkan_nama_file(masukan)
        if not masukan.strip():
            print("\nSelesai. Selamat belajar! 👋")
            break
        if not nama:
            print("⚠️   Nama tidak valid, coba lagi.")
            continue

        nama_tanpa_ext = f"{label}-{nama}"
        nama_file = nama_tanpa_ext + ".cs"
        path = os.path.join(folder, nama_file)

        if os.path.exists(path):
            print(f"⚠️   File '{nama_file}' sudah ada, tidak ditimpa.")
            continue

        kelas = buat_nama_kelas(nama_tanpa_ext)
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(namespace=NAMESPACE, kelas=kelas))

        print(f"✅  Dibuat : {nama_file}")
        print(f"    class  : {kelas}")

        if update_csproj(folder, nama_file):
            print(f"🔧  {NAMA_CSPROJ} sekarang menunjuk ke {nama_file}")


if __name__ == "__main__":
    main()
