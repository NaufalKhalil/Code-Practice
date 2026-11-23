"""
gabung_file.py
==============
Menggabungkan file KODE saja (.cs, .py, .js, .html, .css) dalam folder
pilihan menjadi SATU file dokumentasi
Markdown (.md) yang terstruktur secara hierarkis — lebih hemat token
dan lebih mudah dipahami AI dibanding menggabung manual satu-satu.

File lain (json, md, gambar, dll) dan folder "sampah" umum (bin, obj,
packages, .git, node_modules, __pycache__, venv, dist, build, dll)
otomatis DILEWATI, supaya hasil gabungan tetap bersih & bisa dibaca.

Menu hanya menampilkan folder yang SEJAJAR dengan script ini (top-level
saja, tidak menampilkan sub-folder di menu). Begitu satu folder dipilih,
SELURUH isinya — termasuk semua sub-folder & sub-sub-folder di dalamnya —
otomatis ikut digabung, tanpa perlu memilih satu per satu.

Cara pakai:
  1. Letakkan script ini di LUAR folder-folder yang berisi file kamu.
     Contoh struktur:
       📁 Proyek/
         📄 gabung_file.py      ← script ini
         📁 Backend/            ← akan tampil di menu
           📁 routes/           ← otomatis ikut kalau "Backend" dipilih
           📁 models/
         📁 Frontend/           ← akan tampil di menu
         📁 Dokumen/            ← akan tampil di menu

  2. Jalankan:  python gabung_file.py
  3. Ketik nomor untuk menggabung folder itu, atau "cd <nomor>" untuk
     masuk ke dalam folder tersebut ("cd .." untuk naik, "." untuk
     menggabung folder yang sedang dibuka).
  4. Semua file di folder itu (termasuk seluruh sub-folder di dalamnya,
     minus file biner & folder sampah) akan langsung digabung.
  5. File hasil .md akan muncul di samping script ini. Deskripsi/peraturan
     untuk AI di dalamnya otomatis menyesuaikan bahasa yang dominan di
     folder (.cs = C#, .py = Python, .js = JavaScript, .html/.css = HTML
     dan CSS).
"""

import os
import re
import datetime


# ---------------------------------------------------------------------------
# Konfigurasi: apa yang DILEWATI / bagaimana file ditampilkan
# ---------------------------------------------------------------------------

FOLDER_DIABAIKAN = {
    ".git", ".svn", ".hg",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "node_modules", "venv", ".venv", "env", ".env",
    "dist", "build", "target", "out",
    ".idea", ".vscode", ".vs",
    "egg-info",
    # khusus C# / .NET
    "bin", "obj", "packages", "debug", "release", "testresults",
    # khusus JavaScript
    "bower_components", "coverage", ".next", ".nuxt",
}

# Hanya file dengan ekstensi ini yang digabung (C#, Python, JS, HTML, CSS)
EKSTENSI_DIIZINKAN = {".cs", ".py", ".js", ".html", ".htm", ".css"}

# File hasil generate / minify yang tidak perlu ikut (hanya bikin berat)
AKHIRAN_DIABAIKAN = (
    ".g.cs", ".g.i.cs", ".assemblyinfo.cs", ".assemblyattributes.cs",
    ".min.js", ".min.css", ".bundle.js",
)

EKSTENSI_BINER = {
    # gambar
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".webp", ".tiff",
    # video / audio
    ".mp4", ".mov", ".avi", ".mkv", ".mp3", ".wav", ".flac", ".ogg",
    # font
    ".ttf", ".otf", ".woff", ".woff2", ".eot",
    # arsip / paket
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".whl",
    # binary / executable / compiled
    ".exe", ".dll", ".so", ".dylib", ".bin", ".pyc", ".pyo", ".class",
    ".jar", ".o", ".a", ".lib",
    # data biner / database
    ".db", ".sqlite", ".sqlite3", ".pkl", ".pickle", ".pdf",
}

# Mapping ekstensi -> bahasa untuk code fence Markdown (biar syntax highlight rapi)
BAHASA_FENCE = {
    ".cs": "csharp", ".py": "python", ".js": "javascript", ".jsx": "jsx",
    ".ts": "typescript", ".tsx": "tsx", ".json": "json",
    ".html": "html", ".htm": "html", ".css": "css", ".scss": "scss",
    ".md": "markdown", ".sh": "bash", ".bash": "bash",
    ".yml": "yaml", ".yaml": "yaml", ".sql": "sql",
    ".java": "java", ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp",
    ".go": "go", ".rb": "ruby", ".php": "php", ".rs": "rust",
    ".xml": "xml", ".toml": "toml", ".ini": "ini", ".cfg": "ini",
    ".txt": "", ".env": "",
}


# ---------------------------------------------------------------------------
# Profil bahasa: dipakai untuk menyesuaikan deskripsi/peraturan untuk AI
# ---------------------------------------------------------------------------

# Ekstensi -> kelompok bahasa (html & css dihitung satu kelompok "web")
KELOMPOK_EKSTENSI = {
    ".cs": "csharp", ".py": "python", ".js": "javascript",
    ".html": "web", ".htm": "web", ".css": "web",
}

PROFIL_BAHASA = {
    "csharp": {
        "nama": "C#",
        "lib": "library/NuGet package eksternal",
        "level": ('"Level 3 - Looping Dasar (for)", '
                  '"Level 5 - Array & Pencarian Nilai"'),
        "kasus": ("hitung total belanja kasir, validasi input umur, cari nilai "
                  "tertinggi dari daftar nilai siswa, dsb"),
        "batas": ('"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
                  'pakai: LINQ seperti Max(), OrderBy()."'),
        "unlock": ("setelah pengguna lancar mencari nilai tertinggi/terendah di "
                   "array secara manual, barulah boleh dikenalkan shortcut "
                   "seperti LINQ Max()/Min()"),
    },
    "python": {
        "nama": "Python",
        "lib": "library eksternal",
        "level": ('"Level 3 - Looping Dasar (for)", '
                  '"Level 5 - List & Pencarian Nilai"'),
        "kasus": ("hitung total belanja, validasi input umur, cari nilai "
                  "tertinggi dari daftar nilai siswa, dsb"),
        "batas": ('"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
                  'pakai: min(), max(), sorted()."'),
        "unlock": ("setelah pengguna lancar mencari nilai tertinggi/terendah di "
                   "list secara manual, barulah boleh dikenalkan shortcut "
                   "seperti min()/max()"),
    },
    "javascript": {
        "nama": "JavaScript",
        "lib": "library/framework eksternal",
        "level": ('"Level 3 - Looping Dasar (for)", '
                  '"Level 5 - Array & Pencarian Nilai"'),
        "kasus": ("hitung total keranjang belanja, validasi input form, cari "
                  "nilai tertinggi dari daftar nilai siswa, dsb"),
        "batas": ('"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
                  'pakai: map(), filter(), Math.max()."'),
        "unlock": ("setelah pengguna lancar mencari nilai tertinggi/terendah di "
                   "array secara manual, barulah boleh dikenalkan shortcut "
                   "seperti Math.max() atau method array (map/filter)"),
    },
    "web": {
        "nama": "HTML dan CSS",
        "lib": "framework CSS/JS eksternal (Bootstrap, Tailwind, dll)",
        "level": ('"Level 3 - Layout Dasar (div & class)", '
                  '"Level 5 - Form & Input"'),
        "kasus": ("membuat kartu profil, form pendaftaran, navbar toko online, "
                  "halaman daftar produk, dsb"),
        "batas": ('"Boleh pakai: tag dasar, class, margin/padding, warna. Belum '
                  'boleh pakai: Flexbox, Grid."'),
        "unlock": ("setelah pengguna lancar menyusun layout dengan cara dasar "
                   "(display, float, margin), barulah boleh dikenalkan "
                   "Flexbox/Grid"),
    },
}


def deteksi_bahasa_dominan(file_list):
    """
    Menentukan bahasa dominan dari daftar file: dihitung per kelompok
    (.html + .css = web). Kalau jumlah file sama, yang total ukurannya
    lebih besar yang menang. Mengembalikan (profil, ringkasan_teks).
    """
    jumlah, ukuran = {}, {}
    for path in file_list:
        kel = KELOMPOK_EKSTENSI.get(os.path.splitext(path)[1].lower())
        if not kel:
            continue
        jumlah[kel] = jumlah.get(kel, 0) + 1
        try:
            ukuran[kel] = ukuran.get(kel, 0) + os.path.getsize(path)
        except OSError:
            pass
    if not jumlah:
        return PROFIL_BAHASA["python"], "tidak terdeteksi"
    dominan = max(jumlah, key=lambda k: (jumlah[k], ukuran.get(k, 0)))
    ringkas = f"{jumlah[dominan]} dari {len(file_list)} file"
    return PROFIL_BAHASA[dominan], ringkas


def buat_konteks_ai(profil):
    """Membuat blok 'Konteks & Peraturan untuk AI' sesuai bahasa dominan."""
    b = profil["nama"]
    return (
        "## Konteks & Peraturan untuk AI — Baca Ini Dulu\n\n"
        f"Halo AI! Ini adalah sesi lanjutan belajar {b} seorang pemula. "
        "Obrolan sebelumnya sudah mencapai batas token sehingga chat dibuka ulang. "
        "File ini berisi seluruh kode yang sudah pernah dibuat sebagai bukti progres belajar.\n\n"

        f"Tugasmu adalah menjadi tutor/mentor {b} interaktif dengan aturan berikut:\n\n"

        "### Aturan Pemberian Soal\n\n"

        "1. **Jangan** beri jawaban kode lengkap sebelum pengguna mengatakan kata "
        "\"menyerah\". Sebelum itu, hanya boleh memberi clue/petunjuk.\n"
        "2. Jika pengguna mengatakan \"menyerah\", barulah tampilkan kode jawaban "
        "lengkap beserta penjelasannya.\n"
        "3. Jika kode yang dikirim pengguna **salah** atau belum lulus:\n"
        "   - Jangan langsung kasih jawaban.\n"
        "   - Berikan petunjuk/clue yang mengarahkan ke kesalahan.\n"
        "   - Tanyakan apakah mau coba lagi atau menyerah.\n"
        "4. Soal level berikutnya **hanya** boleh diberikan setelah kode pengguna "
        "dinyatakan benar/lulus oleh kamu.\n"
        "5. Tingkat kesulitan soal harus disesuaikan dengan level:\n"
        "   - Level rendah → soal sederhana, 1 konsep, cocok untuk pemula.\n"
        "   - Level tinggi → soal lebih kompleks, bisa gabungan beberapa konsep.\n"
        "   - Naik level hanya jika sudah lulus soal sebelumnya.\n"
        "6. Soal harus selalu bisa dipahami pemula:\n"
        "   - Gunakan bahasa yang mudah dan jelas.\n"
        "   - Sertakan contoh input/output (atau tampilan) yang diharapkan.\n"
        f"   - Jangan gunakan {profil['lib']} kecuali sudah di level lanjut.\n"
        "7. Lihat daftar kode di bawah untuk mengetahui syntax dan topik apa saja "
        "yang sudah pernah dipelajari. Gunakan ini sebagai acuan level dan titik "
        "lanjut pembelajaran.\n"
        "8. Setiap soal harus punya nama level yang jelas dan sesuai dengan "
        f"materi/topik soal tersebut (contoh: {profil['level']}). "
        "Jangan hanya menulis \"Level 3\" tanpa nama topiknya.\n"
        "9. Soal sebisa mungkin relate/relevan dengan kasus nyata, "
        f"bukan sekadar soal abstrak/teoretis (contoh: {profil['kasus']}).\n"
        "10. Setiap soal harus menyertakan aturan syntax apa saja yang boleh "
        "digunakan untuk mengerjakannya. Utamakan membatasi syntax ke yang sudah "
        "dikuasai pemula, supaya fundamental/pondasi logikanya kuat dulu (contoh: "
        f"{profil['batas']}).\n"
        "11. Syntax/fungsi baru yang lebih ringkas boleh di-unlock jika fundamental "
        f"pengguna di topik terkait sudah cukup kuat ({profil['unlock']}). "
        "Jelaskan bahwa ini \"unlock syntax baru\" sebagai bentuk progres, bukan "
        "diberikan dari awal.\n"
        "12. Materi/topik baru boleh di-unlock jika materi sebelumnya sudah dikuasai "
        "dengan baik, bukan cuma sekali lulus, tapi sudah cukup beberapa soal di "
        "topik tersebut. Saat unlock materi baru, beri tahu pengguna secara eksplisit "
        "bahwa ini adalah materi baru yang baru dibuka.\n\n"

        "### Cara Memulai Sesi Ini\n\n"
        "Setelah membaca file ini, sambut pengguna dan tanyakan: "
        "\"Mau lanjut dari mana? Minta soal baru, atau ada topik tertentu?\"\n\n"

        "---\n\n"
    )


def kumpulkan_folder(base_dir):
    """
    Mengumpulkan folder yang langsung ada di dalam base_dir (satu level
    saja, tanpa masuk ke sub-folder). Dikembalikan sebagai list tuple:
      (nama, path_absolut)
    """
    try:
        entries = sorted(
            e for e in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, e))
            and not e.startswith(".")
            and e.lower() not in FOLDER_DIABAIKAN
        )
    except PermissionError:
        return []

    return [(nama, os.path.join(base_dir, nama)) for nama in entries]


def is_file_biner(path):
    """
    Deteksi file biner: cek ekstensi dulu (cepat), kalau ekstensinya
    tidak dikenal, cek byte null di awal file (heuristik umum).
    """
    ext = os.path.splitext(path)[1].lower()
    if ext in EKSTENSI_BINER:
        return True
    try:
        with open(path, "rb") as f:
            chunk = f.read(2048)
        return b"\x00" in chunk
    except Exception:
        return True  # kalau gagal dibaca sama sekali, anggap tidak bisa disertakan


def kumpulkan_file_rekursif(folder):
    """
    Mengambil SEMUA file (bukan biner) di dalam 'folder', termasuk yang
    ada di sub-folder & sub-sub-folder (rekursif, berapa pun level).
    Folder tersembunyi & folder "sampah" umum dilewati.
    """
    hasil = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and d.lower() not in FOLDER_DIABAIKAN
        )
        for f in sorted(files):
            if f.startswith("."):
                continue
            nama_kecil = f.lower()
            if os.path.splitext(nama_kecil)[1] not in EKSTENSI_DIIZINKAN:
                continue
            if nama_kecil.endswith(AKHIRAN_DIABAIKAN):
                continue
            path = os.path.join(root, f)
            if not is_file_biner(path):
                hasil.append(path)
    return hasil


def hitung_rekursif(folder):
    return len(kumpulkan_file_rekursif(folder))


# ---------------------------------------------------------------------------
# Utilitas untuk membangun struktur pohon (tree) & Markdown
# ---------------------------------------------------------------------------

def bangun_tree(rel_paths):
    """Mengubah list path relatif (pakai '/') jadi struktur dict bertingkat."""
    tree = {}
    for rel in rel_paths:
        parts = rel.replace(os.sep, "/").split("/")
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node.setdefault("__files__", []).append(parts[-1])
    return tree


def render_tree(tree, prefix=""):
    """Merender dict tree jadi baris-baris ASCII tree (gaya perintah `tree`)."""
    lines = []
    folders = sorted(k for k in tree.keys() if k != "__files__")
    files = sorted(tree.get("__files__", []))
    entries = sorted(folders + files, key=str.lower)

    for i, nama in enumerate(entries):
        is_last = (i == len(entries) - 1)
        cabang = "└── " if is_last else "├── "
        if nama in folders:
            lines.append(f"{prefix}{cabang}{nama}/")
            ext = "    " if is_last else "│   "
            lines.extend(render_tree(tree[nama], prefix + ext))
        else:
            lines.append(f"{prefix}{cabang}{nama}")
    return lines


def slug(rel_path):
    """Slug sederhana gaya GitHub untuk anchor link Markdown."""
    s = rel_path.lower()
    s = re.sub(r"[^a-z0-9\-_ /]", "", s)
    s = s.replace("/", "-").replace(" ", "-").replace(".", "")
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def buat_dokumentasi(nama_folder, folder_path, output_path):
    """
    Mengambil SEMUA file (non-biner) di dalam folder_path (rekursif,
    termasuk seluruh sub-folder) lalu menulisnya sebagai satu Markdown
    terstruktur.
    """
    file_list = kumpulkan_file_rekursif(folder_path)

    if not file_list:
        print(f"\n❌  Tidak ada file yang bisa digabung dari folder '{nama_folder}'.")
        return

    rel_list = [os.path.relpath(p, folder_path).replace(os.sep, "/") for p in file_list]
    profil, ringkas_dominan = deteksi_bahasa_dominan(file_list)
    waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jumlah_subfolder = len({os.path.dirname(r) for r in rel_list if os.path.dirname(r)})

    with open(output_path, "w", encoding="utf-8") as out:
        # Header + metadata ringkas (front-matter gaya YAML, hemat token, tetap terbaca AI)
        out.write(f"# {nama_folder}\n\n")
        out.write(f"- **Dibuat:** {waktu_sekarang}\n")
        out.write(f"- **Sumber:** `{folder_path}`\n")
        out.write(f"- **Total file:** {len(file_list)} ({jumlah_subfolder} sub-folder disertakan)\n\n")

        # Konteks & peraturan untuk AI — menyesuaikan bahasa dominan folder
        out.write(f"- **Bahasa dominan:** {profil['nama']} ({ringkas_dominan})\n\n")
        out.write(buat_konteks_ai(profil))

        # Struktur folder sebagai tree ringkas — memberi AI peta hierarki
        # dalam beberapa baris saja, tanpa perlu membaca ulang tiap file.
        out.write("## Struktur\n\n```\n")
        out.write(f"{nama_folder}/\n")
        tree = bangun_tree(rel_list)
        out.write("\n".join(render_tree(tree)))
        out.write("\n```\n\n")

        # Daftar isi dengan anchor link ke tiap file
        out.write("## Daftar Isi\n\n")
        for rel in rel_list:
            out.write(f"- [{rel}](#{slug(rel)})\n")
        out.write("\n")

        # Isi tiap file — heading per file, code fence menyesuaikan bahasa
        out.write("## File\n\n")
        for rel, path in zip(rel_list, file_list):
            out.write(f"### `{rel}`\n\n")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    isi = f.read().strip()
            except UnicodeDecodeError:
                try:
                    with open(path, "r", encoding="latin-1") as f:
                        isi = f.read().strip()
                except Exception as e:
                    isi = f"# Gagal membaca file: {e}"
            except Exception as e:
                isi = f"# Gagal membaca file: {e}"

            ext = os.path.splitext(path)[1].lower()
            bahasa = BAHASA_FENCE.get(ext, ext.lstrip("."))
            out.write(f"```{bahasa}\n")
            out.write(isi if isi else "# (file kosong)")
            out.write("\n```\n\n")

    ukuran_kb = os.path.getsize(output_path) / 1024
    print(f"\n✅  Selesai! {len(file_list)} file digabung "
          f"({jumlah_subfolder} sub-folder disertakan).")
    print(f"📄  Hasil  : {output_path}")
    print(f"📦  Ukuran : {ukuran_kb:.1f} KB")


def tampilkan_menu(folders, base_dir, current_dir):
    rel = os.path.relpath(current_dir, base_dir).replace(os.sep, "/")
    lokasi = "/" if rel == "." else f"/{rel}"
    print("\n" + "=" * 70)
    print("  GABUNG FILE – PILIH FOLDER")
    print(f"  Lokasi sekarang : {lokasi}")
    print("=" * 70)
    if not folders:
        print("  (tidak ada sub-folder di sini)")
    for i, (nama, path) in enumerate(folders, 1):
        total = hitung_rekursif(path)
        print(f"  [{i:>3}]  {nama}  ({total} file termasuk sub-folder)")
    print("-" * 70)
    print("  <nomor>     → gabung folder itu jadi .md      (contoh: 2)")
    print("  cd <nomor>  → masuk ke folder itu             (contoh: cd 2)")
    if current_dir != base_dir:
        print("  cd ..       → naik satu folder")
        print("  .           → gabung folder yang sedang dibuka ini")
    print("  0           → Keluar")
    print("=" * 70)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = base_dir

    while True:
        folders = kumpulkan_folder(current_dir)
        tampilkan_menu(folders, base_dir, current_dir)

        if not folders and current_dir == base_dir:
            print("  ❌  Tidak ada folder yang ditemukan di direktori ini.")
            break

        try:
            pilihan = input("\n> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram dihentikan.")
            break

        if pilihan == "0":
            print("\nKeluar. Sampai jumpa! 👋")
            break

        # --- perintah cd -------------------------------------------------
        m = re.match(r"^cd\s*(.*)$", pilihan)
        if m:
            arg = m.group(1).strip()
            if arg in ("..", "../"):
                if current_dir == base_dir:
                    print("\n⚠️   Sudah di folder paling atas.")
                else:
                    current_dir = os.path.dirname(current_dir)
            elif arg.isdigit() and 1 <= int(arg) <= len(folders):
                current_dir = folders[int(arg) - 1][1]
            else:
                print(f"\n⚠️   Pakai: cd <nomor 1–{len(folders)}> atau cd ..")
            continue

        # --- tentukan folder yang akan digabung ---------------------------
        if pilihan == "." and current_dir != base_dir:
            folder_path = current_dir
            nama_folder = os.path.basename(current_dir)
        elif pilihan.isdigit() and 1 <= int(pilihan) <= len(folders):
            nama_folder, folder_path = folders[int(pilihan) - 1]
        else:
            print("\n⚠️   Input tidak valid. Ketik nomor, 'cd <nomor>', 'cd ..', atau 0.")
            continue

        # Nama output memakai path relatif supaya tidak bentrok antar folder
        rel = os.path.relpath(folder_path, base_dir)
        nama_output = "dokumentasi_" + rel.replace(os.sep, "_").replace(" ", "_") + ".md"
        output_path = os.path.join(base_dir, nama_output)

        print(f"\n⏳  Menggabungkan seluruh isi folder '{nama_folder}' "
              f"(termasuk semua sub-folder)...")
        buat_dokumentasi(nama_folder, folder_path, output_path)

        lagi = input("\nGabung folder lain? (y/n): ").strip().lower()
        if lagi != "y":
            print("\nSelesai. Sampai jumpa! 👋")
            break


if __name__ == "__main__":
    main()
