from itertools import combinations
from math import sqrt

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]
best = 0
best_triple = None
for i, j, k in combinations(range(n), 3):
    x, y, z = a[i], a[j], a[k]
    value = (x + y + z) * (-x + y + z) * (x - y + z) * (x + y - z)
    if value > best:
        best = value
        best_triple = (i + 1, j + 1, k + 1)

with open("output.txt", "w") as f:
    if best_triple is None:
        f.write("-1\n")
    else:
        f.write("%.10f\n" % (sqrt(best) / 4))
        f.write(" ".join(map(str, best_triple)) + "\n")
