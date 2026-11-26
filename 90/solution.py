data = list(map(int, open("input.txt").read().split()))
px, py, k = data[0], data[1], data[2]


def cross(ax, ay, bx, by):
    return (bx - ax) * (py - ay) - (by - ay) * (px - ax)


inside = []
for i in range(k):
    x1, y1, x2, y2, x3, y3 = data[3 + 6 * i:9 + 6 * i]
    c = [cross(x1, y1, x2, y2), cross(x2, y2, x3, y3), cross(x3, y3, x1, y1)]
    if all(v > 0 for v in c) or all(v < 0 for v in c):
        inside.append(i + 1)

with open("output.txt", "w") as f:
    f.write(str(len(inside)) + "\n" + " ".join(map(str, inside)) + "\n")
