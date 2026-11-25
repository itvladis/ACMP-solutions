# Internet olympiads

An online olympiad has a basic and an advanced division. Next time the advanced division
will include every advanced team that solved at least one problem, plus every basic team
that solved at least one problem and either matched the winner's count or solved strictly
more than the team at the median place k/2 (rounded down) among the k basic teams with at
least one solved problem. Teams are ranked by solved problems descending, then by penalty
time ascending. List the teams that will be in the advanced division.

**Input** (`input.txt`): n and m — the number of basic and advanced teams, then n lines and m lines with `id solved penalty`.
**Output** (`output.txt`): the number of teams and their ids in increasing order.

Examples: `6 3 / 1 1 45 / 2 4 678 / 3 5 1000 / 4 5 894 / 5 2 343 / 6 3 555 / 1998 0 0 / 1999 1 34 / 2000 3 366` → `4 / 3 4 1999 2000`.

https://acmp.ru/index.asp?main=task&id_task=635
