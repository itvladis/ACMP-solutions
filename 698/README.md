# Durak

In the card game Durak a card can be beaten by a higher card of the same suit or by any
trump; a trump can be beaten only by a higher trump, and each card of the hand may be used
once. Given a hand of N cards, the trump suit and M attacking cards, decide whether all
attacking cards can be beaten.

**Input** (`input.txt`): N, M (M ≤ 4, M ≤ N ≤ 35) and the trump suit, then the N cards of the hand, then the M attacking cards (rank `6789TJQKA` + suit `SCDH`).
**Output** (`output.txt`): `YES` or `NO`.

Examples: `6 2 C` / `KD KC AD 7C AH 9C` / `6D 6C` → `YES`, `4 1 D` / `9S KC AH 7D` / `8D` → `NO`.

https://acmp.ru/index.asp?main=task&id_task=698
