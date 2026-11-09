# Smallest numeral system

Numbers in base b (2 ≤ b ≤ 36) are written with the first b symbols of `0..9A..Z`.
Given a string, decide whether it is a valid number in some base not greater than 36,
and if so, output the smallest such base.

**Input** (`input.txt`): one non-empty line of length up to 255 with characters of codes 32..127.
**Output** (`output.txt`): the minimal base, or `-1` if the string is not a number in any such base.

Examples: `123` → `4`, `ABCDEF` → `16`, `AD%AF` → `-1`, `03025` → `6`, `abc` → `-1`.

https://acmp.ru/index.asp?main=task&id_task=315
