# Only right or down

Each cell of an N×M board holds a non-negative integer — the exact length of the step
that must be made from that cell, either to the right or down. Steps leaving the board
are not allowed. Count the number of different paths from the top-left corner to the
bottom-right one.

**Input** (`input.txt`): N and M (1 ≤ N, M ≤ 70), then N rows of M integers from 0 to 100.
**Output** (`output.txt`): the number of paths (it is less than 2^31).

Examples: `3 4 / 2 1 1 2 / 3 2 1 44 / 3 1 1 0` → `3`.

https://acmp.ru/index.asp?main=task&id_task=165
