# Finding rectangles

K rectangles were laid on an N × M field one on top of another. Each cell of the table holds the number
of the topmost rectangle covering it, or 0. Restore the position of every rectangle (the input is
guaranteed to determine them uniquely). The origin is the lower-left corner of the field.

**Input** (`input.txt`): N, M, K (1 ≤ N, M ≤ 200, 1 ≤ K ≤ 255), then the N × M table.
**Output** (`output.txt`): K lines `X1 Y1 X2 Y2` — the lower-left and upper-right corners of each rectangle.

Examples: `4 5 2` / `0 2 2 2 2` / `0 2 2 2 2` / `1 1 2 2 2` / `1 1 0 0 0` → `0 0 2 2` / `1 1 5 4`.

https://acmp.ru/index.asp?main=task&id_task=193
