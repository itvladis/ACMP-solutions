with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
dist = [data[1 + i * n:1 + (i + 1) * n] for i in range(n)]

for k in range(n):
    row_k = dist[k]
    for i in range(n):
        row_i = dist[i]
        via = row_i[k]
        for j in range(n):
            if via + row_k[j] < row_i[j]:
                row_i[j] = via + row_k[j]

with open("output.txt", "w") as f:
    f.write("\n".join(" ".join(map(str, row)) for row in dist) + "\n")
