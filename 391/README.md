# Breaking a hash function

The polynomial hash of a digit string S = s1s2...sL is p(S, x, m) = (s1·x^0 + s2·x^1 + ... + sL·x^(L-1)) mod m.
Given x, m, L and v, find any string of L digits whose hash equals v, or report that none exists.

**Input** (`input.txt`): x (prime, 5 ≤ x ≤ 100), m (a power of two, 1 ≤ m ≤ 256), L (10 ≤ L ≤ 100) and v (0 ≤ v < m).
**Output** (`output.txt`): the required string, or `NO SOLUTION`.

Examples: `5 16 10 9` → `0422207956` (any valid string is accepted).

https://acmp.ru/index.asp?main=task&id_task=391
