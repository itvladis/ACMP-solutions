with open("input.txt") as f:
    n, m, k = map(int, f.read().split())

result = 0
if k >= 3:
    child_buses = (n + k - 3) // (k - 2)
    if 2 * child_buses <= m:
        result = max(child_buses, (n + m + k - 1) // k)

with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
