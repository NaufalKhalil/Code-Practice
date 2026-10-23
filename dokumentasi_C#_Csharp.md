# Csharp

- **Dibuat:** 2026-10-24 00:10:11
- **Sumber:** `d:\Project\Coding\Code Practice\C#\Csharp`
- **Total file:** 16 (0 sub-folder disertakan)

- **Bahasa dominan:** C# (14 dari 16 file)

## Konteks & Peraturan untuk AI — Baca Ini Dulu

Halo AI! Ini adalah sesi lanjutan belajar C# seorang pemula. Obrolan sebelumnya sudah mencapai batas token sehingga chat dibuka ulang. File ini berisi seluruh kode yang sudah pernah dibuat sebagai bukti progres belajar.

Tugasmu adalah menjadi tutor/mentor C# interaktif dengan aturan berikut:

### Aturan Pemberian Soal

1. **Jangan** beri jawaban kode lengkap sebelum pengguna mengatakan kata "menyerah". Sebelum itu, hanya boleh memberi clue/petunjuk.
2. Jika pengguna mengatakan "menyerah", barulah tampilkan kode jawaban lengkap beserta penjelasannya.
3. Jika kode yang dikirim pengguna **salah** atau belum lulus:
   - Jangan langsung kasih jawaban.
   - Berikan petunjuk/clue yang mengarahkan ke kesalahan.
   - Tanyakan apakah mau coba lagi atau menyerah.
4. Soal level berikutnya **hanya** boleh diberikan setelah kode pengguna dinyatakan benar/lulus oleh kamu.
5. Tingkat kesulitan soal harus disesuaikan dengan level:
   - Level rendah → soal sederhana, 1 konsep, cocok untuk pemula.
   - Level tinggi → soal lebih kompleks, bisa gabungan beberapa konsep.
   - Naik level hanya jika sudah lulus soal sebelumnya.
6. Soal harus selalu bisa dipahami pemula:
   - Gunakan bahasa yang mudah dan jelas.
   - Sertakan contoh input/output (atau tampilan) yang diharapkan.
   - Jangan gunakan library/NuGet package eksternal kecuali sudah di level lanjut.
7. Lihat daftar kode di bawah untuk mengetahui syntax dan topik apa saja yang sudah pernah dipelajari. Gunakan ini sebagai acuan level dan titik lanjut pembelajaran.
8. Setiap soal harus punya nama level yang jelas dan sesuai dengan materi/topik soal tersebut (contoh: "Level 3 - Looping Dasar (for)", "Level 5 - Array & Pencarian Nilai"). Jangan hanya menulis "Level 3" tanpa nama topiknya.
9. Soal sebisa mungkin relate/relevan dengan kasus nyata, bukan sekadar soal abstrak/teoretis (contoh: hitung total belanja kasir, validasi input umur, cari nilai tertinggi dari daftar nilai siswa, dsb).
10. Setiap soal harus menyertakan aturan syntax apa saja yang boleh digunakan untuk mengerjakannya. Utamakan membatasi syntax ke yang sudah dikuasai pemula, supaya fundamental/pondasi logikanya kuat dulu (contoh: "Boleh pakai: variabel, if/else, perulangan for. Belum boleh pakai: LINQ seperti Max(), OrderBy().").
11. Syntax/fungsi baru yang lebih ringkas boleh di-unlock jika fundamental pengguna di topik terkait sudah cukup kuat (setelah pengguna lancar mencari nilai tertinggi/terendah di array secara manual, barulah boleh dikenalkan shortcut seperti LINQ Max()/Min()). Jelaskan bahwa ini "unlock syntax baru" sebagai bentuk progres, bukan diberikan dari awal.
12. Materi/topik baru boleh di-unlock jika materi sebelumnya sudah dikuasai dengan baik, bukan cuma sekali lulus, tapi sudah cukup beberapa soal di topik tersebut. Saat unlock materi baru, beri tahu pengguna secara eksplisit bahwa ini adalah materi baru yang baru dibuka.

### Cara Memulai Sesi Ini

Setelah membaca file ini, sambut pengguna dan tanyakan: "Mau lanjut dari mana? Minta soal baru, atau ada topik tertentu?"

---

## Struktur

```
Csharp/
├── build_cs_template.py
├── L001-Variabel dan Output Dasar.cs
├── L002-Input dari User.cs
├── L003-Operasi Aritmatika.cs
├── L004-Pembagian Desimal.cs
├── L005-Percabangan if.cs
├── L006-If dan Operator Logika.cs
├── L007-Validasi Input Nilai.cs
├── L008-Operator Logika AND.cs
├── L009-Operator Logika OR.cs
├── L010-Nested if.cs
├── L011-Switch.cs
├── L012-Switch dan Operasi.cs
├── L013-Validasi Pembagian.cs
├── L014-While Loop.cs
└── run_c_sharp.py
```

## Daftar Isi

- [L001-Variabel dan Output Dasar.cs](#l001-variabel-dan-output-dasarcs)
- [L002-Input dari User.cs](#l002-input-dari-usercs)
- [L003-Operasi Aritmatika.cs](#l003-operasi-aritmatikacs)
- [L004-Pembagian Desimal.cs](#l004-pembagian-desimalcs)
- [L005-Percabangan if.cs](#l005-percabangan-ifcs)
- [L006-If dan Operator Logika.cs](#l006-if-dan-operator-logikacs)
- [L007-Validasi Input Nilai.cs](#l007-validasi-input-nilaics)
- [L008-Operator Logika AND.cs](#l008-operator-logika-andcs)
- [L009-Operator Logika OR.cs](#l009-operator-logika-orcs)
- [L010-Nested if.cs](#l010-nested-ifcs)
- [L011-Switch.cs](#l011-switchcs)
- [L012-Switch dan Operasi.cs](#l012-switch-dan-operasics)
- [L013-Validasi Pembagian.cs](#l013-validasi-pembagiancs)
- [L014-While Loop.cs](#l014-while-loopcs)
- [build_cs_template.py](#build_cs_templatepy)
- [run_c_sharp.py](#run_c_sharppy)

## File

### `L001-Variabel dan Output Dasar.cs`

```csharp
﻿using System;

namespace Code_Practice{
    class L001_Variabel_dan_Output_Dasar{
        static void Main(string[] args){
        
            string Nama = "Naufal";
            int Umur = 18;
            string Asal_kota = "Medan";

            Console.WriteLine(Nama);
            Console.WriteLine(Umur);
            Console.WriteLine(Asal_kota);
        
        }
    }
}
```

### `L002-Input dari User.cs`

```csharp
using System;

namespace Code_Practice{
    class L002_Input_dari_User{
        static void Main(string[] args){

            Console.WriteLine("Masukkan Nama :");
            string nama = Console.ReadLine();
            Console.WriteLine("Masukkan Umur :");
            int umur = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(nama);
            Console.WriteLine(umur);
        
        }    
    }
}
```

### `L003-Operasi Aritmatika.cs`

```csharp
using System;

namespace Code_Practice{
    class L003_Operasi_Aritmatika{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama :");
            int Angka_Pertama = Convert.ToInt32(Console.ReadLine());
            Console.Write("Masukkan angka kedua :");
            int Angka_Kedua = Convert.ToInt32(Console.ReadLine());

            int Hasil_Penjumlahan = Angka_Pertama + Angka_Kedua;
            int Hasil_Pengurangan = Angka_Pertama - Angka_Kedua;
            int Hasil_Perkalian = Angka_Pertama * Angka_Kedua;
            int Hasil_Pembagian = Angka_Pertama / Angka_Kedua;

            Console.WriteLine("Hasil Penjumlahan    : " + Hasil_Penjumlahan);
            Console.WriteLine("Hasil Pengurangan    : " + Hasil_Pengurangan);
            Console.WriteLine("Hasil Perkalian      : " + Hasil_Perkalian);
            Console.WriteLine("Hasil Pembagian      : " + Hasil_Pembagian);

        }
    }
}
```

### `L004-Pembagian Desimal.cs`

```csharp
using System;

namespace Code_Practice{
    class L004_Pembagian_Desimal{
        static void Main(string[] args){
            
            Console.Write("Masukkan angka pertama   : ");
            double Angka_Pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan angka kedua     : ");
            double Angka_Kedua = double.Parse(Console.ReadLine());
            
            Console.WriteLine(" ");
            
            double Hasil_Penjumlahan = Angka_Pertama + Angka_Kedua;
            double Hasil_Pengurangan = Angka_Pertama - Angka_Kedua;
            double Hasil_Perkalian = Angka_Pertama * Angka_Kedua;
            double Hasil_Pembagian = Angka_Pertama / Angka_Kedua; 
            
            Console.WriteLine("Hasil Penjumlahan    = " + Hasil_Penjumlahan);
            Console.WriteLine("Hasil Pengurangan    = " + Hasil_Pengurangan);
            Console.WriteLine("Hasil Perkalian      = " + Hasil_Perkalian);
            Console.WriteLine("Hasil Pembagian      = " + Hasil_Pembagian);

        }
    }
}
```

### `L005-Percabangan if.cs`

```csharp
using System;

namespace Code_Practice{
    class L005_Percabangan_if{
        static void Main(string[] args){

            Console.Write("Masukkan Angka : ");
            double Angka = double.Parse(Console.ReadLine()); 

            if (Angka == 0 ){
                Console.WriteLine("Angka tersebut adalah nol.");
            }
            else if (Angka > 0 ){
                Console.WriteLine("Angka tersebut adalah positif.");
            }
            else {
                Console.WriteLine("Angka tersebut adalah negatif.");
            }

        }
    }
}
```

### `L006-If dan Operator Logika.cs`

```csharp
using System;

namespace Code_Practice{
    class L006_If_dan_Operator_Logika{
        static void Main(string[] args){

            Console.Write("Masukkan Nilai : ");
            double Nilai = double.Parse(Console.ReadLine());

            if (Nilai < 60){
                Console.WriteLine("Kurang");
            }
            else if (Nilai < 70){
                Console.WriteLine("Cukup");
            }
            else if (Nilai < 80){
                Console.WriteLine("Baik");
            }
            else if (Nilai <= 100){
                Console.WriteLine("Sangat Baik");
            }


        }
    }
}
```

### `L007-Validasi Input Nilai.cs`

```csharp
using System;

namespace Code_Practice{
    class L007_Validasi_Input_Nilai{
        static void Main(string[] args){

            Console.Write("Masukkan Nilai : ");
            double Nilai = double.Parse(Console.ReadLine());

            if (Nilai < 0 ){
                Console.WriteLine("[Error] Nilai tidak valid!");
            }
            else if (Nilai < 60){
                Console.WriteLine("Kurang");
            }
            else if (Nilai < 70){
                Console.WriteLine("Cukup");
            }
            else if (Nilai < 80){
                Console.WriteLine("Baik");
            }
            else if (Nilai <= 100){
                Console.WriteLine("Sangat Baik");
            } else {
                Console.WriteLine("[Error] Nilai tidak valid!");
            }


        }
    }
}
```

### `L008-Operator Logika AND.cs`

```csharp
using System;

namespace Code_Practice{
    class L008_Operator_Logika_AND{
        static void Main(string[] args){

            Console.Write("Masukkan umur anda : ");
            int Umur = int.Parse(Console.ReadLine());

            if (Umur >= 0 && Umur <= 12){
                Console.WriteLine("Anak - Anak");
            }
            else if (Umur >= 13 && Umur <= 17){
                Console.WriteLine("Remaja");
            }
            else if (Umur >= 18 && Umur <= 59){
                Console.WriteLine("Dewasa");
            }
            else if (Umur >= 60 ){
                Console.WriteLine("Lansia");
            }
            else {
                Console.WriteLine("[Error] Usia anda tidak valid!");
            }

        }
    }
}
```

### `L009-Operator Logika OR.cs`

```csharp
using System;

namespace Code_Practice{
    class L009_Operator_Logika_OR{
        static void Main(string[] args){

            Console.Write("Masukkan Hari : ");
            string Hari = Console.ReadLine();
            
            if (Hari == "Sabtu" || Hari == "Minggu"){
                Console.WriteLine("Hari libur");
            }
            else if (Hari == "Senin" || Hari == "Selasa" || Hari == "Rabu" || Hari == "Kamis" || Hari == "Jumat"){
                Console.WriteLine("Hari Kerja");
            }
            else {
                Console.WriteLine("[Error] Anda memasukkan hari yang tidak valid!");
            }

        }
    }
}
```

### `L010-Nested if.cs`

```csharp
using System;

namespace Code_Practice{
    class L010_Nested_if{
        static void Main(string[] args){

            Console.Write("Username : ");
            string Username = Console.ReadLine();
            
            if (Username == "admin"){
                Console.Write("Password : ");
                string Password = Console.ReadLine();
                if (Password == "12345"){
                    Console.WriteLine("Selamat Datang Dev!");
                }
                else {
                    Console.WriteLine("[Info] Password Salah!");
                }
            }
            else {
                Console.WriteLine("[Info] Username Tidak ditemukan!");
            }

        }
    }
}
```

### `L011-Switch.cs`

```csharp
using System;

namespace Code_Practice{
    class L011_Switch{
        static void Main(string[] args){

            Console.WriteLine("=== Menu ===");
            Console.WriteLine("1. Nasi Goreng");
            Console.WriteLine("2. Mie Goreng");
            Console.WriteLine("3. Ayam Geprek");
            Console.WriteLine("4. Soto");

            Console.WriteLine("------------");
            Console.Write("Pilih Menu : ");
            string Pilihan_user = Console.ReadLine();

            switch (Pilihan_user){
                case "1":
                    Console.WriteLine("Anda memilih Nasi Goreng");
                    break;
                case "2":
                    Console.WriteLine("Anda memilih Mie Goreng");
                    break;
                case "3":
                    Console.WriteLine("Anda memilih Ayam Geprek");
                    break;
                case "4":
                    Console.WriteLine("Anda memilih Soto");
                    break;
                default:
                    Console.WriteLine("[Error] Menu tidak tersedia!");
                    break;
            }

        }
    }
}
```

### `L012-Switch dan Operasi.cs`

```csharp
using System;

namespace Code_Practice{
    class L011_Switch_dan_Operasi{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama : ");
            double Angka_pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan operator (+ - * /) : ");
            string Operator = Console.ReadLine();
            Console.Write("Masukkan angka kedua : ");
            double Angka_kedua = double.Parse(Console.ReadLine());

            double Hasil = 0;
            string Error = "";

            switch (Operator){
                case "+": Hasil = Angka_pertama + Angka_kedua; break;
                case "-": Hasil = Angka_pertama - Angka_kedua; break;
                case "*": Hasil = Angka_pertama * Angka_kedua; break;
                case "/": Hasil = Angka_pertama / Angka_kedua; break;
                default : Error = "[Error] Operator/Angka yang anda masukkan tidak valid!"; break;
            }  

            if (Error == "[Error] Operator/Angka yang anda masukkan tidak valid!"){
                Console.WriteLine(Error);
            } else{
                Console.WriteLine(Hasil);
            }
        
        }
    }
}
```

### `L013-Validasi Pembagian.cs`

```csharp
using System;

namespace Code_practice{
    class L013_Validasi_Pembagian{
        static void Main(string[] args){

            Console.Write("Masukkan angka pertama : ");
            double Angka_pertama = double.Parse(Console.ReadLine());
            Console.Write("Masukkan operator (+ - * /) : ");
            string Operator = Console.ReadLine();
            Console.Write("Masukkan angka kedua : ");
            double Angka_kedua = double.Parse(Console.ReadLine());

            double Hasil = 0;
            string Error = "";

            switch (Operator){
                case "+": Hasil = Angka_pertama + Angka_kedua; break;
                case "-": Hasil = Angka_pertama - Angka_kedua; break;
                case "*": Hasil = Angka_pertama * Angka_kedua; break;
                case "/": Hasil = Angka_pertama / Angka_kedua; break;
                default : Error = "[Error] Operator/Angka yang anda masukkan tidak valid!"; break;
            }

            if (Operator == "/" && Angka_kedua == 0 ){
                Console.WriteLine("[Error] Tidak dapat membagi dengan nol!");
            }
            else{
                if (Error == "[Error] Operator/Angka yang anda masukkan tidak valid!"){
                    Console.WriteLine(Error);
                } else{
                    Console.WriteLine(Hasil);
                }
            }

        }
    }
}
```

### `L014-While Loop.cs`

```csharp
using System;

namespace Code_Practice{
    class L014_While_Loop{
        static void Main(string[] args){

            while(true){
                Console.Write("Masukan Angka [1 - 5] : ");
                int Angka = int.Parse(Console.ReadLine());
                if (Angka >= 1 && Angka <= 5){
                    Console.WriteLine("Angka valid!");
                    break;
                }
                else{
                    Console.WriteLine("[Error] Angka tidak valid!");
                }
            }
            
        }
    }
}
```

### `build_cs_template.py`

```python
"""
buat_cs.py
==========
Membuat file latihan C# baru dengan nomor otomatis + kerangka kode yang
biasa dipakai.

Cara pakai:
  1. Letakkan script ini di folder latihan C# kamu (satu folder dengan
     file L001-..., L002-..., dst).
  2. Jalankan:  python buat_cs.py
  3. Ketik nama file (tanpa nomor & tanpa .cs), contoh:  For Loop
     -> terbuat  L018-For Loop.cs  (nomor = nomor terbesar yang ada + 1)
  4. Kosongkan input lalu Enter untuk selesai.

Nama class otomatis diambil dari nama file, contoh:
  L018-For Loop.cs  ->  class L018_For_Loop
"""

import os
import re

NAMESPACE = "Code_Practice"   # ganti di sini kalau namespace-nya berubah
AWALAN = "L"                  # awalan nomor file (L001, L002, ...)
DIGIT = 3                     # jumlah digit nomor (001, 002, ...)

TEMPLATE = """using System;

namespace {namespace}{{
    class {kelas}{{
        static void Main(string[] args){{

            

        }}
    }}
}}
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
        path = os.path.join(folder, nama_tanpa_ext + ".cs")

        if os.path.exists(path):
            print(f"⚠️   File '{nama_tanpa_ext}.cs' sudah ada, tidak ditimpa.")
            continue

        kelas = buat_nama_kelas(nama_tanpa_ext)
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(namespace=NAMESPACE, kelas=kelas))

        print(f"✅  Dibuat : {nama_tanpa_ext}.cs")
        print(f"    class  : {kelas}")


if __name__ == "__main__":
    main()
```

### `run_c_sharp.py`

```python
import os

# Mendapatkan path folder tempat script Python ini berada secara otomatis
FOLDER_PROYEK = os.path.dirname(os.path.abspath(__file__))

def dapatkan_daftar_file_cs():
    # Mencari file .cs langsung di folder proyek C#
    files = [f for f in os.listdir(FOLDER_PROYEK) if f.endswith('.cs') and f.startswith('L')]
    files.sort()
    return files

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

def main():
    files = dapatkan_daftar_file_cs()
    
    if not files:
        print(f"Tidak ada file latihan C# (.cs) yang ditemukan di: {FOLDER_PROYEK}")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== MENU PEMILIH FILE C# =====")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        print("0. Keluar")
        print("--------------------------------")
        
        try:
            pilihan = int(input("Pilih nomor file yang ingin dijalankan: "))
            if pilihan == 0:
                print("Keluar dari pembantu Python.")
                break
            elif 1 <= pilihan <= len(files):
                file_terpilih = files[pilihan - 1]
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
            else:
                input("Nomor tidak valid! Tekan Enter untuk coba lagi...")
        except ValueError:
            input("Masukkan angka yang valid! Tekan Enter untuk coba lagi...")

if __name__ == "__main__":
    main()
```

