with open("input.txt") as f:
    n = int(f.read())

with open("output.txt", "w") as f:
    f.write(str(3 ** (n * (n - 1) // 2)))
