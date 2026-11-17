with open('input.txt') as f:
    x1, y1, x2, y2 = map(int, f.read().split())

dx = abs(x2 - x1)
dy = abs(y2 - y1)
if (dx + dy) % 2:
    answer = 0
elif dx == dy:
    answer = 1
else:
    answer = 2

with open('output.txt', 'w') as f:
    f.write(str(answer))
