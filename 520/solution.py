PAIR, BUNDLE, BOX = 1050, 10250, 114000

with open("input.txt") as f:
    n = int(f.read())

best = None
for boxes in (n // 144, n // 144 + 1):
    rest = n - boxes * 144
    for bundles in range(13):
        pairs = max(0, rest - bundles * 12)
        cost = boxes * BOX + bundles * BUNDLE + pairs * PAIR
        if best is None or cost < best[0]:
            best = (cost, boxes, bundles, pairs)

with open("output.txt", "w") as f:
    f.write(f"{best[1]} {best[2]} {best[3]}")
