with open("input.txt") as f:
    n, k = map(int, f.read().split())

m = k + 1

with open("output.txt", "w") as f:
    f.write(str(((n - 2) * m * m - (n - 4) * m) // 2) + "\n")
