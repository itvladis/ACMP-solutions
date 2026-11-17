# Robot K-79

A robot executes a program made of commands `S` (one step forward), `L` (turn 90° left)
and `R` (turn 90° right). Determine how many steps the robot makes until it first enters
a cell it has already visited (the starting cell counts as visited), or report that this
never happens.

**Input** (`input.txt`): a single line of letters `S`, `L`, `R` (1 to 200 commands, at most
50 of them are `S`).
**Output** (`output.txt`): the number of executed `S` commands up to and including the step
onto an already visited cell, or `-1` if that never happens.

Examples: `SSLSLSLSSRSRS` → `5`, `LSSSS` → `-1`.

https://acmp.ru/index.asp?main=task&id_task=235
