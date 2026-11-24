with open("input.txt") as f:
    a, b = map(int, f.read().split())

with open("output.txt", "w") as f:
    f.write(str(a + b))
