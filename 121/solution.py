with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = sorted(data[1:n + 1])

best = [0] * n
best[1] = a[1] - a[0]
if n > 2:
    best[2] = a[2] - a[0]
for i in range(3, n):
    best[i] = min(best[i - 1], best[i - 2]) + a[i] - a[i - 1]

with open("output.txt", "w") as f:
    f.write(str(best[n - 1]))
