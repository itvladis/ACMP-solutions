with open("input.txt") as f:
    lines = f.read().split("\n")

p, n, k = map(int, lines[0].split())
names = [line.rstrip() for line in lines[1:p + 1]]
ids = lines[p + 1].split()

taken = {}
result = []
for name, team in zip(names, ids):
    if len(result) == n:
        break
    if taken.get(name, 0) < k:
        taken[name] = taken.get(name, 0) + 1
        result.append(f"{name} #{team}")

with open("output.txt", "w") as f:
    f.write("\n".join(result) + "\n")
