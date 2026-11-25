DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as f:
    a = f.readline().strip()
    b = int(f.readline())

values = [DIGITS.index(c) for c in a]
answer = 0
for base in range(max(max(values) + 1, 2), 37):
    number = 0
    for v in values:
        number = number * base + v
        if number > b:
            break
    if number == b:
        answer = base
        break

with open("output.txt", "w") as f:
    f.write(f"{answer}\n")
