# Language recognition

A word over the alphabet {0, 1, 2} belongs to the language 0^n 1^n 2^n (n >= 1) if it consists
of a block of zeros, then a block of ones, then a block of twos, and all three blocks have the
same length. For each of the given words decide whether it belongs to this language.

**Input** (`input.txt`): the number of words n (n <= 10), then n words, each up to 30000 characters.
**Output** (`output.txt`): for every word, `YES` if it belongs to the language and `NO` otherwise.

Examples: `001122`, `00011122222`, `000111222` → `YES NO YES`; `0000111122220`, `012` → `NO YES`.

https://acmp.ru/index.asp?main=task&id_task=600
