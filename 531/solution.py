from math import isqrt

x1, y1, x2, y2, x3, y3, r = map(int, open("input.txt").read().split())

count = 0
for x in range(max(x1, x3 - r), min(x2, x3 + r) + 1):
    dy = isqrt(r * r - (x - x3) ** 2)
    low = max(y1, y3 - dy)
    high = min(y2, y3 + dy)
    if high >= low:
        count += high - low + 1

with open("output.txt", "w") as f:
    f.write(str(count) + "\n")
