with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, k = data[0], data[1]
faster = [[] for _ in range(n + 1)]
i = 2
while i + 1 < len(data) and data[i] != 0:
    faster[data[i]].append(data[i + 1])
    i += 2

seen = [False] * (n + 1)
seen[k] = True
stack = [k]
while stack:
    v = stack.pop()
    for u in faster[v]:
        if not seen[u]:
            seen[u] = True
            stack.append(u)

with open("output.txt", "w") as f:
    f.write("Yes" if all(seen[1:]) else "No")
