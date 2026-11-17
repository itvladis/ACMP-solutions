# Fast train

Every day n trains run from Saint Petersburg to Moscow, and for each one the departure and
arrival times are known. The railway between the two cities is 650 km long. Travel time
is at least one minute and at most 24 hours, so an arrival time that is not later than the
departure means the train arrives the next day. Find the fastest train and its average
speed in km/h, rounded to the nearest integer (halves round up).

**Input** (`input.txt`): the number of trains n (1 ≤ n ≤ 100), then n lines, each with the
train name in double quotes, the departure time and the arrival time in `HH:MM` format.
**Output** (`output.txt`): two lines in the form `The fastest train is "<name>".` and
`Its speed is <v> km/h, approximately.`

Examples: `"ER-200" 06:43 10:40`, `"Red Arrow" 23:55 07:55`, `"Express" 23:59 08:00` →
`ER-200` at `165` km/h; `"Slow Train 1" 10:00 09:59`, `"Slow Train 2" 10:00 10:00` →
`Slow Train 1` at `27` km/h.

https://acmp.ru/index.asp?main=task&id_task=89
