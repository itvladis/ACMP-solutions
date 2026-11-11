with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
priests = data[1:1 + n]
m = data[1 + n]
change = {}
for i in range(m):
    old, new = data[2 + n + 2 * i], data[3 + n + 2 * i]
    change[old] = new

with open("output.txt", "w") as f:
    f.write(" ".join(str(change.get(p, p)) for p in priests))
