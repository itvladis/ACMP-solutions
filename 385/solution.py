from math import sqrt

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
points = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
squares = set()
for i in range(n):
    for j in range(i + 1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        squares.add(dx * dx + dy * dy)

result = sorted(squares)

with open("output.txt", "w") as f:
    f.write(str(len(result)) + "\n")
    for d in result:
        f.write("%.12f\n" % sqrt(d))
