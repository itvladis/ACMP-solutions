from itertools import product


def can_cover(x, y, a):
    for tl, tr, br, bl in product((0, 1), repeat=4):
        top = x - tl - tr
        bottom = x - bl - br
        left = y - (1 - tl) - (1 - bl)
        right = y - (1 - tr) - (1 - br)
        if all(side % a == 0 for side in (top, bottom, left, right)):
            return True
    return False


with open("input.txt") as f:
    data = list(map(int, f.read().split()))

k = data[0]
result = []
for i in range(k):
    x, y, a = data[1 + 3 * i:4 + 3 * i]
    result.append("1" if can_cover(x, y, a) else "0")

with open("output.txt", "w") as f:
    f.write("".join(result))
