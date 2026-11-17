# Cryptogram

A letter of lowercase words and spaces was encrypted with a substitution cipher (spaces are
kept). Somewhere in it, on a separate line, the key phrase
`the quick brown fox jumps over the lazy dog` was inserted before encryption. Use it to
recover the substitution and decrypt the whole letter; if the key phrase is missing,
decryption is impossible.

**Input** (`input.txt`): N (1 ≤ N ≤ 200), then N lines of the encrypted letter.
**Output** (`output.txt`): the N decrypted lines, or `No solution`.

Examples: the encrypted text whose second line is
`xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj` decrypts to
`now is the time for all good men ...`; without a matching line → `No solution`.

https://acmp.ru/index.asp?main=task&id_task=905
