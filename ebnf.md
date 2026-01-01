# EBNF

Catatan:
- Semua keyword Bahasa Indonesia
- Tidak ada rekursi pada v0.1
- Semua perulangan wajib bukti berhenti

## Program
```
program = { pernyataan } ;
```

## Pernyataan
```
pernyataan = penugasan | perulangan | kondisi | bukti | hasil | dokumentasi ;
```

## Variabel dan Ekspresi
```
penugasan = variabel "=" ekspresi ;

variabel = IDENTIFIER ;

ekspresi = operand { operator operand } ;
operand = NUMBER | variabel ;
operator = "+" | "-" | "*" | "/" | "%" ;
```

## Perulangan
```
perulangan =
"perulangan" "(" variabel "dari" angka "sampai" angka ")" ":" blok ;

angka = NUMBER ;
```

## Kondisi
```
kondisi =
"jika" "(" ekspresi ")" ":" blok
[ "selain itu" ":" blok ] ;
```

## Bukti berhenti (mandatory)
```
bukti =
"bukti berhenti:" alasan ;

alasan = TEKS_BEBAS ; // bukan script, hanya anotasi logis
```

## Dokumentasi otomatis
```
dokumentasi =
"jelaskan:" STRING ;
```

## Hasil keluaran
```
hasil =
"hasil" ekspresi ;
```

## Blok
```
blok = INDENT { pernyataan } DEDENT ;
```