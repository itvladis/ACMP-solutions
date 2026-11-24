with open("input.txt") as f:
    n = int(f.read())

with open("output.txt", "w") as f:
    f.write(str(bin(n - 1).count("1") % 3))
