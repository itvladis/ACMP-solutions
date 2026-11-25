from math import hypot

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
points = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
k = data[1 + 2 * n]

for _ in range(k):
    points = [((points[i][0] + points[(i + 1) % n][0]) / 2,
               (points[i][1] + points[(i + 1) % n][1]) / 2) for i in range(n)]

length = sum(hypot(points[i][0] - points[(i + 1) % n][0],
                   points[i][1] - points[(i + 1) % n][1]) for i in range(n))

with open("output.txt", "w") as f:
    f.write(f"{length:.10f}\n")
