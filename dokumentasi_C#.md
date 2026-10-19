# C#

- **Dibuat:** 2026-10-19 19:39:35
- **Sumber:** `d:\Project\Coding\Code Practice\C#`
- **Total file:** 239 (51 sub-folder disertakan)

## Konteks & Peraturan untuk AI — Baca Ini Dulu

Halo AI! Ini adalah sesi lanjutan belajar Python seorang pemula. Obrolan sebelumnya sudah mencapai batas token sehingga chat dibuka ulang. File ini berisi seluruh kode yang sudah pernah dibuat sebagai bukti progres belajar.

Tugasmu adalah menjadi tutor/mentor Python interaktif dengan aturan berikut:

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
   - Sertakan contoh input/output yang diharapkan.
   - Jangan gunakan library eksternal kecuali sudah di level lanjut.
7. Lihat daftar kode di bawah untuk mengetahui syntax dan topik apa saja yang sudah pernah dipelajari. Gunakan ini sebagai acuan level dan titik lanjut pembelajaran.
8. Setiap soal harus punya nama level yang jelas dan sesuai dengan materi/topik soal tersebut (contoh: "Level 3 - Looping Dasar (for)", "Level 5 - Array & Pencarian Nilai"). Jangan hanya menulis "Level 3" tanpa nama topiknya.
9. Soal sebisa mungkin relate/relevan dengan kasus nyata dalam pemrograman, bukan sekadar soal abstrak/teoretis (contoh: hitung total belanja, validasi input umur, cari nilai tertinggi dari daftar nilai siswa, dsb).
10. Setiap soal harus menyertakan aturan syntax apa saja yang boleh digunakan untuk mengerjakannya. Utamakan membatasi syntax ke yang sudah dikuasai pemula, supaya fundamental/pondasi logikanya kuat dulu (contoh: "Boleh pakai: variabel, if/else, perulangan for. Belum boleh pakai: min(), max(), sorted().").
11. Syntax/fungsi baru yang lebih ringkas boleh di-unlock jika fundamental pengguna di topik terkait sudah cukup kuat (contoh: setelah pengguna lancar mencari nilai tertinggi/terendah di array secara manual, barulah boleh dikenalkan shortcut seperti min()/max()). Jelaskan bahwa ini "unlock syntax baru" sebagai bentuk progres, bukan diberikan dari awal.
12. Materi/topik baru boleh di-unlock jika materi sebelumnya sudah dikuasai dengan baik, bukan cuma sekali lulus, tapi sudah cukup beberapa soal di topik tersebut. Saat unlock materi baru, beri tahu pengguna secara eksplisit bahwa ini adalah materi baru yang baru dibuka.

### Cara Memulai Sesi Ini

Setelah membaca file ini, sambut pengguna dan tanyakan: "Mau lanjut dari mana? Minta soal baru, atau ada topik tertentu?"

---

## Struktur

```
C#/
├── Big Project/
│   └── Radix Converter/
│       ├── bin/
│       │   └── Debug/
│       │       └── net8.0/
│       │           ├── Radix Converter.deps.json
│       │           └── Radix Converter.runtimeconfig.json
│       ├── obj/
│       │   ├── Debug/
│       │   │   └── net8.0/
│       │   │       ├── Radix Converter.AssemblyInfo.cs
│       │   │       ├── Radix Converter.AssemblyInfoInputs.cache
│       │   │       ├── Radix Converter.csproj.CoreCompileInputs.cache
│       │   │       ├── Radix Converter.csproj.FileListAbsolute.txt
│       │   │       ├── Radix Converter.GeneratedMSBuildEditorConfig.editorconfig
│       │   │       ├── Radix Converter.genruntimeconfig.cache
│       │   │       ├── Radix Converter.GlobalUsings.g.cs
│       │   │       └── Radix Converter.sourcelink.json
│       │   ├── project.assets.json
│       │   ├── project.nuget.cache
│       │   ├── Radix Converter.csproj.nuget.dgspec.json
│       │   ├── Radix Converter.csproj.nuget.g.props
│       │   └── Radix Converter.csproj.nuget.g.targets
│       ├── Program.cs
│       └── Radix Converter.csproj
├── bin/
│   └── Debug/
│       └── net8.0/
│           ├── C#.deps.json
│           └── C#.runtimeconfig.json
├── C#.csproj
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
├── L015-While Loop dengan kondisi.cs
├── L016-While dengan Counter.cs
├── L017-Do While.cs
├── obj/
│   ├── C#.csproj.nuget.dgspec.json
│   ├── C#.csproj.nuget.g.props
│   ├── C#.csproj.nuget.g.targets
│   ├── Debug/
│   │   └── net8.0/
│   │       ├── C#.AssemblyInfo.cs
│   │       ├── C#.AssemblyInfoInputs.cache
│   │       ├── C#.csproj.CoreCompileInputs.cache
│   │       ├── C#.csproj.FileListAbsolute.txt
│   │       ├── C#.GeneratedMSBuildEditorConfig.editorconfig
│   │       ├── C#.genruntimeconfig.cache
│   │       ├── C#.GlobalUsings.g.cs
│   │       └── C#.sourcelink.json
│   ├── project.assets.json
│   └── project.nuget.cache
├── Praktik/
│   ├── Praktik 1/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 1.deps.json
│   │   │           └── Praktik 1.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 1.AssemblyInfo.cs
│   │   │   │       ├── Praktik 1.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 1.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 1.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 1.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 1.genruntimeconfig.cache
│   │   │   │       ├── Praktik 1.GlobalUsings.g.cs
│   │   │   │       └── Praktik 1.sourcelink.json
│   │   │   ├── Praktik 1.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 1.csproj.nuget.g.props
│   │   │   ├── Praktik 1.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 1.csproj
│   │   └── Program.cs
│   ├── Praktik 10/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 10.deps.json
│   │   │           └── Praktik 10.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 10.AssemblyInfo.cs
│   │   │   │       ├── Praktik 10.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 10.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 10.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 10.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 10.genruntimeconfig.cache
│   │   │   │       ├── Praktik 10.GlobalUsings.g.cs
│   │   │   │       └── Praktik 10.sourcelink.json
│   │   │   ├── Praktik 10.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 10.csproj.nuget.g.props
│   │   │   ├── Praktik 10.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 10.csproj
│   │   └── Program.cs
│   ├── Praktik 2/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 2.deps.json
│   │   │           └── Praktik 2.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 2.AssemblyInfo.cs
│   │   │   │       ├── Praktik 2.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 2.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 2.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 2.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 2.genruntimeconfig.cache
│   │   │   │       ├── Praktik 2.GlobalUsings.g.cs
│   │   │   │       └── Praktik 2.sourcelink.json
│   │   │   ├── Praktik 2.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 2.csproj.nuget.g.props
│   │   │   ├── Praktik 2.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 2.csproj
│   │   └── Program.cs
│   ├── Praktik 3/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 3.deps.json
│   │   │           └── Praktik 3.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 3.AssemblyInfo.cs
│   │   │   │       ├── Praktik 3.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 3.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 3.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 3.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 3.genruntimeconfig.cache
│   │   │   │       ├── Praktik 3.GlobalUsings.g.cs
│   │   │   │       └── Praktik 3.sourcelink.json
│   │   │   ├── Praktik 3.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 3.csproj.nuget.g.props
│   │   │   ├── Praktik 3.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 3.csproj
│   │   └── Program.cs
│   ├── Praktik 4/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 4.deps.json
│   │   │           └── Praktik 4.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 4.AssemblyInfo.cs
│   │   │   │       ├── Praktik 4.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 4.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 4.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 4.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 4.genruntimeconfig.cache
│   │   │   │       ├── Praktik 4.GlobalUsings.g.cs
│   │   │   │       └── Praktik 4.sourcelink.json
│   │   │   ├── Praktik 4.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 4.csproj.nuget.g.props
│   │   │   ├── Praktik 4.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 4.csproj
│   │   └── Program.cs
│   ├── Praktik 5/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 5.deps.json
│   │   │           └── Praktik 5.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 5.AssemblyInfo.cs
│   │   │   │       ├── Praktik 5.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 5.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 5.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 5.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 5.genruntimeconfig.cache
│   │   │   │       ├── Praktik 5.GlobalUsings.g.cs
│   │   │   │       └── Praktik 5.sourcelink.json
│   │   │   ├── Praktik 5.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 5.csproj.nuget.g.props
│   │   │   ├── Praktik 5.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 5.csproj
│   │   └── Program.cs
│   ├── Praktik 6/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 6.deps.json
│   │   │           └── Praktik 6.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 6.AssemblyInfo.cs
│   │   │   │       ├── Praktik 6.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 6.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 6.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 6.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 6.genruntimeconfig.cache
│   │   │   │       ├── Praktik 6.GlobalUsings.g.cs
│   │   │   │       └── Praktik 6.sourcelink.json
│   │   │   ├── Praktik 6.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 6.csproj.nuget.g.props
│   │   │   ├── Praktik 6.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 6.csproj
│   │   └── Program.cs
│   ├── Praktik 7/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 7.deps.json
│   │   │           └── Praktik 7.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 7.AssemblyInfo.cs
│   │   │   │       ├── Praktik 7.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 7.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 7.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 7.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 7.genruntimeconfig.cache
│   │   │   │       ├── Praktik 7.GlobalUsings.g.cs
│   │   │   │       └── Praktik 7.sourcelink.json
│   │   │   ├── Praktik 7.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 7.csproj.nuget.g.props
│   │   │   ├── Praktik 7.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 7.csproj
│   │   └── Program.cs
│   ├── Praktik 8/
│   │   ├── bin/
│   │   │   └── Debug/
│   │   │       └── net8.0/
│   │   │           ├── Praktik 8.deps.json
│   │   │           └── Praktik 8.runtimeconfig.json
│   │   ├── obj/
│   │   │   ├── Debug/
│   │   │   │   └── net8.0/
│   │   │   │       ├── Praktik 8.AssemblyInfo.cs
│   │   │   │       ├── Praktik 8.AssemblyInfoInputs.cache
│   │   │   │       ├── Praktik 8.csproj.CoreCompileInputs.cache
│   │   │   │       ├── Praktik 8.csproj.FileListAbsolute.txt
│   │   │   │       ├── Praktik 8.GeneratedMSBuildEditorConfig.editorconfig
│   │   │   │       ├── Praktik 8.genruntimeconfig.cache
│   │   │   │       ├── Praktik 8.GlobalUsings.g.cs
│   │   │   │       └── Praktik 8.sourcelink.json
│   │   │   ├── Praktik 8.csproj.nuget.dgspec.json
│   │   │   ├── Praktik 8.csproj.nuget.g.props
│   │   │   ├── Praktik 8.csproj.nuget.g.targets
│   │   │   ├── project.assets.json
│   │   │   └── project.nuget.cache
│   │   ├── Praktik 8.csproj
│   │   └── Program.cs
│   └── Praktik 9/
│       ├── bin/
│       │   └── Debug/
│       │       └── net8.0/
│       │           ├── Praktik 9.deps.json
│       │           └── Praktik 9.runtimeconfig.json
│       ├── obj/
│       │   ├── Debug/
│       │   │   └── net8.0/
│       │   │       ├── Praktik 9.AssemblyInfo.cs
│       │   │       ├── Praktik 9.AssemblyInfoInputs.cache
│       │   │       ├── Praktik 9.csproj.CoreCompileInputs.cache
│       │   │       ├── Praktik 9.csproj.FileListAbsolute.txt
│       │   │       ├── Praktik 9.GeneratedMSBuildEditorConfig.editorconfig
│       │   │       ├── Praktik 9.genruntimeconfig.cache
│       │   │       ├── Praktik 9.GlobalUsings.g.cs
│       │   │       └── Praktik 9.sourcelink.json
│       │   ├── Praktik 9.csproj.nuget.dgspec.json
│       │   ├── Praktik 9.csproj.nuget.g.props
│       │   ├── Praktik 9.csproj.nuget.g.targets
│       │   ├── project.assets.json
│       │   └── project.nuget.cache
│       ├── Praktik 9.csproj
│       └── Program.cs
├── run_c_sharp.py
├── Template C sharp.cs
└── Tugas/
    └── Tugas 4/
        ├── bin/
        │   └── Debug/
        │       └── net8.0/
        │           ├── Tugas 4.deps.json
        │           └── Tugas 4.runtimeconfig.json
        ├── obj/
        │   ├── Debug/
        │   │   └── net8.0/
        │   │       ├── Tugas 4.AssemblyInfo.cs
        │   │       ├── Tugas 4.AssemblyInfoInputs.cache
        │   │       ├── Tugas 4.csproj.CoreCompileInputs.cache
        │   │       ├── Tugas 4.csproj.FileListAbsolute.txt
        │   │       ├── Tugas 4.GeneratedMSBuildEditorConfig.editorconfig
        │   │       ├── Tugas 4.genruntimeconfig.cache
        │   │       ├── Tugas 4.GlobalUsings.g.cs
        │   │       └── Tugas 4.sourcelink.json
        │   ├── project.assets.json
        │   ├── project.nuget.cache
        │   ├── Tugas 4.csproj.nuget.dgspec.json
        │   ├── Tugas 4.csproj.nuget.g.props
        │   └── Tugas 4.csproj.nuget.g.targets
        ├── Program.cs
        └── Tugas 4.csproj
```

## Daftar Isi

- [C#.csproj](#ccsproj)
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
- [L015-While Loop dengan kondisi.cs](#l015-while-loop-dengan-kondisics)
- [L016-While dengan Counter.cs](#l016-while-dengan-countercs)
- [L017-Do While.cs](#l017-do-whilecs)
- [Template C sharp.cs](#template-c-sharpcs)
- [run_c_sharp.py](#run_c_sharppy)
- [Big Project/Radix Converter/Program.cs](#big-project-radix-converter-programcs)
- [Big Project/Radix Converter/Radix Converter.csproj](#big-project-radix-converter-radix-convertercsproj)
- [Big Project/Radix Converter/bin/Debug/net8.0/Radix Converter.deps.json](#big-project-radix-converter-bin-debug-net80-radix-converterdepsjson)
- [Big Project/Radix Converter/bin/Debug/net8.0/Radix Converter.runtimeconfig.json](#big-project-radix-converter-bin-debug-net80-radix-converterruntimeconfigjson)
- [Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.dgspec.json](#big-project-radix-converter-obj-radix-convertercsprojnugetdgspecjson)
- [Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.g.props](#big-project-radix-converter-obj-radix-convertercsprojnugetgprops)
- [Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.g.targets](#big-project-radix-converter-obj-radix-convertercsprojnugetgtargets)
- [Big Project/Radix Converter/obj/project.assets.json](#big-project-radix-converter-obj-projectassetsjson)
- [Big Project/Radix Converter/obj/project.nuget.cache](#big-project-radix-converter-obj-projectnugetcache)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.AssemblyInfo.cs](#big-project-radix-converter-obj-debug-net80-radix-converterassemblyinfocs)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.AssemblyInfoInputs.cache](#big-project-radix-converter-obj-debug-net80-radix-converterassemblyinfoinputscache)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.GeneratedMSBuildEditorConfig.editorconfig](#big-project-radix-converter-obj-debug-net80-radix-convertergeneratedmsbuildeditorconfigeditorconfig)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.GlobalUsings.g.cs](#big-project-radix-converter-obj-debug-net80-radix-converterglobalusingsgcs)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.csproj.CoreCompileInputs.cache](#big-project-radix-converter-obj-debug-net80-radix-convertercsprojcorecompileinputscache)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.csproj.FileListAbsolute.txt](#big-project-radix-converter-obj-debug-net80-radix-convertercsprojfilelistabsolutetxt)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.genruntimeconfig.cache](#big-project-radix-converter-obj-debug-net80-radix-convertergenruntimeconfigcache)
- [Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.sourcelink.json](#big-project-radix-converter-obj-debug-net80-radix-convertersourcelinkjson)
- [Praktik/Praktik 1/Praktik 1.csproj](#praktik-praktik-1-praktik-1csproj)
- [Praktik/Praktik 1/Program.cs](#praktik-praktik-1-programcs)
- [Praktik/Praktik 1/bin/Debug/net8.0/Praktik 1.deps.json](#praktik-praktik-1-bin-debug-net80-praktik-1depsjson)
- [Praktik/Praktik 1/bin/Debug/net8.0/Praktik 1.runtimeconfig.json](#praktik-praktik-1-bin-debug-net80-praktik-1runtimeconfigjson)
- [Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.dgspec.json](#praktik-praktik-1-obj-praktik-1csprojnugetdgspecjson)
- [Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.g.props](#praktik-praktik-1-obj-praktik-1csprojnugetgprops)
- [Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.g.targets](#praktik-praktik-1-obj-praktik-1csprojnugetgtargets)
- [Praktik/Praktik 1/obj/project.assets.json](#praktik-praktik-1-obj-projectassetsjson)
- [Praktik/Praktik 1/obj/project.nuget.cache](#praktik-praktik-1-obj-projectnugetcache)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.AssemblyInfo.cs](#praktik-praktik-1-obj-debug-net80-praktik-1assemblyinfocs)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.AssemblyInfoInputs.cache](#praktik-praktik-1-obj-debug-net80-praktik-1assemblyinfoinputscache)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-1-obj-debug-net80-praktik-1generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.GlobalUsings.g.cs](#praktik-praktik-1-obj-debug-net80-praktik-1globalusingsgcs)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.csproj.CoreCompileInputs.cache](#praktik-praktik-1-obj-debug-net80-praktik-1csprojcorecompileinputscache)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.csproj.FileListAbsolute.txt](#praktik-praktik-1-obj-debug-net80-praktik-1csprojfilelistabsolutetxt)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.genruntimeconfig.cache](#praktik-praktik-1-obj-debug-net80-praktik-1genruntimeconfigcache)
- [Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.sourcelink.json](#praktik-praktik-1-obj-debug-net80-praktik-1sourcelinkjson)
- [Praktik/Praktik 10/Praktik 10.csproj](#praktik-praktik-10-praktik-10csproj)
- [Praktik/Praktik 10/Program.cs](#praktik-praktik-10-programcs)
- [Praktik/Praktik 10/bin/Debug/net8.0/Praktik 10.deps.json](#praktik-praktik-10-bin-debug-net80-praktik-10depsjson)
- [Praktik/Praktik 10/bin/Debug/net8.0/Praktik 10.runtimeconfig.json](#praktik-praktik-10-bin-debug-net80-praktik-10runtimeconfigjson)
- [Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.dgspec.json](#praktik-praktik-10-obj-praktik-10csprojnugetdgspecjson)
- [Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.g.props](#praktik-praktik-10-obj-praktik-10csprojnugetgprops)
- [Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.g.targets](#praktik-praktik-10-obj-praktik-10csprojnugetgtargets)
- [Praktik/Praktik 10/obj/project.assets.json](#praktik-praktik-10-obj-projectassetsjson)
- [Praktik/Praktik 10/obj/project.nuget.cache](#praktik-praktik-10-obj-projectnugetcache)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.AssemblyInfo.cs](#praktik-praktik-10-obj-debug-net80-praktik-10assemblyinfocs)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.AssemblyInfoInputs.cache](#praktik-praktik-10-obj-debug-net80-praktik-10assemblyinfoinputscache)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-10-obj-debug-net80-praktik-10generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.GlobalUsings.g.cs](#praktik-praktik-10-obj-debug-net80-praktik-10globalusingsgcs)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.csproj.CoreCompileInputs.cache](#praktik-praktik-10-obj-debug-net80-praktik-10csprojcorecompileinputscache)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.csproj.FileListAbsolute.txt](#praktik-praktik-10-obj-debug-net80-praktik-10csprojfilelistabsolutetxt)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.genruntimeconfig.cache](#praktik-praktik-10-obj-debug-net80-praktik-10genruntimeconfigcache)
- [Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.sourcelink.json](#praktik-praktik-10-obj-debug-net80-praktik-10sourcelinkjson)
- [Praktik/Praktik 2/Praktik 2.csproj](#praktik-praktik-2-praktik-2csproj)
- [Praktik/Praktik 2/Program.cs](#praktik-praktik-2-programcs)
- [Praktik/Praktik 2/bin/Debug/net8.0/Praktik 2.deps.json](#praktik-praktik-2-bin-debug-net80-praktik-2depsjson)
- [Praktik/Praktik 2/bin/Debug/net8.0/Praktik 2.runtimeconfig.json](#praktik-praktik-2-bin-debug-net80-praktik-2runtimeconfigjson)
- [Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.dgspec.json](#praktik-praktik-2-obj-praktik-2csprojnugetdgspecjson)
- [Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.g.props](#praktik-praktik-2-obj-praktik-2csprojnugetgprops)
- [Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.g.targets](#praktik-praktik-2-obj-praktik-2csprojnugetgtargets)
- [Praktik/Praktik 2/obj/project.assets.json](#praktik-praktik-2-obj-projectassetsjson)
- [Praktik/Praktik 2/obj/project.nuget.cache](#praktik-praktik-2-obj-projectnugetcache)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.AssemblyInfo.cs](#praktik-praktik-2-obj-debug-net80-praktik-2assemblyinfocs)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.AssemblyInfoInputs.cache](#praktik-praktik-2-obj-debug-net80-praktik-2assemblyinfoinputscache)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-2-obj-debug-net80-praktik-2generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.GlobalUsings.g.cs](#praktik-praktik-2-obj-debug-net80-praktik-2globalusingsgcs)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.csproj.CoreCompileInputs.cache](#praktik-praktik-2-obj-debug-net80-praktik-2csprojcorecompileinputscache)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.csproj.FileListAbsolute.txt](#praktik-praktik-2-obj-debug-net80-praktik-2csprojfilelistabsolutetxt)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.genruntimeconfig.cache](#praktik-praktik-2-obj-debug-net80-praktik-2genruntimeconfigcache)
- [Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.sourcelink.json](#praktik-praktik-2-obj-debug-net80-praktik-2sourcelinkjson)
- [Praktik/Praktik 3/Praktik 3.csproj](#praktik-praktik-3-praktik-3csproj)
- [Praktik/Praktik 3/Program.cs](#praktik-praktik-3-programcs)
- [Praktik/Praktik 3/bin/Debug/net8.0/Praktik 3.deps.json](#praktik-praktik-3-bin-debug-net80-praktik-3depsjson)
- [Praktik/Praktik 3/bin/Debug/net8.0/Praktik 3.runtimeconfig.json](#praktik-praktik-3-bin-debug-net80-praktik-3runtimeconfigjson)
- [Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.dgspec.json](#praktik-praktik-3-obj-praktik-3csprojnugetdgspecjson)
- [Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.g.props](#praktik-praktik-3-obj-praktik-3csprojnugetgprops)
- [Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.g.targets](#praktik-praktik-3-obj-praktik-3csprojnugetgtargets)
- [Praktik/Praktik 3/obj/project.assets.json](#praktik-praktik-3-obj-projectassetsjson)
- [Praktik/Praktik 3/obj/project.nuget.cache](#praktik-praktik-3-obj-projectnugetcache)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.AssemblyInfo.cs](#praktik-praktik-3-obj-debug-net80-praktik-3assemblyinfocs)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.AssemblyInfoInputs.cache](#praktik-praktik-3-obj-debug-net80-praktik-3assemblyinfoinputscache)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-3-obj-debug-net80-praktik-3generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.GlobalUsings.g.cs](#praktik-praktik-3-obj-debug-net80-praktik-3globalusingsgcs)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.csproj.CoreCompileInputs.cache](#praktik-praktik-3-obj-debug-net80-praktik-3csprojcorecompileinputscache)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.csproj.FileListAbsolute.txt](#praktik-praktik-3-obj-debug-net80-praktik-3csprojfilelistabsolutetxt)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.genruntimeconfig.cache](#praktik-praktik-3-obj-debug-net80-praktik-3genruntimeconfigcache)
- [Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.sourcelink.json](#praktik-praktik-3-obj-debug-net80-praktik-3sourcelinkjson)
- [Praktik/Praktik 4/Praktik 4.csproj](#praktik-praktik-4-praktik-4csproj)
- [Praktik/Praktik 4/Program.cs](#praktik-praktik-4-programcs)
- [Praktik/Praktik 4/bin/Debug/net8.0/Praktik 4.deps.json](#praktik-praktik-4-bin-debug-net80-praktik-4depsjson)
- [Praktik/Praktik 4/bin/Debug/net8.0/Praktik 4.runtimeconfig.json](#praktik-praktik-4-bin-debug-net80-praktik-4runtimeconfigjson)
- [Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.dgspec.json](#praktik-praktik-4-obj-praktik-4csprojnugetdgspecjson)
- [Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.g.props](#praktik-praktik-4-obj-praktik-4csprojnugetgprops)
- [Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.g.targets](#praktik-praktik-4-obj-praktik-4csprojnugetgtargets)
- [Praktik/Praktik 4/obj/project.assets.json](#praktik-praktik-4-obj-projectassetsjson)
- [Praktik/Praktik 4/obj/project.nuget.cache](#praktik-praktik-4-obj-projectnugetcache)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.AssemblyInfo.cs](#praktik-praktik-4-obj-debug-net80-praktik-4assemblyinfocs)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.AssemblyInfoInputs.cache](#praktik-praktik-4-obj-debug-net80-praktik-4assemblyinfoinputscache)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-4-obj-debug-net80-praktik-4generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.GlobalUsings.g.cs](#praktik-praktik-4-obj-debug-net80-praktik-4globalusingsgcs)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.csproj.CoreCompileInputs.cache](#praktik-praktik-4-obj-debug-net80-praktik-4csprojcorecompileinputscache)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.csproj.FileListAbsolute.txt](#praktik-praktik-4-obj-debug-net80-praktik-4csprojfilelistabsolutetxt)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.genruntimeconfig.cache](#praktik-praktik-4-obj-debug-net80-praktik-4genruntimeconfigcache)
- [Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.sourcelink.json](#praktik-praktik-4-obj-debug-net80-praktik-4sourcelinkjson)
- [Praktik/Praktik 5/Praktik 5.csproj](#praktik-praktik-5-praktik-5csproj)
- [Praktik/Praktik 5/Program.cs](#praktik-praktik-5-programcs)
- [Praktik/Praktik 5/bin/Debug/net8.0/Praktik 5.deps.json](#praktik-praktik-5-bin-debug-net80-praktik-5depsjson)
- [Praktik/Praktik 5/bin/Debug/net8.0/Praktik 5.runtimeconfig.json](#praktik-praktik-5-bin-debug-net80-praktik-5runtimeconfigjson)
- [Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.dgspec.json](#praktik-praktik-5-obj-praktik-5csprojnugetdgspecjson)
- [Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.g.props](#praktik-praktik-5-obj-praktik-5csprojnugetgprops)
- [Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.g.targets](#praktik-praktik-5-obj-praktik-5csprojnugetgtargets)
- [Praktik/Praktik 5/obj/project.assets.json](#praktik-praktik-5-obj-projectassetsjson)
- [Praktik/Praktik 5/obj/project.nuget.cache](#praktik-praktik-5-obj-projectnugetcache)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.AssemblyInfo.cs](#praktik-praktik-5-obj-debug-net80-praktik-5assemblyinfocs)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.AssemblyInfoInputs.cache](#praktik-praktik-5-obj-debug-net80-praktik-5assemblyinfoinputscache)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-5-obj-debug-net80-praktik-5generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.GlobalUsings.g.cs](#praktik-praktik-5-obj-debug-net80-praktik-5globalusingsgcs)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.csproj.CoreCompileInputs.cache](#praktik-praktik-5-obj-debug-net80-praktik-5csprojcorecompileinputscache)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.csproj.FileListAbsolute.txt](#praktik-praktik-5-obj-debug-net80-praktik-5csprojfilelistabsolutetxt)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.genruntimeconfig.cache](#praktik-praktik-5-obj-debug-net80-praktik-5genruntimeconfigcache)
- [Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.sourcelink.json](#praktik-praktik-5-obj-debug-net80-praktik-5sourcelinkjson)
- [Praktik/Praktik 6/Praktik 6.csproj](#praktik-praktik-6-praktik-6csproj)
- [Praktik/Praktik 6/Program.cs](#praktik-praktik-6-programcs)
- [Praktik/Praktik 6/bin/Debug/net8.0/Praktik 6.deps.json](#praktik-praktik-6-bin-debug-net80-praktik-6depsjson)
- [Praktik/Praktik 6/bin/Debug/net8.0/Praktik 6.runtimeconfig.json](#praktik-praktik-6-bin-debug-net80-praktik-6runtimeconfigjson)
- [Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.dgspec.json](#praktik-praktik-6-obj-praktik-6csprojnugetdgspecjson)
- [Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.g.props](#praktik-praktik-6-obj-praktik-6csprojnugetgprops)
- [Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.g.targets](#praktik-praktik-6-obj-praktik-6csprojnugetgtargets)
- [Praktik/Praktik 6/obj/project.assets.json](#praktik-praktik-6-obj-projectassetsjson)
- [Praktik/Praktik 6/obj/project.nuget.cache](#praktik-praktik-6-obj-projectnugetcache)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.AssemblyInfo.cs](#praktik-praktik-6-obj-debug-net80-praktik-6assemblyinfocs)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.AssemblyInfoInputs.cache](#praktik-praktik-6-obj-debug-net80-praktik-6assemblyinfoinputscache)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-6-obj-debug-net80-praktik-6generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.GlobalUsings.g.cs](#praktik-praktik-6-obj-debug-net80-praktik-6globalusingsgcs)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.csproj.CoreCompileInputs.cache](#praktik-praktik-6-obj-debug-net80-praktik-6csprojcorecompileinputscache)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.csproj.FileListAbsolute.txt](#praktik-praktik-6-obj-debug-net80-praktik-6csprojfilelistabsolutetxt)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.genruntimeconfig.cache](#praktik-praktik-6-obj-debug-net80-praktik-6genruntimeconfigcache)
- [Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.sourcelink.json](#praktik-praktik-6-obj-debug-net80-praktik-6sourcelinkjson)
- [Praktik/Praktik 7/Praktik 7.csproj](#praktik-praktik-7-praktik-7csproj)
- [Praktik/Praktik 7/Program.cs](#praktik-praktik-7-programcs)
- [Praktik/Praktik 7/bin/Debug/net8.0/Praktik 7.deps.json](#praktik-praktik-7-bin-debug-net80-praktik-7depsjson)
- [Praktik/Praktik 7/bin/Debug/net8.0/Praktik 7.runtimeconfig.json](#praktik-praktik-7-bin-debug-net80-praktik-7runtimeconfigjson)
- [Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.dgspec.json](#praktik-praktik-7-obj-praktik-7csprojnugetdgspecjson)
- [Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.g.props](#praktik-praktik-7-obj-praktik-7csprojnugetgprops)
- [Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.g.targets](#praktik-praktik-7-obj-praktik-7csprojnugetgtargets)
- [Praktik/Praktik 7/obj/project.assets.json](#praktik-praktik-7-obj-projectassetsjson)
- [Praktik/Praktik 7/obj/project.nuget.cache](#praktik-praktik-7-obj-projectnugetcache)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.AssemblyInfo.cs](#praktik-praktik-7-obj-debug-net80-praktik-7assemblyinfocs)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.AssemblyInfoInputs.cache](#praktik-praktik-7-obj-debug-net80-praktik-7assemblyinfoinputscache)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-7-obj-debug-net80-praktik-7generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.GlobalUsings.g.cs](#praktik-praktik-7-obj-debug-net80-praktik-7globalusingsgcs)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.csproj.CoreCompileInputs.cache](#praktik-praktik-7-obj-debug-net80-praktik-7csprojcorecompileinputscache)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.csproj.FileListAbsolute.txt](#praktik-praktik-7-obj-debug-net80-praktik-7csprojfilelistabsolutetxt)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.genruntimeconfig.cache](#praktik-praktik-7-obj-debug-net80-praktik-7genruntimeconfigcache)
- [Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.sourcelink.json](#praktik-praktik-7-obj-debug-net80-praktik-7sourcelinkjson)
- [Praktik/Praktik 8/Praktik 8.csproj](#praktik-praktik-8-praktik-8csproj)
- [Praktik/Praktik 8/Program.cs](#praktik-praktik-8-programcs)
- [Praktik/Praktik 8/bin/Debug/net8.0/Praktik 8.deps.json](#praktik-praktik-8-bin-debug-net80-praktik-8depsjson)
- [Praktik/Praktik 8/bin/Debug/net8.0/Praktik 8.runtimeconfig.json](#praktik-praktik-8-bin-debug-net80-praktik-8runtimeconfigjson)
- [Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.dgspec.json](#praktik-praktik-8-obj-praktik-8csprojnugetdgspecjson)
- [Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.g.props](#praktik-praktik-8-obj-praktik-8csprojnugetgprops)
- [Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.g.targets](#praktik-praktik-8-obj-praktik-8csprojnugetgtargets)
- [Praktik/Praktik 8/obj/project.assets.json](#praktik-praktik-8-obj-projectassetsjson)
- [Praktik/Praktik 8/obj/project.nuget.cache](#praktik-praktik-8-obj-projectnugetcache)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.AssemblyInfo.cs](#praktik-praktik-8-obj-debug-net80-praktik-8assemblyinfocs)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.AssemblyInfoInputs.cache](#praktik-praktik-8-obj-debug-net80-praktik-8assemblyinfoinputscache)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-8-obj-debug-net80-praktik-8generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.GlobalUsings.g.cs](#praktik-praktik-8-obj-debug-net80-praktik-8globalusingsgcs)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.csproj.CoreCompileInputs.cache](#praktik-praktik-8-obj-debug-net80-praktik-8csprojcorecompileinputscache)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.csproj.FileListAbsolute.txt](#praktik-praktik-8-obj-debug-net80-praktik-8csprojfilelistabsolutetxt)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.genruntimeconfig.cache](#praktik-praktik-8-obj-debug-net80-praktik-8genruntimeconfigcache)
- [Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.sourcelink.json](#praktik-praktik-8-obj-debug-net80-praktik-8sourcelinkjson)
- [Praktik/Praktik 9/Praktik 9.csproj](#praktik-praktik-9-praktik-9csproj)
- [Praktik/Praktik 9/Program.cs](#praktik-praktik-9-programcs)
- [Praktik/Praktik 9/bin/Debug/net8.0/Praktik 9.deps.json](#praktik-praktik-9-bin-debug-net80-praktik-9depsjson)
- [Praktik/Praktik 9/bin/Debug/net8.0/Praktik 9.runtimeconfig.json](#praktik-praktik-9-bin-debug-net80-praktik-9runtimeconfigjson)
- [Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.dgspec.json](#praktik-praktik-9-obj-praktik-9csprojnugetdgspecjson)
- [Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.g.props](#praktik-praktik-9-obj-praktik-9csprojnugetgprops)
- [Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.g.targets](#praktik-praktik-9-obj-praktik-9csprojnugetgtargets)
- [Praktik/Praktik 9/obj/project.assets.json](#praktik-praktik-9-obj-projectassetsjson)
- [Praktik/Praktik 9/obj/project.nuget.cache](#praktik-praktik-9-obj-projectnugetcache)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.AssemblyInfo.cs](#praktik-praktik-9-obj-debug-net80-praktik-9assemblyinfocs)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.AssemblyInfoInputs.cache](#praktik-praktik-9-obj-debug-net80-praktik-9assemblyinfoinputscache)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.GeneratedMSBuildEditorConfig.editorconfig](#praktik-praktik-9-obj-debug-net80-praktik-9generatedmsbuildeditorconfigeditorconfig)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.GlobalUsings.g.cs](#praktik-praktik-9-obj-debug-net80-praktik-9globalusingsgcs)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.csproj.CoreCompileInputs.cache](#praktik-praktik-9-obj-debug-net80-praktik-9csprojcorecompileinputscache)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.csproj.FileListAbsolute.txt](#praktik-praktik-9-obj-debug-net80-praktik-9csprojfilelistabsolutetxt)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.genruntimeconfig.cache](#praktik-praktik-9-obj-debug-net80-praktik-9genruntimeconfigcache)
- [Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.sourcelink.json](#praktik-praktik-9-obj-debug-net80-praktik-9sourcelinkjson)
- [Tugas/Tugas 4/Program.cs](#tugas-tugas-4-programcs)
- [Tugas/Tugas 4/Tugas 4.csproj](#tugas-tugas-4-tugas-4csproj)
- [Tugas/Tugas 4/bin/Debug/net8.0/Tugas 4.deps.json](#tugas-tugas-4-bin-debug-net80-tugas-4depsjson)
- [Tugas/Tugas 4/bin/Debug/net8.0/Tugas 4.runtimeconfig.json](#tugas-tugas-4-bin-debug-net80-tugas-4runtimeconfigjson)
- [Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.dgspec.json](#tugas-tugas-4-obj-tugas-4csprojnugetdgspecjson)
- [Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.g.props](#tugas-tugas-4-obj-tugas-4csprojnugetgprops)
- [Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.g.targets](#tugas-tugas-4-obj-tugas-4csprojnugetgtargets)
- [Tugas/Tugas 4/obj/project.assets.json](#tugas-tugas-4-obj-projectassetsjson)
- [Tugas/Tugas 4/obj/project.nuget.cache](#tugas-tugas-4-obj-projectnugetcache)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.AssemblyInfo.cs](#tugas-tugas-4-obj-debug-net80-tugas-4assemblyinfocs)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.AssemblyInfoInputs.cache](#tugas-tugas-4-obj-debug-net80-tugas-4assemblyinfoinputscache)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.GeneratedMSBuildEditorConfig.editorconfig](#tugas-tugas-4-obj-debug-net80-tugas-4generatedmsbuildeditorconfigeditorconfig)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.GlobalUsings.g.cs](#tugas-tugas-4-obj-debug-net80-tugas-4globalusingsgcs)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.csproj.CoreCompileInputs.cache](#tugas-tugas-4-obj-debug-net80-tugas-4csprojcorecompileinputscache)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.csproj.FileListAbsolute.txt](#tugas-tugas-4-obj-debug-net80-tugas-4csprojfilelistabsolutetxt)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.genruntimeconfig.cache](#tugas-tugas-4-obj-debug-net80-tugas-4genruntimeconfigcache)
- [Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.sourcelink.json](#tugas-tugas-4-obj-debug-net80-tugas-4sourcelinkjson)
- [bin/Debug/net8.0/C#.deps.json](#bin-debug-net80-cdepsjson)
- [bin/Debug/net8.0/C#.runtimeconfig.json](#bin-debug-net80-cruntimeconfigjson)
- [obj/C#.csproj.nuget.dgspec.json](#obj-ccsprojnugetdgspecjson)
- [obj/C#.csproj.nuget.g.props](#obj-ccsprojnugetgprops)
- [obj/C#.csproj.nuget.g.targets](#obj-ccsprojnugetgtargets)
- [obj/project.assets.json](#obj-projectassetsjson)
- [obj/project.nuget.cache](#obj-projectnugetcache)
- [obj/Debug/net8.0/C#.AssemblyInfo.cs](#obj-debug-net80-cassemblyinfocs)
- [obj/Debug/net8.0/C#.AssemblyInfoInputs.cache](#obj-debug-net80-cassemblyinfoinputscache)
- [obj/Debug/net8.0/C#.GeneratedMSBuildEditorConfig.editorconfig](#obj-debug-net80-cgeneratedmsbuildeditorconfigeditorconfig)
- [obj/Debug/net8.0/C#.GlobalUsings.g.cs](#obj-debug-net80-cglobalusingsgcs)
- [obj/Debug/net8.0/C#.csproj.CoreCompileInputs.cache](#obj-debug-net80-ccsprojcorecompileinputscache)
- [obj/Debug/net8.0/C#.csproj.FileListAbsolute.txt](#obj-debug-net80-ccsprojfilelistabsolutetxt)
- [obj/Debug/net8.0/C#.genruntimeconfig.cache](#obj-debug-net80-cgenruntimeconfigcache)
- [obj/Debug/net8.0/C#.sourcelink.json](#obj-debug-net80-csourcelinkjson)

## File

### `C#.csproj`

```csproj
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>

  <ItemGroup>
    <Compile Include="L017-Do While.cs" />
  </ItemGroup>

</Project>
```

### `L001-Variabel dan Output Dasar.cs`

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

```cs
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

### `L015-While Loop dengan kondisi.cs`

```cs
using System;

namespace Code_Practice{
    class L015_While_Loop_dengan_kondisi{
        static void Main(string[] args){

            int Angka = 0;

            while (Angka < 1 || Angka > 5)
            {
                Console.Write("Masukan Angka [1 - 5] : ");
                Angka = int.Parse(Console.ReadLine());

                if (Angka < 1 || Angka > 5)
                {
                    Console.WriteLine("[Error] Angka tidak valid!");
                }
            }

            Console.WriteLine("Angka valid!");
            
        }
    }
}
```

### `L016-While dengan Counter.cs`

```cs
using System;

namespace Code_Practice{
    class L016_While_dengan_Counter{
        static void Main(string[] args){

            int Angka = 0;
            int Percobaan = 0;

            while(Angka < 1 || Angka > 5){
                Percobaan += 1;
                Console.Write("Masukkan angka [1 - 5] : ");
                Angka = int.Parse(Console.ReadLine());
                
                if (Angka < 1 || Angka > 5){
                    Console.WriteLine("[Error] Anda harus memasukkan angka [1 - 5]!");
                }
            }

            Console.WriteLine("Angka valid!");
            Console.WriteLine($"Jumlah Percobaan : {Percobaan}");

        }
    }
}
```

### `L017-Do While.cs`

```cs
using System;

namespace Code_Practice{
    class L0{
        static void Main(string[] args){

           Console.Write("Apakah Anda member? (true/false): ");
            string input = Console.ReadLine();

            // Mencoba mengubah string menjadi bool
            if (bool.TryParse(input, out bool statusMember))ss
            {
                Console.WriteLine($"Berhasil! Status member Anda adalah: {statusMember}");
            }
            else
            {
                Console.WriteLine("Input tidak valid! Harap ketik 'true' atau 'false'.");
                
            }
        }
    }
}
```

### `Template C sharp.cs`

```cs
using System;

namespace Code_Practice{
    class L0{
        static void Main(string[] args){

            //Tulis Kode anda disini

        }
    }
}
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

### `Big Project/Radix Converter/Program.cs`

```cs
﻿using System;
using System.Linq;

namespace Radix_Converter {
    class Program_utama {
        static void Main(string[] args) {
            C_Tampilkan_Menu.Tampilkan();
            string Pilihan_Input = C_Input_Pilihan_Menu_Utama.Input_Awal();
            string Pilihan_Convert = C_Input_Pilihan_Menu_Utama.Input_Convert();
        }

        class C_Tampilkan_Menu {
            public static void Tampilkan() {
                Console.WriteLine("===== RADIX CONVERTER =====");
                Console.WriteLine("[A] Biner (2)");
                Console.WriteLine("[B] Oktal (8)");
                Console.WriteLine("[C] Desimal (10)");
                Console.WriteLine("[D] Hexadesimal (16)");
            }
        }

        class C_Input_Pilihan_Menu_Utama {
            public static string Input_Awal() {

            string[] Pilihan = { "A", "B", "C", "D" };

            Console.Write("=> Pilih jenis angka yang akan anda input : ");
            string Input = Console.ReadLine();
            Input = Input.ToUpper();

            while (!Pilihan.Contains(Input))
            {
                Console.Clear();
                C_Tampilkan_Menu.Tampilkan();
                Console.WriteLine("Pilihan salah! Harap masukkan A, B, C, atau D.");
                Console.Write("=> Pilih jenis angka yang akan anda input : ");
                Input = Console.ReadLine();
                Input = Input.ToUpper();
            }

            return Input;

            }

            public static string Input_Convert() {

                string[] Pilihan = { "A", "B", "C", "D" };

                Console.Write("=> Pilih jenis angka yang akan anda ubah menjadi : ");
                string Input = Console.ReadLine();
                Input = Input.ToUpper();

                while (!Pilihan.Contains(Input))
                {
                    Console.Clear();
                    C_Tampilkan_Menu.Tampilkan();
                    Console.WriteLine("Pilihan salah! Harap masukkan A, B, C, atau D.");
                    Console.Write("=> Pilih jenis angka yang akan anda ubah menjadi : ");
                    Input = Console.ReadLine();
                    Input = Input.ToUpper();
                }

                return Input;
            }

        }

        class C_Input_Angka {
            public static string() {

            }
        }

    }
}
```

### `Big Project/Radix Converter/Radix Converter.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Radix_Converter</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Big Project/Radix Converter/bin/Debug/net8.0/Radix Converter.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Radix Converter/1.0.0": {
        "runtime": {
          "Radix Converter.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Radix Converter/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Big Project/Radix Converter/bin/Debug/net8.0/Radix Converter.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj",
        "projectName": "Radix Converter",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Big Project/Radix Converter/obj/Radix Converter.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Big Project/Radix Converter/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj",
      "projectName": "Radix Converter",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Big Project/Radix Converter/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "QZjZpm8H3lc=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Big Project\\Radix Converter\\Radix Converter.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Radix Converter")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+401bc41e51e559f36d3b401ed39dde292efb2417")]
[assembly: System.Reflection.AssemblyProductAttribute("Radix Converter")]
[assembly: System.Reflection.AssemblyTitleAttribute("Radix Converter")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.AssemblyInfoInputs.cache`

```cache
d5ea9cb7d5c0dfcba0a2000af424222205d7e8efd2854e0a271752cf8994f823
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Radix_Converter
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.csproj.CoreCompileInputs.cache`

```cache
f6f2a640796ffdfe11b5b3a6bc195e31dd2380758489c26af1d7cb6716335b7f
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\bin\Debug\net8.0\Radix Converter.exe
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\bin\Debug\net8.0\Radix Converter.deps.json
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\bin\Debug\net8.0\Radix Converter.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\bin\Debug\net8.0\Radix Converter.dll
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\bin\Debug\net8.0\Radix Converter.pdb
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.sourcelink.json
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.dll
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\refint\Radix Converter.dll
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.pdb
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\Radix Converter.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Big Project\Radix Converter\obj\Debug\net8.0\ref\Radix Converter.dll
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.genruntimeconfig.cache`

```cache
adc85eeb144045e6dc6daaaa21499ce578cc5b8cf16b534ecffe344fadd19082
```

### `Big Project/Radix Converter/obj/Debug/net8.0/Radix Converter.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/401bc41e51e559f36d3b401ed39dde292efb2417/*"}}
```

### `Praktik/Praktik 1/Praktik 1.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_1</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 1/Program.cs`

```cs
﻿using System;

class Program{
    static void Main(string[] args){

        Console.WriteLine("TEKNOLOGI REKAYASA MULTIMEDIA GRAFIS");
        Console.WriteLine("        BIODATA MAHASISWA BARU");
        Console.WriteLine("======================================");
        Console.WriteLine("NIM      : 2605191024");
        Console.WriteLine("NAMA     : NAUFAL KHALIL RAKHASYAH");
        Console.WriteLine("KELAS    : TRMG 1D");
        Console.WriteLine("ALAMAT   : Jln. Bunga Teratai, No.35");
        Console.WriteLine("           Padang Bulan Selayang II,");
        Console.WriteLine("           Medan Selayang, Kota Medan");
        Console.WriteLine("NO. HP   : 0882015954636");
        Console.WriteLine("======================================");

    }
}
```

### `Praktik/Praktik 1/bin/Debug/net8.0/Praktik 1.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 1/1.0.0": {
        "runtime": {
          "Praktik 1.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 1/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 1/bin/Debug/net8.0/Praktik 1.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj",
        "projectName": "Praktik 1",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 1/obj/Praktik 1.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 1/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj",
      "projectName": "Praktik 1",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 1/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "bKp/nvbTEiM=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 1\\Praktik 1.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 1")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+a0f5122b435b21fdd8d2b895fd3aa05453ebed5a")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 1")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 1")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.AssemblyInfoInputs.cache`

```cache
cdde14efad1138a4f069397feb5eb44e2116bdfe9ca109ff1da63713c87b5f6f
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_1
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik 1\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.csproj.CoreCompileInputs.cache`

```cache
7b1c0cfd561b8ef18318682d4decfc529e9ba32967d2feb6a15fabf0f42bcbc4
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik 1\bin\Debug\net8.0\Praktik 1.exe
D:\Project\Coding\Code Practice\C#\Praktik 1\bin\Debug\net8.0\Praktik 1.deps.json
D:\Project\Coding\Code Practice\C#\Praktik 1\bin\Debug\net8.0\Praktik 1.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik 1\bin\Debug\net8.0\Praktik 1.dll
D:\Project\Coding\Code Practice\C#\Praktik 1\bin\Debug\net8.0\Praktik 1.pdb
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.dll
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\refint\Praktik 1.dll
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.pdb
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\Praktik 1.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik 1\obj\Debug\net8.0\ref\Praktik 1.dll
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.genruntimeconfig.cache`

```cache
10122be20e30bc9854fff259674a7bee2f0a098fe11362ff0895cc3635c1930c
```

### `Praktik/Praktik 1/obj/Debug/net8.0/Praktik 1.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/a0f5122b435b21fdd8d2b895fd3aa05453ebed5a/*"}}
```

### `Praktik/Praktik 10/Praktik 10.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_10</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 10/Program.cs`

```cs
﻿using System;

class Praktik_10 {
    static void Main(string[] args) {

        string NIM = "";
        string Nama = "";
        string Validasi = "";

        while (Validasi != "T") {
            Console.Write("Masukkan NIM :");
            NIM = Console.ReadLine();

            Console.Write("Masukkan Nama :");
            Nama = Console.ReadLine();

            Console.Write("Input data lagi? [Y/T] : ");
            Validasi = Console.ReadLine(); 
        }

        Console.WriteLine("Selesai");
    }
}
```

### `Praktik/Praktik 10/bin/Debug/net8.0/Praktik 10.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 10/1.0.0": {
        "runtime": {
          "Praktik 10.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 10/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 10/bin/Debug/net8.0/Praktik 10.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj",
        "projectName": "Praktik 10",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 10/obj/Praktik 10.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 10/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj",
      "projectName": "Praktik 10",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 10/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "MgkilmKoc3w=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 10\\Praktik 10.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 10")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+70e424d9c91e216695d258eee88258f4a3f2e998")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 10")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 10")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.AssemblyInfoInputs.cache`

```cache
bcca92b757d7219fe64f2f29660f06c07e8738da8cbf5ddca61be951a21dea86
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_10
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.csproj.CoreCompileInputs.cache`

```cache
dd1c4543b70dc95c5c6b99f313fd5e83918c349ec4c8bb1d9aebf0b24c2bb319
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\bin\Debug\net8.0\Praktik 10.exe
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\bin\Debug\net8.0\Praktik 10.deps.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\bin\Debug\net8.0\Praktik 10.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\bin\Debug\net8.0\Praktik 10.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\bin\Debug\net8.0\Praktik 10.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\refint\Praktik 10.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\Praktik 10.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 10\obj\Debug\net8.0\ref\Praktik 10.dll
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.genruntimeconfig.cache`

```cache
054cfcaaa3090277d8cbf6bf4a6bedcf1add40824eedeb6262c3dbb66c247d65
```

### `Praktik/Praktik 10/obj/Debug/net8.0/Praktik 10.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/70e424d9c91e216695d258eee88258f4a3f2e998/*"}}
```

### `Praktik/Praktik 2/Praktik 2.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_2</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 2/Program.cs`

```cs
﻿using System;

class Program{
    static void Main(string[] args){
        
        Console.WriteLine("TEKNOLOGI REKAYASA MULTIMEDIA GRAFIS");
        Console.WriteLine("        BIODATA MAHASISWA BARU");
        Console.WriteLine("======================================");

        Console.Write("NIM : ");
        string Nim = Console.ReadLine();

        Console.Write("Nama : ");
        string Nama = Console.ReadLine();
        
        Console.Write("Kelas : ");
        string Kelas = Console.ReadLine();
        
        Console.Write("Alamat : ");
        string Alamat = Console.ReadLine();
        
        Console.Write("No HP : ");
        string Nomor_HP = Console.ReadLine();
        
        Console.Write("Umur : ");
        int Umur = int.Parse(Console.ReadLine());
 
    }
}
```

### `Praktik/Praktik 2/bin/Debug/net8.0/Praktik 2.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 2/1.0.0": {
        "runtime": {
          "Praktik 2.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 2/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 2/bin/Debug/net8.0/Praktik 2.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj",
        "projectName": "Praktik 2",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 2/obj/Praktik 2.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 2/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj",
      "projectName": "Praktik 2",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 2/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "EpfKWlqaZOI=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 2\\Praktik 2.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 2")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+8684d62c4fcf08716d916acdc8ae2665ae1dd1dc")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 2")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 2")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.AssemblyInfoInputs.cache`

```cache
b925ed2b40e7de1782f7be6077edf761fdd8204f9e5ded6b60e18d25403279d8
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_2
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik 2\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.csproj.CoreCompileInputs.cache`

```cache
cb004be6543b271a76e29d45fc010ee7df0b284763c45626ec9d6036bfdbb9f2
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik 2\bin\Debug\net8.0\Praktik 2.exe
D:\Project\Coding\Code Practice\C#\Praktik 2\bin\Debug\net8.0\Praktik 2.deps.json
D:\Project\Coding\Code Practice\C#\Praktik 2\bin\Debug\net8.0\Praktik 2.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik 2\bin\Debug\net8.0\Praktik 2.dll
D:\Project\Coding\Code Practice\C#\Praktik 2\bin\Debug\net8.0\Praktik 2.pdb
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.dll
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\refint\Praktik 2.dll
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.pdb
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\Praktik 2.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik 2\obj\Debug\net8.0\ref\Praktik 2.dll
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.genruntimeconfig.cache`

```cache
250b0204e07e183e4f5d0fe1f17fe85cfbc69097b4fede32f8f000a84e2a4bf4
```

### `Praktik/Praktik 2/obj/Debug/net8.0/Praktik 2.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/8684d62c4fcf08716d916acdc8ae2665ae1dd1dc/*"}}
```

### `Praktik/Praktik 3/Praktik 3.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_3</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 3/Program.cs`

```cs
﻿using System;

class Program{
    static void Main(string[] args){
        
        int Panjang, Lebar, Hasil_Luas, Hasil_Keliling;
        Console.Write("Nilai Panjang : "); 
        Panjang = int.Parse(Console.ReadLine());
        Console.Write("Nilai Lebar : ");
        Lebar = int.Parse(Console.ReadLine());
        Hasil_Luas = 2 * (Panjang + Lebar);
        Hasil_Keliling = (Panjang * Lebar);
        Console.Writeln($"Luas Persegi Panjang     : {Hasil_Luas}");
        Console.Writeln($"Keliling Persegi Panjang : {Hasil_Keliling}");
    }
}
```

### `Praktik/Praktik 3/bin/Debug/net8.0/Praktik 3.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 3/1.0.0": {
        "runtime": {
          "Praktik 3.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 3/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 3/bin/Debug/net8.0/Praktik 3.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj",
        "projectName": "Praktik 3",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 3/obj/Praktik 3.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 3/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj",
      "projectName": "Praktik 3",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 3/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "SOgQ+Kspw9o=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 3\\Praktik 3.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 3")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+8684d62c4fcf08716d916acdc8ae2665ae1dd1dc")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 3")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 3")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.AssemblyInfoInputs.cache`

```cache
2bdca87af30897518293af32516c667569c226bb1ce829a4616d7e9e84e9e71c
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_3
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik 3\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.csproj.CoreCompileInputs.cache`

```cache
190896e0e93efe9606716c10cb98d8d808eee20950d1a5f6b2f601a83713d6b9
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik 3\bin\Debug\net8.0\Praktik 3.exe
D:\Project\Coding\Code Practice\C#\Praktik 3\bin\Debug\net8.0\Praktik 3.deps.json
D:\Project\Coding\Code Practice\C#\Praktik 3\bin\Debug\net8.0\Praktik 3.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik 3\bin\Debug\net8.0\Praktik 3.dll
D:\Project\Coding\Code Practice\C#\Praktik 3\bin\Debug\net8.0\Praktik 3.pdb
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.dll
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\refint\Praktik 3.dll
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.pdb
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\Praktik 3.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik 3\obj\Debug\net8.0\ref\Praktik 3.dll
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.genruntimeconfig.cache`

```cache
48b63d8a871a67afd3ac11a6bd857e61673807c9fa8223d02ab2e07a459fc659
```

### `Praktik/Praktik 3/obj/Debug/net8.0/Praktik 3.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/8684d62c4fcf08716d916acdc8ae2665ae1dd1dc/*"}}
```

### `Praktik/Praktik 4/Praktik 4.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_4</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 4/Program.cs`

```cs
﻿using System;

class Latihan_4{
    static void Main(string[] args){

        Console.Write("Masukkan Password : ");
        int Password = int.Parse(Console.ReadLine());

        if(Password == 1234){
            Console.WriteLine("Password Anda Benar!");
        } 
        else{
            Console.WriteLine("Password Anda Salah!");
        }

    }
}
```

### `Praktik/Praktik 4/bin/Debug/net8.0/Praktik 4.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 4/1.0.0": {
        "runtime": {
          "Praktik 4.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 4/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 4/bin/Debug/net8.0/Praktik 4.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj",
        "projectName": "Praktik 4",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 4/obj/Praktik 4.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 4/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj",
      "projectName": "Praktik 4",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 4/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "ShpKTfs5C1g=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 4\\Praktik 4.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 4")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+0e0a6500c9febc9b293c299688feb9358605b076")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 4")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 4")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.AssemblyInfoInputs.cache`

```cache
22a79c12bfba84cc4eaaa699e0250397d63c805e2521e0843bf1c3ffdac077e9
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_4
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik 4\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.csproj.CoreCompileInputs.cache`

```cache
f1d46b7552d3b776c195167770cfe05838adb1ca2f442519ad27457cc99cd13a
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik 4\bin\Debug\net8.0\Praktik 4.exe
D:\Project\Coding\Code Practice\C#\Praktik 4\bin\Debug\net8.0\Praktik 4.deps.json
D:\Project\Coding\Code Practice\C#\Praktik 4\bin\Debug\net8.0\Praktik 4.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik 4\bin\Debug\net8.0\Praktik 4.dll
D:\Project\Coding\Code Practice\C#\Praktik 4\bin\Debug\net8.0\Praktik 4.pdb
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.dll
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\refint\Praktik 4.dll
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.pdb
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\Praktik 4.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik 4\obj\Debug\net8.0\ref\Praktik 4.dll
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.genruntimeconfig.cache`

```cache
b462984c95b06980fb1ea296db2fbba22a025560b50af6aa2644207297fc266c
```

### `Praktik/Praktik 4/obj/Debug/net8.0/Praktik 4.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/0e0a6500c9febc9b293c299688feb9358605b076/*"}}
```

### `Praktik/Praktik 5/Praktik 5.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_5</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 5/Program.cs`

```cs
﻿using System;

class Praktik_5{
    static void Main(string[] args){
        
        Console.Write("Masukkan Nilai anda :");
        int Nilai = int.Parse(Console.ReadLine());
        string Predikat;

        if (Nilai >= 90){
            Predikat = "A";
        } 
        else if(Nilai >= 85){
            Predikat = "A-";
        }
        else if(Nilai >= 80){
            Predikat = "B+";
        }
        else if(Nilai >= 75){
            Predikat = "B";
        }
        else {
            Predikat = "B-";
        }

    }
}
```

### `Praktik/Praktik 5/bin/Debug/net8.0/Praktik 5.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 5/1.0.0": {
        "runtime": {
          "Praktik 5.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 5/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 5/bin/Debug/net8.0/Praktik 5.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj",
        "projectName": "Praktik 5",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 5/obj/Praktik 5.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 5/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj",
      "projectName": "Praktik 5",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 5/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "ZDQM781i4pI=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik 5\\Praktik 5.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 5")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+0e0a6500c9febc9b293c299688feb9358605b076")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 5")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 5")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.AssemblyInfoInputs.cache`

```cache
1fbba3a0af971fda3e2a2c5b4642ab9c933c170ac6eda7ff985be61f4294241c
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_5
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik 5\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.csproj.CoreCompileInputs.cache`

```cache
f8be637e9423797a75fe0272ba198f97952e563f4ab9eb212a6c667efdaf1e60
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik 5\bin\Debug\net8.0\Praktik 5.exe
D:\Project\Coding\Code Practice\C#\Praktik 5\bin\Debug\net8.0\Praktik 5.deps.json
D:\Project\Coding\Code Practice\C#\Praktik 5\bin\Debug\net8.0\Praktik 5.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik 5\bin\Debug\net8.0\Praktik 5.dll
D:\Project\Coding\Code Practice\C#\Praktik 5\bin\Debug\net8.0\Praktik 5.pdb
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.dll
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\refint\Praktik 5.dll
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.pdb
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\Praktik 5.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik 5\obj\Debug\net8.0\ref\Praktik 5.dll
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.genruntimeconfig.cache`

```cache
8aa772c6ff6f6cd03fa30efed60c97e2b022e9b6e32dfecdbecdce1ca6e7b056
```

### `Praktik/Praktik 5/obj/Debug/net8.0/Praktik 5.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/0e0a6500c9febc9b293c299688feb9358605b076/*"}}
```

### `Praktik/Praktik 6/Praktik 6.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_6</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 6/Program.cs`

```cs
﻿using System;
class Praktik_6{
    static void Main(string[] args){
        
        int Bulan;
        string Nama_Bulan = "";
        Console.Write("Masukkan Bulan (dalam angka): ");
        Bulan = int.Parse(Console.ReadLine());

        switch (Bulan){
            case 1: Nama_Bulan = "Januari";
                    break;
            case 2: Nama_Bulan = "Februari";
                    break;
            case 3: Nama_Bulan = "Maret";
                    break;
            case 4: Nama_Bulan = "April";
                    break;
            case 5: Nama_Bulan = "Mei";
                    break;
            case 6: Nama_Bulan = "Juni";
                    break;
            case 7: Nama_Bulan = "Juli";
                    break;
            case 8: Nama_Bulan = "Agustus";
                    break;
            case 9: Nama_Bulan = "September";
                    break;
            case 10: Nama_Bulan = "Oktober";
                    break;
            case 11: Nama_Bulan = "November";
                    break;
            case 12: Nama_Bulan = "Desember";
                    break;
                        
        }

        Console.WriteLine($"Nama Bulan : {Nama_Bulan}");

    }    
}
```

### `Praktik/Praktik 6/bin/Debug/net8.0/Praktik 6.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 6/1.0.0": {
        "runtime": {
          "Praktik 6.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 6/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 6/bin/Debug/net8.0/Praktik 6.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj",
        "projectName": "Praktik 6",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 6/obj/Praktik 6.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 6/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj",
      "projectName": "Praktik 6",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 6/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "UrRWQEBzySM=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 6\\Praktik 6.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 6")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+a96a26a9244c64184a48d01594be9b88fe69a504")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 6")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 6")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.AssemblyInfoInputs.cache`

```cache
c0c3bda7983f688d4c0efe72f2469b70e6fa03783eb35ae84198f0a68bcb6af1
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_6
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.csproj.CoreCompileInputs.cache`

```cache
716e3f2e1082efa439bf0e37225b6c54d45a619a434a5d2fd8f2c4dfa91c0e4e
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\bin\Debug\net8.0\Praktik 6.exe
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\bin\Debug\net8.0\Praktik 6.deps.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\bin\Debug\net8.0\Praktik 6.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\bin\Debug\net8.0\Praktik 6.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\bin\Debug\net8.0\Praktik 6.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\refint\Praktik 6.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\Praktik 6.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 6\obj\Debug\net8.0\ref\Praktik 6.dll
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.genruntimeconfig.cache`

```cache
fb23c740d2bc0746272f9d0afa89d4f47fdd6b4027592466d11aca628599b379
```

### `Praktik/Praktik 6/obj/Debug/net8.0/Praktik 6.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/a96a26a9244c64184a48d01594be9b88fe69a504/*"}}
```

### `Praktik/Praktik 7/Praktik 7.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_7</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 7/Program.cs`

```cs
﻿using System;

class Praktik {
        static void Main(string[] args){
        
                int Nilai = int.Parse(Console.ReadLine());

                switch (Nilai){
                        case 85 > 100: Console.WriteLine("b"); break;
                        default : Console.WriteLine("D");break;
                }

        }    
}
```

### `Praktik/Praktik 7/bin/Debug/net8.0/Praktik 7.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 7/1.0.0": {
        "runtime": {
          "Praktik 7.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 7/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 7/bin/Debug/net8.0/Praktik 7.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj",
        "projectName": "Praktik 7",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 7/obj/Praktik 7.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 7/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj",
      "projectName": "Praktik 7",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 7/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "RCEWbxwKpTw=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 7\\Praktik 7.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 7")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+70e424d9c91e216695d258eee88258f4a3f2e998")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 7")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 7")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.AssemblyInfoInputs.cache`

```cache
32e1fc2d9aef45bf7b63b5ee3f8d392bdb0918ecb723a83bac2b36e2ae5fd3c3
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_7
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.csproj.CoreCompileInputs.cache`

```cache
7b3e21e573dececbc32205301913b1fe97604c66c824c457356361e87f9a264a
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\bin\Debug\net8.0\Praktik 7.exe
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\bin\Debug\net8.0\Praktik 7.deps.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\bin\Debug\net8.0\Praktik 7.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\bin\Debug\net8.0\Praktik 7.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\bin\Debug\net8.0\Praktik 7.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\refint\Praktik 7.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\Praktik 7.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 7\obj\Debug\net8.0\ref\Praktik 7.dll
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.genruntimeconfig.cache`

```cache
d3bd96e9ee7226306edfba6e67ccb6f0cc5a8f86909e58f8c535bf1608e3c7c5
```

### `Praktik/Praktik 7/obj/Debug/net8.0/Praktik 7.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/70e424d9c91e216695d258eee88258f4a3f2e998/*"}}
```

### `Praktik/Praktik 8/Praktik 8.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_8</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 8/Program.cs`

```cs
﻿using System;

class Praktik_8 { 
    static void Main(string[] args) { 
        
        Console.Write("Masukkan 2 Digit NIM terakhir anda : "); 
        int NIM = int.Parse(Console.ReadLine()); 
        string hasil = ""; 

        for (int i = 0; i <= NIM; i++){
            if(i % 2 == 0){
                hasil = "Genap"; 
            } else { 
                hasil = "Ganjil"; 
            } 
        }

        Console.Write($"NIM {NIM} adalah {hasil}"); 
    } 
}
```

### `Praktik/Praktik 8/bin/Debug/net8.0/Praktik 8.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 8/1.0.0": {
        "runtime": {
          "Praktik 8.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 8/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 8/bin/Debug/net8.0/Praktik 8.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj",
        "projectName": "Praktik 8",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 8/obj/Praktik 8.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 8/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj",
      "projectName": "Praktik 8",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 8/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "/te4A3T83gY=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 8\\Praktik 8.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 8")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+70e424d9c91e216695d258eee88258f4a3f2e998")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 8")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 8")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.AssemblyInfoInputs.cache`

```cache
3bdeb24f6cd05d2079952a38ae6ae7a76e9d66228ceda70669967c604380d216
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_8
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.csproj.CoreCompileInputs.cache`

```cache
b89385ab069a69163cdcae08161f350cdae2bcaa592f096a89fa0711acf44cca
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\bin\Debug\net8.0\Praktik 8.exe
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\bin\Debug\net8.0\Praktik 8.deps.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\bin\Debug\net8.0\Praktik 8.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\bin\Debug\net8.0\Praktik 8.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\bin\Debug\net8.0\Praktik 8.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\refint\Praktik 8.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\Praktik 8.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 8\obj\Debug\net8.0\ref\Praktik 8.dll
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.genruntimeconfig.cache`

```cache
fe6429ac36b8a019de3aa2e3b18a56e7454cb5d28f2009bf07baf2b434c5a96b
```

### `Praktik/Praktik 8/obj/Debug/net8.0/Praktik 8.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/70e424d9c91e216695d258eee88258f4a3f2e998/*"}}
```

### `Praktik/Praktik 9/Praktik 9.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Praktik_9</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Praktik/Praktik 9/Program.cs`

```cs
﻿using System;

class Praktik_9{
    static void Main(string[] args){

        string passwordKunci = "csharp123";
        string inputUser = "";
        Console.WriteLine("=== Sistem Login Sederhana ===");
        
        while (inputUser != passwordKunci){

            Console.Write("Masukkan Password: ");
            inputUser = Console.ReadLine();
      
            if (inputUser != passwordKunci){
                Console.WriteLine("Password salah! Silakan coba lagi.\n");
            }
        }
      
        Console.WriteLine("✅ Akses Diterima! Selamat datang.");
    
    }     
}
```

### `Praktik/Praktik 9/bin/Debug/net8.0/Praktik 9.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Praktik 9/1.0.0": {
        "runtime": {
          "Praktik 9.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Praktik 9/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Praktik/Praktik 9/bin/Debug/net8.0/Praktik 9.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj",
        "projectName": "Praktik 9",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Praktik/Praktik 9/obj/Praktik 9.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Praktik/Praktik 9/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj",
      "projectName": "Praktik 9",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Praktik/Praktik 9/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "VK6Vta7rQIc=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Praktik\\Praktik 9\\Praktik 9.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Praktik 9")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+70e424d9c91e216695d258eee88258f4a3f2e998")]
[assembly: System.Reflection.AssemblyProductAttribute("Praktik 9")]
[assembly: System.Reflection.AssemblyTitleAttribute("Praktik 9")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.AssemblyInfoInputs.cache`

```cache
574385b216543ccc7b58499a619d41f589a311f273e3dee70e878f7d07424d5c
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Praktik_9
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.csproj.CoreCompileInputs.cache`

```cache
094777c0bc588f7687f64f3bba2599b4a34410323ca7e1fcba6f0f0067dab573
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\bin\Debug\net8.0\Praktik 9.exe
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\bin\Debug\net8.0\Praktik 9.deps.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\bin\Debug\net8.0\Praktik 9.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\bin\Debug\net8.0\Praktik 9.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\bin\Debug\net8.0\Praktik 9.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.sourcelink.json
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\refint\Praktik 9.dll
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.pdb
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\Praktik 9.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Praktik\Praktik 9\obj\Debug\net8.0\ref\Praktik 9.dll
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.genruntimeconfig.cache`

```cache
0a7991ed43ba78d385a3b1174fbeec83497610562827556f71dcf157eb80e512
```

### `Praktik/Praktik 9/obj/Debug/net8.0/Praktik 9.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/70e424d9c91e216695d258eee88258f4a3f2e998/*"}}
```

### `Tugas/Tugas 4/Program.cs`

```cs
﻿using System;

class Tugas_4 {
    static void Main(string[] args) {

        string Jenis_kendaraan = "";
        string Opsi_kendaraan = "";
        int Bulan_keterlambatan = 0;
        double Pokok_swdkllj = 0;
        double Pokok_pkb = 0;
        double Denda_pkb = 0;
        double Denda_swdkllj = 0;
        double Total_pembayaran = 0;
        string Garis = "-------------------------------------";

        Console.WriteLine("====== PROGRAM PAJAK KENDARAAN ======");
        Console.WriteLine("[1] Kendaraan Roda 2");
        Console.WriteLine("[2] Kendaraan Roda 4");
        Console.WriteLine(Garis);
        Console.Write("=> Pilih jenis kendaraan anda : ");
        Opsi_kendaraan = Console.ReadLine();

        if (Opsi_kendaraan == "1"){
            Jenis_kendaraan = "Roda 2";
            Pokok_swdkllj = 35000;
        }
        else if (Opsi_kendaraan == "2"){
            Jenis_kendaraan = "Roda 4";
            Pokok_swdkllj = 143000;
        }

        if (Opsi_kendaraan == "1" || Opsi_kendaraan == "2"){
            Console.Write("=> Masukkan Pokok PKB (Rp) : ");
            Pokok_pkb = double.Parse(Console.ReadLine());

            Console.Write("=> Masukkan Jumlah Bulan Keterlambatan (0-24) : ");
            Bulan_keterlambatan = int.Parse(Console.ReadLine());

            if (Bulan_keterlambatan < 0 || Bulan_keterlambatan > 24){
                Console.WriteLine(Garis);
                Console.WriteLine("[Error] Bulan keterlambatan harus di antara 0 hingga 24 bulan!");
            }
            else{
                if (Bulan_keterlambatan == 0){
                    Denda_pkb = 0;
                    Denda_swdkllj = 0;
                }
                else if (Bulan_keterlambatan >= 1 && Bulan_keterlambatan <= 3){
                    Denda_pkb = 0.10 * Pokok_pkb;
                    if (Opsi_kendaraan == "1"){
                        Denda_swdkllj = 25000;
                    }
                    else{
                        Denda_swdkllj = 50000;
                    }
                }
                else if (Bulan_keterlambatan > 3){
                    Denda_pkb = (0.25 * Pokok_pkb) + (0.01 * Bulan_keterlambatan * Pokok_pkb);
                    if (Opsi_kendaraan == "1"){
                        Denda_swdkllj = 50000;
                    }
                    else{
                        Denda_swdkllj = 100000;
                    }
                }

                Total_pembayaran = Pokok_pkb + Pokok_swdkllj + Denda_pkb + Denda_swdkllj;

                Console.WriteLine(Garis);
                Console.WriteLine("          STRUK HASIL HITUNG PAJAK   ");
                Console.WriteLine(Garis);
                Console.WriteLine("Jenis Kendaraan  : " + Jenis_kendaraan);
                Console.WriteLine("Keterlambatan    : " + Bulan_keterlambatan + " Bulan");
                Console.WriteLine("Pokok PKB        : Rp" + Pokok_pkb); 
                Console.WriteLine("Pokok SWDKLLJ    : Rp" + Pokok_swdkllj);
                Console.WriteLine("Denda PKB        : Rp" + Denda_pkb);
                Console.WriteLine("Denda SWDKLLJ    : Rp" + Denda_swdkllj);
                Console.WriteLine(Garis);
                Console.WriteLine("TOTAL PEMBAYARAN : Rp" + Total_pembayaran);
                Console.WriteLine(Garis);
                Console.WriteLine("Nama Operator    : Naufal Khalil Rakhasyah");
                Console.WriteLine(Garis);
            }
        }
        else {
            Console.WriteLine("[Error] Anda harus memasukkan input yang valid!");
        }
    }
}
```

### `Tugas/Tugas 4/Tugas 4.csproj`

```csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Tugas_4</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### `Tugas/Tugas 4/bin/Debug/net8.0/Tugas 4.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "Tugas 4/1.0.0": {
        "runtime": {
          "Tugas 4.dll": {}
        }
      }
    }
  },
  "libraries": {
    "Tugas 4/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `Tugas/Tugas 4/bin/Debug/net8.0/Tugas 4.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj",
        "projectName": "Tugas 4",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `Tugas/Tugas 4/obj/Tugas 4.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `Tugas/Tugas 4/obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj",
      "projectName": "Tugas 4",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `Tugas/Tugas 4/obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "dDLkS61GBmg=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\Tugas\\Tugas 4\\Tugas 4.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("Tugas 4")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+a96a26a9244c64184a48d01594be9b88fe69a504")]
[assembly: System.Reflection.AssemblyProductAttribute("Tugas 4")]
[assembly: System.Reflection.AssemblyTitleAttribute("Tugas 4")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.AssemblyInfoInputs.cache`

```cache
2133e66885406c1081a07c54c137b032b70370bd2ce640b5f94e9c6028e65406
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Tugas_4
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.csproj.CoreCompileInputs.cache`

```cache
02d8de5961b6041fed0afde1c79a6faf8023a129836b1167e7c8401a8043e1dc
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.sourcelink.json
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\bin\Debug\net8.0\Tugas 4.exe
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\bin\Debug\net8.0\Tugas 4.deps.json
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\bin\Debug\net8.0\Tugas 4.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\bin\Debug\net8.0\Tugas 4.dll
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\bin\Debug\net8.0\Tugas 4.pdb
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.dll
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\refint\Tugas 4.dll
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.pdb
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\Tugas 4.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\Tugas\Tugas 4\obj\Debug\net8.0\ref\Tugas 4.dll
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.genruntimeconfig.cache`

```cache
4fa706b204133068c1319e985561f2191663bc4eaa4556374d49df8c6b7327d1
```

### `Tugas/Tugas 4/obj/Debug/net8.0/Tugas 4.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/a96a26a9244c64184a48d01594be9b88fe69a504/*"}}
```

### `bin/Debug/net8.0/C#.deps.json`

```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "C#/1.0.0": {
        "runtime": {
          "C#.dll": {}
        }
      }
    }
  },
  "libraries": {
    "C#/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

### `bin/Debug/net8.0/C#.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "8.0.0"
    },
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": false
    }
  }
}
```

### `obj/C#.csproj.nuget.dgspec.json`

```json
{
  "format": 1,
  "restore": {
    "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj": {}
  },
  "projects": {
    "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj": {
      "version": "1.0.0",
      "restore": {
        "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj",
        "projectName": "C#",
        "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj",
        "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
        "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\obj\\",
        "projectStyle": "PackageReference",
        "configFilePaths": [
          "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
        ],
        "originalTargetFrameworks": [
          "net8.0"
        ],
        "sources": {
          "https://api.nuget.org/v3/index.json": {}
        },
        "frameworks": {
          "net8.0": {
            "targetAlias": "net8.0",
            "projectReferences": {}
          }
        },
        "warningProperties": {
          "warnAsError": [
            "NU1605"
          ]
        },
        "restoreAuditProperties": {
          "enableAudit": "true",
          "auditLevel": "low",
          "auditMode": "direct"
        }
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "imports": [
            "net461",
            "net462",
            "net47",
            "net471",
            "net472",
            "net48",
            "net481"
          ],
          "assetTargetFallback": true,
          "warn": true,
          "frameworkReferences": {
            "Microsoft.NETCore.App": {
              "privateAssets": "all"
            }
          },
          "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
        }
      }
    }
  }
}
```

### `obj/C#.csproj.nuget.g.props`

```props
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <RestoreSuccess Condition=" '$(RestoreSuccess)' == '' ">True</RestoreSuccess>
    <RestoreTool Condition=" '$(RestoreTool)' == '' ">NuGet</RestoreTool>
    <ProjectAssetsFile Condition=" '$(ProjectAssetsFile)' == '' ">$(MSBuildThisFileDirectory)project.assets.json</ProjectAssetsFile>
    <NuGetPackageRoot Condition=" '$(NuGetPackageRoot)' == '' ">$(UserProfile)\.nuget\packages\</NuGetPackageRoot>
    <NuGetPackageFolders Condition=" '$(NuGetPackageFolders)' == '' ">C:\Users\Naufal Khalil\.nuget\packages\</NuGetPackageFolders>
    <NuGetProjectStyle Condition=" '$(NuGetProjectStyle)' == '' ">PackageReference</NuGetProjectStyle>
    <NuGetToolVersion Condition=" '$(NuGetToolVersion)' == '' ">6.11.2</NuGetToolVersion>
  </PropertyGroup>
  <ItemGroup Condition=" '$(ExcludeRestorePackageImports)' != 'true' ">
    <SourceRoot Include="C:\Users\Naufal Khalil\.nuget\packages\" />
  </ItemGroup>
</Project>
```

### `obj/C#.csproj.nuget.g.targets`

```targets
﻿<?xml version="1.0" encoding="utf-8" standalone="no"?>
<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" />
```

### `obj/project.assets.json`

```json
{
  "version": 3,
  "targets": {
    "net8.0": {}
  },
  "libraries": {},
  "projectFileDependencyGroups": {
    "net8.0": []
  },
  "packageFolders": {
    "C:\\Users\\Naufal Khalil\\.nuget\\packages\\": {}
  },
  "project": {
    "version": "1.0.0",
    "restore": {
      "projectUniqueName": "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj",
      "projectName": "C#",
      "projectPath": "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj",
      "packagesPath": "C:\\Users\\Naufal Khalil\\.nuget\\packages\\",
      "outputPath": "D:\\Project\\Coding\\Code Practice\\C#\\obj\\",
      "projectStyle": "PackageReference",
      "configFilePaths": [
        "C:\\Users\\Naufal Khalil\\AppData\\Roaming\\NuGet\\NuGet.Config"
      ],
      "originalTargetFrameworks": [
        "net8.0"
      ],
      "sources": {
        "https://api.nuget.org/v3/index.json": {}
      },
      "frameworks": {
        "net8.0": {
          "targetAlias": "net8.0",
          "projectReferences": {}
        }
      },
      "warningProperties": {
        "warnAsError": [
          "NU1605"
        ]
      },
      "restoreAuditProperties": {
        "enableAudit": "true",
        "auditLevel": "low",
        "auditMode": "direct"
      }
    },
    "frameworks": {
      "net8.0": {
        "targetAlias": "net8.0",
        "imports": [
          "net461",
          "net462",
          "net47",
          "net471",
          "net472",
          "net48",
          "net481"
        ],
        "assetTargetFallback": true,
        "warn": true,
        "frameworkReferences": {
          "Microsoft.NETCore.App": {
            "privateAssets": "all"
          }
        },
        "runtimeIdentifierGraphPath": "C:\\Program Files\\dotnet\\sdk\\8.0.425/PortableRuntimeIdentifierGraph.json"
      }
    }
  }
}
```

### `obj/project.nuget.cache`

```cache
{
  "version": 2,
  "dgSpecHash": "AJU3+02PYX0=",
  "success": true,
  "projectFilePath": "D:\\Project\\Coding\\Code Practice\\C#\\C#.csproj",
  "expectedPackageFiles": [],
  "logs": []
}
```

### `obj/Debug/net8.0/C#.AssemblyInfo.cs`

```cs
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Reflection;

[assembly: System.Reflection.AssemblyCompanyAttribute("C#")]
[assembly: System.Reflection.AssemblyConfigurationAttribute("Debug")]
[assembly: System.Reflection.AssemblyFileVersionAttribute("1.0.0.0")]
[assembly: System.Reflection.AssemblyInformationalVersionAttribute("1.0.0+70e424d9c91e216695d258eee88258f4a3f2e998")]
[assembly: System.Reflection.AssemblyProductAttribute("C#")]
[assembly: System.Reflection.AssemblyTitleAttribute("C#")]
[assembly: System.Reflection.AssemblyVersionAttribute("1.0.0.0")]

// Generated by the MSBuild WriteCodeFragment class.
```

### `obj/Debug/net8.0/C#.AssemblyInfoInputs.cache`

```cache
f4be28d0493829a51d54d3349a38e4783e065e8801c9ef9c6dab9f7a1efd54f0
```

### `obj/Debug/net8.0/C#.GeneratedMSBuildEditorConfig.editorconfig`

```editorconfig
is_global = true
build_property.TargetFramework = net8.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = C#
build_property.ProjectDir = D:\Project\Coding\Code Practice\C#\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

### `obj/Debug/net8.0/C#.GlobalUsings.g.cs`

```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```

### `obj/Debug/net8.0/C#.csproj.CoreCompileInputs.cache`

```cache
245865b1c2c8f543b580666d98f46b01e2ccdf89b170c87a74b048477cd0d1c0
```

### `obj/Debug/net8.0/C#.csproj.FileListAbsolute.txt`

```
D:\Project\Coding\Code Practice\C#\bin\Debug\net8.0\C#.exe
D:\Project\Coding\Code Practice\C#\bin\Debug\net8.0\C#.deps.json
D:\Project\Coding\Code Practice\C#\bin\Debug\net8.0\C#.runtimeconfig.json
D:\Project\Coding\Code Practice\C#\bin\Debug\net8.0\C#.dll
D:\Project\Coding\Code Practice\C#\bin\Debug\net8.0\C#.pdb
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.GeneratedMSBuildEditorConfig.editorconfig
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.AssemblyInfoInputs.cache
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.AssemblyInfo.cs
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.csproj.CoreCompileInputs.cache
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.sourcelink.json
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.dll
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\refint\C#.dll
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.pdb
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\C#.genruntimeconfig.cache
D:\Project\Coding\Code Practice\C#\obj\Debug\net8.0\ref\C#.dll
```

### `obj/Debug/net8.0/C#.genruntimeconfig.cache`

```cache
2b34876b423ae42df9aab3b053f68550a461342e9755dd1d325d8883f3e97fcf
```

### `obj/Debug/net8.0/C#.sourcelink.json`

```json
{"documents":{"D:\\Project\\Coding\\Code Practice\\*":"https://raw.githubusercontent.com/NaufalKhalil/Code-Practice/70e424d9c91e216695d258eee88258f4a3f2e998/*"}}
```

