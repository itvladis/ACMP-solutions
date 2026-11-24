# Contraction operator

An operator maps each given point x of the plane to a point Ax. It is contracting with coefficient q
if for every point the distance of Ax from the origin is at most q times the distance of x. Check
whether the given operator is contracting with the given q.

**Input** (`input.txt`): n (1 ≤ n ≤ 100) and q (0 ≤ q < 1, at most 3 decimal places), then n lines with four integers:
the coordinates of a point and of its image.
**Output** (`output.txt`): `Yes` or `No`.

Examples: `2 0.5` / `0 10 5 0` / `10 0 0 1` → `Yes`, the same points with `q = 0.1` → `No`.

https://acmp.ru/index.asp?main=task&id_task=37
