# Timer

Given the current time and an interval, find when the timer rings. The interval is written
as `H:M:S`, `M:S` or `S`, and its parts may exceed their usual limits (for example `100:60`
is 101 minutes). If the signal happens on a later day, append `+<d> days`.

**Input** (`input.txt`): the current time `HH:MM:SS` and the interval on the next line.
**Output** (`output.txt`): the ringing time `HH:MM:SS`, optionally followed by `+<d> days`.

Examples: `01:01:01` / `48:0:0` → `01:01:01+2 days`, `01:01:01` / `58:119` → `02:01:00`,
`23:59:59` / `1` → `00:00:00+1 days`.

https://acmp.ru/index.asp?main=task&id_task=205
