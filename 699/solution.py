from math import hypot

with open('input.txt') as f:
    data = list(map(int, f.read().split()))

k, t = data[0], data[1]
caps = [data[2 + 3 * i:5 + 3 * i] for i in range(k)]

grow = float(t)
for i in range(k):
    for j in range(i + 1, k):
        x1, y1, r1 = caps[i]
        x2, y2, r2 = caps[j]
        gap = (hypot(x1 - x2, y1 - y2) - r1 - r2) / 2
        grow = min(grow, max(gap, 0.0))

with open('output.txt', 'w') as f:
    f.write(f'{grow:.2f}')
