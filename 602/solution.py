with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
xs = sorted(data[1:n + 1])

best = 0
for i in range(1, n - 1):
    if xs[i + 1] - xs[i] < xs[best + 1] - xs[best]:
        best = i

with open("output.txt", "w") as f:
    f.write(f"{xs[best]} {xs[best + 1]}")
