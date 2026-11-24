with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
agents = sorted((data[1 + 2 * i], data[2 + 2 * i]) for i in range(n))
risk = [r for _, r in agents]

INF = float("inf")
best = [INF] * n
best[1] = risk[1]
for i in range(2, n):
    best[i] = risk[i] + min(best[i - 1], best[i - 2])

with open("output.txt", "w") as f:
    f.write(str(best[n - 1]))
