with open("input.txt") as f:
    n, k = map(int, f.read().split())

with open("output.txt", "w") as f:
    f.write(str(n ** n - (n - 1) * k) + "\n")
