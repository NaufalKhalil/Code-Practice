import json
import os

# ============================================================
#  SESUAIKAN PATH INI dengan lokasi folder project kamu
# ============================================================
FOLDER = r"d:\Project\Coding\Code Practice\Python"
JSON_FILE = os.path.join(FOLDER, "rename_list.json")
# ============================================================

def main():
    # Baca JSON
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        nama_baru_list = json.load(f)

    # Ambil semua file .py di folder, urutkan berdasarkan nomor L001, L002, dst
    file_lama_list = sorted(
        [f for f in os.listdir(FOLDER) if f.endswith(".py")],
        key=lambda x: int(x[1:4]) if x[1:4].isdigit() else 9999
    )

    # Validasi jumlah harus sama
    if len(file_lama_list) != len(nama_baru_list):
        print(f"⚠️  PERINGATAN: Jumlah file di folder ({len(file_lama_list)}) "
              f"tidak sama dengan jumlah nama di JSON ({len(nama_baru_list)})")
        print("Pastikan folder hanya berisi 129 file .py yang ingin direname.\n")

    print("=" * 60)
    print("  PREVIEW RENAME (belum dieksekusi)")
    print("=" * 60)
    for lama, baru in zip(file_lama_list, nama_baru_list):
        print(f"  {lama}")
        print(f"  → {baru}")
        print()

    # Konfirmasi sebelum eksekusi
    konfirmasi = input("Lanjutkan rename semua file? (ketik 'ya' untuk lanjut): ").strip().lower()

    if konfirmasi != "ya":
        print("❌ Dibatalkan. Tidak ada file yang direname.")
        return

    print("\n" + "=" * 60)
    print("  PROSES RENAME")
    print("=" * 60)

    sukses = 0
    gagal = 0

    for lama, baru in zip(file_lama_list, nama_baru_list):
        path_lama = os.path.join(FOLDER, lama)
        path_baru = os.path.join(FOLDER, baru)

        try:
            if not os.path.exists(path_lama):
                print(f"⚠️  Tidak ditemukan : {lama}")
                gagal += 1
                continue

            if os.path.exists(path_baru):
                print(f"⚠️  Sudah ada       : {baru} (dilewati)")
                gagal += 1
                continue

            os.rename(path_lama, path_baru)
            print(f"✅ {lama}\n   → {baru}\n")
            sukses += 1

        except Exception as e:
            print(f"❌ Gagal rename {lama}: {e}")
            gagal += 1

    print("=" * 60)
    print(f"  SELESAI — Berhasil: {sukses} | Gagal/Dilewati: {gagal}")
    print("=" * 60)

if __name__ == "__main__":
    main()
