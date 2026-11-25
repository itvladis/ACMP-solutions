from collections import Counter

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
stars = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

diagonals = Counter()
for i in range(n):
    x1, y1 = stars[i]
    for j in range(i + 1, n):
        x2, y2 = stars[j]
        diagonals[(x1 + x2, y1 + y2, (x1 - x2) ** 2 + (y1 - y2) ** 2)] += 1

total = sum(c * (c - 1) // 2 for c in diagonals.values())

with open("output.txt", "w") as f:
    f.write(f"{total}\n")
