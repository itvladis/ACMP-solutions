with open("input.txt") as f:
    n = int(f.read())


def distinct_digits(x, base):
    seen = set()
    while x:
        d = x % base
        if d in seen:
            return False
        seen.add(d)
        x //= base
    return True


bases = [str(b) for b in range(2, 37) if distinct_digits(n, b)]

with open("output.txt", "w") as f:
    f.write(" ".join(bases))
