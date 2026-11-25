with open("input.txt") as f:
    n = int(f.read())

steps = [0] * (n + 1)
for i in range(2, n + 1):
    best = steps[i - 1]
    if i % 2 == 0 and steps[i // 2] < best:
        best = steps[i // 2]
    if i % 3 == 0 and steps[i // 3] < best:
        best = steps[i // 3]
    steps[i] = best + 1

with open("output.txt", "w") as f:
    f.write(f"{steps[n]}\n")
