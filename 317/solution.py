with open("input.txt") as f:
    x, y, z, w = map(int, f.read().split())

count = 0
for i in range(w // x + 1):
    left = w - i * x
    for j in range(left // y + 1):
        if (left - j * y) % z == 0:
            count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
