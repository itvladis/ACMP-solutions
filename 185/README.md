# Horse racing

N horses with pairwise different speeds take part in a race. For some pairs of horses it
is known which one is faster. Determine whether it follows for sure from this information
that horse K is faster than all the others.

**Input** (`input.txt`): N and K (1 ≤ K ≤ N ≤ 100), then pairs `X Y` meaning horse X is faster than horse Y, terminated by a line with a single `0`.
**Output** (`output.txt`): `Yes` if horse K is guaranteed to win, otherwise `No`.

Examples: `3 1 / 1 2 / 1 3 / 0` → `Yes`, `3 2 / 2 3 / 0` → `No`, `4 2 / 3 1 / 2 3 / 0` → `No`.

https://acmp.ru/index.asp?main=task&id_task=185
