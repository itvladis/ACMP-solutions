from collections import deque

with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
shelf = deque()
taken = []
i = 1
for _ in range(n):
    op = data[i]
    i += 1
    if op == '1':
        shelf.appendleft(data[i])
        i += 1
    elif op == '2':
        shelf.append(data[i])
        i += 1
    elif op == '3':
        taken.append(shelf.popleft())
    else:
        taken.append(shelf.pop())

with open('output.txt', 'w') as f:
    f.write(' '.join(taken))
