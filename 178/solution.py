from collections import Counter

with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
a = list(map(int, data[1:n + 1]))
counts = Counter(a)
top = max(counts.values())
target = min(x for x, c in counts.items() if c == top)

result = [x for x in a if x != target] + [target] * top

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, result)))
