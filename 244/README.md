# Tickets

A ticket stores N bits written so that bits at distance K from each other must be equal.
While reading, at most one bit may be flipped, and such a ticket is still genuine. Decide
whether the ticket is genuine and, if a bit was misread, report its position.

**Input** (`input.txt`): N and K (1 ≤ K ≤ 1000, K ≤ N ≤ 50000), then N bits (0 or 1).
**Output** (`output.txt`): `OK` and on the next line `0` (no errors) or the smallest possible position of the misread bit; or `FAIL` if the ticket is fake.

Examples: `6 2 / 1 0 1 0 1 0` → `OK 0`, `8 5 / 0 1 1 0 1 0 0 1` → `OK 2`, `6 2 / 1 1 1 0 0 0` → `FAIL`.

https://acmp.ru/index.asp?main=task&id_task=244
