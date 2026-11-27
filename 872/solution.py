with open('input.txt') as f:
    data = f.read().split()

m = int(data[0])
words = sorted(set(data[1:1 + m]), key=len)

best = [1] * len(words)
for i, w in enumerate(words):
    for j in range(i):
        u = words[j]
        if len(u) < len(w) and w.startswith(u):
            best[i] = max(best[i], best[j] + 1)

with open('output.txt', 'w') as f:
    f.write(str(max(best)))
