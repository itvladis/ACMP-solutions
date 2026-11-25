# Dual polyline

The dual of a closed polyline is the closed polyline whose vertices are the midpoints of
the original segments. The dual of order 0 is the polyline itself, and the dual of order K
is the dual of the order K-1 dual. Given a closed polyline and K, find the length of its
dual of order K.

**Input** (`input.txt`): N (3 ≤ N ≤ 100), then N vertices `x y`, then K (0 ≤ K ≤ 10).
**Output** (`output.txt`): the length with precision of at least 10^-4.

Examples: unit square with K = 0 → `4`, the same square with K = 1 → `2.8284271247`.

https://acmp.ru/index.asp?main=task&id_task=495
