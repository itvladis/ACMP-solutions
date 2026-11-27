with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
h = data[1:1 + n]

dp = [0] * n
for i in range(1, n):
    dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 3 * abs(h[i] - h[i - 2]))

with open('output.txt', 'w') as f:
    f.write(str(dp[n - 1]))
