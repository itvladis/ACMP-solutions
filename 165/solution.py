with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
grid = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]

ways = [[0] * m for _ in range(n)]
ways[0][0] = 1
for i in range(n):
    for j in range(m):
        step = grid[i][j]
        if ways[i][j] == 0 or step == 0 or (i == n - 1 and j == m - 1):
            continue
        if j + step < m:
            ways[i][j + step] += ways[i][j]
        if i + step < n:
            ways[i + step][j] += ways[i][j]

with open("output.txt", "w") as f:
    f.write(str(ways[n - 1][m - 1]))
