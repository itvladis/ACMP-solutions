with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n, m, k = data[0], data[1], data[2]
viruses = [(data[3 + 2 * i], data[4 + 2 * i]) for i in range(k)]

best = 0
for row in range(1, n + 1):
    shifted = [(x, abs(row - y)) for y, x in viruses]
    candidates = {1, m}
    for x, d in shifted:
        candidates.add(x)
    for xa, da in shifted:
        for xb, db in shifted:
            mid = (xa + xb + db - da) // 2
            candidates.add(mid)
            candidates.add(mid + 1)
    for col in candidates:
        if 1 <= col <= m:
            dist = min(d + abs(col - x) for x, d in shifted)
            if dist > best:
                best = dist

with open('output.txt', 'w') as f:
    f.write(str(best))
