# Cellular network in a big city

There are n base stations, each belonging to an operator and having coordinates and a radius
of reliable connection. For a subscriber at a given point, count for every operator how many
of its stations are within reach (distance not greater than the radius).

**Input** (`input.txt`): n (1 ≤ n ≤ 10000), then for each station a line with the operator name and a line `x y r`, and finally the subscriber's coordinates.
**Output** (`output.txt`): the number of operators, then each operator with its count, in order of first appearance.

Examples: `3 / Megahorn / 0 0 10 / MPS / 1 1 10 / Megahorn / 2 2 10 / 1 1` → `2 / Megahorn 2 / MPS 1`.

https://acmp.ru/index.asp?main=task&id_task=596
