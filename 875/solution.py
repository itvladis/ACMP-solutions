with open('input.txt') as f:
    data = f.read().split()

n, m, k = int(data[0]), int(data[1]), int(data[2])
grid = [[1 if c == '*' else 0 for c in row] for row in data[3:3 + n]]

for _ in range(k):
    horiz = []
    for row in grid:
        horiz.append([row[j - 1] + row[j] + row[(j + 1) % m] for j in range(m)])
    new = []
    for i in range(n):
        up, mid, down = horiz[i - 1], horiz[i], horiz[(i + 1) % n]
        row = grid[i]
        cur = []
        for j in range(m):
            s = up[j] + mid[j] + down[j] - row[j]
            cur.append(1 if s == 3 or (s == 2 and row[j]) else 0)
        new.append(cur)
    grid = new

with open('output.txt', 'w') as f:
    f.write('\n'.join(''.join('*' if c else '.' for c in row) for row in grid))
