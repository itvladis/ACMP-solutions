# Fifteen puzzle

An N × N sliding puzzle starts in the solved position: numbers 1 to N²-1 row by row and
the empty cell (0) in the bottom right corner. A string of commands `U`, `D`, `L`, `R`
moves the empty cell up, down, left or right. Apply the commands and print the final
board, or `ERROR K` if the K-th move would take the empty cell outside the board.

**Input** (`input.txt`): N (N ≤ 20), then a string of at most 10^4 commands.
**Output** (`output.txt`): the final board, or `ERROR K`.

Examples: `3` / `ULDLURULD` → `8 1 3` / `0 2 5` / `4 7 6`, `2` / `URL` → `ERROR 2`.

https://acmp.ru/index.asp?main=task&id_task=821
