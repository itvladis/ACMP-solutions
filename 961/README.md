# Everything that moves

An N×M field is shown at two consecutive moments of time T and T+1. Every object is a distinct
English letter occupying one cell, and the set of objects is the same at both moments. An object
moves if its cell changed. Find all moving objects.

**Input** (`input.txt`): N and M (1 ≤ N, M ≤ 100), then N rows of the field at time T, an empty line, and N rows at time T+1 (`.` is an empty cell).
**Output** (`output.txt`): the number of moving objects and, on the next line, their letters: lowercase first, then uppercase, each group in alphabetical order.

Examples: `2 2` / `.A ..` / `A. ..` → `1` / `A`.

https://acmp.ru/index.asp?main=task&id_task=961
