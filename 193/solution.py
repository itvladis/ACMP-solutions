with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m, k = data[0], data[1], data[2]
grid = data[3:]

boxes = [[n, m, -1, -1] for _ in range(k + 1)]
for r in range(n):
    for c in range(m):
        v = grid[r * m + c]
        if v:
            box = boxes[v]
            box[0] = min(box[0], r)
            box[1] = min(box[1], c)
            box[2] = max(box[2], r)
            box[3] = max(box[3], c)

lines = []
for v in range(1, k + 1):
    top, left, bottom, right = boxes[v]
    lines.append(f"{left} {n - 1 - bottom} {right + 1} {n - top}")

with open("output.txt", "w") as f:
    f.write("\n".join(lines))
