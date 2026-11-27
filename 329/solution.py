with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = [0] + data[1:1 + n]

dp = [0] * (n + 1)
prev = [0] * (n + 1)
dp[1] = a[1]
for i in range(2, n + 1):
    if dp[i - 1] >= dp[i - 2]:
        dp[i] = dp[i - 1] + a[i]
        prev[i] = i - 1
    else:
        dp[i] = dp[i - 2] + a[i]
        prev[i] = i - 2

path = []
i = n
while i > 0:
    path.append(i)
    i = prev[i]
path.reverse()

with open('output.txt', 'w') as f:
    f.write(str(dp[n]) + '\n' + ' '.join(map(str, path)))
