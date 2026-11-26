# The most extravagant hollow

Circles with given radii are cut out of a 20000 × 20000 board one after another, in a
fixed order; only their centers can be chosen. When a circle is cut, it scores its own base
points plus the final scores of all earlier circles it intersects (one circle lying inside
another also counts). The total is the sum of all final scores. Place the centers so the
total is maximal, keeping the circles on the board and any two centers at least 1 cm apart.

**Input** (`input.txt`): n (1 ≤ n ≤ 1000), then n pairs ri ci (0 < ri, ci ≤ 1000) — radius and base points.
**Output** (`output.txt`): n lines with the coordinates of the centers in meters, (0, 0) being the center of the board.

Examples: `3` / `10 10` / `20 20` / `30 30` → `0 1` / `0 2` / `0 3` (any optimal placement is accepted).

https://acmp.ru/index.asp?main=task&id_task=883
