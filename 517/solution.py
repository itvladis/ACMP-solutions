with open("input.txt") as f:
    data = list(map(int, f.read().split()))

throws = data[1:data[0] + 1] + [0, 0]
score = 0
i = 0
for frame in range(10):
    if throws[i] == 10:
        score += 10 + throws[i + 1] + throws[i + 2]
        i += 1
    elif throws[i] + throws[i + 1] == 10:
        score += 10 + throws[i + 2]
        i += 2
    else:
        score += throws[i] + throws[i + 1]
        i += 2

with open("output.txt", "w") as f:
    f.write(str(score) + "\n")
