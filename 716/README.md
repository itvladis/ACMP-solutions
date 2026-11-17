# Maxim's triangle

The frequency of a triangle instrument is somewhere between 30 and 4000 Hz. Maxim plays a
sequence of notes on a tuner and, for every note after the first, writes down whether it
is closer to or further from the triangle's sound than the previous note (equal distance
may be recorded either way). Find the interval in which the triangle's frequency can lie.

**Input** (`input.txt`): n (2 ≤ n ≤ 1000), then n lines: the first contains a frequency,
each of the others a frequency followed by `closer` or `further`.
**Output** (`output.txt`): the smallest and largest possible frequency, accurate to 10^-6.

Examples: `440.0`, `220.0 closer`, `300.0 further` → `30.0 260.0`;
`554.0`, `880.0 further`, `440.0 closer`, `622.0 closer` → `531.0 660.0`.

https://acmp.ru/index.asp?main=task&id_task=716
