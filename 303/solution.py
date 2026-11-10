with open("input.txt") as f:
    digits = list(map(int, f.read().strip()))

best = None
for i in range(len(digits)):
    rest = digits[:i] + digits[i + 1:]
    total = sum(d if j % 2 == 0 else -d for j, d in enumerate(rest))
    if best is None or total > best:
        best = total

with open("output.txt", "w") as f:
    f.write(str(best))
