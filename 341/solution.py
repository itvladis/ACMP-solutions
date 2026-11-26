def next_value(value):
    s = str(value)
    allowed = [d for d in "0123456789" if d not in s]
    low = allowed[0]
    for i in range(len(s) - 1, -1, -1):
        if any(c not in allowed for c in s[:i]):
            continue
        bigger = [d for d in allowed if d > s[i] and (i > 0 or d != "0")]
        if bigger:
            return int(s[:i] + bigger[0] + low * (len(s) - i - 1))
    first = [d for d in allowed if d != "0"][0]
    return int(first + low * len(s))


n = int(open("input.txt").read())

value = 0
for _ in range(n - 1):
    value = next_value(value)

with open("output.txt", "w") as f:
    f.write(str(value) + "\n")
