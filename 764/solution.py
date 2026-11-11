from math import gcd

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
counts = {}
for i in range(n):
    x, y = data[1 + 2 * i], data[2 + 2 * i]
    g = gcd(abs(x), abs(y))
    key = (x // g, y // g)
    counts[key] = counts.get(key, 0) + 1

with open("output.txt", "w") as f:
    f.write(str(max(counts.values())))
