with open("input.txt") as f:
    n = int(f.read())

matches = max(n - 1, 0)
if n > 3:
    matches += 1

with open("output.txt", "w") as f:
    f.write(str(matches) + "\n")
