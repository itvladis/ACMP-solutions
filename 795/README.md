# Wheel of Fortune

A wheel is split into n sectors with numbers, and the pointer initially points at the first
one. Each time the pointer passes a border between sectors the angular speed drops by k; if the
speed is at most k the wheel cannot pass the border and stops. The wheel may be spun in either
direction with an initial speed from a to b. Find the largest number the pointer can stop at.

**Input** (`input.txt`): n (3 ≤ n ≤ 100), the n sector values clockwise (positive, at most 1000), then a b k (1 ≤ a ≤ b ≤ 10⁹, 1 ≤ k ≤ 10⁹).
**Output** (`output.txt`): the maximum possible win.

Examples: `5 / 1 2 3 4 5 / 3 5 2` → `5`, `5 / 1 2 3 4 5 / 15 15 2` → `4`, `5 / 5 4 3 2 1 / 2 5 2` → `5`.

https://acmp.ru/index.asp?main=task&id_task=795
