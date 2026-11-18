# Letter

Vasya wants to print N lines of text on a sheet of width K. Each line has to be centered:
adjust its leading and trailing spaces so that its total length is exactly K, the number of
leading spaces does not exceed the number of trailing ones, and moving one more space from
the end to the start would break that property.

**Input** (`input.txt`): K and N (1 ≤ K ≤ 100, 1 ≤ N ≤ 1000), then N lines in a single-byte encoding, each with at least one non-space character.
**Output** (`output.txt`): the formatted lines, or `Impossible.` if some line does not fit.

Examples (spaces shown as `+`): `20 3 / ++Привет!++ / +Напиши+мне.++ / ++++Пока+=)+` → `++++++Привет!+++++++ / ++++Напиши+мне.+++++ / ++++++Пока+=)+++++++`, `5 1 / Привет.` → `Impossible.`.

https://acmp.ru/index.asp?main=task&id_task=408
