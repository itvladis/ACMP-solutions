# Chess workshop

An N×M board was painted badly: some adjacent cells (sharing a side) have the same color.
Repaint the minimum number of cells so that every two adjacent cells differ in color, and
list the cells to repaint.

**Input** (`input.txt`): N and M (1 ≤ N, M ≤ 100), then N rows of M characters `W` or `B`.
**Output** (`output.txt`): the minimum number k, then k lines with the row and column of
each cell to repaint.

Examples: a 4×4 board of `B` → `8` cells (1 1, 1 3, 2 2, 2 4, 3 1, 3 3, 4 2, 4 4);
`WBW` / `BWB` / `WBW` → `0`.

https://acmp.ru/index.asp?main=task&id_task=811
