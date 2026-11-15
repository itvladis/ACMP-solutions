with open("input.txt") as f:
    n = int(f.read())

sheets = (n + 3) // 4
total = sheets * 4


def page(p):
    return p if p <= n else 0


lines = []
for i in range(1, sheets + 1):
    sides = [
        (1, page(total - 2 * i + 2), page(2 * i - 1)),
        (2, page(2 * i), page(total - 2 * i + 1)),
    ]
    for side, left, right in sides:
        if left or right:
            lines.append(f"{i} {side} {left} {right}")

with open("output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
