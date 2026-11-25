with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
levels = data[1:1 + n]
top = max(levels)
gaps = [top - a for a in levels]

total = gaps[0]
for i in range(1, n):
    if gaps[i] > gaps[i - 1]:
        total += gaps[i] - gaps[i - 1]

with open("output.txt", "w") as f:
    f.write(f"{total}\n")
