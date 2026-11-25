with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
parent = list(range(n + 1))


def find(v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v


seen = set()
found = False
for i in range(m):
    u, v = data[2 + 2 * i], data[3 + 2 * i]
    edge = (min(u, v), max(u, v))
    if edge in seen:
        continue
    seen.add(edge)
    ru, rv = find(u), find(v)
    if ru == rv:
        found = True
        break
    parent[ru] = rv

with open("output.txt", "w") as f:
    f.write("YES\n" if found else "NO\n")
