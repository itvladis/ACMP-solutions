from math import acos, hypot, pi, sqrt

with open('input.txt') as f:
    x1, y1, x2, y2, r, s = map(int, f.read().split())

d = hypot(x1 - x2, y1 - y2)
if d >= 2 * r:
    common = 0.0
else:
    common = 2 * r * r * acos(d / (2 * r)) - d / 2 * sqrt(4 * r * r - d * d)

lit = 2 * pi * r * r - common

with open('output.txt', 'w') as f:
    f.write('YES' if lit > s else 'NO')
