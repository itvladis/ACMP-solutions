# Computational biology

DNA sequences are strings over {A, G, C, T}. A sequence t can evolve from s if s is a
subsequence of t. Given s and t, decide whether t could have evolved from s.

**Input** (`input.txt`): s on the first line and t on the second; the file is at most 256 KB.
**Output** (`output.txt`): `YES` if s is a subsequence of t, otherwise `NO`.

Examples: `GTA / AGCTA` → `YES`, `AAAG / GAAAAAT` → `NO`.

https://acmp.ru/index.asp?main=task&id_task=278
