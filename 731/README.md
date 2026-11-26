# Percentages

A product consists of n ingredients with given amounts; each ingredient is marked as good
(`+`) or bad (`-`) for sales. Compute every ingredient's share in percent and round each
share either down or up so that the rounded values add up to exactly 100. It is not
allowed to have at the same time a bad ingredient rounded up and a good one rounded down.
Any valid answer is accepted.

**Input** (`input.txt`): n (1 ≤ n ≤ 30), then n lines with a sign and an amount from 1 to 1000.
**Output** (`output.txt`): n integers summing to 100, one per line.

Examples: `2` / `- 10` / `+ 5` → `66` / `34`, `3` / `- 10` / `- 10` / `- 10` → `33` / `34` / `33`.

https://acmp.ru/index.asp?main=task&id_task=731
