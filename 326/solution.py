from collections import Counter

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]
counts = Counter(a)
best = max(counts.values())
target = min(x for x in counts if counts[x] == best)
result = [x for x in a if x != target] + [target] * best

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, result)) + "\n")
