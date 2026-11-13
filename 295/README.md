# Cipher

A message of capital English letters was encrypted with a Caesar shift between 0 and 25: every
letter was replaced by the letter that many positions further in the alphabet (cyclically). One
word that certainly appears in the original message is known. Decrypt the message using the
smallest shift that makes the known word appear, or report that it is impossible.

**Input** (`input.txt`): the encrypted message on the first line and the known word on the second (1 to 40 letters each).
**Output** (`output.txt`): the decrypted message, or `IMPOSSIBLE`.

Examples: `HELLOAMERICA / AMERICA` → `HELLOAMERICA`, `KHOORDPHULFD / HELLOAMERICA` → `HELLOAMERICA`, `KHOORDPHULFD / KHOORDPHULFC` → `IMPOSSIBLE`.

https://acmp.ru/index.asp?main=task&id_task=295
