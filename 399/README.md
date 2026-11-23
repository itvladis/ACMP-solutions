# Beetle

A beetle walks through a rectangular maze surrounded by walls, starting in the top-left free
cell (2, 2) and heading for the bottom-right free cell. On every move it looks at the four
neighbouring free cells and goes to the one it has visited the fewest times. If several cells
tie and one of them lies in its current direction, it keeps going straight; otherwise it picks by
priority: down, right, up, left. Count the number of moves until it reaches the exit, or report
that the exit is unreachable.

**Input** (`input.txt`): N and M (4 ≤ N, M ≤ 100), then N lines of M characters where `@` is a wall and a space is free.
**Output** (`output.txt`): the number of moves, or -1 if there is no way out.

Examples: the 6×6 maze from the statement → `20`, a closed 4×4 maze → `-1`.

https://acmp.ru/index.asp?main=task&id_task=399
