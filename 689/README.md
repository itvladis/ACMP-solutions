# Simplifying phone numbers

A number is easier to remember when it is short and has many repeating digits. The difficulty
of a number is its digit count plus the number of distinct digits in it. For each given number,
choose a base from 2 to 36 (digits 0-9 and A-Z) that minimizes the difficulty; on ties take the
smallest base.

**Input** (`input.txt`): n (1 ≤ n ≤ 100), then n integers from 1 to 999999999, one per line.
**Output** (`output.txt`): n lines, each with the chosen base and the number written in that base, separated by a space.

Examples: `2 / 2 / 65535` → `3 2 / 16 FFFF`.

https://acmp.ru/index.asp?main=task&id_task=689
