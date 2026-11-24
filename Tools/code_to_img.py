#!/usr/bin/env python3
"""
code2img.py - ubah file kode jadi SATU foto panjang sampai baris terakhir.
Tema: VS Code Dark+ (dark mode standar), lengkap dengan garis indent (tab guides).

Install sekali:
    pip install pillow pygments

Cara pakai:
    python code2img.py kode.py                  -> kode.png
    python code2img.py kode.py -o hasil.png
    python code2img.py kode.js --split 150      -> dipecah per 150 baris (kode_part1.png, ...)
    python code2img.py                          -> muncul jendela pilih file

Opsi lain:
    --lang python        paksa bahasa (kalau deteksi dari ekstensi salah)
    --tab-size 4         lebar 1 tab / jarak antar garis indent
    --font-size 20       ukuran huruf (makin besar = gambar makin tajam & lebar)
    --font path.ttf      pakai font sendiri (harus monospace)
    --no-line-numbers    tanpa nomor baris
"""
import argparse
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
    from pygments.lexers import (
        TextLexer,
        get_lexer_by_name,
        get_lexer_for_filename,
        guess_lexer,
    )
    from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Token
    from pygments.util import ClassNotFound
except ImportError:
    sys.exit("Library belum terpasang. Jalankan dulu:  pip install pillow pygments")


# ---------------------------------------------------------------- warna VS Code Dark+
BG = "#1e1e1e"
FG = "#d4d4d4"
LINE_NO = "#858585"
GUIDE = "#404040"

PURPLE = "#c586c0"  # keyword alur (if, for, return, import, ...)
BLUE = "#569cd6"    # keyword biasa (def, class, True, ...)
TEAL = "#4ec9b0"    # class / tipe
YELLOW = "#dcdcaa"  # fungsi
LBLUE = "#9cdcfe"   # variabel
CONST = "#4fc1ff"   # konstanta

COLORS = {
    Token: FG,
    Keyword: BLUE,
    Keyword.Namespace: PURPLE,
    Name: LBLUE,
    Name.Function: YELLOW,
    Name.Class: TEAL,
    Name.Builtin: YELLOW,
    Name.Builtin.Pseudo: BLUE,  # self, cls
    Name.Decorator: YELLOW,
    Name.Exception: TEAL,
    Name.Namespace: TEAL,
    Name.Constant: CONST,
    Name.Tag: BLUE,
    Name.Attribute: LBLUE,
    Name.Label: "#c8c8c8",
    String: "#ce9178",
    String.Escape: "#d7ba7d",
    String.Interpol: BLUE,
    String.Regex: "#d16969",
    Number: "#b5cea8",
    Comment: "#6a9955",
    Comment.Preproc: PURPLE,
    Comment.PreprocFile: "#ce9178",
    Operator: FG,
    Operator.Word: BLUE,
    Punctuation: FG,
}

CONTROL = {
    "if", "elif", "else", "for", "while", "do", "return", "try", "except", "finally",
    "raise", "throw", "catch", "with", "yield", "await", "break", "continue", "pass",
    "assert", "import", "from", "as", "switch", "case", "default", "export", "goto",
}
TYPE_BUILTINS = {
    "str", "int", "float", "bool", "list", "dict", "set", "tuple", "object", "bytes",
    "type", "frozenset", "bytearray", "complex", "range",
}


def color_for(ttype):
    while ttype not in COLORS:
        ttype = ttype.parent
    return COLORS[ttype]


def colorize(tokens):
    """Beri warna per token, plus sedikit heuristik supaya mirip VS Code."""
    styled = []
    for i, (tt, val) in enumerate(tokens):
        color = color_for(tt)
        if tt in Keyword and val in CONTROL:
            color = PURPLE
        elif tt is Name.Builtin and val in TYPE_BUILTINS:
            color = TEAL
        elif tt is Name or tt is Name.Other:
            nxt = tokens[i + 1][1] if i + 1 < len(tokens) else ""
            if nxt.startswith("("):
                color = YELLOW  # pemanggilan fungsi
            elif val.isupper() and len(val) > 1:
                color = CONST
            elif val[:1].isupper():
                color = TEAL    # nama class / tipe
        styled.append((val, color))
    return styled


# ---------------------------------------------------------------- font
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\consola.ttf",       # Consolas (default VS Code di Windows)
    r"C:\Windows\Fonts\CascadiaMono.ttf",
    r"C:\Windows\Fonts\CascadiaCode.ttf",
    r"C:\Windows\Fonts\cour.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "/usr/share/fonts/TTF/DejaVuSansMono.ttf",
    "consola.ttf",
    "DejaVuSansMono.ttf",
    "LiberationMono-Regular.ttf",
]


def load_font(path, size):
    for cand in ([path] if path else FONT_CANDIDATES):
        try:
            return ImageFont.truetype(cand, size)
        except OSError:
            continue
    sys.exit("Font monospace tidak ketemu. Pakai opsi  --font C:\\path\\ke\\font.ttf")


# ---------------------------------------------------------------- baca & tokenisasi
def pick_lexer(path, code, lang):
    opts = dict(stripnl=False, stripall=False, ensurenl=True)
    try:
        if lang:
            return get_lexer_by_name(lang, **opts)
        return get_lexer_for_filename(path, code, **opts)
    except ClassNotFound:
        try:
            return guess_lexer(code, **opts)
        except ClassNotFound:
            return TextLexer(**opts)


def build_lines(code, lexer, n_lines):
    styled = colorize(list(lexer.get_tokens(code)))
    lines = [[]]
    for text, color in styled:
        for j, part in enumerate(text.split("\n")):
            if j > 0:
                lines.append([])
            if part:
                lines[-1].append((part, color))
    lines = (lines + [[] for _ in range(n_lines)])[:n_lines]
    return lines


def indent_levels(raw_lines):
    """Indent (dalam kolom) tiap baris. Baris kosong ikut indent tetangganya
    supaya garis indent tidak putus-putus."""
    ind = [None if not l.strip() else len(l) - len(l.lstrip(" ")) for l in raw_lines]
    n = len(ind)
    prev, nxt = [0] * n, [0] * n
    last = 0
    for i in range(n):
        if ind[i] is not None:
            last = ind[i]
        prev[i] = last
    last = 0
    for i in range(n - 1, -1, -1):
        if ind[i] is not None:
            last = ind[i]
        nxt[i] = last
    return [ind[i] if ind[i] is not None else min(prev[i], nxt[i]) for i in range(n)]


# ---------------------------------------------------------------- gambar
def render(lines, indents, start, end, total, args, font, cw, line_h, out_path):
    chunk = range(start, end)
    digits = len(str(total))
    pad = int(cw * 2)
    x0 = pad + (digits * cw + cw * 3 if not args.no_line_numbers else 0)
    maxcols = max((sum(len(t) for t, _ in lines[i]) for i in chunk), default=0)
    width = int(x0 + maxcols * cw + pad * 2)
    height = int((end - start) * line_h + line_h * 2)

    if width * height * 3 > 600_000_000:
        print("  [!] Gambar sangat besar, bisa makan banyak RAM. "
              "Coba pakai  --split 300  supaya dipecah jadi beberapa foto.")

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    for k, i in enumerate(chunk):
        top = line_h + k * line_h
        mid = top + line_h / 2

        # garis indent (tab guides)
        for col in range(0, indents[i], args.tab_size):
            x = int(round(x0 + col * cw))
            draw.line([(x, top), (x, top + line_h)], fill=GUIDE, width=1)

        # nomor baris
        if not args.no_line_numbers:
            draw.text((pad + digits * cw, mid), str(i + 1), font=font, fill=LINE_NO, anchor="rm")

        # kode
        col = 0
        for text, color in lines[i]:
            if text.strip():
                draw.text((x0 + col * cw, mid), text, font=font, fill=color, anchor="lm")
            col += len(text)

    img.save(out_path)
    print(f"  -> {out_path}  ({width}x{height}px, baris {start + 1}-{end})")


def convert(path, args):
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        code = f.read()
    code = code.replace("\r\n", "\n").replace("\r", "\n").expandtabs(args.tab_size).rstrip()
    if not code:
        sys.exit("File kosong.")

    raw_lines = code.split("\n")
    total = len(raw_lines)
    lexer = pick_lexer(path, code, args.lang)
    lines = build_lines(code, lexer, total)
    indents = indent_levels(raw_lines)

    font = load_font(args.font, args.font_size)
    cw = font.getlength("M" * 100) / 100
    line_h = int(args.font_size * 1.45)

    base = args.output or os.path.splitext(path)[0] + ".png"
    root, ext = os.path.splitext(base)
    ext = ext or ".png"

    print(f"{os.path.basename(path)}: {total} baris, bahasa {lexer.name}")
    outputs = []
    if args.split and args.split < total:
        parts = (total + args.split - 1) // args.split
        for p in range(parts):
            s, e = p * args.split, min(total, (p + 1) * args.split)
            out = f"{root}_part{p + 1}{ext}"
            render(lines, indents, s, e, total, args, font, cw, line_h, out)
            outputs.append(out)
    else:
        out = root + ext
        render(lines, indents, 0, total, total, args, font, cw, line_h, out)
        outputs.append(out)
    return outputs


def main():
    ap = argparse.ArgumentParser(description="Ubah file kode jadi foto panjang (VS Code Dark+).")
    ap.add_argument("file", nargs="?", help="file kode (kosongkan untuk pilih lewat jendela)")
    ap.add_argument("-o", "--output", help="nama file hasil (default: nama_file.png)")
    ap.add_argument("--lang", help="paksa bahasa, mis. python, javascript, cpp")
    ap.add_argument("--tab-size", type=int, default=4)
    ap.add_argument("--font-size", type=int, default=20)
    ap.add_argument("--font", help="path font monospace .ttf")
    ap.add_argument("--no-line-numbers", action="store_true")
    ap.add_argument("--split", type=int, default=0, metavar="N",
                    help="pecah jadi beberapa foto, masing-masing N baris")
    args = ap.parse_args()

    from_dialog = False
    path = args.file
    if not path:
        try:
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename(title="Pilih file kode")
            root.destroy()
            from_dialog = True
        except Exception:
            ap.error("Sebutkan file kodenya, contoh:  python code2img.py kode.py")
        if not path:
            return
    if not os.path.isfile(path):
        sys.exit(f"File tidak ditemukan: {path}")

    outputs = convert(path, args)

    if from_dialog and sys.platform == "win32":
        os.startfile(os.path.dirname(os.path.abspath(outputs[0])))


if __name__ == "__main__":
    main()
