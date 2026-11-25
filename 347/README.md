# Poker

Five integers are given. Classify them like a poker hand, checking the rules in this order:
all five equal → `Impossible`; four equal → `Four of a Kind`; three equal plus a pair →
`Full House`; five consecutive values → `Straight`; three equal → `Three of a Kind`;
two different pairs → `Two Pairs`; one pair → `One Pair`; otherwise `Nothing`.

**Input** (`input.txt`): five integers from 1 to 13.
**Output** (`output.txt`): the name of the combination.

Examples: `1 3 9 3 2` → `One Pair`, `1 5 5 4 4` → `Two Pairs`, `1 5 2 4 3` → `Straight`, `10 11 12 13 1` → `Nothing`.

https://acmp.ru/index.asp?main=task&id_task=347
