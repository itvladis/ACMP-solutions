# Hash function

For a digit string S = s1 s2 … sl the polynomial hash is
p(S, x, m) = (s1·x⁰ + s2·x¹ + … + sl·x^(l-1)) mod m. Given n digit strings and the numbers
m and x, count the pairs i < j whose strings have equal hashes.

**Input** (`input.txt`): n, m, x (1 ≤ n ≤ 30000, 1 ≤ m ≤ 2000, 1 ≤ x ≤ 100), then n non-empty digit strings of length up to 100.
**Output** (`output.txt`): the number of such pairs.

Examples: the first sample with m = 3, x = 8 → `11`; `5 10 100` with strings 1..5 → `0`.

https://acmp.ru/index.asp?main=task&id_task=443
