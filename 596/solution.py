with open("input.txt") as f:
    lines = f.read().split("\n")

n = int(lines[0])
stations = []
for i in range(n):
    name = lines[1 + 2 * i].strip()
    x, y, r = map(int, lines[2 + 2 * i].split())
    stations.append((name, x, y, r))
xa, ya = map(int, lines[1 + 2 * n].split())

counts = {}
for name, x, y, r in stations:
    counts.setdefault(name, 0)
    if (x - xa) ** 2 + (y - ya) ** 2 <= r * r:
        counts[name] += 1

with open("output.txt", "w") as f:
    f.write(f"{len(counts)}\n")
    for name, count in counts.items():
        f.write(f"{name} {count}\n")
