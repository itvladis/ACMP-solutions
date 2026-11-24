# Cell frame

From an X × Y rectangle of cells the inner (X - 2) × (Y - 2) rectangle is cut out, leaving a frame
one cell wide. Decide whether the frame can be tiled exactly with A × 1 tiles without overlaps
and without going outside the frame.

**Input** (`input.txt`): K (1 ≤ K ≤ 10), then K lines with X, Y, A (3 ≤ X, Y ≤ 2·10^9, 1 ≤ A ≤ 2·10^9).
**Output** (`output.txt`): one line of K characters, `1` if a tiling exists and `0` otherwise.

Examples: `1` / `3 3 1` → `1`, `2` / `3 3 2` / `3 3 3` → `10`.

https://acmp.ru/index.asp?main=task&id_task=310
