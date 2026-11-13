DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert(x, base):
    if x == 0:
        return "0"
    out = []
    while x:
        out.append(DIGITS[x % base])
        x //= base
    return "".join(reversed(out))


with open("input.txt") as f:
    d, m, y = map(int, f.read().strip().split("/"))

base = d + 1
with open("output.txt", "w") as f:
    f.write("/".join(convert(v, base) for v in (d, m, y)) + "\n")
