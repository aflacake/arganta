![Logo Arganta](https://raw.githubusercontent.com/aflacake/arganta/main/img/logo.png)

# Arganta 
###### Akurat, Terbukti, Terstruktur.
_Dijadikan latihan, tidak akan langsung “menyelesaikan”_

Arganta dari “Argumen” + “Peranta” (perantara logika): bahasa yang menjembatani logika & komputasi.

> "Setiap program adalah pernyataan matematis yang wajib memiliki bukti berhenti & batas kompleksitas."

Desain bahasa:
- Sadar terhadap P vs NP (contoh: mengizinkan hanya algoritma tertentu)
- Memiliki analisis berhenti terbatas (heuristik)
- Memiliki desain modular untuk menjawab tantangan extensibility

## Masalah dari bahasa pemrograman:
### P vs NP (Teori Kompleksitas)
Apakah semua masalah yang solusinya bisa diverifikasi dengan cepat juga bisa diselesaikan dengan cepat?

Ini adalah salah satu open problem paling terkenal di ilmu komputer. Belum ada yang membuktikan benar atau salah sampai sekarang.

### Halting Problem (Masalah berhenti program)
Diketahui secara matematis bahwa tidak ada algoritma umum yang bisa memastikan apakah sebuah program akan berhenti atau berjalan selamanya untuk semua kasus input.

### Masalah dalam Programming Languages Theory
Bahasa pemrograman terus berkembang, tapi masih ada masalah desain bahasa seperti:

Expression problem: bagaimana menambah tipe dan operasi tanpa mengubah kode yang sudah ada?

## Spesifikasi
### 1. Tujuan Bahasa
   Arganta adalah bahasa pemrograman berbahasa Indonesia yang dirancang untuk:

   - Menjamin program selalu berhenti secara logis (solusi praktis untuk Halting Problem)
   - Menolak atau membatasi algoritma dengan kompleksitas non-polynomial (merespons P vs NP)
   - Mendukung perluasan tanpa merusak kode lama (Expression Problem dalam Programming Language Theory)
   Filosofi: Setiap perintah memiliki bukti berhenti dan batas kompleksitas.

### 2. Struktur Dasar Program
   Sebuah program Arganta terdiri dari:
   - Pernyataan variabel
   - Blok logika (loop, kondisi)
   - Deklarasi bukti berhenti
   - Dokumentasi otomatis pada setiap blok
   - Impor modul untuk perluasan fitur

### 3. Sistem Variabel & Ekspresi Matematika
   - Tipe nilai otomatis (integer, boolean, string versi berikutnya)

   - Deklarasi variabel dengan penugasan eksplisit

   - Hanya operasi matematika dasar yang dijamin polynomial-time:
     - tambah (+)
     - kurang (-)
     - kali (*)
     - bagi (/)
     - modulus (%)
   - Tidak diperbolehkan operasi brute-force berbasis enumerasi pada v0.1

Contoh:
```
nilai = 10
total = nilai * 2
```

### 4. Struktur Kontrol
Struktur dijamin berhenti dengan batasan eksplisit.

a) Kondisi

Format:
```
jika (kondisi):
...perintah
selain itu:
...perintah opsional
```

b) Loop
Hanya loop dengan batas iterasi eksplisit yang diizinkan.

Format:
```
perulangan (variabel dari A sampai B):
...perintah
```

Tidak ada “selama()”, “while()”, atau rekursi tanpa bukti.

### 5. Pembuktian Berhenti Wajib
Setiap blok loop dan seluruh program harus menyertakan pernyataan bukti berhenti.

Format:
```
bukti berhenti: alasan
```

Aturan
- Compiler melakukan analisis statis apakah bukti valid
- Jika loop terdeteksi tidak memiliki batas pasti: error
- Jika algoritma melibatkan eksplorasi eksponensial: error kompleksitas

Contoh:
```
perulangan (i dari 1 sampai 100):
jumlah = jumlah + i
bukti berhenti: batas iterasi pasti 100
```

### 6. Pembatasan Kompleksitas (P vs NP)
Arganta hanya mengizinkan operasi dengan kompleksitas Polynomial Time (P-Time).

Pemeriksaan compiler:
- Larangan pemanggilan algoritma NP-Hard tanpa heuristik disetujui
- Loop bersarang lebih dari dua tingkat menghasilkan peringatan keras
- Struktur lookup harus memiliki batas eksplisit
Jika tidak jelas kompleksitasnya:
Compiler meminta anotasi “kompleksitas terbukti: O(n^k)” dengan k jelas.

### 7. Komentar & Dokumentasi Otomatis
Komentar adalah dokumentasi formal, bukan teks bebas.

Format:
```
jelaskan: "Deskripsi tujuan blok ini"
```

Dimasukkan sebelum setiap perulangan atau fungsi di masa depan.

Compiler menyimpan dokumentasi ke file terpisah otomatis untuk mencegah kode bau dan spaghetti.

### 8. Sistem Modul (Extensibility)
Arganta mendukung ekspansi bahasa tanpa modifikasi inti.

Format:
```
gunakan modul NamaModul
```

Ketentuan:

Modul harus mendeklarasikan kompleksitas semua fungsinya

Modul yang tidak memiliki bukti berhenti akan ditolak

Ini menjawab Expression Problem: dapat ditambah tipe dan operasi tanpa merusak kode lama.

### 9. Struktur Kesalahan / Error Compiler
Error langsung menghentikan kompilasi:
- Tidak ada bukti berhenti pada loop
- Kompleksitas tidak dapat diverifikasi polynomial
- Variabel tak terdefinisi
- Cabang kondisi tidak menutup semua kemungkinan (tidak lengkap)

### 10. Contoh Program Arganta v0.1 (Murni Format Bahasa)
```
jelaskan: "Menghitung jumlah 1 sampai 100"
jumlah = 0

perulangan (i dari 1 sampai 100):
jumlah = jumlah + i
bukti berhenti: batas iterasi pasti 100

hasil jumlah
bukti berhenti: semua perulangan memiliki batas
```

### Garis Besar Implementasi Compiler
Tahap v0.1:
Lexing -> Parsing -> Static Halting Verification -> Static Complexity Estimation -> Execution (di atas Python VM)

STATUS: Draft awal. Siap diperdalam pada versi 0.2

Selesai.
