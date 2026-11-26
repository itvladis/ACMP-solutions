# DNA transformation

A DNA chain is a string over {A, G, C, T}; one operation reverses a substring from position
L to position R. Given the initial and the target chain (the target is reachable), output
any sequence of at most 4999 reversals that turns the first into the second.

**Input** (`input.txt`): two strings of equal length up to 5000.
**Output** (`output.txt`): the number K of reversals, then K lines `L R`.

Examples: `AGCT` / `GCAT` → `2` / `1 2` / `2 3`, `AGCTA` / `ATCGA` → `1` / `1 5` (any valid sequence is accepted).

https://acmp.ru/index.asp?main=task&id_task=833
