# Mushroom rain

There are K mushrooms on a meadow, each with cap center (X, Y) and cap radius R. While it
rains (at most T minutes) every cap radius grows by 1 cm per minute. As soon as any two
caps touch, all mushrooms stop growing. Find by how many centimeters the cap radius
increased after the rain.

**Input** (`input.txt`): K (K ≤ 10) and T (T ≤ 100), then K lines with integers X, Y
(0 ≤ X, Y ≤ 100) and R (1 ≤ R ≤ 10).
**Output** (`output.txt`): the radius increase with at least two digits after the decimal
point.

Examples: `2 1`, `0 0 1`, `2 2 1` → `0.41`; `3 2`, `0 0 1`, `5 5 1`, `10 10 1` → `2.00`.

https://acmp.ru/index.asp?main=task&id_task=699
