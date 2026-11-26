n = int(open("input.txt").read().split()[0])

side = 1
while side * side < n:
    side += 1

points = []
for k in range(n):
    points.append(f"{(k % side) * 0.02:.6f} {(k // side) * 0.02:.6f}")

with open("output.txt", "w") as f:
    f.write("\n".join(points) + "\n")
