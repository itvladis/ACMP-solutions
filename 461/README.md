# Elections

All voters are split into K groups. A group votes "for" if strictly more than half of its
members vote "for", and the decision passes if strictly more than half of the groups vote "for".
Given the group sizes, find the minimum number of supporters a party needs to pass any decision.

**Input** (`input.txt`): K (K < 1001) on the first line, then K positive group sizes (total population at most 30000).
**Output** (`output.txt`): the minimum number of supporters.

Examples: `3 / 5 5 7` → `6`, `5 / 4 2 1 3 7` → `5`.

https://acmp.ru/index.asp?main=task&id_task=461
