def parse(cell):
    return ord(cell[0]) - ord("a"), int(cell[1]) - 1


with open("input.txt") as f:
    wk, wq, bk = map(parse, f.read().split())

dx = bk[0] - wq[0]
dy = bk[1] - wq[1]
answer = "NO"
if dx == 0 or dy == 0 or abs(dx) == abs(dy):
    sx = (dx > 0) - (dx < 0)
    sy = (dy > 0) - (dy < 0)
    x, y = wq[0] + sx, wq[1] + sy
    blocked = False
    while (x, y) != bk:
        if (x, y) == wk:
            blocked = True
            break
        x += sx
        y += sy
    if not blocked:
        answer = "YES"

with open("output.txt", "w") as f:
    f.write(answer)
