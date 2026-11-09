with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
cells = set()
for i in range(n):
    cells.add((int(data[1 + 2 * i]), int(data[2 + 2 * i])))

shared = 0
for r, c in cells:
    if (r + 1, c) in cells:
        shared += 1
    if (r, c + 1) in cells:
        shared += 1

with open("output.txt", "w") as f:
    f.write(str(4 * n - 2 * shared))
