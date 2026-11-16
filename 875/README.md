# Game of Life

Conway's Game of Life is played on a torus: an n × m grid whose top edge is glued to the bottom
and left edge to the right, so every cell has exactly eight neighbours. A dead cell with exactly
three live neighbours becomes alive, a live cell survives with two or three live neighbours and
dies otherwise. Output the configuration after k generations.

**Input** (`input.txt`): integers n, m, k (4 ≤ n, m ≤ 100, 0 ≤ k ≤ 100), then n lines of m
characters: `.` for a dead cell and `*` for a live one.
**Output** (`output.txt`): the grid after k generations in the same format.

Examples: `4 7 5` with a checkerboard `.*.*.*.` / `*.*.*.*` pattern → an empty grid of dots.

https://acmp.ru/index.asp?main=task&id_task=875
