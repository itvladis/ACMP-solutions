with open("input.txt") as f:
    lines = f.read().split()

n, m = int(lines[0]), int(lines[1])
grid = lines[2:2 + n]

count = 0
for i in range(n):
    row = grid[i]
    for j in range(m):
        if row[j] != "#":
            continue
        if i > 0 and grid[i - 1][j] == "#":
            continue
        if j > 0 and row[j - 1] == "#":
            continue
        count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
