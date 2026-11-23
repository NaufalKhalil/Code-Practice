"""
bundle_code.py
==============
Menggabungkan file KODE (.cs, .py, .js, .html, .css) menjadi SATU file
dokumentasi Markdown (.md) yang terstruktur, hemat token, dan mudah dibaca AI.

Cara pakai:
    python bundle_code.py

    [1] Pilih FOLDER  -> dialog "browse folder"; seluruh isi folder
                         (termasuk sub-folder) ikut digabung.
    [2] Pilih FILE    -> dialog pilih banyak file (Ctrl/Shift + klik).

Yang otomatis dilewati:
    - file non-kode (json, md, gambar, dll) dan file biner
    - file hasil generate/minify (.min.js, .g.cs, dll)
    - folder sampah umum (.git, node_modules, bin, obj, venv, dist, dll)

Hasil .md disimpan di samping script ini. Deskripsi & aturan untuk AI di
dalamnya menyesuaikan bahasa yang dominan.
"""

from __future__ import annotations

import datetime
import os
import re
from dataclasses import dataclass
from pathlib import Path


# =============================================================================
# KONFIGURASI
# =============================================================================

FOLDER_DIABAIKAN = {
    ".git", ".svn", ".hg",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "node_modules", "venv", ".venv", "env",
    "dist", "build", "target", "out",
    ".idea", ".vscode", ".vs", "egg-info",
    # C# / .NET
    "bin", "obj", "packages", "debug", "release", "testresults",
    # JavaScript
    "bower_components", "coverage", ".next", ".nuxt",
}

AKHIRAN_DIABAIKAN = (
    ".g.cs", ".g.i.cs", ".assemblyinfo.cs", ".assemblyattributes.cs",
    ".min.js", ".min.css", ".bundle.js",
)

# ekstensi -> (kelompok bahasa, nama untuk code fence Markdown)
EKSTENSI_KODE = {
    ".cs":   ("csharp",     "csharp"),
    ".py":   ("python",     "python"),
    ".js":   ("javascript", "javascript"),
    ".html": ("web",        "html"),
    ".htm":  ("web",        "html"),
    ".css":  ("web",        "css"),
}


# =============================================================================
# PROFIL BAHASA (untuk menyesuaikan aturan AI)
# =============================================================================

@dataclass(frozen=True)
class ProfilBahasa:
    nama: str
    lib: str
    level: str
    kasus: str
    batas: str
    unlock: str


PROFIL = {
    "csharp": ProfilBahasa(
        nama="C#",
        lib="library/NuGet package eksternal",
        level='"Level 3 - Looping Dasar (for)", "Level 5 - Array & Pencarian Nilai"',
        kasus="hitung total belanja kasir, validasi input umur, cari nilai "
              "tertinggi dari daftar nilai siswa, dsb",
        batas='"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
              'pakai: LINQ seperti Max(), OrderBy()."',
        unlock="setelah pengguna lancar mencari nilai tertinggi/terendah di "
               "array secara manual, barulah boleh dikenalkan shortcut "
               "seperti LINQ Max()/Min()",
    ),
    "python": ProfilBahasa(
        nama="Python",
        lib="library eksternal",
        level='"Level 3 - Looping Dasar (for)", "Level 5 - List & Pencarian Nilai"',
        kasus="hitung total belanja, validasi input umur, cari nilai "
              "tertinggi dari daftar nilai siswa, dsb",
        batas='"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
              'pakai: min(), max(), sorted()."',
        unlock="setelah pengguna lancar mencari nilai tertinggi/terendah di "
               "list secara manual, barulah boleh dikenalkan shortcut "
               "seperti min()/max()",
    ),
    "javascript": ProfilBahasa(
        nama="JavaScript",
        lib="library/framework eksternal",
        level='"Level 3 - Looping Dasar (for)", "Level 5 - Array & Pencarian Nilai"',
        kasus="hitung total keranjang belanja, validasi input form, cari "
              "nilai tertinggi dari daftar nilai siswa, dsb",
        batas='"Boleh pakai: variabel, if/else, perulangan for. Belum boleh '
              'pakai: map(), filter(), Math.max()."',
        unlock="setelah pengguna lancar mencari nilai tertinggi/terendah di "
               "array secara manual, barulah boleh dikenalkan shortcut "
               "seperti Math.max() atau method array (map/filter)",
    ),
    "web": ProfilBahasa(
        nama="HTML dan CSS",
        lib="framework CSS/JS eksternal (Bootstrap, Tailwind, dll)",
        level='"Level 3 - Layout Dasar (div & class)", "Level 5 - Form & Input"',
        kasus="membuat kartu profil, form pendaftaran, navbar toko online, "
              "halaman daftar produk, dsb",
        batas='"Boleh pakai: tag dasar, class, margin/padding, warna. Belum '
              'boleh pakai: Flexbox, Grid."',
        unlock="setelah pengguna lancar menyusun layout dengan cara dasar "
               "(display, float, margin), barulah boleh dikenalkan Flexbox/Grid",
    ),
}


def deteksi_bahasa_dominan(files: list[Path]) -> tuple[ProfilBahasa, str]:
    """Bahasa dominan = kelompok dengan file terbanyak (seri -> ukuran terbesar)."""
    jumlah: dict[str, int] = {}
    ukuran: dict[str, int] = {}

    for f in files:
        kelompok, _ = EKSTENSI_KODE[f.suffix.lower()]
        jumlah[kelompok] = jumlah.get(kelompok, 0) + 1
        try:
            ukuran[kelompok] = ukuran.get(kelompok, 0) + f.stat().st_size
        except OSError:
            pass

    dominan = max(jumlah, key=lambda k: (jumlah[k], ukuran.get(k, 0)))
    return PROFIL[dominan], f"{jumlah[dominan]} dari {len(files)} file"


# =============================================================================
# KONTEKS & ATURAN UNTUK AI
# =============================================================================

def buat_konteks_ai(p: ProfilBahasa) -> str:
    aturan = [
        'Jangan beri jawaban kode lengkap sebelum pengguna mengatakan kata '
        '"menyerah". Sebelum itu, hanya boleh memberi clue/petunjuk.',

        'Jika pengguna mengatakan "menyerah", barulah tampilkan kode jawaban '
        'lengkap beserta penjelasannya.',

        'Jika kode yang dikirim pengguna **salah** atau belum lulus:\n'
        '   - Jangan langsung kasih jawaban.\n'
        '   - Berikan petunjuk/clue yang mengarahkan ke kesalahan.\n'
        '   - Tanyakan apakah mau coba lagi atau menyerah.',

        'Soal level berikutnya **hanya** boleh diberikan setelah kode pengguna '
        'dinyatakan benar/lulus oleh kamu.',

        'Tingkat kesulitan soal harus disesuaikan dengan level:\n'
        '   - Level rendah → soal sederhana, 1 konsep, cocok untuk pemula.\n'
        '   - Level tinggi → soal lebih kompleks, bisa gabungan beberapa konsep.\n'
        '   - Naik level hanya jika sudah lulus soal sebelumnya.',

        'Soal harus selalu bisa dipahami pemula:\n'
        '   - Gunakan bahasa yang mudah dan jelas.\n'
        '   - Sertakan contoh input/output (atau tampilan) yang diharapkan.\n'
        f'   - Jangan gunakan {p.lib} kecuali sudah di level lanjut.',

        'Lihat daftar kode di bawah untuk mengetahui syntax dan topik apa saja '
        'yang sudah pernah dipelajari. Gunakan ini sebagai acuan level dan titik '
        'lanjut pembelajaran.',

        'Setiap soal harus punya nama level yang jelas dan sesuai dengan '
        f'materi/topik soal tersebut (contoh: {p.level}). '
        'Jangan hanya menulis "Level 3" tanpa nama topiknya.',

        'Soal sebisa mungkin relate/relevan dengan kasus nyata, '
        f'bukan sekadar soal abstrak/teoretis (contoh: {p.kasus}).',

        'Setiap soal harus menyertakan aturan syntax apa saja yang boleh '
        'digunakan untuk mengerjakannya. Utamakan membatasi syntax ke yang sudah '
        'dikuasai pemula, supaya fundamental/pondasi logikanya kuat dulu '
        f'(contoh: {p.batas}).',

        'Syntax/fungsi baru yang lebih ringkas boleh di-unlock jika fundamental '
        f'pengguna di topik terkait sudah cukup kuat ({p.unlock}). '
        'Jelaskan bahwa ini "unlock syntax baru" sebagai bentuk progres, bukan '
        'diberikan dari awal.',

        'Materi/topik baru boleh di-unlock jika materi sebelumnya sudah dikuasai '
        'dengan baik, bukan cuma sekali lulus, tapi sudah cukup beberapa soal di '
        'topik tersebut. Saat unlock materi baru, beri tahu pengguna secara '
        'eksplisit bahwa ini adalah materi baru yang baru dibuka.',
    ]
    daftar_aturan = "\n".join(f"{i}. {teks}" for i, teks in enumerate(aturan, 1))

    return (
        "## Konteks & Peraturan untuk AI — Baca Ini Dulu\n\n"
        f"Halo AI! Ini adalah sesi lanjutan belajar {p.nama} seorang pemula. "
        "Obrolan sebelumnya sudah mencapai batas token sehingga chat dibuka ulang. "
        "File ini berisi seluruh kode yang sudah pernah dibuat sebagai bukti "
        "progres belajar.\n\n"
        f"Tugasmu adalah menjadi tutor/mentor {p.nama} interaktif dengan aturan "
        "berikut:\n\n"
        "### Aturan Pemberian Soal\n\n"
        f"{daftar_aturan}\n\n"
        "### Cara Memulai Sesi Ini\n\n"
        "Setelah membaca file ini, sambut pengguna dan tanyakan: "
        '"Mau lanjut dari mana? Minta soal baru, atau ada topik tertentu?"\n\n'
        "---\n\n"
    )


# =============================================================================
# PENGUMPULAN FILE
# =============================================================================

def file_kode_valid(path: Path) -> bool:
    """True jika file kode yang layak digabung (bukan hidden/generated/biner)."""
    nama = path.name.lower()
    if nama.startswith(".") or path.suffix.lower() not in EKSTENSI_KODE:
        return False
    if nama.endswith(AKHIRAN_DIABAIKAN):
        return False
    try:
        with path.open("rb") as f:
            return b"\x00" not in f.read(2048)
    except OSError:
        return False


def kumpulkan_dari_folder(folder: Path) -> list[Path]:
    """Semua file kode di dalam folder, rekursif, folder sampah dilewati."""
    hasil: list[Path] = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and d.lower() not in FOLDER_DIABAIKAN
        )
        for nama in sorted(files):
            path = Path(root) / nama
            if file_kode_valid(path):
                hasil.append(path)
    return hasil


# =============================================================================
# STRUKTUR TREE & UTILITAS MARKDOWN
# =============================================================================

_KEY_FILES = "__files__"


def bangun_tree(rel_paths: list[str]) -> dict:
    tree: dict = {}
    for rel in rel_paths:
        *folders, nama = rel.split("/")
        node = tree
        for folder in folders:
            node = node.setdefault(folder, {})
        node.setdefault(_KEY_FILES, []).append(nama)
    return tree


def render_tree(tree: dict, prefix: str = "") -> list[str]:
    folders = [k for k in tree if k != _KEY_FILES]
    files = tree.get(_KEY_FILES, [])
    entries = sorted(folders + files, key=str.lower)

    baris: list[str] = []
    for i, nama in enumerate(entries):
        terakhir = i == len(entries) - 1
        cabang = "└── " if terakhir else "├── "
        if nama in folders:
            baris.append(f"{prefix}{cabang}{nama}/")
            anak_prefix = prefix + ("    " if terakhir else "│   ")
            baris.extend(render_tree(tree[nama], anak_prefix))
        else:
            baris.append(f"{prefix}{cabang}{nama}")
    return baris


def slug(rel_path: str) -> str:
    """Anchor link ala GitHub untuk daftar isi."""
    s = re.sub(r"[^a-z0-9\-_ /]", "", rel_path.lower())
    s = s.replace("/", "-").replace(" ", "-").replace(".", "")
    return re.sub(r"-+", "-", s).strip("-")


def baca_teks(path: Path) -> str:
    for encoding in ("utf-8", "latin-1"):
        try:
            return path.read_text(encoding=encoding).strip()
        except UnicodeDecodeError:
            continue
        except OSError as e:
            return f"# Gagal membaca file: {e}"
    return "# Gagal membaca file"


# =============================================================================
# PEMBUATAN DOKUMENTASI
# =============================================================================

def buat_dokumentasi(
    nama: str,
    folder_acuan: Path,
    files: list[Path],
    output: Path,
) -> None:
    """Menulis semua `files` ke satu Markdown; path relatif terhadap `folder_acuan`."""
    rel_list = [f.relative_to(folder_acuan).as_posix() for f in files]
    profil, ringkas = deteksi_bahasa_dominan(files)
    jumlah_subfolder = len({str(Path(r).parent) for r in rel_list if "/" in r})
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bagian: list[str] = [
        f"# {nama}\n\n"
        f"- **Dibuat:** {waktu}\n"
        f"- **Sumber:** `{folder_acuan}`\n"
        f"- **Total file:** {len(files)} ({jumlah_subfolder} sub-folder disertakan)\n"
        f"- **Bahasa dominan:** {profil.nama} ({ringkas})\n\n",

        buat_konteks_ai(profil),

        "## Struktur\n\n```\n"
        f"{nama}/\n" + "\n".join(render_tree(bangun_tree(rel_list))) + "\n```\n\n",

        "## Daftar Isi\n\n"
        + "\n".join(f"- [{rel}](#{slug(rel)})" for rel in rel_list)
        + "\n\n",

        "## File\n\n",
    ]

    for rel, path in zip(rel_list, files):
        fence = EKSTENSI_KODE[path.suffix.lower()][1]
        isi = baca_teks(path) or "# (file kosong)"
        bagian.append(f"### `{rel}`\n\n```{fence}\n{isi}\n```\n\n")

    output.write_text("".join(bagian), encoding="utf-8")

    print(f"\n✅  Selesai! {len(files)} file digabung "
          f"({jumlah_subfolder} sub-folder disertakan).")
    print(f"📄  Hasil  : {output}")
    print(f"📦  Ukuran : {output.stat().st_size / 1024:.1f} KB")


# =============================================================================
# DIALOG PEMILIHAN (tkinter)
# =============================================================================

def _buka_dialog():
    """Membuat root tkinter tersembunyi di atas jendela lain."""
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return root


def dialog_pilih_folder(awal: Path) -> Path | None:
    from tkinter import filedialog

    root = _buka_dialog()
    try:
        hasil = filedialog.askdirectory(
            title="Pilih folder untuk digabung", initialdir=str(awal)
        )
    finally:
        root.destroy()
    return Path(hasil).resolve() if hasil else None


def dialog_pilih_file(awal: Path) -> list[Path]:
    from tkinter import filedialog

    root = _buka_dialog()
    try:
        hasil = filedialog.askopenfilenames(
            title="Pilih file (Ctrl/Shift + klik untuk banyak file)",
            initialdir=str(awal),
            filetypes=[
                ("File kode", "*.cs *.py *.js *.html *.htm *.css"),
                ("Semua file", "*.*"),
            ],
        )
    finally:
        root.destroy()
    return [Path(p).resolve() for p in hasil]


# =============================================================================
# PROGRAM UTAMA
# =============================================================================

def proses_folder(base_dir: Path) -> tuple[str, Path, list[Path], str] | None:
    folder = dialog_pilih_folder(base_dir)
    if not folder:
        print("\n⚠️   Tidak ada folder dipilih.")
        return None

    files = kumpulkan_dari_folder(folder)
    nama = folder.name or "root"
    return nama, folder, files, f"dokumentasi_{nama.replace(' ', '_')}.md"


def proses_file(base_dir: Path) -> tuple[str, Path, list[Path], str] | None:
    dipilih = dialog_pilih_file(base_dir)
    files = sorted(p for p in dipilih if file_kode_valid(p))
    if not files:
        print("\n⚠️   Tidak ada file kode valid yang dipilih.")
        return None

    try:
        folder_acuan = Path(os.path.commonpath([p.parent for p in files]))
    except ValueError:  # beda drive di Windows
        print("\n⚠️   Semua file harus berada di drive yang sama.")
        return None

    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nama = folder_acuan.name or "pilihan"
    return nama, folder_acuan, files, f"dokumentasi_pilihan_{stamp}.md"


def tampilkan_menu() -> None:
    print("\n" + "=" * 70)
    print("  GABUNG FILE")
    print("=" * 70)
    print("  [1]  Pilih FOLDER  (semua isi + sub-folder ikut)")
    print("  [2]  Pilih banyak FILE  (Ctrl/Shift + klik)")
    print("  [0]  Keluar")
    print("=" * 70)


def main() -> None:
    base_dir = Path(__file__).resolve().parent

    try:
        import tkinter  # noqa: F401
    except ImportError:
        print("❌  tkinter tidak ditemukan. Di Linux: install paket 'tk' "
              "(Arch: sudo pacman -S tk).")
        return

    handler = {"1": proses_folder, "2": proses_file}

    while True:
        tampilkan_menu()
        try:
            pilihan = input("\n> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram dihentikan.")
            return

        if pilihan == "0":
            print("\nKeluar. Sampai jumpa! 👋")
            return

        if pilihan not in handler:
            print("\n⚠️   Input tidak valid. Ketik 1, 2, atau 0.")
            continue

        hasil = handler[pilihan](base_dir)
        if hasil is None:
            continue

        nama, folder_acuan, files, nama_output = hasil
        if not files:
            print(f"\n❌  Tidak ada file kode yang bisa digabung dari '{nama}'.")
            continue

        print(f"\n⏳  Menggabungkan '{nama}'...")
        buat_dokumentasi(nama, folder_acuan, files, base_dir / nama_output)

        if input("\nGabung lagi? (y/n): ").strip().lower() != "y":
            print("\nSelesai. Sampai jumpa! 👋")
            return


if __name__ == "__main__":
    main()
