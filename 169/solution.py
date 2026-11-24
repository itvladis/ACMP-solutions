with open("input.txt") as f:
    n, k = map(int, f.read().split())

size = n + k + 2
ways = [0] * size
ways[n] = 1
for _ in range(k):
    nxt = [0] * size
    for pos in range(1, size - 1):
        if ways[pos]:
            nxt[pos - 1] += ways[pos]
            nxt[pos + 1] += ways[pos]
    ways = nxt
    finished = ways[0]
    ways[0] = 0

with open("output.txt", "w") as f:
    f.write(str(finished))
