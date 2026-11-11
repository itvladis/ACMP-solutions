with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
rows = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]
row_min = [min(row) for row in rows]
col_max = [max(col) for col in zip(*rows)]

count = 0
for i in range(n):
    for j in range(m):
        if rows[i][j] == row_min[i] and rows[i][j] == col_max[j]:
            count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
