# Bowling

A bowling game consists of 10 frames. In each frame the player has up to two throws to
knock down all 10 pins; if all 10 fall on the first throw (a strike) the second throw is
skipped. A frame scores the number of pins knocked down, except for a strike, which scores
10 plus the next two throws, and a spare (all 10 pins in two throws), which scores 10 plus
the next throw. A strike or a spare in the tenth frame gives two or one bonus throws
respectively. Given the list of all throws, compute the total score.

**Input** (`input.txt`): the number of throws, then the number of pins knocked down by each throw.
**Output** (`output.txt`): the total score of the game.

Examples: `12` / `10 10 10 10 10 10 10 10 10 10 10 10` → `300`, `20` / twenty zeros → `0`,
`15` / `10 10 10 8 2 10 3 4 8 2 4 5 10 4 5` → `173`.

https://acmp.ru/index.asp?main=task&id_task=517
