# Archery championship

The scores of all archers are known in the order they shot, but the names are lost. The father's
score ends with digit 5, at least one of the winners (participants with the maximum score) shot
before him, and the participant who shot right after him scored strictly less. A participant takes
place k if exactly k - 1 participants scored strictly more. Find the best place the father could
have taken.

**Input** (`input.txt`): n (3 ≤ n ≤ 10^5), then n positive scores not exceeding 1000.
**Output** (`output.txt`): the best possible place, or 0 if no participant fits the description.

Examples: `7` / `10 20 15 10 30 5 1` → `6`, `3` / `15 15 10` → `1`, `3` / `10 15 20` → `0`.

https://acmp.ru/index.asp?main=task&id_task=799
