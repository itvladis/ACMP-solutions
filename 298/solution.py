from math import gcd

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
rays = set()
at_origin = False
for i in range(n):
    x, y = data[1 + 2 * i], data[2 + 2 * i]
    if x == 0 and y == 0:
        at_origin = True
        continue
    g = gcd(abs(x), abs(y))
    rays.add((x // g, y // g))

answer = len(rays)
if answer == 0 and at_origin:
    answer = 1

with open("output.txt", "w") as f:
    f.write(str(answer))
