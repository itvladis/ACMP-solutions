data = list(map(int, open("input.txt").read().split()))
n = data[0]
ax, ay, bx, by = data[1:5]
dx, dy = bx - ax, by - ay
length2 = dx * dx + dy * dy

hit = []
for i in range(n):
    x, y, r = data[5 + 3 * i:8 + 3 * i]
    cross = dx * (y - ay) - dy * (x - ax)
    if cross * cross <= r * r * length2:
        hit.append(i + 1)

with open("output.txt", "w") as f:
    f.write(str(len(hit)) + "\n" + " ".join(map(str, hit)) + "\n")
