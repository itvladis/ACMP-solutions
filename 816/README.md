# Overlapping sets

Implement a structure that stores n sets of numbers from 1 to m and supports three commands:
`ADD element set`, `LISTSET set` (print the elements of a set) and `LISTSETSOF element`
(print the numbers of all sets containing the element). Lists are printed in increasing order,
an empty list is printed as -1.

**Input** (`input.txt`): m and n (1 ≤ m, n ≤ 100), the number of commands k, then k commands.
**Output** (`output.txt`): the answer to every listing command on its own line.

Examples: `10 10 / 5 / ADD 1 1 / ADD 1 2 / ADD 2 1 / LISTSET 1 / LISTSETSOF 1` → `1 2 / 1 2`.

https://acmp.ru/index.asp?main=task&id_task=816
