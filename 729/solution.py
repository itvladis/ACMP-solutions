data = list(map(int, open("input.txt").read().split()))
n, m = data[0], data[1]
volume = data[2:2 + n]
parent = list(range(n))


def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


for k in range(m):
    a = find(data[2 + n + 2 * k] - 1)
    b = find(data[3 + n + 2 * k] - 1)
    if a != b:
        parent[a] = b

groups = {}
for i in range(n):
    root = find(i)
    gas, total = groups.get(root, (0, 0))
    groups[root] = (max(gas, i + 1), total + volume[i])

with open("output.txt", "w") as f:
    for gas, total in sorted(groups.values()):
        f.write(f"{gas} {total}\n")
