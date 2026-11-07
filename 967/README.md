# Easy sorting

Let s(x, k) be the sum of digits of x written in base k. For each of the given numbers ai compute
bi = s(ai, k1) · s(ai, k2) and print all bi sorted in non-decreasing order.

**Input** (`input.txt`): n, k1, k2 (1 ≤ n ≤ 1000, 2 ≤ k1, k2 ≤ 10), then n numbers ai (1 ≤ ai ≤ 10^9).
**Output** (`output.txt`): the sorted values bi.

Examples: `9 10 10 / 1 2 3 4 5 6 7 9 8` → `1 4 9 16 25 36 49 64 81`, `10 2 2 / 1 2 4 ... 512` → `1 1 1 1 1 1 1 1 1 1`.

https://acmp.ru/index.asp?main=task&id_task=967
