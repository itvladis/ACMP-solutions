with open('input.txt') as f:
    program = f.read().strip()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x = y = 0
visited = {(0, 0)}
steps = 0
answer = -1
for c in program:
    if c == 'L':
        d = (d + 3) % 4
    elif c == 'R':
        d = (d + 1) % 4
    elif c == 'S':
        x += dx[d]
        y += dy[d]
        steps += 1
        if (x, y) in visited:
            answer = steps
            break
        visited.add((x, y))

with open('output.txt', 'w') as f:
    f.write(str(answer))
