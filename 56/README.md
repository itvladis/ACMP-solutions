# Jive Journal

A user has a list of friends, and there is also a list of users who have this user in their own
friend lists. Print three alphabetically sorted lists: the user's friends, the mutual friends
(present in both lists), and the users who list this user as a friend but are not mutual friends.

**Input** (`input.txt`): n (0 <= n <= 200) followed by n friend names, then m (0 <= m <= 200) followed by m names of users who have this user as a friend.
**Output** (`output.txt`): three lines `Friends: ...`, `Mutual Friends: ...`, `Also Friend of: ...` with names separated by `, `.

Examples: friends `vasya-pupkin, bill-hates, ivan-ivanov`, friend of `vasya-pupkin, destroyer` →
`Friends: bill-hates, ivan-ivanov, vasya-pupkin`, `Mutual Friends: vasya-pupkin`, `Also Friend of: destroyer`.

https://acmp.ru/index.asp?main=task&id_task=56
