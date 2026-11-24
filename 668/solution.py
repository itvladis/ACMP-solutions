with open("input.txt") as f:
    heads, tails = map(int, f.read().split())

best = -1
options = range(4) if tails > 0 else range(1)
for extra in options:
    total_tails = tails + extra
    if total_tails % 2:
        continue
    total_heads = heads + total_tails // 2
    if total_heads % 2:
        continue
    hits = extra + total_tails // 2 + total_heads // 2
    if best == -1 or hits < best:
        best = hits

with open("output.txt", "w") as f:
    f.write(str(best))
