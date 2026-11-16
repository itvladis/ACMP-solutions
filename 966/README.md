# Pipes

Water is poured into and drained out of a pool according to a plan. Each record says that
during the time interval from l to r a pipe works with rate v (positive means water flows in,
negative means it flows out); several pipes may work at once. Water cannot flow out of an empty
pool. The pool is empty at the start; find the amount of water in it at time T.

**Input** (`input.txt`): N (1 ≤ N ≤ 1000), then N lines with l, r, v
(0 ≤ l ≤ r ≤ 1000, |v| ≤ 1000), and finally T (0 ≤ T ≤ 10000).
**Output** (`output.txt`): the volume of water at time T.

Examples: plan `0 10 1`, `5 10 1`, `10 15 -1` gives `15` at T = 10 and `10` at T = 100;
plan `0 10 -10`, `5 10 1`, `10 15 1` gives `5` at T = 15.

https://acmp.ru/index.asp?main=task&id_task=966
