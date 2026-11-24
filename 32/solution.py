def largest(digits):
    return int("".join(sorted(digits, reverse=True)))


def smallest(digits):
    digits = sorted(digits)
    for i, d in enumerate(digits):
        if d != "0":
            digits.insert(0, digits.pop(i))
            break
    return int("".join(digits))


with open("input.txt") as f:
    a, b = f.read().split()

if a.startswith("-"):
    best_a = -smallest(a[1:])
else:
    best_a = largest(a)

if b.startswith("-"):
    best_b = -largest(b[1:])
else:
    best_b = smallest(b)

with open("output.txt", "w") as f:
    f.write(str(best_a - best_b))
