with open("input.txt") as f:
    k = int(f.readline())
    groups = sorted(map(int, f.read().split()))

need = k // 2 + 1
answer = sum(g // 2 + 1 for g in groups[:need])

with open("output.txt", "w") as f:
    f.write(str(answer))
