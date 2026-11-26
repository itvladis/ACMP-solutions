data = list(map(int, open("input.txt").read().split()))
n = data[0]
ships = [data[1 + 3 * i:4 + 3 * i] for i in range(n)]

a = min(x for x, _, _ in ships)
b = min(y for _, y, _ in ships)
c = max(x + y - s for x, y, s in ships)
side = max(0, a + b - c)

with open("output.txt", "w") as f:
    f.write(f"{side * side / 2:.3f}\n")
