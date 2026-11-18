with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
grid = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]

dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + grid[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

with open("output.txt", "w") as f:
    f.write(str(dp[n - 1][m - 1]))
