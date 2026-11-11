from math import sqrt

with open("input.txt") as f:
    a, b, c = map(int, f.read().split())

if a == 0:
    if b == 0:
        roots = None if c == 0 else []
    else:
        roots = [-c / b]
else:
    d = b * b - 4 * a * c
    if d < 0:
        roots = []
    elif d == 0:
        roots = [-b / (2 * a)]
    else:
        q = sqrt(d)
        roots = sorted([(-b - q) / (2 * a), (-b + q) / (2 * a)])

with open("output.txt", "w") as f:
    if roots is None:
        f.write("-1")
    else:
        f.write(str(len(roots)) + "\n")
        for x in roots:
            f.write("%.6f\n" % (x + 0.0))
