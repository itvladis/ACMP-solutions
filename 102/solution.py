def cross(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


with open("input.txt") as f:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, f.read().split()[:8])

d1 = cross(x1, y1, x2, y2, x4, y4)
d2 = cross(x2, y2, x3, y3, x4, y4)
d3 = cross(x3, y3, x1, y1, x4, y4)

has_neg = d1 < 0 or d2 < 0 or d3 < 0
has_pos = d1 > 0 or d2 > 0 or d3 > 0

with open("output.txt", "w") as f:
    f.write("Out" if has_neg and has_pos else "In")
