data = open("input.txt").read().split()
n = int(data[0])
neg = -10 ** 9
grid = [[neg] * (n + 2)]
pos = 1
for _ in range(n):
    grid.append([neg] + list(map(int, data[pos:pos + n])) + [neg])
    pos += n
grid.append([neg] * (n + 2))

best = neg
for i in range(1, n + 1):
    up, row, down = grid[i - 1], grid[i], grid[i + 1]
    for j in range(1, n + 1):
        l, r, u, d = row[j - 1], row[j + 1], up[j], down[j]
        s = max(l + r, u + d, max(l, r) + max(u, d)) + row[j]
        if s > best:
            best = s

with open("output.txt", "w") as f:
    f.write(str(best) + "\n")
