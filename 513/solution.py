with open("input.txt") as f:
    n = int(f.read())

with open("output.txt", "w") as f:
    f.write(str(2 ** n - n - 1))
