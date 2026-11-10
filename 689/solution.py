DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(x, b):
    res = []
    while x:
        res.append(DIGITS[x % b])
        x //= b
    return "".join(reversed(res))


with open("input.txt") as f:
    n = int(f.readline())
    numbers = [int(f.readline()) for _ in range(n)]

lines = []
for x in numbers:
    best = None
    for b in range(2, 37):
        s = to_base(x, b)
        cost = len(s) + len(set(s))
        if best is None or cost < best[0]:
            best = (cost, b, s)
    lines.append(f"{best[1]} {best[2]}")

with open("output.txt", "w") as f:
    f.write("\n".join(lines))
