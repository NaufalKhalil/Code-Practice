import os
import re

def urutkan_file(nama_file):
    """
    Fungsi untuk mengekstrak angka setelah huruf 'L' di depan nama file
    agar file terurut rapi dari L1 sampai L38+
    """
    pencarian = re.search(r'L(\d+)', nama_file)
    if pencarian:
        return int(pencarian.group(1))
    return 999  # Jika tidak ada pola L+angka, taruh di paling bawah

def gabung_kode_untuk_ai(folder_input, file_output="semua_kode_belajar.md"):
    try:
        # Ambil semua file .py di folder tersebut
        daftar_file = [f for f in os.listdir(folder_input) if f.endswith('.py')]
        
        # Urutkan file berdasarkan nomor L (L1, L2, L3...)
        daftar_file.sort(key=urutkan_file)
        
        with open(file_output, 'w', encoding='utf-8') as f_out:
            # Tulis instruksi awal untuk AI di paling atas file
            f_out.write("# HALO AI, INI ADALAH REKAM JEJAK BELAJAR PYTHON SAYA\n")
            f_out.write("Berikut adalah seluruh file latihan coding yang sudah saya kerjakan secara berurutan. ")
            f_out.write("Mohon analisis sintaksis apa saja yang sudah saya pelajari dan berikan evaluasi.\n\n")
            f_out.write("=" * 60 + "\n\n")
            
            for file in daftar_file:
                # Lewati file skrip penggabung ini sendiri jika berada di folder yang sama
                if file == os.path.basename(__file__):
                    continue
                    
                jalur_file = os.path.join(folder_input, file)
                
                # Membuat header nama file sebagai bab untuk AI
                f_out.write(f"## NAMA FILE: {file}\n")
                f_out.write("```python\n")
                
                # Membaca isi kode pemrograman
                try:
                    with open(jalur_file, 'r', encoding='utf-8') as f_in:
                        f_out.write(f_in.read())
                except Exception as e:
                    f_out.write(f"# [Gagal membaca isi file ini: {str(e)}]\n")
                
                f_out.write("\n```\n\n")
                f_out.write("-" * 40 + "\n\n") # Pembatas antar file
                
        print(f"Selesai! File '{file_output}' siap dikirim ke AI.")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan program pada folder saat ini
gabung_kode_untuk_ai("D:\Project\Coding\Code Practice\document_md")
