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