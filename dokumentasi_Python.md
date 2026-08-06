# Python

- **Dibuat:** 2026-07-31 23:35:45
- **Sumber:** `d:\Project\Coding\Code Practice\Python`
- **Total file:** 157 (0 sub-folder disertakan)

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
Python/
├── L001-Membuat Satu Variable dan Menampilkan Isinya.py
├── L002-Membuat Beberapa Variable Sekaligus.py
├── L003-Mengubah Nilai Variable.py
├── L004-Tipe Data String.py
├── L005-Tipe Data Integer.py
├── L006-Tipe Data Float (Bilangan Desimal).py
├── L007-Operasi Penjumlahan pada Integer.py
├── L008-Menyimpan Hasil Perhitungan ke Variable.py
├── L009-Operasi Pengurangan.py
├── L010-Operasi Perkalian.py
├── L011-Operasi Pembagian.py
├── L012-Operasi Pangkat.py
├── L013-Menerima Dua Input Angka dan Menjumlahkannya.py
├── L014-Percabangan IF-ELSE Dasar.py
├── L015-Percabangan IF-ELIF-ELSE.py
├── L016-Tipe Data Boolean (True atau False).py
├── L017-Operator Logika AND (Cek Angka dalam Rentang).py
├── L018-Operator Logika OR (Cek Angka di Luar Rentang).py
├── L019-Operator Logika NOT (Membalik Kondisi).py
├── L020-Mini Project Validasi Angka dengan AND dan Tidak Sama.py
├── L021-For Loop Dasar Menampilkan Angka 1 sampai 5.py
├── L022-For Loop Menampilkan Kelipatan 2.py
├── L023-For Loop Hitung Mundur dari 5 ke 1.py
├── L024-Menjumlahkan Angka 1 sampai 5 dengan For Loop.py
├── L025-Menjumlahkan Bilangan Genap 2 sampai 10.py
├── L026-Menghitung Berapa Kali Loop Berjalan.py
├── L027-For Loop dengan IF Menampilkan Angka di Atas 5.py
├── L028-Menampilkan Bilangan Genap dari 1 sampai 10.py
├── L029-Menampilkan Bilangan Ganjil dari 1 sampai 9.py
├── L030-Menjumlahkan Semua Bilangan Ganjil dari 1 sampai 10.py
├── L031-While Loop Menampilkan Angka 1 sampai 5.py
├── L032-While Loop Hitung Mundur dari 5 ke 1.py
├── L033-Menjumlahkan Angka 1 sampai 5 dengan While Loop.py
├── L034-While Loop Input Terus Sampai Angka Benar.py
├── L035-While Loop Program Berjalan Sampai Ketik Keluar.py
├── L036-Menghentikan Loop di Tengah Jalan dengan Break.py
├── L037-Melewati Iterasi Tertentu dengan Continue.py
├── L038-Mencetak Tabel Perkalian dengan 2.py
├── L039-Mencetak Tabel Perkalian Berdasarkan Input User.py
├── L040-Menampilkan Bilangan Genap sampai Batas Input User.py
├── L041-Mencetak Pola Kotak Bintang 3x3.py
├── L042-Mencetak Pola Segitiga Bintang.py
├── L043-Mencetak Pola Persegi dari Angka Baris.py
├── L044-Mencetak Pola Segitiga Angka Baris Berulang.py
├── L045-Mencetak Pola Segitiga Bintang Terbalik.py
├── L046-Mencetak Pola Segitiga Terbalik dari Angka Baris.py
├── L047-Mencetak Pola Segitiga Angka Berurutan dari 1.py
├── L048-Mencetak Pola Segitiga Terbalik Angka Berurutan.py
├── L049-Mencetak Pola Segitiga Siku Kanan Rata Kanan.py
├── L050-Mencetak Pola Piramida Bintang.py
├── L051-Mencetak Pola Piramida Bintang Terbalik.py
├── L052-Mencetak Pola Diamond (Piramida dan Piramida Terbalik).py
├── L053-Mencetak Pola Persegi Berongga (Hanya Tepi Bintang).py
├── L054-Mencetak Pola Segitiga Berongga (Hanya Tepi Bintang).py
├── L055-Mencetak Pola Huruf X dari Bintang.py
├── L056-Mencetak Pola Papan Catur (Bintang dan Spasi Selang-Seling).py
├── L057-Mencetak Tabel Perkalian 5x5 dengan Nested Loop.py
├── L058-FizzBuzz Cetak Fizz Buzz atau Angka 1 sampai 20.py
├── L059-Membuat List dan Menampilkan Semua Isinya.py
├── L060-Mengakses Elemen List Berdasarkan Index.py
├── L061-Mengganti Nilai Elemen List Berdasarkan Index.py
├── L062-Menambah Elemen Baru ke List dengan Append.py
├── L063-Menghapus Elemen dari List dengan Remove.py
├── L064-Menghitung Jumlah Elemen dalam List dengan Len.py
├── L065-Loop List Sambil Menampilkan Index dan Nilainya.py
├── L066-Mencari Apakah Data Ada dalam List.py
├── L067-Menjumlahkan Semua Elemen dalam List.py
├── L068-Mencari Nilai Terbesar dalam List.py
├── L069-Mencari Nilai Terkecil dalam List.py
├── L070-Menghitung Rata-rata Semua Elemen dalam List.py
├── L071-Menghitung Banyak Angka Genap dalam List.py
├── L072-Menghitung Banyak Angka Ganjil dalam List.py
├── L073-Input Sejumlah Angka dari User ke dalam List.py
├── L074-Menjumlahkan Angka yang Diinput User ke List.py
├── L075-Mencari Nilai Terbesar dari Angka yang Diinput User.py
├── L076-Mencari Nilai Terkecil dari Angka yang Diinput User.py
├── L077-Menghitung Rata-rata dari 5 Angka yang Diinput User.py
├── L078-Menghitung Banyak Bilangan Genap dari Input User.py
├── L079-Menghitung Banyak Bilangan Ganjil dari Input User.py
├── L080-Mencari Nilai Terbesar dan Posisi Index-nya.py
├── L081-Mencari Nilai Terkecil dan Posisi Index-nya.py
├── L082-Mencari Semua Posisi Jika Nilai Terbesar Muncul Berulang.py
├── L083-Menghitung Berapa Kali Setiap Angka Muncul dalam List.py
├── L084-Menampilkan Semua Index dari Angka yang Dicari.py
├── L085-Mencari Nilai Terbesar dan Terkecil dalam Satu Loop.py
├── L086-Menghitung Selisih antara Nilai Terbesar dan Terkecil.py
├── L087-Menampilkan Nilai Maks, Min, dan Rata-rata Sekaligus.py
├── L088-Menghitung Banyak Angka yang Nilainya di Atas Rata-rata.py
├── L089-Menampilkan Semua Angka yang Nilainya di Atas Rata-rata.py
├── L090-Mencari Angka dengan Nilai Paling Dekat ke Rata-rata.py
├── L091-Mencari Posisi Index Angka Paling Dekat ke Rata-rata.py
├── L092-Menampilkan Angka yang Nilainya Sama dengan Rata-rata Bulat Bawah.py
├── L093-Mencari Satu Angka dengan Frekuensi Kemunculan Terbanyak.py
├── L094-Menampilkan Semua Angka dengan Frekuensi Tertinggi (Modus).py
├── L095-Menampilkan Semua Angka yang Frekuensinya Tepat 1 Kali.py
├── L096-Menampilkan Semua Angka yang Muncul Lebih dari 1 Kali.py
├── L097-Menghitung Berapa Banyak Angka Unik dalam List.py
├── L098-Menampilkan Angka Unik Urut Sesuai Kemunculan Pertama.py
├── L099-Menampilkan Setiap Angka Unik Beserta Frekuensinya.py
├── L100-Mengurutkan dan Menampilkan Angka dari Frekuensi Terbesar.py
├── L101-Menampilkan Statistik Lengkap (Maks, Min, Rata-rata, Frekuensi).py
├── L102-Mencari Angka dengan Frekuensi Kemunculan Paling Sedikit.py
├── L103-Mencari Angka dengan Frekuensi di Posisi Tengah (Median Frekuensi).py
├── L104-Menghitung Selisih antara Frekuensi Terbesar dan Terkecil.py
├── L105-Menampilkan Selisih Frekuensi antara Setiap Pasangan Angka Berurutan.py
├── L106-Mencari Dua Angka dengan Selisih Nilai Terkecil.py
├── L107-Mencari Dua Angka dengan Selisih Nilai Terbesar.py
├── L108-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terbesar.py
├── L109-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terkecil.py
├── L110-Mencari 3 Angka Terbesar dan Total Penjumlahannya.py
├── L111-Mencari 3 Angka Terkecil dan Total Penjumlahannya.py
├── L112-Mencari Median dari 9 Angka (Jumlah Data Ganjil).py
├── L113-Mencari Median dari 10 Angka (Jumlah Data Genap).py
├── L114-Mencari Angka yang Frekuensinya di Posisi Tengah Setelah Diurutkan.py
├── L115-Menampilkan Selisih Frekuensi Setiap Pasangan Angka Berurutan.py
├── L116-Menampilkan Angka yang Selisih Frekuensinya Lebih dari 1 dengan Berikutnya.py
├── L117-Menampilkan Pasangan Angka yang Selisih Frekuensinya Lebih dari 1.py
├── L118-Mengecek Apakah Ada Satu Angka dengan Frekuensi Tertinggi Mutlak.py
├── L119-Menampilkan Semua Angka yang Berbagi Frekuensi Tertinggi Bersama.py
├── L120-Mencari Angka dengan Frekuensi Kemunculan Tertinggi Kedua.py
├── L121-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Tinggi ke Rendah.py
├── L122-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Rendah ke Tinggi.py
├── L123-Mencari Angka yang Frekuensinya Unik (Tidak Berbagi dengan Angka Lain).py
├── L124-Mencari Kelompok Frekuensi yang Paling Banyak Anggotanya.py
├── L125-Menampilkan Angka yang Frekuensinya Bukan Tertinggi dan Bukan Terendah.py
├── L126-Menampilkan Kelompok Frekuensi yang Jumlah Anggotanya Genap.py
├── L127-Menampilkan Huruf yang Muncul Lebih dari Sekali beserta Jumlahnya.py
├── L128-Menampilkan Huruf yang Hanya Muncul Tepat Sekali dalam Teks.py
├── L129-Mencari Huruf dengan Frekuensi Kemunculan Terbanyak dalam Teks.py
├── L130-Menampilkan Huruf dengan Frekuensi Kemunculan Terkecil.py
├── L131-Menampilkan Huruf dengan Frekuensi Kemunculan Tertinggi Kedua.py
├── L132-Menampilkan Pasangan Huruf dengan Selisih Frekuensi Terkecil.py
├── L133-Menampilkan Kelompok Huruf Berdasarkan Tingkat Frekuensi.py
├── L134-Menampilkan Huruf dengan Tetangga Frekuensi Terdekat.py
├── L135-Analisis Kata Paling Sering Dipakai.py
├── L136-Hitung Kata Terlarang (moderasi chat sederhana).py
├── L137-Sensor Kata Otomatis.py
├── L138-Hitung Persentase Toxic Chat.py
├── L139-Ranking Kata Paling Sering di Chat.py
├── L140-Analisis Log Login User.py
├── L141-Cari User Paling Aktif.py
├── L142-Persentase Aktivitas User.py
├── L143-Deteksi User Mencurigakan.py
├── L144-Top 3 User Paling Aktif.py
├── L145-Jam Sibuk Website (peak activity).py
├── L146-Analisis Penjualan Produk Terlaris.py
├── L147-Search Engine Produk Sederhana.py
├── L148-Filter Produk Berdasarkan Kategori.py
├── L149-Cari Produk Berdasarkan Nama atau Kategori.py
├── L150-Mini Aplikasi Inventaris Toko.py
├── L151-Function.py
├── L152-Function dengan Parameter.py
├── L153-Function yang Mengembalikan Nilai (return).py
├── L154-Sistem Kasir Sederhana.py
├── L155-Mini Sistem Nilai Mahasiswa.py
├── L157-Sistem Inventaris dengan penggunaan Parameter yang Tepat.py
└── L158-String Processing Challenge.py
```

## Daftar Isi

- [L001-Membuat Satu Variable dan Menampilkan Isinya.py](#l001-membuat-satu-variable-dan-menampilkan-isinyapy)
- [L002-Membuat Beberapa Variable Sekaligus.py](#l002-membuat-beberapa-variable-sekaliguspy)
- [L003-Mengubah Nilai Variable.py](#l003-mengubah-nilai-variablepy)
- [L004-Tipe Data String.py](#l004-tipe-data-stringpy)
- [L005-Tipe Data Integer.py](#l005-tipe-data-integerpy)
- [L006-Tipe Data Float (Bilangan Desimal).py](#l006-tipe-data-float-bilangan-desimalpy)
- [L007-Operasi Penjumlahan pada Integer.py](#l007-operasi-penjumlahan-pada-integerpy)
- [L008-Menyimpan Hasil Perhitungan ke Variable.py](#l008-menyimpan-hasil-perhitungan-ke-variablepy)
- [L009-Operasi Pengurangan.py](#l009-operasi-penguranganpy)
- [L010-Operasi Perkalian.py](#l010-operasi-perkalianpy)
- [L011-Operasi Pembagian.py](#l011-operasi-pembagianpy)
- [L012-Operasi Pangkat.py](#l012-operasi-pangkatpy)
- [L013-Menerima Dua Input Angka dan Menjumlahkannya.py](#l013-menerima-dua-input-angka-dan-menjumlahkannyapy)
- [L014-Percabangan IF-ELSE Dasar.py](#l014-percabangan-if-else-dasarpy)
- [L015-Percabangan IF-ELIF-ELSE.py](#l015-percabangan-if-elif-elsepy)
- [L016-Tipe Data Boolean (True atau False).py](#l016-tipe-data-boolean-true-atau-falsepy)
- [L017-Operator Logika AND (Cek Angka dalam Rentang).py](#l017-operator-logika-and-cek-angka-dalam-rentangpy)
- [L018-Operator Logika OR (Cek Angka di Luar Rentang).py](#l018-operator-logika-or-cek-angka-di-luar-rentangpy)
- [L019-Operator Logika NOT (Membalik Kondisi).py](#l019-operator-logika-not-membalik-kondisipy)
- [L020-Mini Project Validasi Angka dengan AND dan Tidak Sama.py](#l020-mini-project-validasi-angka-dengan-and-dan-tidak-samapy)
- [L021-For Loop Dasar Menampilkan Angka 1 sampai 5.py](#l021-for-loop-dasar-menampilkan-angka-1-sampai-5py)
- [L022-For Loop Menampilkan Kelipatan 2.py](#l022-for-loop-menampilkan-kelipatan-2py)
- [L023-For Loop Hitung Mundur dari 5 ke 1.py](#l023-for-loop-hitung-mundur-dari-5-ke-1py)
- [L024-Menjumlahkan Angka 1 sampai 5 dengan For Loop.py](#l024-menjumlahkan-angka-1-sampai-5-dengan-for-looppy)
- [L025-Menjumlahkan Bilangan Genap 2 sampai 10.py](#l025-menjumlahkan-bilangan-genap-2-sampai-10py)
- [L026-Menghitung Berapa Kali Loop Berjalan.py](#l026-menghitung-berapa-kali-loop-berjalanpy)
- [L027-For Loop dengan IF Menampilkan Angka di Atas 5.py](#l027-for-loop-dengan-if-menampilkan-angka-di-atas-5py)
- [L028-Menampilkan Bilangan Genap dari 1 sampai 10.py](#l028-menampilkan-bilangan-genap-dari-1-sampai-10py)
- [L029-Menampilkan Bilangan Ganjil dari 1 sampai 9.py](#l029-menampilkan-bilangan-ganjil-dari-1-sampai-9py)
- [L030-Menjumlahkan Semua Bilangan Ganjil dari 1 sampai 10.py](#l030-menjumlahkan-semua-bilangan-ganjil-dari-1-sampai-10py)
- [L031-While Loop Menampilkan Angka 1 sampai 5.py](#l031-while-loop-menampilkan-angka-1-sampai-5py)
- [L032-While Loop Hitung Mundur dari 5 ke 1.py](#l032-while-loop-hitung-mundur-dari-5-ke-1py)
- [L033-Menjumlahkan Angka 1 sampai 5 dengan While Loop.py](#l033-menjumlahkan-angka-1-sampai-5-dengan-while-looppy)
- [L034-While Loop Input Terus Sampai Angka Benar.py](#l034-while-loop-input-terus-sampai-angka-benarpy)
- [L035-While Loop Program Berjalan Sampai Ketik Keluar.py](#l035-while-loop-program-berjalan-sampai-ketik-keluarpy)
- [L036-Menghentikan Loop di Tengah Jalan dengan Break.py](#l036-menghentikan-loop-di-tengah-jalan-dengan-breakpy)
- [L037-Melewati Iterasi Tertentu dengan Continue.py](#l037-melewati-iterasi-tertentu-dengan-continuepy)
- [L038-Mencetak Tabel Perkalian dengan 2.py](#l038-mencetak-tabel-perkalian-dengan-2py)
- [L039-Mencetak Tabel Perkalian Berdasarkan Input User.py](#l039-mencetak-tabel-perkalian-berdasarkan-input-userpy)
- [L040-Menampilkan Bilangan Genap sampai Batas Input User.py](#l040-menampilkan-bilangan-genap-sampai-batas-input-userpy)
- [L041-Mencetak Pola Kotak Bintang 3x3.py](#l041-mencetak-pola-kotak-bintang-3x3py)
- [L042-Mencetak Pola Segitiga Bintang.py](#l042-mencetak-pola-segitiga-bintangpy)
- [L043-Mencetak Pola Persegi dari Angka Baris.py](#l043-mencetak-pola-persegi-dari-angka-barispy)
- [L044-Mencetak Pola Segitiga Angka Baris Berulang.py](#l044-mencetak-pola-segitiga-angka-baris-berulangpy)
- [L045-Mencetak Pola Segitiga Bintang Terbalik.py](#l045-mencetak-pola-segitiga-bintang-terbalikpy)
- [L046-Mencetak Pola Segitiga Terbalik dari Angka Baris.py](#l046-mencetak-pola-segitiga-terbalik-dari-angka-barispy)
- [L047-Mencetak Pola Segitiga Angka Berurutan dari 1.py](#l047-mencetak-pola-segitiga-angka-berurutan-dari-1py)
- [L048-Mencetak Pola Segitiga Terbalik Angka Berurutan.py](#l048-mencetak-pola-segitiga-terbalik-angka-berurutanpy)
- [L049-Mencetak Pola Segitiga Siku Kanan Rata Kanan.py](#l049-mencetak-pola-segitiga-siku-kanan-rata-kananpy)
- [L050-Mencetak Pola Piramida Bintang.py](#l050-mencetak-pola-piramida-bintangpy)
- [L051-Mencetak Pola Piramida Bintang Terbalik.py](#l051-mencetak-pola-piramida-bintang-terbalikpy)
- [L052-Mencetak Pola Diamond (Piramida dan Piramida Terbalik).py](#l052-mencetak-pola-diamond-piramida-dan-piramida-terbalikpy)
- [L053-Mencetak Pola Persegi Berongga (Hanya Tepi Bintang).py](#l053-mencetak-pola-persegi-berongga-hanya-tepi-bintangpy)
- [L054-Mencetak Pola Segitiga Berongga (Hanya Tepi Bintang).py](#l054-mencetak-pola-segitiga-berongga-hanya-tepi-bintangpy)
- [L055-Mencetak Pola Huruf X dari Bintang.py](#l055-mencetak-pola-huruf-x-dari-bintangpy)
- [L056-Mencetak Pola Papan Catur (Bintang dan Spasi Selang-Seling).py](#l056-mencetak-pola-papan-catur-bintang-dan-spasi-selang-selingpy)
- [L057-Mencetak Tabel Perkalian 5x5 dengan Nested Loop.py](#l057-mencetak-tabel-perkalian-5x5-dengan-nested-looppy)
- [L058-FizzBuzz Cetak Fizz Buzz atau Angka 1 sampai 20.py](#l058-fizzbuzz-cetak-fizz-buzz-atau-angka-1-sampai-20py)
- [L059-Membuat List dan Menampilkan Semua Isinya.py](#l059-membuat-list-dan-menampilkan-semua-isinyapy)
- [L060-Mengakses Elemen List Berdasarkan Index.py](#l060-mengakses-elemen-list-berdasarkan-indexpy)
- [L061-Mengganti Nilai Elemen List Berdasarkan Index.py](#l061-mengganti-nilai-elemen-list-berdasarkan-indexpy)
- [L062-Menambah Elemen Baru ke List dengan Append.py](#l062-menambah-elemen-baru-ke-list-dengan-appendpy)
- [L063-Menghapus Elemen dari List dengan Remove.py](#l063-menghapus-elemen-dari-list-dengan-removepy)
- [L064-Menghitung Jumlah Elemen dalam List dengan Len.py](#l064-menghitung-jumlah-elemen-dalam-list-dengan-lenpy)
- [L065-Loop List Sambil Menampilkan Index dan Nilainya.py](#l065-loop-list-sambil-menampilkan-index-dan-nilainyapy)
- [L066-Mencari Apakah Data Ada dalam List.py](#l066-mencari-apakah-data-ada-dalam-listpy)
- [L067-Menjumlahkan Semua Elemen dalam List.py](#l067-menjumlahkan-semua-elemen-dalam-listpy)
- [L068-Mencari Nilai Terbesar dalam List.py](#l068-mencari-nilai-terbesar-dalam-listpy)
- [L069-Mencari Nilai Terkecil dalam List.py](#l069-mencari-nilai-terkecil-dalam-listpy)
- [L070-Menghitung Rata-rata Semua Elemen dalam List.py](#l070-menghitung-rata-rata-semua-elemen-dalam-listpy)
- [L071-Menghitung Banyak Angka Genap dalam List.py](#l071-menghitung-banyak-angka-genap-dalam-listpy)
- [L072-Menghitung Banyak Angka Ganjil dalam List.py](#l072-menghitung-banyak-angka-ganjil-dalam-listpy)
- [L073-Input Sejumlah Angka dari User ke dalam List.py](#l073-input-sejumlah-angka-dari-user-ke-dalam-listpy)
- [L074-Menjumlahkan Angka yang Diinput User ke List.py](#l074-menjumlahkan-angka-yang-diinput-user-ke-listpy)
- [L075-Mencari Nilai Terbesar dari Angka yang Diinput User.py](#l075-mencari-nilai-terbesar-dari-angka-yang-diinput-userpy)
- [L076-Mencari Nilai Terkecil dari Angka yang Diinput User.py](#l076-mencari-nilai-terkecil-dari-angka-yang-diinput-userpy)
- [L077-Menghitung Rata-rata dari 5 Angka yang Diinput User.py](#l077-menghitung-rata-rata-dari-5-angka-yang-diinput-userpy)
- [L078-Menghitung Banyak Bilangan Genap dari Input User.py](#l078-menghitung-banyak-bilangan-genap-dari-input-userpy)
- [L079-Menghitung Banyak Bilangan Ganjil dari Input User.py](#l079-menghitung-banyak-bilangan-ganjil-dari-input-userpy)
- [L080-Mencari Nilai Terbesar dan Posisi Index-nya.py](#l080-mencari-nilai-terbesar-dan-posisi-index-nyapy)
- [L081-Mencari Nilai Terkecil dan Posisi Index-nya.py](#l081-mencari-nilai-terkecil-dan-posisi-index-nyapy)
- [L082-Mencari Semua Posisi Jika Nilai Terbesar Muncul Berulang.py](#l082-mencari-semua-posisi-jika-nilai-terbesar-muncul-berulangpy)
- [L083-Menghitung Berapa Kali Setiap Angka Muncul dalam List.py](#l083-menghitung-berapa-kali-setiap-angka-muncul-dalam-listpy)
- [L084-Menampilkan Semua Index dari Angka yang Dicari.py](#l084-menampilkan-semua-index-dari-angka-yang-dicaripy)
- [L085-Mencari Nilai Terbesar dan Terkecil dalam Satu Loop.py](#l085-mencari-nilai-terbesar-dan-terkecil-dalam-satu-looppy)
- [L086-Menghitung Selisih antara Nilai Terbesar dan Terkecil.py](#l086-menghitung-selisih-antara-nilai-terbesar-dan-terkecilpy)
- [L087-Menampilkan Nilai Maks, Min, dan Rata-rata Sekaligus.py](#l087-menampilkan-nilai-maks-min-dan-rata-rata-sekaliguspy)
- [L088-Menghitung Banyak Angka yang Nilainya di Atas Rata-rata.py](#l088-menghitung-banyak-angka-yang-nilainya-di-atas-rata-ratapy)
- [L089-Menampilkan Semua Angka yang Nilainya di Atas Rata-rata.py](#l089-menampilkan-semua-angka-yang-nilainya-di-atas-rata-ratapy)
- [L090-Mencari Angka dengan Nilai Paling Dekat ke Rata-rata.py](#l090-mencari-angka-dengan-nilai-paling-dekat-ke-rata-ratapy)
- [L091-Mencari Posisi Index Angka Paling Dekat ke Rata-rata.py](#l091-mencari-posisi-index-angka-paling-dekat-ke-rata-ratapy)
- [L092-Menampilkan Angka yang Nilainya Sama dengan Rata-rata Bulat Bawah.py](#l092-menampilkan-angka-yang-nilainya-sama-dengan-rata-rata-bulat-bawahpy)
- [L093-Mencari Satu Angka dengan Frekuensi Kemunculan Terbanyak.py](#l093-mencari-satu-angka-dengan-frekuensi-kemunculan-terbanyakpy)
- [L094-Menampilkan Semua Angka dengan Frekuensi Tertinggi (Modus).py](#l094-menampilkan-semua-angka-dengan-frekuensi-tertinggi-moduspy)
- [L095-Menampilkan Semua Angka yang Frekuensinya Tepat 1 Kali.py](#l095-menampilkan-semua-angka-yang-frekuensinya-tepat-1-kalipy)
- [L096-Menampilkan Semua Angka yang Muncul Lebih dari 1 Kali.py](#l096-menampilkan-semua-angka-yang-muncul-lebih-dari-1-kalipy)
- [L097-Menghitung Berapa Banyak Angka Unik dalam List.py](#l097-menghitung-berapa-banyak-angka-unik-dalam-listpy)
- [L098-Menampilkan Angka Unik Urut Sesuai Kemunculan Pertama.py](#l098-menampilkan-angka-unik-urut-sesuai-kemunculan-pertamapy)
- [L099-Menampilkan Setiap Angka Unik Beserta Frekuensinya.py](#l099-menampilkan-setiap-angka-unik-beserta-frekuensinyapy)
- [L100-Mengurutkan dan Menampilkan Angka dari Frekuensi Terbesar.py](#l100-mengurutkan-dan-menampilkan-angka-dari-frekuensi-terbesarpy)
- [L101-Menampilkan Statistik Lengkap (Maks, Min, Rata-rata, Frekuensi).py](#l101-menampilkan-statistik-lengkap-maks-min-rata-rata-frekuensipy)
- [L102-Mencari Angka dengan Frekuensi Kemunculan Paling Sedikit.py](#l102-mencari-angka-dengan-frekuensi-kemunculan-paling-sedikitpy)
- [L103-Mencari Angka dengan Frekuensi di Posisi Tengah (Median Frekuensi).py](#l103-mencari-angka-dengan-frekuensi-di-posisi-tengah-median-frekuensipy)
- [L104-Menghitung Selisih antara Frekuensi Terbesar dan Terkecil.py](#l104-menghitung-selisih-antara-frekuensi-terbesar-dan-terkecilpy)
- [L105-Menampilkan Selisih Frekuensi antara Setiap Pasangan Angka Berurutan.py](#l105-menampilkan-selisih-frekuensi-antara-setiap-pasangan-angka-berurutanpy)
- [L106-Mencari Dua Angka dengan Selisih Nilai Terkecil.py](#l106-mencari-dua-angka-dengan-selisih-nilai-terkecilpy)
- [L107-Mencari Dua Angka dengan Selisih Nilai Terbesar.py](#l107-mencari-dua-angka-dengan-selisih-nilai-terbesarpy)
- [L108-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terbesar.py](#l108-mencari-dua-angka-yang-jika-dijumlah-hasilnya-terbesarpy)
- [L109-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terkecil.py](#l109-mencari-dua-angka-yang-jika-dijumlah-hasilnya-terkecilpy)
- [L110-Mencari 3 Angka Terbesar dan Total Penjumlahannya.py](#l110-mencari-3-angka-terbesar-dan-total-penjumlahannyapy)
- [L111-Mencari 3 Angka Terkecil dan Total Penjumlahannya.py](#l111-mencari-3-angka-terkecil-dan-total-penjumlahannyapy)
- [L112-Mencari Median dari 9 Angka (Jumlah Data Ganjil).py](#l112-mencari-median-dari-9-angka-jumlah-data-ganjilpy)
- [L113-Mencari Median dari 10 Angka (Jumlah Data Genap).py](#l113-mencari-median-dari-10-angka-jumlah-data-genappy)
- [L114-Mencari Angka yang Frekuensinya di Posisi Tengah Setelah Diurutkan.py](#l114-mencari-angka-yang-frekuensinya-di-posisi-tengah-setelah-diurutkanpy)
- [L115-Menampilkan Selisih Frekuensi Setiap Pasangan Angka Berurutan.py](#l115-menampilkan-selisih-frekuensi-setiap-pasangan-angka-berurutanpy)
- [L116-Menampilkan Angka yang Selisih Frekuensinya Lebih dari 1 dengan Berikutnya.py](#l116-menampilkan-angka-yang-selisih-frekuensinya-lebih-dari-1-dengan-berikutnyapy)
- [L117-Menampilkan Pasangan Angka yang Selisih Frekuensinya Lebih dari 1.py](#l117-menampilkan-pasangan-angka-yang-selisih-frekuensinya-lebih-dari-1py)
- [L118-Mengecek Apakah Ada Satu Angka dengan Frekuensi Tertinggi Mutlak.py](#l118-mengecek-apakah-ada-satu-angka-dengan-frekuensi-tertinggi-mutlakpy)
- [L119-Menampilkan Semua Angka yang Berbagi Frekuensi Tertinggi Bersama.py](#l119-menampilkan-semua-angka-yang-berbagi-frekuensi-tertinggi-bersamapy)
- [L120-Mencari Angka dengan Frekuensi Kemunculan Tertinggi Kedua.py](#l120-mencari-angka-dengan-frekuensi-kemunculan-tertinggi-keduapy)
- [L121-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Tinggi ke Rendah.py](#l121-mengelompokkan-angka-berdasarkan-tingkat-frekuensi-dari-tinggi-ke-rendahpy)
- [L122-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Rendah ke Tinggi.py](#l122-mengelompokkan-angka-berdasarkan-tingkat-frekuensi-dari-rendah-ke-tinggipy)
- [L123-Mencari Angka yang Frekuensinya Unik (Tidak Berbagi dengan Angka Lain).py](#l123-mencari-angka-yang-frekuensinya-unik-tidak-berbagi-dengan-angka-lainpy)
- [L124-Mencari Kelompok Frekuensi yang Paling Banyak Anggotanya.py](#l124-mencari-kelompok-frekuensi-yang-paling-banyak-anggotanyapy)
- [L125-Menampilkan Angka yang Frekuensinya Bukan Tertinggi dan Bukan Terendah.py](#l125-menampilkan-angka-yang-frekuensinya-bukan-tertinggi-dan-bukan-terendahpy)
- [L126-Menampilkan Kelompok Frekuensi yang Jumlah Anggotanya Genap.py](#l126-menampilkan-kelompok-frekuensi-yang-jumlah-anggotanya-genappy)
- [L127-Menampilkan Huruf yang Muncul Lebih dari Sekali beserta Jumlahnya.py](#l127-menampilkan-huruf-yang-muncul-lebih-dari-sekali-beserta-jumlahnyapy)
- [L128-Menampilkan Huruf yang Hanya Muncul Tepat Sekali dalam Teks.py](#l128-menampilkan-huruf-yang-hanya-muncul-tepat-sekali-dalam-tekspy)
- [L129-Mencari Huruf dengan Frekuensi Kemunculan Terbanyak dalam Teks.py](#l129-mencari-huruf-dengan-frekuensi-kemunculan-terbanyak-dalam-tekspy)
- [L130-Menampilkan Huruf dengan Frekuensi Kemunculan Terkecil.py](#l130-menampilkan-huruf-dengan-frekuensi-kemunculan-terkecilpy)
- [L131-Menampilkan Huruf dengan Frekuensi Kemunculan Tertinggi Kedua.py](#l131-menampilkan-huruf-dengan-frekuensi-kemunculan-tertinggi-keduapy)
- [L132-Menampilkan Pasangan Huruf dengan Selisih Frekuensi Terkecil.py](#l132-menampilkan-pasangan-huruf-dengan-selisih-frekuensi-terkecilpy)
- [L133-Menampilkan Kelompok Huruf Berdasarkan Tingkat Frekuensi.py](#l133-menampilkan-kelompok-huruf-berdasarkan-tingkat-frekuensipy)
- [L134-Menampilkan Huruf dengan Tetangga Frekuensi Terdekat.py](#l134-menampilkan-huruf-dengan-tetangga-frekuensi-terdekatpy)
- [L135-Analisis Kata Paling Sering Dipakai.py](#l135-analisis-kata-paling-sering-dipakaipy)
- [L136-Hitung Kata Terlarang (moderasi chat sederhana).py](#l136-hitung-kata-terlarang-moderasi-chat-sederhanapy)
- [L137-Sensor Kata Otomatis.py](#l137-sensor-kata-otomatispy)
- [L138-Hitung Persentase Toxic Chat.py](#l138-hitung-persentase-toxic-chatpy)
- [L139-Ranking Kata Paling Sering di Chat.py](#l139-ranking-kata-paling-sering-di-chatpy)
- [L140-Analisis Log Login User.py](#l140-analisis-log-login-userpy)
- [L141-Cari User Paling Aktif.py](#l141-cari-user-paling-aktifpy)
- [L142-Persentase Aktivitas User.py](#l142-persentase-aktivitas-userpy)
- [L143-Deteksi User Mencurigakan.py](#l143-deteksi-user-mencurigakanpy)
- [L144-Top 3 User Paling Aktif.py](#l144-top-3-user-paling-aktifpy)
- [L145-Jam Sibuk Website (peak activity).py](#l145-jam-sibuk-website-peak-activitypy)
- [L146-Analisis Penjualan Produk Terlaris.py](#l146-analisis-penjualan-produk-terlarispy)
- [L147-Search Engine Produk Sederhana.py](#l147-search-engine-produk-sederhanapy)
- [L148-Filter Produk Berdasarkan Kategori.py](#l148-filter-produk-berdasarkan-kategoripy)
- [L149-Cari Produk Berdasarkan Nama atau Kategori.py](#l149-cari-produk-berdasarkan-nama-atau-kategoripy)
- [L150-Mini Aplikasi Inventaris Toko.py](#l150-mini-aplikasi-inventaris-tokopy)
- [L151-Function.py](#l151-functionpy)
- [L152-Function dengan Parameter.py](#l152-function-dengan-parameterpy)
- [L153-Function yang Mengembalikan Nilai (return).py](#l153-function-yang-mengembalikan-nilai-returnpy)
- [L154-Sistem Kasir Sederhana.py](#l154-sistem-kasir-sederhanapy)
- [L155-Mini Sistem Nilai Mahasiswa.py](#l155-mini-sistem-nilai-mahasiswapy)
- [L157-Sistem Inventaris dengan penggunaan Parameter yang Tepat.py](#l157-sistem-inventaris-dengan-penggunaan-parameter-yang-tepatpy)
- [L158-String Processing Challenge.py](#l158-string-processing-challengepy)

## File

### `L001-Membuat Satu Variable dan Menampilkan Isinya.py`

```python
nama = "Naufal"
print(nama)
```

### `L002-Membuat Beberapa Variable Sekaligus.py`

```python
nama = "Naufal"
umur = 18

print(nama)
print(umur)
```

### `L003-Mengubah Nilai Variable.py`

```python
nama = "Naufal"
nama = "Budi"

print(nama)
```

### `L004-Tipe Data String.py`

```python
kota = "Medan"
print(kota)

kota = "Jakarta"
print(kota)
```

### `L005-Tipe Data Integer.py`

```python
umur = 18
print(umur)

umur = 19
print(umur)
```

### `L006-Tipe Data Float (Bilangan Desimal).py`

```python
tinggi = 170.5
print(tinggi)

tinggi = 171.2
print(tinggi)
```

### `L007-Operasi Penjumlahan pada Integer.py`

```python
angka_1 = 10
angka_2 = 5

print(angka_1 + angka_2)
```

### `L008-Menyimpan Hasil Perhitungan ke Variable.py`

```python
angka_1 = 20
angka_2 = 10

hasil = angka_1 + angka_2
print(hasil)
```

### `L009-Operasi Pengurangan.py`

```python
angka_1 = 20
angka_2 = 7

hasil = angka_1 - angka_2
print(hasil)
```

### `L010-Operasi Perkalian.py`

```python
angka_1 = 6
angka_2 = 4

hasil = angka_1 * angka_2
print(hasil)
```

### `L011-Operasi Pembagian.py`

```python
angka_1 = 20
angka_2 = 5

hasil = angka_1 / angka_2
print(hasil)
```

### `L012-Operasi Pangkat.py`

```python
angka_1 = 3
angka_2 = 2

hasil = angka_1 ** angka_2
print(hasil)
```

### `L013-Menerima Dua Input Angka dan Menjumlahkannya.py`

```python
angka_1 = int(input("Masukan angka pertama : "))
angka_2 = int(input("Masukan angka kedua : "))

hasil = angka_1 + angka_2
print(hasil)
```

### `L014-Percabangan IF-ELSE Dasar.py`

```python
angka = int(input("Masukan angka : "))

if angka > 10 :
    print("Besar")
else :
    print("Kecil atau sama dengan 10")
```

### `L015-Percabangan IF-ELIF-ELSE.py`

```python
angka = int(input("Masukan angka : "))

if angka > 10 :
    print("Besar")
elif angka == 10 :
    print("Pas")
else :
    print("Kecil")
```

### `L016-Tipe Data Boolean (True atau False).py`

```python
angka = int(input("Masukan angka : "))

hasil = angka > 10

print(hasil)
```

### `L017-Operator Logika AND (Cek Angka dalam Rentang).py`

```python
angka = int(input("Masukan angka : "))

hasil = 5 < angka < 15

print(hasil)
```

### `L018-Operator Logika OR (Cek Angka di Luar Rentang).py`

```python
angka = int(input("Masukkan angka : "))

hasil = angka < 5 or angka > 15

print(hasil)
```

### `L019-Operator Logika NOT (Membalik Kondisi).py`

```python
angka = int(input("Masukkan angka : "))

hasil = not angka == 10

print(hasil)
```

### `L020-Mini Project Validasi Angka dengan AND dan Tidak Sama.py`

```python
angka = int(input("Masukkan angka : "))

if angka > 10 and angka != 15 :
    print("VALID")
else :
    print("TIDAK VALID")
```

### `L021-For Loop Dasar Menampilkan Angka 1 sampai 5.py`

```python
for i in range(1, 5 + 1):
    print(i)
```

### `L022-For Loop Menampilkan Kelipatan 2.py`

```python
for i in range(2 ,10 + 1, 2):
    print(i)
```

### `L023-For Loop Hitung Mundur dari 5 ke 1.py`

```python
for i in range(5, 0, -1):
    print(i)
```

### `L024-Menjumlahkan Angka 1 sampai 5 dengan For Loop.py`

```python
total = 0

for i in range (1, 5 + 1):
    total = total + i

print(total)
```

### `L025-Menjumlahkan Bilangan Genap 2 sampai 10.py`

```python
total = 0
for i in range(2, 10 + 1, 2):
    total = total + i
print(total)
```

### `L026-Menghitung Berapa Kali Loop Berjalan.py`

```python
jumlah = 0
for i in range(1, 5 + 1):
    jumlah += 1
print(jumlah)
```

### `L027-For Loop dengan IF Menampilkan Angka di Atas 5.py`

```python
for i in range(1, 10 + 1) :
    if i > 5 :
        print(i)
```

### `L028-Menampilkan Bilangan Genap dari 1 sampai 10.py`

```python
for i in range (1, 10 + 1) :
    if i % 2 == 0 :
        print(i)
```

### `L029-Menampilkan Bilangan Ganjil dari 1 sampai 9.py`

```python
for i in range (1, 10) :
    if i % 2 != 0 :
        print(i)
```

### `L030-Menjumlahkan Semua Bilangan Ganjil dari 1 sampai 10.py`

```python
total = 0

for i in range (1, 10 + 1):
    if i % 2 != 0 :
        total += i
print(total)
```

### `L031-While Loop Menampilkan Angka 1 sampai 5.py`

```python
angka = 1

while angka <= 5 :
    print(angka)
    angka += 1
```

### `L032-While Loop Hitung Mundur dari 5 ke 1.py`

```python
angka = 5

while angka > 0 :
    print(angka)
    angka -= 1
```

### `L033-Menjumlahkan Angka 1 sampai 5 dengan While Loop.py`

```python
angka = 1
total = 0

while angka <= 5 :
    total += angka
    angka += 1
print(total)
```

### `L034-While Loop Input Terus Sampai Angka Benar.py`

```python
angka = 0

while angka != 7 :
    angka = int(input("Masukkan angka : "))

if angka == 7 :
    print("Benar!")
```

### `L035-While Loop Program Berjalan Sampai Ketik Keluar.py`

```python
perintah = ""

while perintah != "keluar" :
    perintah = input("Masukkan Perintah : ")

print("Program Selesai")
```

### `L036-Menghentikan Loop di Tengah Jalan dengan Break.py`

```python
angka = 0

while True :
    angka += 1
    print(angka)
    if angka == 3 :
        break
```

### `L037-Melewati Iterasi Tertentu dengan Continue.py`

```python
for i in range(1, 5 + 1) :
    if i == 3 :
        continue
    print(i)
```

### `L038-Mencetak Tabel Perkalian dengan 2.py`

```python
for i in range(1, 5 + 1) :
    hasil = i * 2
    print(f"{i} x 2 = {hasil}")
```

### `L039-Mencetak Tabel Perkalian Berdasarkan Input User.py`

```python
angka = int(input("Masukan angka : "))

for i in range(1, 10 + 1) :
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")
```

### `L040-Menampilkan Bilangan Genap sampai Batas Input User.py`

```python
angka = int(input("Masukkan batas angka : "))

for i in range(1, angka + 1):
    if i % 2 == 0:
        print(i)
```

### `L041-Mencetak Pola Kotak Bintang 3x3.py`

```python
for i in range(1, 3 + 1) :
    print()
    for j in range(1, 3 + 1) :
        print("*", end="")
```

### `L042-Mencetak Pola Segitiga Bintang.py`

```python
for i in range(1, 5 + 1) :
    print("*" * i)
```

### `L043-Mencetak Pola Persegi dari Angka Baris.py`

```python
for i in range(1, 5 + 1) :
    for j in range(1, 5 + 1) :
        print(f"{i}", end="")
    print()
```

### `L044-Mencetak Pola Segitiga Angka Baris Berulang.py`

```python
for i in range(1, 5 + 1) :
    print()
    for j in range(0, i) :
        print(i, end="")
```

### `L045-Mencetak Pola Segitiga Bintang Terbalik.py`

```python
for i in range(5, 1 - 1, -1) :
    print()
    for j in range(1, i + 1) :
        print("*", end="")
```

### `L046-Mencetak Pola Segitiga Terbalik dari Angka Baris.py`

```python
for i in range(5, 1 - 1, -1) :
    print()
    for j in range(1, i + 1) :
        print(i, end="")
```

### `L047-Mencetak Pola Segitiga Angka Berurutan dari 1.py`

```python
for i in range(1, 5 + 1) :
    for j in range(1, i + 1) :
        print(j, end="")
    print()
```

### `L048-Mencetak Pola Segitiga Terbalik Angka Berurutan.py`

```python
for i in range(5, 1 - 1 , -1) :
    for j in range(1, i + 1) :
        print(j, end="")
    print()
```

### `L049-Mencetak Pola Segitiga Siku Kanan Rata Kanan.py`

```python
for i in range(1, 5 + 1):

    for j in range(1, (5 - i) + 1):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end="")
```

### `L050-Mencetak Pola Piramida Bintang.py`

```python
for i in range(1, 5 + 1):

    for j in range(5 - i):
        print(" ", end="")
    for j in range((i * 2) - 1):
        print("*", end="")
        
    print()
```

### `L051-Mencetak Pola Piramida Bintang Terbalik.py`

```python
for i in range(5, 0, -1 ):

    for j in range(5 - i):
        print(" ", end="")
    for j in range((i * 2) - 1):
        print("*", end="")
    
    print()
```

### `L052-Mencetak Pola Diamond (Piramida dan Piramida Terbalik).py`

```python
for i in range (1, 5 + 1):

    for j in range(5 - i):
        print(" ", end="")
    
    for j in range((i * 2) - 1):
        print("*", end="")

    print()

for i in range(4, 0, -1 ):

    for j in range(5 - i):
        print(" ", end="")
    for j in range((i * 2) - 1):
        print("*", end="")
    
    print()
```

### `L053-Mencetak Pola Persegi Berongga (Hanya Tepi Bintang).py`

```python
for i in range(1, 5 + 1):
    for j in range(1 , 5 + 1):
        if i == 1 or i == 5 :
            print("*", end="")
        else :
            if j == 1 or j == 5 :
                print("*", end="")
            else :
                print(" ", end="")
    print()
```

### `L054-Mencetak Pola Segitiga Berongga (Hanya Tepi Bintang).py`

```python
for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        if j == 1 or i == j or i == 5:  
            print("*", end="")
        else :
            print(" ", end="")
    print()
```

### `L055-Mencetak Pola Huruf X dari Bintang.py`

```python
for i in range(1, 5 + 1):
    for j in range(1, 5 + 1):
        if i == j or (i + j) == 6:
            print("*", end="")
        else :
            print(" ", end="")
    print()
```

### `L056-Mencetak Pola Papan Catur (Bintang dan Spasi Selang-Seling).py`

```python
for i in range(1, 5 + 1):
    for j in range(1, 8 + 1):
        if (i + j) % 2 == 0:
            print("*", end="")
        else :
            print(" ", end="")
    print()
```

### `L057-Mencetak Tabel Perkalian 5x5 dengan Nested Loop.py`

```python
for i in range(1, 5 + 1):
    for j in range(1, 5 + 1):
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")

    print()
```

### `L058-FizzBuzz Cetak Fizz Buzz atau Angka 1 sampai 20.py`

```python
for i in range(1, 20 + 1):
    if i % 5 == 0 and i % 3 == 0 :
        print("FizzBuzz")
    elif i % 5 == 0 :
        print("Buzz")
    elif i % 3 == 0 :
        print("Fizz")
    else :
        print(i)
```

### `L059-Membuat List dan Menampilkan Semua Isinya.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

for i in buah :
    print(i)
```

### `L060-Mengakses Elemen List Berdasarkan Index.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
print(buah[0])
print(buah[2])
```

### `L061-Mengganti Nilai Elemen List Berdasarkan Index.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

buah[1] = "Durian"

for i in buah :
    print(i)
```

### `L062-Menambah Elemen Baru ke List dengan Append.py`

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.append("Pisang")

for i in buah :
    print(i)
```

### `L063-Menghapus Elemen dari List dengan Remove.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

buah.remove("Mangga")

for i in buah :
    print(i)
```

### `L064-Menghitung Jumlah Elemen dalam List dengan Len.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

print(f"Jumlah buah: {len(buah)}")
```

### `L065-Loop List Sambil Menampilkan Index dan Nilainya.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

for i in range(len(buah)):
    print(i, buah[i])
```

### `L066-Mencari Apakah Data Ada dalam List.py`

```python
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

cari = input("Cari buah: ")

if cari in buah :
    print("Buah ditemukan")
else :
    print("Buah tidak ditemukan")
```

### `L067-Menjumlahkan Semua Elemen dalam List.py`

```python
angka = [10, 20, 30, 40, 50]
total = 0

for i in angka:
    total += i
print(total)
```

### `L068-Mencari Nilai Terbesar dalam List.py`

```python
angka = [10, 45, 23, 99, 12]

terbesar = angka[0]

for i in range(len(angka)):
    if angka[i] > terbesar:
        terbesar = angka[i]
print(terbesar)
```

### `L069-Mencari Nilai Terkecil dalam List.py`

```python
angka = [10, 45, 23, 99, 12]
terkecil = angka[0]

for i in range(len(angka)):
    if  angka[i] < terkecil:
        terkecil = angka[i]
print(terkecil)
```

### `L070-Menghitung Rata-rata Semua Elemen dalam List.py`

```python
angka = [10, 20, 30, 40, 50]
total = 0

for i in range(len(angka)):
    total += angka[i]

print(f"Rata-rata: {total / len(angka)}")
```

### `L071-Menghitung Banyak Angka Genap dalam List.py`

```python
angka = [10, 21, 30, 45, 50, 61]
jumlah = 0

for i in range(len(angka)):
    if angka[i] % 2 == 0 :
        jumlah += 1
print(jumlah)
```

### `L072-Menghitung Banyak Angka Ganjil dalam List.py`

```python
angka = [10, 21, 30, 45, 50, 61]
total = 0
ganjil = 0
for i in range(len(angka)):
    if angka[i] % 2 == 1:
        ganjil += 1
print(f"Jumlah angka ganjil: {ganjil}")
```

### `L073-Input Sejumlah Angka dari User ke dalam List.py`

```python
angka = []

n = int(input("Berapa data? :"))

for i in range(n):
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)

print(angka)
```

### `L074-Menjumlahkan Angka yang Diinput User ke List.py`

```python
angka = []
total = 0
jumlah_input = int(input("Berapa data? : "))

for i in range(jumlah_input):
    angka_input = int(input("Masukkan angka : "))
    angka.append(angka_input)
    total += angka[i]
print(f"Total : {total}")
```

### `L075-Mencari Nilai Terbesar dari Angka yang Diinput User.py`

```python
angka = []

jumlah_input = int(input("Berapa data? : "))

for i in range(jumlah_input):

    angka_input = int(input("Masukkan angka : "))
    angka.append(angka_input)

    if i == 0 :
        terbesar = angka[0]

    elif angka[i] > terbesar :
        terbesar = angka[i]

print(f"Nilai Terbesar : {terbesar}")
```

### `L076-Mencari Nilai Terkecil dari Angka yang Diinput User.py`

```python
angka = []

jumlah_angka = int(input("Berapa data? : "))
    
for i in range(jumlah_angka):

    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)

    if i == 0 : 
        terkecil = angka[0]

    elif input_angka > angka[i]:
        terkecil = angka[i]

print(f"Nilai terkecil : {terkecil}")
```

### `L077-Menghitung Rata-rata dari 5 Angka yang Diinput User.py`

```python
angka = []
total = 0

for i in range(1, 5 + 1):
    input_angka = int(input(f"Masukkan angka ke-{i} : "))
    angka.append(input_angka)

    total += input_angka

print(f"Jumlah = {total}")
print(f"Rata - rata = {total / len(angka)}")
```

### `L078-Menghitung Banyak Bilangan Genap dari Input User.py`

```python
angka = []
genap = 0

for i in range(1, 5 + 1):
    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)
    if input_angka % 2 == 0 :
        genap += 1
print(f"Jumlah bilangan genap : {genap}")
```

### `L079-Menghitung Banyak Bilangan Ganjil dari Input User.py`

```python
angka = []
ganjil = 0

for i in range(1, 5 + 1):
    input_angka = int(input("Masukkan angka : "))
    angka.append(input_angka)
    if input_angka % 2 == 1 :
        ganjil += 1
print(f"Jumlah bilangan ganjil : {ganjil}")
```

### `L080-Mencari Nilai Terbesar dan Posisi Index-nya.py`

```python
angka = []
posisi = 0

for i in range(0 , 5):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = angka[0]
    elif input_angka > terbesar:
        terbesar = angka[i]
        posisi = i

print(f"Nilai terbesar = {terbesar}")
print(f"Angka ke = {posisi + 1}, Posisi ke = {posisi} pada array")
```

### `L081-Mencari Nilai Terkecil dan Posisi Index-nya.py`

```python
angka = []
posisi = 0

for i in range(0 , 5):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terkecil = angka[0]
    elif input_angka < terkecil:
        terkecil = angka[i]
        posisi = i

print(f"Nilai terkecil = {terkecil}")
print(f"Angka ke = {posisi + 1}, Posisi ke = {posisi} pada array")
```

### `L082-Mencari Semua Posisi Jika Nilai Terbesar Muncul Berulang.py`

```python
angka = []

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = angka[i]
    
    elif input_angka > terbesar :
        terbesar = input_angka


print()

print(f"Nilai terbesar = {terbesar}")

print("Muncul pada :")

for i in range(len(angka)):
    if angka[i] == terbesar :
        print(f"Angka ke = {i + 1}, Posisi ke = {i} ")
```

### `L083-Menghitung Berapa Kali Setiap Angka Muncul dalam List.py`

```python
angka = []
total = 0

for i in range(0, 8):
    input_angka = int(input(f"Masukkan Angka ke-{i + 1} : "))
    angka.append(input_angka)

print("-"*16)

cari = int(input("Cari angka : "))

for i in range(len(angka)):
    if cari == angka[i]:
        total += 1

print(f"Angka {cari} muncul sebanyak {total}")
```

### `L084-Menampilkan Semua Index dari Angka yang Dicari.py`

```python
angka = []
total = 0

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

cari = int(input("Cari angka : "))

for i in range(len(angka)):
    if angka[i] == cari :
        total += 1

print("-"*16)
print(f"Angka {cari} muncul sebanyak {total}")
print()
print("Muncul pada :")

for i in range(len(angka)):
    if angka[i] == cari :
        print(f"Angka ke = {i + 1}, Posisi = {i}")
```

### `L085-Mencari Nilai Terbesar dan Terkecil dalam Satu Loop.py`

```python
angka = []

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = input_angka
    elif input_angka > terbesar :
        terbesar = input_angka
    
    if i == 0 :
        terkecil = input_angka
    elif input_angka < terkecil  :
        terkecil = input_angka
    
print(f"Nilai terbesar = {terbesar}")
print(f"Nilai terkecil = {terkecil}")
```

### `L086-Menghitung Selisih antara Nilai Terbesar dan Terkecil.py`

```python
angka = []

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)

    if i == 0 :
        terbesar = input_angka
    elif input_angka > terbesar :
        terbesar = input_angka
    
    if i == 0 :
        terkecil = input_angka
    elif input_angka < terkecil  :
        terkecil = input_angka
    
print(f"Nilai terbesar = {terbesar}")
print(f"Nilai terkecil = {terkecil}")
print(f"Selisih = {terbesar - terkecil}")
```

### `L087-Menampilkan Nilai Maks, Min, dan Rata-rata Sekaligus.py`

```python
angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

    if i == 0 :
        terbesar = input_angka
    elif input_angka > terbesar :
        terbesar = input_angka
    
    if i == 0 :
        terkecil = input_angka
    elif input_angka < terkecil  :
        terkecil = input_angka
    
print(f"Nilai terbesar = {terbesar}")
print(f"Nilai terkecil = {terkecil}")
print(f"Rata-rata = {total / len(angka)}")
```

### `L088-Menghitung Banyak Angka yang Nilainya di Atas Rata-rata.py`

```python
angka = []
total = 0
di_atas_rata_rata = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

for i in range(len(angka)):
    if angka[i] > rata_rata :
        di_atas_rata_rata += 1

print(f"Rata-rata = {rata_rata}")
print(f"Jumlah angka di atas rata-rata = {di_atas_rata_rata}")
```

### `L089-Menampilkan Semua Angka yang Nilainya di Atas Rata-rata.py`

```python
angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} : "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)


print(f"Rata-rata = {rata_rata}")
print("Angka di atas rata-rata :")

for i in range(len(angka)):
    if angka[i] > rata_rata :
        print(angka[i])
```

### `L090-Mencari Angka dengan Nilai Paling Dekat ke Rata-rata.py`

```python
angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

for i in range(len(angka)):
    
    jarak = rata_rata - angka[i]

    jarak = abs(jarak)

    if i == 0 :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]
    elif jarak < jarak_terdekat :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]

print(f"Rata-rata = {rata_rata}")

print(f"Angka Terdekat dari rata-rata = {angka_terdekat}")
```

### `L091-Mencari Posisi Index Angka Paling Dekat ke Rata-rata.py`

```python
angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)
    total += input_angka

rata_rata = total / len(angka)

for i in range(len(angka)):

    jarak = rata_rata - angka[i]

    jarak = abs(jarak)

    if i == 0 :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]
        posisi = i
    elif jarak < jarak_terdekat :
        jarak_terdekat = jarak
        angka_terdekat = angka[i]
        posisi = i

print("-"*16)
print(f"Rata-rata = {rata_rata}")
print(f"Angka terdekat = {angka_terdekat}")
print(f"Angka ke = {posisi + 1}")
print(f"Posisi index ke = {posisi}")
```

### `L092-Menampilkan Angka yang Nilainya Sama dengan Rata-rata Bulat Bawah.py`

```python
angka = []
total = 0

for i in range(0, 7):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)
    total += input_angka

rata_rata = int(total / len(angka))

print("-"*16)
print(f"Rata-rata = {rata_rata}")
print("Di temukan pada :")

for i in range(len(angka)):

    if angka[i] == rata_rata :
        print(f"Angka ke = {i + 1}, Posisi = {i}")
```

### `L093-Mencari Satu Angka dengan Frekuensi Kemunculan Terbanyak.py`

```python
angka = []
# deklarasi julah_kemunculan_sebelumnya yang belum ada karena masih putaran ke 0
jumlah_kemunculan_sebelumnya = 0

# masukkan input user ke dalam array angka
for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

# perulangan untuk array
for i in range(len(angka)):
    
    # deklarasi cari adalah angka array sekarang
    cari = angka[i]

    # reset jumlah kemunculan apabila perulangan "j" sudah selesai
    jumlah_kemunculan = 0    

    # perulangan untuk jumlah angka yang di cari
    for j in range(len(angka)):
        if cari == angka[j] :
            jumlah_kemunculan += 1
    
    if jumlah_kemunculan > jumlah_kemunculan_sebelumnya :
        jumlah_kemunculan_sebelumnya = jumlah_kemunculan
        angka_modus = angka[i]
    
print("-"*16)
print(f"Angka paling sering muncul = {angka_modus}")
print(f"Jumlah kemunculan = {jumlah_kemunculan_sebelumnya}")
```

### `L094-Menampilkan Semua Angka dengan Frekuensi Tertinggi (Modus).py`

```python
angka = []
jumlah_modus_sebelumnya = 0


for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    jumlah_modus = 0

    for j in range(len(angka)):

        if angka[i] == angka[j] :
            jumlah_modus += 1

    if jumlah_modus > jumlah_modus_sebelumnya :
        jumlah_modus_sebelumnya = jumlah_modus

print(f"Jumlah kemunculan terbesar = {jumlah_modus_sebelumnya}")
print("Angka :")

angka_yang_sudah_ditampilkan = []

for i in range(len(angka)):

    jumlah_kemunculan = 0

    for j in range(len(angka)):

        if angka[i] == angka[j] :    
            jumlah_kemunculan += 1

    if jumlah_modus_sebelumnya == jumlah_kemunculan and angka[i] not in angka_yang_sudah_ditampilkan :
        print(angka[i])
        angka_yang_sudah_ditampilkan.append(angka[i])
```

### `L095-Menampilkan Semua Angka yang Frekuensinya Tepat 1 Kali.py`

```python
angka = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

print("-"*16)
print("Angka yang muncul sekali :")

for i in range(len(angka)):

    total_modus = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total_modus += 1

    if total_modus == 1 :
        print(angka[i])
```

### `L096-Menampilkan Semua Angka yang Muncul Lebih dari 1 Kali.py`

```python
angka = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

print("Angka yang muncul lebih dari sekali :")

angka_sudah_ditampilkan = []

for i in range(len(angka)):
    
    total_modus = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total_modus += 1
    
    if total_modus > 1 and angka[i] not in angka_sudah_ditampilkan :
        print(angka[i])
        angka_sudah_ditampilkan.append(angka[i])
```

### `L097-Menghitung Berapa Banyak Angka Unik dalam List.py`

```python
angka = []
angka_tampil = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    if angka[i] not in angka_tampil:
        angka_tampil.append(angka[i])

print("Angka Unik")

for i in range(len(angka_tampil)):
    print(angka_tampil[i])

jumlah_angka_unik = len(angka_tampil)
print(f"Jumlah angka unik = {jumlah_angka_unik}")
```

### `L098-Menampilkan Angka Unik Urut Sesuai Kemunculan Pertama.py`

```python
angka = []
angka_tampil = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

print("Angka Unik")

for i in range(len(angka)):
    if angka[i] not in angka_tampil:
        angka_tampil.append(angka[i])
        print(angka[i])
```

### `L099-Menampilkan Setiap Angka Unik Beserta Frekuensinya.py`

```python
angka = []
angka_sortir = []
jumlah_muncul = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total_muncul = 0

    for j in range(len(angka)):
        if angka[j] == angka[i]:
            total_muncul += 1

    if angka[i] not in angka_sortir :
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total_muncul)

print("-"*16)

for i in range(len(angka_sortir)):
    print(f"{angka_sortir[i]} muncul {jumlah_muncul[i]} kali")
```

### `L100-Mengurutkan dan Menampilkan Angka dari Frekuensi Terbesar.py`

```python
angka = []

angka_sortir = []
jumlah_muncul = []

for i in range(0, 8):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total_muncul = 0

    for j in range(len(angka)):
        if angka[j] == angka[i]:
            total_muncul += 1

    if angka[i] not in angka_sortir :
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total_muncul)

for i in range(len(jumlah_muncul)):

    for j in range(len(jumlah_muncul) - 1 ):

        if jumlah_muncul[j] < jumlah_muncul[j + 1]:
            jumlah_muncul[j], jumlah_muncul[j + 1] = jumlah_muncul[j + 1], jumlah_muncul[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]
        
print("-"*16)

for i in range(len(angka_sortir)):
    print(f"{angka_sortir[i]} muncul {jumlah_muncul[i]} kali")
```

### `L101-Menampilkan Statistik Lengkap (Maks, Min, Rata-rata, Frekuensi).py`

```python
angka = []
angka_sortir = []
list_modus = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sortir :
        angka_sortir.append(angka[i])
        list_modus.append(total)

print("-"*24)

print(f"=> Jumlah angka unik = {len(angka_sortir)}")

for i in range(len(angka_sortir)):

    for j in range(len(angka_sortir) - 1):

        if list_modus[j] < list_modus[j + 1]:
            list_modus[j], list_modus[j + 1] = list_modus[j + 1], list_modus[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]

print()
print(f"Jumlah kemunculan = {list_modus[0]}")
print()

print("-"*24)
print("=> Angka paling sering muncul :")

for i in range(len(angka_sortir)):
    if list_modus[0] == list_modus[i]:
        print(f"{angka_sortir[i]}")

print()

print("-"*24)
print("=> Statistik :")

for i in range(len(angka_sortir)):
    print(f"{angka_sortir[i]} muncul {list_modus[i]}")
```

### `L102-Mencari Angka dengan Frekuensi Kemunculan Paling Sedikit.py`

```python
angka = []

angka_sortir = []
jumlah_muncul = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sortir:
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total)

for i in range(len(angka_sortir)):

    for j in range(len(angka_sortir) - 1):

        if jumlah_muncul[j] < jumlah_muncul[j + 1]:
            jumlah_muncul[j], jumlah_muncul[j + 1] = jumlah_muncul[j + 1], jumlah_muncul[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]

n = len(jumlah_muncul) - 1

kemunculan_terkecil = jumlah_muncul[n]

print("-"*24)

print(f"Jumlah kemunculan terkecil = {kemunculan_terkecil}")

print("Angka :")

for i in range(len(angka_sortir)):
    if jumlah_muncul[i] == kemunculan_terkecil:
        print(angka_sortir[i])
```

### `L103-Mencari Angka dengan Frekuensi di Posisi Tengah (Median Frekuensi).py`

```python
angka = []

angka_sortir = []
jumlah_muncul = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0
    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sortir:
        angka_sortir.append(angka[i])
        jumlah_muncul.append(total)

for i in range(len(angka_sortir)):

    for j in range(len(angka_sortir) - 1):

        if jumlah_muncul[j] < jumlah_muncul[j + 1]:
            jumlah_muncul[j], jumlah_muncul[j + 1] = jumlah_muncul[j + 1], jumlah_muncul[j]
            angka_sortir[j], angka_sortir[j + 1] = angka_sortir[j + 1], angka_sortir[j]


if len(jumlah_muncul) % 2 == 1:
    nilai_tengah = (len(jumlah_muncul) // 2 )
else :
    nilai_tengah = (len(jumlah_muncul) // 2 )

modus_tengah = jumlah_muncul[nilai_tengah]

print("-"*24)
print(f"Modus tengah = {modus_tengah}")
print("Angka :")

for i in range(len(angka_sortir)):
    if jumlah_muncul[nilai_tengah] == jumlah_muncul[i]:
        print(angka_sortir[i])
```

### `L104-Menghitung Selisih antara Frekuensi Terbesar dan Terkecil.py`

```python
angka = []

angka_sorting = []
jumlah_modus = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j] :
            total += 1

    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        jumlah_modus.append(total)

for i in range(len(angka_sorting)):
    
    for j in range(len(angka_sorting) - 1):
        
        if jumlah_modus[j] < jumlah_modus[j + 1]:
            jumlah_modus[j], jumlah_modus[j + 1] = jumlah_modus[j + 1], jumlah_modus[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

posisi_terakhir = len(angka_sorting) - 1
modus_terbesar = jumlah_modus[0]
modus_terkecil = jumlah_modus[posisi_terakhir]
selisih = modus_terbesar - modus_terkecil

print("-"*24)

print(f"Modus terbesar = {modus_terbesar}")
print("Angka :")

for i in range(len(angka_sorting)):
    if jumlah_modus[i] == modus_terbesar:
        print(angka_sorting[i])

print("-"*24)

print(f"Modus terkecil = {modus_terkecil}")
print("Angka :")

for i in range(len(angka_sorting)):
    if jumlah_modus[i] == modus_terkecil:
        print(angka_sorting[i])

print("-"*24)

print(f"Selisih = {selisih}")
```

### `L105-Menampilkan Selisih Frekuensi antara Setiap Pasangan Angka Berurutan.py`

```python
angka = []

angka_sorting = []
modus_sorting = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    
    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        modus_sorting.append(total)

for i in range(len(angka_sorting)):
    
    for j in range(len(angka_sorting) - 1):
        
        if modus_sorting[j] < modus_sorting[j + 1]:
            modus_sorting[j], modus_sorting[j + 1] = modus_sorting[j + 1], modus_sorting[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

print("-"*24)

for i in range(len(modus_sorting) - 1):

    print(f"{angka_sorting[i]} dan {angka_sorting[i + 1]} selisih modus = {modus_sorting[i] - modus_sorting[i + 1]} ")
```

### `L106-Mencari Dua Angka dengan Selisih Nilai Terkecil.py`

```python
angka = []

for i in range(0, 10):
    input_user = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_user)

# sorting terbesar → terkecil
for i in range(len(angka)):
    for j in range(len(angka)-1):

        if angka[j] < angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]

print("-"*24)
print(angka)

# cari selisih terkecil
for i in range(len(angka)-1):

    selisih = abs(angka[i] - angka[i+1])

    if i == 0:
        selisih_update = selisih
    elif selisih < selisih_update:
        selisih_update = selisih

print("-"*24)
print("Pasangan terdekat :")

for i in range(len(angka)-1):

    selisih = abs(angka[i] - angka[i+1])

    if selisih == selisih_update:
        print(f"{angka[i]} dan {angka[i+1]}")

print(f"Selisih = {selisih_update}")
```

### `L107-Mencari Dua Angka dengan Selisih Nilai Terbesar.py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for j in range(len(angka)):

    for i in range(len(angka) - 1):

        if angka[i] < angka[i + 1]:
            angka[i], angka[i + 1] = angka[i + 1], angka[i]

n = len(angka)

print(f"Pasangan terjauh = {angka[0]} dan {angka[n - 1]}, dengan selisih = {angka[0] - angka[n - 1]}")
```

### `L108-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terbesar.py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Pasangan terbesar : {angka[0]} dan {angka[1]}")
print(f"Jumlah = {angka[0] + angka[1]}")
```

### `L109-Mencari Dua Angka yang Jika Dijumlah Hasilnya Terkecil.py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Pasangan dengan penjumlahan terkecil = {angka[0]} dan {angka[1]}")
print(f"Jumlah = {angka[1] + angka[0]}")
```

### `L110-Mencari 3 Angka Terbesar dan Total Penjumlahannya.py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Tiga angka terbesar jika di jumlahkan : {angka[0]}, {angka[1]}, dan {angka[2]}")
print(f"Dengan hasil penjumlahan = {angka[0] + angka[1] + angka[2]}")
```

### `L111-Mencari 3 Angka Terkecil dan Total Penjumlahannya.py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(f"Tiga angka terkecil jika di jumlahkan : {angka[0]}, {angka[1]}, dan {angka[2]}")
print(f"Dengan hasil penjumlahan = {angka[0] + angka[1] + angka[2]}")
```

### `L112-Mencari Median dari 9 Angka (Jumlah Data Ganjil).py`

```python
angka = []

for i in range(0, 9):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

median = len(angka) // 2

print(f"Median = {angka[median]}")
```

### `L113-Mencari Median dari 10 Angka (Jumlah Data Genap).py`

```python
angka = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

x = (len(angka) // 2) - 1
median = (angka[x] + angka[x + 1]) / 2

print(f"Median = {median}")
```

### `L114-Mencari Angka yang Frekuensinya di Posisi Tengah Setelah Diurutkan.py`

```python
angka = []

angka_sorting = []
frekuensi_sorting = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):
    
    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1

    if angka[i] not in angka_sorting:
        angka_sorting.append(angka[i])
        frekuensi_sorting.append(total)

for i in range(len(frekuensi_sorting)):
    for j in range(len(frekuensi_sorting) - 1):
        if frekuensi_sorting[j] < frekuensi_sorting[j + 1]:
            frekuensi_sorting[j], frekuensi_sorting[j + 1] = frekuensi_sorting[j + 1], frekuensi_sorting[j]
            angka_sorting[j], angka_sorting[j + 1] = angka_sorting[j + 1], angka_sorting[j]

median_frekuensi = len(frekuensi_sorting) // 2

print(f"Frekuensi tengah = {frekuensi_sorting[median_frekuensi - 1]}")

for i in range(len(angka_sorting)):
    if frekuensi_sorting[median_frekuensi - 1] == frekuensi_sorting[i]:
        print(angka_sorting[i])
```

### `L115-Menampilkan Selisih Frekuensi Setiap Pasangan Angka Berurutan.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

print("-"*24)

for i in range(len(frekuensi_sort) - 1):

    selisih = abs(frekuensi_sort[i] - frekuensi_sort[i + 1])

    print(f"{angka_sort[i]} dan {angka_sort[i + 1]} : selisih frekuensi = {selisih}")
```

### `L116-Menampilkan Angka yang Selisih Frekuensinya Lebih dari 1 dengan Berikutnya.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

f_sudah_tampil = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

for i in range(len(frekuensi_sort)):

    for k in range(len(frekuensi_sort) - 1):

        selisih = abs(frekuensi_sort[k] - frekuensi_sort[k + 1])

        if selisih > 1:
            print(f"{angka_sort[k] }")
```

### `L117-Menampilkan Pasangan Angka yang Selisih Frekuensinya Lebih dari 1.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

print("-"*24)

for i in range(len(frekuensi_sort) - 1):

    selisih = abs(frekuensi_sort[i] - frekuensi_sort[i + 1])

    if selisih > 1 :
        print(f"{angka_sort[i]} dan {angka_sort[i + 1]} : selisih frekuensi = {selisih}")
```

### `L118-Mengecek Apakah Ada Satu Angka dengan Frekuensi Tertinggi Mutlak.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]


if frekuensi_sort[0] > frekuensi_sort[1]:
    print(f"Raja frekuensi : {angka_sort[0]}")
else :
    print("Tidak ada raja")
```

### `L119-Menampilkan Semua Angka yang Berbagi Frekuensi Tertinggi Bersama.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

raja_frekuensi = frekuensi_sort[0]

print("Raja bersama :")

for i in range(len(frekuensi_sort)):
    if raja_frekuensi == frekuensi_sort[i]:
        print(angka_sort[i])
```

### `L120-Mencari Angka dengan Frekuensi Kemunculan Tertinggi Kedua.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_raja_1 = frekuensi_sort[0]
f_raja_2 = 0

for i in range(len(frekuensi_sort)):
    if f_raja_1 > frekuensi_sort[i]:
        f_raja_2 = frekuensi_sort[i]
        break

if f_raja_2 == 0:
    print("Tidak ada raja kedua")
else :
    print("Raja kedua :")
    for i in range(len(frekuensi_sort)):
        if f_raja_2 == frekuensi_sort[i]:
            print(angka_sort[i])
```

### `L121-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Tinggi ke Rendah.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_sudah = []
tahta = 0

for i in range(len(frekuensi_sort)):

    if frekuensi_sort[i] not in f_sudah:
        tahta += 1
        print(f"Tahta {tahta}")

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j] and frekuensi_sort[i] not in f_sudah:
            print(angka_sort[j])

    f_sudah.append(frekuensi_sort[i])
```

### `L122-Mengelompokkan Angka Berdasarkan Tingkat Frekuensi dari Rendah ke Tinggi.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 10):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_sudah = []
total_tahta = 1

for i in range(len(frekuensi_sort) - 1):
    if frekuensi_sort[i + 1] != frekuensi_sort[i]:
        total_tahta += 1

print(f"Total tahta = {total_tahta}")
print()

for i in range(len(frekuensi_sort) - 1, -1, - 1):

    if frekuensi_sort[i] not in f_sudah:
        print(f"Tahta {total_tahta} => kemunculan sebanyak {frekuensi_sort[i]} kali :")
        total_tahta -= 1

    for j in range(len(frekuensi_sort) - 1, -1, - 1):
        if frekuensi_sort[i] == frekuensi_sort[j] and frekuensi_sort[i] not in f_sudah:
            print(angka_sort[j])

    f_sudah.append(frekuensi_sort[i])
```

### `L123-Mencari Angka yang Frekuensinya Unik (Tidak Berbagi dengan Angka Lain).py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 20):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

print("Penghianat Tahta :")
for i in range(len(frekuensi_sort)):
  
    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total == 1:
        print(angka_sort[i])
```

### `L124-Mencari Kelompok Frekuensi yang Paling Banyak Anggotanya.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 20):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_total_besar = 0

for i in range(len(frekuensi_sort)):
  
    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total_besar < f_total:
        f_total_besar = f_total

print("Tahta paling ramai :")

jumlah_anggota = 0

for i in range(len(angka_sort)):

    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total == f_total_besar:
        print(angka_sort[i])
        jumlah_anggota += 1 

print(f"Jumlah anggota = {jumlah_anggota} ")
```

### `L125-Menampilkan Angka yang Frekuensinya Bukan Tertinggi dan Bukan Terendah.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 20):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_total_besar = 0

for i in range(len(frekuensi_sort)):
  
    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total += 1

    if f_total_besar < f_total:
        f_total_besar = f_total

print(f"Tahta tertinggi : {f_total_besar}")

f_total_kecil = 0

for i in range(len(frekuensi_sort)):
  
    f_total = 0

    for j in range(len(frekuensi_sort)):
        if frekuensi_sort[i] == frekuensi_sort[j]:
            f_total -= 1

    if f_total_kecil > f_total:
        f_total_kecil = f_total

f_total_kecil = abs(f_total_kecil)

print(f"Tahta terendah : {f_total_kecil}")

print()
print("Yang di tengah :")

if f_total_besar != f_total_kecil:

    jumlah_anggota = 0

    for i in range(len(angka_sort)):

        f_total = 0

        for j in range(len(frekuensi_sort)):
            if frekuensi_sort[i] == frekuensi_sort[j]:
                f_total += 1

        if f_total != f_total_besar and f_total != f_total_kecil:
            print(angka_sort[i],",", end="")
            jumlah_anggota += 1 

else:
    print("Tidak ada yang tahta ditengah, tertinggi, dan terendah")
    print("=> kerena anggota tiap tahta sama atau hanya terdapat 2 tahta")
```

### `L126-Menampilkan Kelompok Frekuensi yang Jumlah Anggotanya Genap.py`

```python
angka = []

angka_sort = []
frekuensi_sort = []

for i in range(0, 20):
    input_angka = int(input(f"Masukkan angka ke-{i + 1} = "))
    angka.append(input_angka)

for i in range(len(angka)):

    total = 0

    for j in range(len(angka)):
        if angka[i] == angka[j]:
            total += 1
    
    if angka[i] not in angka_sort:
        angka_sort.append(angka[i])
        frekuensi_sort.append(total)

for i in range(len(angka_sort)):
    for j in range(len(angka_sort) - 1):
        if frekuensi_sort[j] < frekuensi_sort[j + 1]:
            frekuensi_sort[j], frekuensi_sort[j + 1] = frekuensi_sort[j + 1], frekuensi_sort[j]
            angka_sort[j], angka_sort[j + 1] = angka_sort[j + 1], angka_sort[j]

f_sudah = []
ada_genap = False

for i in range(len(angka_sort)):

        f_total = 0

        for j in range(len(frekuensi_sort)):
            if frekuensi_sort[i] == frekuensi_sort[j]:
                f_total += 1

        if f_total % 2 == 0 and frekuensi_sort[i] not in f_sudah:

            print("Tahta :")

            for k in range(len(angka_sort)):
                if frekuensi_sort[k] == frekuensi_sort[i]:
                    print(angka_sort[k])

            f_sudah.append(frekuensi_sort[i])

            ada_genap = True
            
print()

if ada_genap == False: 
    print("Tidak ada tahta yang beranggota genap")
```

### `L127-Menampilkan Huruf yang Muncul Lebih dari Sekali beserta Jumlahnya.py`

```python
text = input("Masukkan Text : ")
sudah_tampil = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > 1:
        if text[i] not in sudah_tampil:
            print(f"{text[i]} = {total}")
            sudah_tampil.append(text[i])
```

### `L128-Menampilkan Huruf yang Hanya Muncul Tepat Sekali dalam Teks.py`

```python
text = input("Masukkan Text : ")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == 1:
        print(text[i])
```

### `L129-Mencari Huruf dengan Frekuensi Kemunculan Terbanyak dalam Teks.py`

```python
text = input("Masukkan Text : ")

sudah_tampil = []
total_besar = 0

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > total_besar:
        total_besar = total

print("Raja huruf :")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == total_besar:
        if text[i] not in sudah_tampil:
            print(text[i])
            sudah_tampil.append(text[i])
```

### `L130-Menampilkan Huruf dengan Frekuensi Kemunculan Terkecil.py`

```python
text = input("Masukkan Text : ")

sudah_tampil = []
total_kecil = len(text)

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total < total_kecil:
        total_kecil = total

print(f"Frekuensi terkecil = {total_kecil}")
print("huruf :")

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total == total_kecil:
        if text[i] not in sudah_tampil:
            print(text[i])
            sudah_tampil.append(text[i])
```

### `L131-Menampilkan Huruf dengan Frekuensi Kemunculan Tertinggi Kedua.py`

```python
text = input("Masukkan Text : ")

sudah_tampil = []
total_besar_1 = 0

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total > total_besar_1:
        total_besar_1 = total

total_besar_2 = 0

flag = False

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1

    if total_besar_2 < total < total_besar_1:
        total_besar_2 = total
        flag = True

if flag == True :

    print(f"Frekuensi Terbesar ke dua = {total_besar_2}")
    print("huruf :")

    for i in range(len(text)):

        total = 0

        for j in range(len(text)):
            if text[i] == text[j]:
                total += 1

        if total == total_besar_2:
            if text[i] not in sudah_tampil:
                print(text[i])
                sudah_tampil.append(text[i])

else:
    print("Tidak ada Frekuensi Terbesar ke dua")
```

### `L132-Menampilkan Pasangan Huruf dengan Selisih Frekuensi Terkecil.py`

```python
text = input("Masukkan Text : ")

f_huruf = []
huruf_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in huruf_disortir:
        f_huruf.append(total)
        huruf_disortir.append(text[i])

for i in range(len(f_huruf)):
    for j in range(len(f_huruf) - 1):
        if f_huruf[j] < f_huruf[j + 1]:
            f_huruf[j], f_huruf[j + 1] = f_huruf[j + 1], f_huruf[j]
            huruf_disortir[j], huruf_disortir[j + 1] = huruf_disortir[j + 1], huruf_disortir[j]

selisih_terkecil = len(text)
flag = False

for i in range(len(f_huruf) - 1):

    selisih = abs(f_huruf[i] - f_huruf[i + 1])

    if selisih < selisih_terkecil and selisih != 0 :
        selisih_terkecil = selisih
        flag = True

if flag == True :

    print("Pasangan :")

    for i in range(len(f_huruf) - 1):
        
        selisih = abs(f_huruf[i] - f_huruf[i + 1])

        if selisih_terkecil == selisih :
            print(f"{huruf_disortir[i]} dan {huruf_disortir[i + 1]}")
    
    print()
    print(f"Selisih = {selisih_terkecil}")

else :
    print("Tidak ada selisih terkecil")
```

### `L133-Menampilkan Kelompok Huruf Berdasarkan Tingkat Frekuensi.py`

```python
text = input("Masukkan Text : ")

f_huruf = []
huruf_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in huruf_disortir:
        f_huruf.append(total)
        huruf_disortir.append(text[i])

for i in range(len(f_huruf)):
    for j in range(len(f_huruf) - 1):
        if f_huruf[j] < f_huruf[j + 1]:
            f_huruf[j], f_huruf[j + 1] = f_huruf[j + 1], f_huruf[j]
            huruf_disortir[j], huruf_disortir[j + 1] = huruf_disortir[j + 1], huruf_disortir[j]

f_sudah = []

for i in range(len(f_huruf)):
    
    if f_huruf[i] not in f_sudah:
        print(f"Frekuensi {f_huruf[i]} :")
        f_sudah.append(f_huruf[i])

        for j in range(len(f_huruf)):
            if f_huruf[i] == f_huruf[j]:
                print(huruf_disortir[j])
```

### `L134-Menampilkan Huruf dengan Tetangga Frekuensi Terdekat.py`

```python
text = input("Masukkan Text : ")

f_huruf = []
huruf_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in huruf_disortir:
        f_huruf.append(total)
        huruf_disortir.append(text[i])

for i in range(len(f_huruf)):
    for j in range(len(f_huruf) - 1):
        if f_huruf[j] < f_huruf[j + 1]:
            f_huruf[j], f_huruf[j + 1] = f_huruf[j + 1], f_huruf[j]
            huruf_disortir[j], huruf_disortir[j + 1] = huruf_disortir[j + 1], huruf_disortir[j]

for i in range(len(huruf_disortir) - 1):
    print(f"{huruf_disortir[i]} -> {huruf_disortir[i + 1]}")
```

### `L135-Analisis Kata Paling Sering Dipakai.py`

```python
text = input("Masukkan text :")

kata = text.split()

total_terbesar = 0


for i in range(len(kata)):
    
    total = 0
        
    for j in range(len(kata)):
        if kata[i] == kata[j]:
            total += 1

    if total_terbesar < total:
        total_terbesar = total

sudah_tampil = []

for i in range(len(kata)):
    
    total = 0

    for j in range(len(kata)):
        if kata[i] == kata[j]:
            total += 1
        
    if total == total_terbesar and kata[i] not in sudah_tampil:
        print(f"{kata[i]} = {total_terbesar}")
        sudah_tampil.append(kata[i])
```

### `L136-Hitung Kata Terlarang (moderasi chat sederhana).py`

```python
terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

sudah_tampil = []

total = 0

for i in range(len(text)):
    if text[i] in terlarang and text[i] not in sudah_tampil:
        print(text[i])
    if text[i] in terlarang:
        total += 1
    sudah_tampil.append(text[i])
    

print(f"Total kata terlarang yang di temukan = {total}")
```

### `L137-Sensor Kata Otomatis.py`

```python
terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

for i in range(len(text)):
    if text[i] in terlarang:
        print("*" * len(text[i]), end=" ")
    else :
        print(text[i], end=" ")
```

### `L138-Hitung Persentase Toxic Chat.py`

```python
terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

total = 0

for i in range(len(text)):

    if text[i] in terlarang:
        print("*" * len(text[i]), end=" ")
        total += 1
    if text[i] not in terlarang:
        print(text[i], end=" ")
    
persentase = (total / len(text)) * 100
persentase = round(persentase, 1)
print()
print("-"*24)
print(f"Total kata : {len(text)}")
print(f"Total kata toxic : {total}")
print(f"Toxic : {persentase} %")
```

### `L139-Ranking Kata Paling Sering di Chat.py`

```python
text = input("Masukkan Text : ")

text = text.split() 

frekuensi_text = []
text_disortir = []

for i in range(len(text)):

    total = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            total += 1
        
    if text[i] not in text_disortir:
        frekuensi_text.append(total)
        text_disortir.append(text[i])

for i in range(len(frekuensi_text)):
    for j in range(len(frekuensi_text) - 1):
        if frekuensi_text[j] < frekuensi_text[j + 1]:
            frekuensi_text[j], frekuensi_text[j + 1] = frekuensi_text[j + 1], frekuensi_text[j]
            text_disortir[j], text_disortir[j + 1] = text_disortir[j + 1], text_disortir[j]

print("-" * 24)
print("Rangking :")

for i in range(len(frekuensi_text)):
    print(f"{text_disortir[i]} = {frekuensi_text[i]}")
```

### `L140-Analisis Log Login User.py`

```python
login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)
print("User aktif :")

for i in range(len(f_login)):
    print(f"{login_sortir[i]} = {f_login[i]} kali login")
```

### `L141-Cari User Paling Aktif.py`

```python
login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)
print("User aktif :")

for i in range(len(f_login)):
    print(f"{login_sortir[i]} = {f_login[i]} kali login")

print()
print("-" * 24)
print("User paling aktif :")

for i in range(len(f_login)):
    if f_login[i] == f_login[0]:
        print(f"{login_sortir[i]} = {f_login[i]} kali login")
```

### `L142-Persentase Aktivitas User.py`

```python
login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)
print("Persentase aktivitas :")

for i in range(len(f_login)):

    persentase = (f_login[i] / len(login)) * 100
    persentase = round(persentase, 1)

    print(f"{login_sortir[i]} = {persentase}%")
```

### `L143-Deteksi User Mencurigakan.py`

```python
login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)
print("Persentase aktivitas :")

flag = False

for i in range(len(f_login)):

    persentase = (f_login[i] / len(login)) * 100
    persentase = round(persentase, 1)

    if persentase > 50 :
        print(f"{login_sortir[i]} = {persentase}%")
        flag = True
    
if flag == False :
    print("Tidak ada user mencurigakan")
```

### `L144-Top 3 User Paling Aktif.py`

```python
login = input("Masukkan Username : ")

login = login.split() 

f_login = []
login_sortir = []

for i in range(len(login)):

    total = 0

    for j in range(len(login)):
        if login[i] == login[j]:
            total += 1
        
    if login[i] not in login_sortir:
        f_login.append(total)
        login_sortir.append(login[i])

for i in range(len(f_login)):
    for j in range(len(f_login) - 1):
        if f_login[j] < f_login[j + 1]:
            f_login[j], f_login[j + 1] = f_login[j + 1], f_login[j]
            login_sortir[j], login_sortir[j + 1] = login_sortir[j + 1], login_sortir[j]

print("-" * 24)

if len(f_login) < 3 :
    total_tampil = len(f_login)
else :
    total_tampil = 3

if len(f_login) > 3:
    for i in range(3, len(f_login)):
        if f_login[i] == f_login[2]:
            total_tampil += 1
        else:
            break

print(f"Top {total_tampil} User :")
for i in range(total_tampil):
    print(f"- {login_sortir[i]} = {f_login[i]}")
```

### `L145-Jam Sibuk Website (peak activity).py`

```python
jam_login = (input("Masukkan Jam login User = "))
jam_login = jam_login.split()

f_jam_login = []
a_jam_login = []

for i in range(len(jam_login)):

    total = 0

    for j in range(len(jam_login)):
        if jam_login[i] == jam_login[j]:
            total += 1
        
    if jam_login[i] not in a_jam_login:
        f_jam_login.append(total)
        a_jam_login.append(jam_login[i])

for i in range(len(f_jam_login)):
    for j in range(len(f_jam_login) - 1):
        if f_jam_login[j] < f_jam_login[j + 1]:
            f_jam_login[j], f_jam_login[j + 1] = f_jam_login[j + 1], f_jam_login[j]
            a_jam_login[j], a_jam_login[j + 1] = a_jam_login[j + 1], a_jam_login[j]

print()
print("Jam tersibuk :")

for i in range(len(f_jam_login)):
    if f_jam_login[i] == f_jam_login[0]:
        print(f"{a_jam_login[i]} = {f_jam_login[i]} login")
```

### `L146-Analisis Penjualan Produk Terlaris.py`

```python
produk = [
    "Mouse",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Webcam",
    "Monitor",
    "Keyboard",
    "Mouse"
]

array_produk = []
array_jumlah = []

for i in range(len(produk)):

    total = 0

    for j in range(len(produk)):
        if produk[i] == produk[j]:
            total += 1

    if produk[i] not in array_produk:
        array_produk.append(produk[i])
        array_jumlah.append(total)

for i in range(len(array_jumlah)):
    for j in range(len(array_jumlah) - 1):
        if array_jumlah[j] < array_jumlah[j + 1]:
            array_jumlah[j], array_jumlah[j + 1] = array_jumlah[j + 1], array_jumlah[j]
            array_produk[j], array_produk[j + 1] = array_produk[j + 1], array_produk[j]
print("===[ Statistik Penjualan ]===")
print()

for i in range(len(array_jumlah)):
    print(f"- {array_produk[i]} : {array_jumlah[i]} kali")

print()
print("=> Produk terlaris :")

for i in range(len(array_jumlah)):
    if array_jumlah[i] >= array_jumlah[0]:
        print(f"- {array_produk[i]}, dengan jumlah penjualan : {array_jumlah[0]} kali")
```

### `L147-Search Engine Produk Sederhana.py`

```python
produk = [
    "Gaming Mouse",
    "Mechanical Keyboard",
    "Gaming Headset",
    "Mouse Pad XXL",
    "Webcam HD",
    "Gaming Chair",
    "Office Keyboard",
    "Wireless Mouse"
]

cari = input("Cari Produk : ")
print()

total_pencarian = 0

for i in range(len(produk)):
    if cari in produk[i]:
        total_pencarian += 1
        print(f"{total_pencarian}. {produk[i]}")

print()
if total_pencarian > 0 :
    print(f"Total produk ditemukan : {total_pencarian}")
else :
    print("Produk tidak ditemukan.")
```

### `L148-Filter Produk Berdasarkan Kategori.py`

```python
produk = [
    ["Gaming Mouse", "gaming"],
    ["Mechanical Keyboard", "gaming"],
    ["Office Keyboard", "office"],
    ["Gaming Chair", "gaming"],
    ["Webcam HD", "aksesoris"],
    ["Mouse Pad XXL", "aksesoris"],
    ["Office Chair", "office"]
]

kategori = input("Cari kategori produk : ")
kategori = kategori.lower()

print("-" * 20)
print(f"Daftar produk kategori {kategori} :")

total = 0

for i in range(len(produk)):
    if kategori == produk[i][1]:
        total += 1
        print(f"{total}. {produk[i][0]}")

print()
if total > 0 :
    print(f"Total produk ditemukan : {total}")
else :
    print("Produk tidak ditemukan!")
```

### `L149-Cari Produk Berdasarkan Nama atau Kategori.py`

```python
produk = [
    ["gaming mouse", "gaming"],
    ["mechanical keyboard", "gaming"],
    ["office keyboard", "office"],
    ["gaming chair", "gaming"],
    ["webcam hd", "aksesoris"],
    ["mouse pad xxl", "aksesoris"],
    ["office chair", "office"]
]

cari = input("Cari : ")
cari = cari.lower()

total = 0

for i in range(len(produk)):
    if cari == produk[i][1]:
        total += 1
        print(f"{total}. {produk[i][0]} ({produk[i][1]})")
    elif cari in produk[i][0]:
        total += 1
        print(f"{total}. {produk[i][0]} ({produk[i][1]})")

if total > 0:
    print(f"Total ditemukan : {total}")
else:
    print("Data tidak di temukan")
```

### `L150-Mini Aplikasi Inventaris Toko.py`

```python
produk = [

    ["gaming mouse", "gaming", 250_000],
    ["mechanical keyboard", "gaming", 850_000],
    ["gaming chair", "gaming", 2_500_000],
    ["gaming headset", "gaming", 450_000],
    ["gamepad wireless", "gaming", 350_000],
    ["cooling pad laptop", "gaming", 180_000],

    ["office keyboard", "office", 300_000],
    ["office chair", "office", 1_500_000],
    ["office mouse", "office", 150_000],
    ["meja kerja minimalis", "office", 1_200_000],
    ["shredder kertas mini", "office", 350_000],
    ["papan jalan jepit", "office", 25_000],

    ["webcam hd", "aksesoris", 450_000],
    ["mouse pad xxl", "aksesoris", 120_000],
    ["usb hub type-c", "aksesoris", 150_000],
    ["kabel hdmi 2m", "aksesoris", 65_000],
    ["pouch organizer", "aksesoris", 80_000],
    ["cleaning kit lcd", "aksesoris", 30_000],

    ["desk lamp led", "belajar", 125_000],
    ["laptop stand", "belajar", 150_000],
    ["buku catatan a5", "belajar", 35_000],
    ["kalkulator ilmiah", "belajar", 220_000],
    ["rak buku meja", "belajar", 90_000],
    ["highlighter set", "belajar", 30_000]
]


flag = True

while flag == True:
    print()
    print("===== INVENTARIS TOKO =====")
    print("1. Lihat semua produk")
    print("2. Cari produk")
    print("3. Filter kategori")
    print("4. Produk termurah")
    print("5. Produk termahal")
    print("6. Keluar")
    print("---------------------------")

    input_user = input(f"=> Pilih Menu : ")

    print()
    print("---------------------------")

    if input_user == "1":
        print("=> Menampilkan semua produk :")
        for i in range(len(produk)):
            print(f"{i + 1}. {produk[i][0]} ({produk[i][1]}) - {produk[i][2]}")
    elif input_user == "2":
        cari = input("Cari produk :")
        cari = cari.lower()
        print()

        total = 0
        for i in range(len(produk)):
            if cari == produk[i][1] or cari in produk[i][0]:
                total += 1
                print(f"{total}. {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
        print()
        if total > 0:
            print(f"=> Sebanyak {total} Produk ditemukan.")
        else:
            print("Produk tidak ditemukan")
    
    elif input_user == "3":
        cari = input("Cari Kategori :")
        cari = cari.lower()
        print()

        total = 0
        for i in range(len(produk)):
            if cari == produk[i][1]:
                total += 1
                print(f"{total}. {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
        print()

        if total > 0:
            print(f"=> Sebanyak {total} Produk dengan kategori {cari} ditemukan.")
        else:
            print(f"Produk dengan kategori {cari} tidak ditemukan")
    
    elif input_user == "4":
        for i in range(len(produk)):
            if i == 0 :
                termurah = produk[i][2]
            elif termurah > produk[i][2]:
                termurah = produk[i][2]
        
        print("Produk termurah :")

        for i in range(len(produk)):
            if termurah == produk[i][2]:
                print(f"- {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
    
    elif input_user == "5":
        for i in range(len(produk)):
            if i == 0 :
                termahal = produk[i][2]
            elif termahal < produk[i][2]:
                termahal = produk[i][2]
        
        print("Produk termahal :")

        for i in range(len(produk)):
            if termahal == produk[i][2]:
                print(f"- {produk[i][0]} ({produk[i][1]}) - Rp.{produk[i][2]}")
    
    elif input_user == "6":
        flag = False
    
    else:
        print("[Error] Masukkan perintah yang valid!")
```

### `L151-Function.py`

```python
def menu():
    print()
    print("===== MENU =====")
    print("1. Halo")
    print("2. Tentang")
    print("3. Keluar")

def opsi_1():
    print()
    print("Halo, selamat datang di aplikasi inventaris!")

def opsi_2():
    print()
    print("Aplikasi ini dibuat untuk belajar Python Function.")

flag = True

while True:
    
    if flag == True :
        menu()

    input_user = input("=> :")

    if input_user == "1":
        opsi_1()
        flag = True
    elif input_user == "2":
        opsi_2()
        flag = True
    elif input_user == "3":
        break
    else:
        flag = False
        print("Perintah tidak valid!")
```

### `L152-Function dengan Parameter.py`

```python
def tampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]}) - Rp.{data[i][2]}.")

produk = [
    ["Gaming Mouse", "gaming", 250000],
    ["Office Keyboard", "office", 300000],
    ["Webcam HD", "aksesoris", 450000]
]

produk_diskon = [
    ["Flashdisk", "storage", 90000],
    ["SSD 1TB", "storage", 1200000]
]

print("Produk utama :")
tampilkan_produk(produk)
print()
print("Produk diskon :")
tampilkan_produk(produk_diskon)
```

### `L153-Function yang Mengembalikan Nilai (return).py`

```python
def hitung_total(data):
    total = 0
    for i in range(len(data)):
        total += data[i][2]
    return total 

def tampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]}) - Rp.{data[i][2]}.")

produk = [
    ["Gaming Mouse", "gaming", 250000],
    ["Office Keyboard", "office", 300000],
    ["Webcam HD", "aksesoris", 450000]
]

tampilkan_produk(produk)
print("-"*18)
hasil = hitung_total(produk)
print(f"Total belanjaan : Rp.{hasil}")
```

### `L154-Sistem Kasir Sederhana.py`

```python
def tampilkan_produk(data):
    print("===== DAFTAR PRODUK =====")
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} - Rp.{data[i][1]}.")
    print()

def hitung_total(data, pilih_produk, jumlah_produk):
    total = 0
    pilih_produk -= 1
    for i in range(jumlah_produk):
        total += data[pilih_produk][1]
    return total

produk = [
    ["Gaming Mouse", 250000],
    ["Office Keyboard", 300000],
    ["Webcam HD", 450000],
    ["Mouse Pad XXL", 120000],
    ["Gaming Chair", 2500000]
]

tampilkan_produk(produk)

pilih_produk = 0
jumlah_produk = 0

while pilih_produk <= 0 or pilih_produk > len(produk):
    pilih_produk = int(input("Pilih Produk : "))

while jumlah_produk <= 0:
    jumlah_produk = int(input("Jumlah Produk : "))

hasil = hitung_total(produk, pilih_produk, jumlah_produk)

print()
print(f"Total belajaan : Rp.{hasil}")
```

### `L155-Mini Sistem Nilai Mahasiswa.py`

```python
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
```

### `L157-Sistem Inventaris dengan penggunaan Parameter yang Tepat.py`

```python
import os

def clear():
    os.system("cls")

array_produk = [

    ["Gaming Mouse", "Gaming", 250000, 10],
    ["Mechanical Keyboard", "Gaming", 850000, 5],
    ["Gaming Chair", "Gaming", 2500000, 2],
    ["Gaming Headset", "Gaming", 600000, 12],
    ["Monitor Gaming 24 Inc", "Gaming", 1800000, 4],
    ["Mousepad RGB", "Gaming", 120000, 20],
    
    ["Wireless Office Mouse", "Office", 180000, 14],
    ["Laptop Stand Aluminium", "Office", 220000, 9],
    ["Desk Mat Felt", "Office", 130000, 0],
    ["Ergonomic Footrest", "Office", 250000, 7],
    ["Office Keyboard", "Office", 300000, 8],
    ["Office Chair", "Office", 1500000, 3],

    ["Microphone Kondensor", "Aksesoris", 550000, 0],
    ["Ring Light LED", "Aksesoris", 175000, 13],
    ["Kabel HDMI 4K", "Aksesoris", 85000, 25],
    ["External SSD 1TB", "Aksesoris", 1250000, 8],
    ["Speaker Bluetooth", "Aksesoris", 350000, 10],
    ["Cooling Pad Laptop", "Aksesoris", 140000, 18],
    ["Webcam HD", "Aksesoris", 450000, 7],
    ["USB Hub", "Aksesoris", 150000, 15]

]

#def tampilkan menu

def d_tampilkan_menu():
    print("===== MENU UTAMA =====")
    print("1. Lihat Semua Produk")
    print("2. Cari")
    print("3. Edit Produk")
    print("4. Keluar")
    print()

def d_menampilkan_sub_menu_cari():
    print("===== MENU CARI =====")
    print("1. Cari produk")
    print("2. Cari Kategori")
    print("3. Cari Harga")
    print("4. Cari Stock")
    print("5. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_sub_menu_harga():
    print("===== MENU HARGA PRODUK =====")
    print("1. Cari Produk dengan harga tertentu")
    print("2. Cari produk dengan harga tertinggi")
    print("3. Cari Produk dengan harga terendah")
    print("4. Total inventaris gudang")
    print("5. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_sub_menu_stock():
    print("===== MENU STOCK PRODUK =====")
    print("1. Cari Produk dengan stock tertentu")
    print("2. Cari Produk dengan stock tertinggi")
    print("3. Cari Produk dengan stock terendah/kosong")
    print("4. Kembali ke Menu utama")
    print()

def d_menampilkan_sub_menu_edit_produk():
    print("===== MENU EDIT PRODUK =====")
    print("1. Edit Nama Produk")
    print("2. Edit Kategori Produk")
    print("3. Edit Harga Produk")
    print("4. Edit Stock Produk")
    print("5. Batalkan Edit Produk")
    print()


#def tampilkan hasil dari fungsi

def d_menampilkan_produk(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} ({data[i][1]})")
        print(f"   -> Harga: Rp.{data[i][2]}.")
        print(f"   -> Stock: {data[i][3]}")
        print()

def d_menampilkan_produk_tanpa_nomor(data):
    for i in range(len(data)):
        print(f"==> {data[i][0]} ({data[i][1]})")
        print(f" -> Harga: Rp.{data[i][2]}.")
        print(f" -> Stock: {data[i][3]}")
        print()

#def cari

def d_validasi_array(data, cari):
    cari += 1
    valid = False
    if cari <= len(data) and cari >= 0:
        valid = True
        return valid
    else :
        return valid
    
def d_cari_array(data, cari):
    array_ketemu = []
    array_ketemu.append(data[cari])
    return array_ketemu

def d_cari_produk(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari in data[i][0]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_kategori(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][1]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_harga(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][2]:
            array_ketemu.append(data[i])
    return array_ketemu

def d_cari_stock(data, cari):
    array_ketemu = []
    for i in range(len(data)):
        if cari == data[i][3]:
            array_ketemu.append(data[i])
    return array_ketemu

#def fungsi max, min, total all inventaris

#harga max/min
def d_cari_harga_max(data):
    for i in range(len(data)):
        if i == 0 :
            harga_max = data[i][2]
        elif harga_max < data[i][2]:
            harga_max = data[i][2]
    return harga_max

def d_cari_harga_min(data):
    for i in range(len(data)):
        if i == 0 :
            harga_min = data[i][2]
        elif harga_min > data[i][2]:
            harga_min = data[i][2]
    return harga_min

#stock max/min
def d_cari_stock_max(data):
    for i in range(len(data)):
        if i == 0 :
            stock_max = data[i][3]
        elif stock_max < data[i][3]:
            stock_max = data[i][3]
    return stock_max

def d_cari_stock_min(data):
    for i in range(len(data)):
        if i == 0 :
            stock_min = data[i][3]
        elif stock_min > data[i][3]:
            stock_min = data[i][3]
    return stock_min

#def edit
def d_edit_nama(data, posisi, nama):
    data[posisi][0] = nama

def d_edit_kategori(data, posisi, kategori):
    data[posisi][1] = kategori

def d_edit_harga(data, posisi, harga):
    data[posisi][2] = harga

def d_edit_stock(data, posisi, stock):
    data[posisi][3] = stock

#total invetaris
def d_total_nilai_gudang(data):
    total = 0
    for i in range(len(data)):
        total += (data[i][2] * data[i][3])
    return total

def d_total_stock_gudang(data):
    total = 0
    for i in range(len(data)):
        total += data[i][3]
    return total

menu_tampil = True

while True:

    #mencegah menu tercetak ketika perintah invalid
    if menu_tampil == True:
        clear()
        d_tampilkan_menu()
    menu_tampil = False

    opsi = input("=> Pilih Menu : ")
    
    #eksekusi perintah
    if opsi == "1":
        clear()
        print("===== SEMUA PRODUK =====")
        print()
        d_menampilkan_produk(array_produk)

        program_selesai = input("Tekan (Enter) untuk kembali ke menu utama ->")
        menu_tampil = True
        clear()
        
    elif opsi == "2":

        clear()
        menu_tampil = True

        while True:

            if menu_tampil == True:
                d_menampilkan_sub_menu_cari()
            menu_tampil = False

            sub_opsi_2 = input("=> Pilih Menu : ")

            if sub_opsi_2 == "1": #cari produk

                clear()
                cari = input("Cari Nama Produk : ")
                print()

                hasil = d_cari_produk(array_produk, cari)
                if len(hasil) == 0 :
                    print(f"Produk dengan nama : {cari}, Tidak ditemukan!")
                else :
                    d_menampilkan_produk_tanpa_nomor(hasil)

                program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                clear()
                menu_tampil = True

            elif sub_opsi_2 == "2": #cari kategori
                
                clear()
                cari = input("Cari Kategori Produk : ")
                print()

                hasil = d_cari_kategori(array_produk, cari)
                if len(hasil) == 0 :
                    print(f"Produk dengan kategori : {cari}, Tidak ditemukan!")
                else :
                    d_menampilkan_produk_tanpa_nomor(hasil)

                program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                clear()
                menu_tampil = True

            elif sub_opsi_2 == "3": #cari harga

                menu_tampil = True
                clear()
                
                while True:  

                    if menu_tampil == True:
                        d_menampilkan_sub_sub_menu_harga()
                    menu_tampil = False

                    sub_sub_opsi_3 = input("=> Pilih Menu : ")

                    if sub_sub_opsi_3 == "1":

                        clear()
                        cari = int(input("Cari Harga Produk : "))
                        print()

                        hasil = d_cari_harga(array_produk, cari)
                        if len(hasil) == 0 :
                            print(f"Produk dengan harga : {cari}, Tidak ditemukan!")
                        else :
                            d_menampilkan_produk_tanpa_nomor(hasil)

                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "2":

                        clear()
                        print("===== PRODUK DENGAN HARGA TERTINGGI =====")
                        
                        hasil = d_cari_harga_max(array_produk)
                        hasil = d_cari_harga(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True
                        
                    elif sub_sub_opsi_3 == "3":

                        clear()
                        print("===== PRODUK DENGAN HARGA TERENDAH/KOSONG =====")
                        
                        hasil = d_cari_harga_min(array_produk)
                        hasil = d_cari_harga(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "4":

                        clear()
                        print("===== TOTAL INVENTARIS GUDANG =====")
                        
                        hasil = d_total_nilai_gudang(array_produk)
                        print(f"-> Harga Total Gudang    : {hasil}")
                        
                        hasil = d_total_stock_gudang(array_produk)
                        print(f"-> Stock Barang Tersedia : {hasil}")

                        print(f"-> Jumlah Jenis Barang   : {len(array_produk)}")

                        hasil = d_cari_stock(array_produk, 0)
                        if len(hasil) != 0:
                            print()
                            print("[Peringatan]")
                            print(f"-> Terdapat {len(hasil)} Produk dengan stock kosong! ")

                        print()
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "5":

                        clear()
                        menu_tampil = True
                        break

                    else:
                        menu_tampil = False
                        print("[Error] Masukkan perintah yang valid!")
                        

            elif sub_opsi_2 == "4": #cari stock
                
                menu_tampil = True
                clear()

                while True:  

                    if menu_tampil == True:
                        d_menampilkan_sub_sub_menu_stock()
                    menu_tampil = False

                    sub_sub_opsi_3 = input("=> Pilih Menu : ")

                    if sub_sub_opsi_3 == "1":

                        clear()
                        cari = int(input("Cari Stock Produk : "))
                        print()

                        hasil = d_cari_stock(array_produk, cari)
                        if len(hasil) == 0 :
                            print(f"Produk dengan stock : {cari}, Tidak ditemukan!")
                        else :
                            d_menampilkan_produk_tanpa_nomor(hasil)

                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "2":

                        clear()
                        print("===== PRODUK DENGAN STOCK BARANG TERTINGGI =====")
                        
                        hasil = d_cari_stock_max(array_produk)
                        hasil = d_cari_stock(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True
                        
                    elif sub_sub_opsi_3 == "3":

                        clear()
                        print("===== PRODUK DENGAN STOCK BARANG TERENDAH/KOSONG =====")
                        
                        hasil = d_cari_stock_min(array_produk)
                        hasil = d_cari_stock(array_produk, hasil)
                        d_menampilkan_produk_tanpa_nomor(hasil)
                        program_selesai = input("Tekan (Enter) untuk kembali ke Sub menu cari ->")
                        clear()
                        menu_tampil = True

                    elif sub_sub_opsi_3 == "4":

                        clear()
                        menu_tampil = True
                        break

                    else :
                        print("[Error] Masukkan perintah yang valid!")

                clear()

            elif sub_opsi_2 == "5": #kembali ke menu utama
                clear()
                menu_tampil = True
                break

            else:
                print("[Error] Masukkan perintah yang valid!")
        
        clear()

    elif opsi == "3":

        menu_tampil = True
        clear()

        while True:
            
            print()
            if menu_tampil == True :
                print("===== EDIT PRODUK =====")
                d_menampilkan_produk(array_produk)
            menu_tampil = False

            
            sub_opsi_3 = int(input("=> Masukkan Nomor Barang, 0 = Kembali Ke Menu Utama : "))
            sub_opsi_3 -= 1
            valid = d_validasi_array(array_produk, sub_opsi_3)

            if sub_opsi_3 == -1:
                break
            elif valid == False:
                print(f"Produk dengan nomor barang {sub_opsi_3 + 1}, Tidak ditemukan... Nomor barang di luar jangkauan data.")
                menu_tampil = False
            else:
                
                hasil = d_cari_array(array_produk, sub_opsi_3)

                clear()
                print("===== EDIT PRODUK =====")
                print(f">>> Nomor Produk : {sub_opsi_3 + 1} <<<")
                print()
                d_menampilkan_produk_tanpa_nomor(hasil)
                print()

                menu_tampil = True

                while True:

                    if menu_tampil == True:
                        d_menampilkan_sub_menu_edit_produk()
                        menu_tampil = False

                    sub_sub_opsi_ada = input("=> Pilih Menu : ")

                    clear()
                    if sub_sub_opsi_ada == "1":
                        isi = input(f"=> Ganti Nama Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : ")
                        d_edit_nama(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "2":
                        isi = input(f"=> Ganti Kategori Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : ")
                        d_edit_kategori(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "3":
                        isi = int(input(f"=> Ganti Harga Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : "))
                        d_edit_harga(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "4":
                        isi = int(input(f"=> Ganti Stock Produk [ {array_produk[sub_opsi_3][0]} ], Menjadi : "))
                        d_edit_stock(array_produk, sub_opsi_3, isi)
                        menu_tampil = True
                    elif sub_sub_opsi_ada == "5":
                        menu_tampil = True
                        break
                    else :
                        print("[Error] Masukkan perintah yang valid!")
                        menu_tampil = False

        menu_tampil = True

    elif opsi == "4":
        
        print("[Info] Keluar dari program...")
        break
    
    else:
        print("[Error] Masukkan perintah yang valid!")
```

### `L158-String Processing Challenge.py`

```python
import os, time

mahasiswa = [
    [" andi saputra ", 85],
    ["BUDI santoso", 72],
    ["citra lestari", 91],
    ["Dinda Pratiwi", 68],
    ["eko nugroho", 77],
    ["FARAH amelia", 95],
    ["galih Wibowo", 80],
    ["Kartika Prasetyo", 75],
    ["oki lestari", 94],
    ["joko wibowo", 61],
    ["JOKO SAPUTRI", 92],
    ["FAJAR PRASETYO", 94],
    [" vino HIDAYAT ", 97],
    ["PUTRI PRASETYO", 87],
    ["SITI SARI", 73],
    ["siti kusuma", 84],
    ["Kartika Pratiwi", 98],
    [" putri UTAMI ", 94],
    ["kartika santoso", 95],
    ["RIAN PRATIWI", 64],
    ["Indah Hidayat", 65],
    [" oki KUSUMA ", 77],
    ["WATI PRATIWI", 83],
    ["Taufik Saputri", 64],
    ["FAJAR RAMADHAN", 70],
    ["Wati Santoso", 100],
    ["Bambang Hidayat", 63],
    ["Oki Utami", 85],
    ["PUTRI WIJAYA", 96],
    [" siti SAPUTRI ", 85],
    ["Wati Lestari", 68],
    [" oki SARI ", 97],
    ["UTAMI PRATIWI", 68],
    ["zaki amelia", 63],
    ["KARTIKA LESTARI", 87],
    [" fajar WIJAYA ", 84],
    ["Fajar Nugroho", 95],
    ["Hadi Kusuma", 81],
    [" kartika KURNIAWAN ", 70],
    ["Wati Prasetyo", 92],
    ["mega saputra", 100],
    ["RIAN SAPUTRA", 69],
    ["taufik ramadhan", 98],
    ["siti amelia", 67],
    ["TAUFIK KURNIAWAN", 63],
    ["oki wijaya", 91],
    ["JOKO LESTARI", 90],
    ["Bambang Ramadhan", 93],
    ["FAJAR WIBOWO", 94],
    [" nugraha KURNIAWAN ", 83]
]

# ===== tampilan menu =====

def d_tampilkan_menu_utama():
    print("===== SISTEM DATA MAHASISWA =====")
    print("1. Lihat Data")
    print("2. Rapikan Semua Nama")
    print("3. Cari Mahasiswa")
    print("4. Ganti Nama Mahasiswa")
    print("5. Statistik Nilai")
    print("6. Keluar")
    print("-" * 23)

def d_tampilkan_menu_edit():
    print("-" * 23)
    print("1. Edit Nama")
    print("2. Edit Nilai")
    print("3. Hapus Mahasiswa Dari Data")
    print("4. Tambahkan Data Baru")
    print("5. Keluar")
    print("-" * 23)

def d_tampilkan_daftar(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]} = {data[i][1]}", flush=True)
        time.sleep(0.02)

def d_tampilkan_daftar_tanpa_nomor(data):
    for i in range(len(data)):
        print(f"- {data[i][0]} = {data[i][1]}", flush=True)
        time.sleep(0.02)

def d_tampilkan_statistik(data):
    total = len(data)

    if total == 0:
        print("[Info] Data mahasiswa masih kosong!")
        return

    jumlah_nilai = 0
    tertinggi = data[0][1]
    terendah = data[0][1]

    for i in range(len(data)):
        nilai = data[i][1]
        jumlah_nilai += nilai

        if nilai > tertinggi:
            tertinggi = nilai

        if nilai < terendah:
            terendah = nilai

    nama_tertinggi = []
    nama_terendah = []

    for i in range(len(data)):
        if data[i][1] == tertinggi:
            nama_tertinggi.append(data[i][0])
        if data[i][1] == terendah:
            nama_terendah.append(data[i][0])

    rata_rata = jumlah_nilai / total
    daftar_tertinggi = ", ".join(nama_tertinggi)
    daftar_terendah = ", ".join(nama_terendah)

    print(f"Jumlah Mahasiswa   : {total}")
    print(f"Rata-rata Nilai    : {rata_rata:.2f}")
    print(f"Nilai Tertinggi    : {tertinggi} ({daftar_tertinggi})")
    print(f"Nilai Terendah     : {terendah} ({daftar_terendah})")

# ===== fungsi logika =====

def d_merapikan_nama(data):
    hasil = []
    for i in range(len(data)):
        nama = data[i][0]
        nama = nama.split()
        nama = " ".join(nama)
        nama = nama.title()
        hasil.append([nama, data[i][1]])
    return hasil

def d_cari_data(data, cari):
    hasil = []

    if cari.isdigit():
        cari = int(cari)
        for i in range(len(data)):
            if cari == data[i][1]:
                hasil.append(data[i])
        return hasil
    else:
        cari = cari.title()
        for i in range(len(data)):
            if cari in data[i][0]:
                hasil.append(data[i])
        return hasil

def d_validasi_index_data(data):
    while True:
        cari = input("=> Masukkan nomor mahasiswa :")

        try:
            cari = int(cari)
            cari -= 1
            if cari < 0:
                print("[Error] Anda harus memasukkan nomor/angka tanpa simbol apapun!")
            elif 0 <= cari < len(data):
                return cari
            else:
                print(f"[Error] Mahasiswa dengan posisi nomor {cari + 1} tidak ditemukan/diluar jangkauan data!")

        except ValueError:
            print("[Error] Anda harus memasukkan sebuah nomor dari posisi nama mahasiswa!")

def d_edit_nama(data, posisi):
    ganti = input(f"=> Mengganti nama : {data[posisi][0]}, Menjadi : ")
    pesan = f"[y/n] Mengganti nama : {data[posisi][0]}, Menjadi : {ganti} :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data[posisi][0] = ganti
        print("[Info] Nama mahasiswa telah diperbarui!")
        time.sleep(1.5)
        return None
    else:
        print("[Info] Membatalkan perubahan nama...")
        time.sleep(1.5)
        return None

def d_edit_nilai(data, posisi):
    while True:
        try:
            ganti = int(input(f"=> Mengganti nilai : {data[posisi][1]}, Menjadi : "))
            break
        except ValueError:
            print("[Error] Anda wajib memasukkan sebuah nilai berupa angka!")

    pesan = f"[y/n] Mengganti nilai : {data[posisi][1]}, Menjadi : {ganti} :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data[posisi][1] = ganti
        print("[Info] Nilai mahasiswa telah diperbarui!")
        time.sleep(1.5)
        return None
    else:
        print("[Info] Membatalkan perubahan nilai...")
        time.sleep(1.5)
        return None

def d_hapus_data(data, posisi):
    pesan = f"[y/n] Menghapus data mahasiswa bernama : {data[posisi][0]}, dari daftar :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        del data[posisi]
        print("[Info] Data mahasiswa telah dihapus!")
        time.sleep(1.5)
        return "hapus"
    else:
        print("[Info] Membatalkan penghapusan data...")
        time.sleep(1.5)
        return None

def d_tambah_data(data, posisi):
    d_clear_terminal()
    print("===== TAMBAH DATA MAHASISWA BARU =====")
    nama_baru = input("=> Masukkan nama mahasiswa baru : ")
    while True:
        try:
            nilai_baru = int(input("=> Masukkan nilai mahasiswa baru : "))
            break
        except ValueError:
            print("[Error] Anda wajib memasukkan sebuah nilai berupa angka!")

    pesan = f"[y/n] Menambahkan mahasiswa baru : {nama_baru} = {nilai_baru}, ke dalam daftar :"
    konfirmasi = d_opsi_sub(opsi_accept, pesan)
    if konfirmasi.lower() == "y":
        data.append([nama_baru, nilai_baru])
        print("[Info] Data mahasiswa baru telah ditambahkan!")
        time.sleep(1.5)
        return "tambah"
    else:
        print("[Info] Membatalkan penambahan data...")
        time.sleep(1.5)
        return None

def d_edit_data(data, opsi, posisi):

    if opsi == "1":
        return d_edit_nama(data, posisi)

    elif opsi == "2":
        return d_edit_nilai(data, posisi)

    elif opsi == "3":
        return d_hapus_data(data, posisi)

    elif opsi == "4":
        return d_tambah_data(data, posisi)

def d_opsi_utama(pilihan, tampilan_menu):
    d_clear_terminal()
    tampilan_menu()
    while True:
        try:
            opsi = int(input("=> :"))
            if opsi in pilihan:
                d_clear_terminal()
                return opsi
            else:
                print("[Error] Masukkan perintah yang valid!")
        except ValueError:
            print("[Error] Masukkan perintah yang valid!")

def d_program_selesai():
    print()
    input("=> Enter untuk kembali :")

def d_clear_terminal():
    os.system("cls")

def d_loading(durasi, pesan, selesai):
    jeda = durasi / 100
    bar_loading = "#"

    print(f"{pesan}")

    for i in range(1, 100 + 1):
        jumlah_bar = i // 10
        print(f"\r{bar_loading * jumlah_bar}[{i}]%", end="", flush=True)
        time.sleep(jeda)

    print(f"\n{selesai}")

def d_opsi_sub(pilihan, pesan):
    print()
    while True:
        opsi = input(f"{pesan}")
        if opsi in pilihan:
            return opsi
        else:
            print("[Error] Masukkan perintah yang valid!")

opsi_utama = [1, 2, 3, 4, 5, 6]
opsi_accept = ["y", "n", "Y", "N"]
opsi_edit = ["1", "2", "3", "4", "5"]

while True:

    opsi = d_opsi_utama(opsi_utama, d_tampilkan_menu_utama)

    if opsi == 1:
        print("===== DAFTAR NILAI MAHASISWA =====")
        d_tampilkan_daftar(mahasiswa)
        d_program_selesai()

    elif opsi == 2:
        print("===== PREVIEW PERUBAHAN NAMA =====")
        hasil = d_merapikan_nama(mahasiswa)
        d_tampilkan_daftar(hasil)
        opsi = d_opsi_sub(opsi_accept, "[y/n] Setujui perubahan/perbaikan nama pada data asli :")
        if opsi.lower() == "y":
            d_loading(5, "[Info] Sedang melakukan perubahan pada data asli...", "[Info] Data asli telah diperbarui!")
            mahasiswa = hasil
            d_program_selesai()
        else:
            print("[Info] Membatalkan perubahan nama...")
            time.sleep(3)

    elif opsi == 3:
        cari = input("Cari nama/nilai :")
        hasil = d_merapikan_nama(mahasiswa)
        hasil = d_cari_data(hasil, cari)
        if len(hasil) == 0:
            print("Nama/Nilai yang anda cari tidak ditemukan!")
            d_program_selesai()
        else:
            d_tampilkan_daftar_tanpa_nomor(hasil)
            d_program_selesai()

    elif opsi == 4:
        print("===== EDIT DATA MAHASISWA =====")
        posisi = d_validasi_index_data(mahasiswa)

        while True:
            d_clear_terminal()
            print("===== EDIT DATA MAHASISWA =====")
            d_tampilkan_daftar_tanpa_nomor([mahasiswa[posisi]])
            print()
            d_tampilkan_menu_edit()
            sub_opsi = d_opsi_sub(opsi_edit, "=> :")

            if sub_opsi == "5":
                break

            status = d_edit_data(mahasiswa, sub_opsi, posisi)
            if status == "hapus" or status == "tambah":
                break

        d_program_selesai()

    elif opsi == 5:
        print("===== STATISTIK NILAI MAHASISWA =====")
        hasil = d_merapikan_nama(mahasiswa)
        d_tampilkan_statistik(hasil)
        d_program_selesai()

    elif opsi == 6:
        d_clear_terminal()
        print("Terima kasih telah menggunakan Sistem Data Mahasiswa!")
        break
```

