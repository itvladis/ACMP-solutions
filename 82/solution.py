with open("input.txt") as f:
    data = f.read().split()

n, m = int(data[0]), int(data[1])
first = set(data[2:2 + n])
second = set(data[2 + n:2 + n + m])
common = sorted(int(x) for x in first & second)

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, common)))
