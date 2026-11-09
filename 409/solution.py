with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
h = list(map(int, data[1:n + 1]))

area = sum(h[i] + h[i + 1] for i in range(n - 1)) / 2
height = area / (n - 1)

with open("output.txt", "w") as f:
    f.write(f"{height:.10f}")
