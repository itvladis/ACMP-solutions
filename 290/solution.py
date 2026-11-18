with open("input.txt") as f:
    tokens = f.read().split()

nb, mb = int(tokens[0]), int(tokens[1])
plan = tokens[2:2 + nb]
nd, md = int(tokens[2 + nb]), int(tokens[3 + nb])
desert = tokens[4 + nb:4 + nb + nd]

cells = [(i, j) for i in range(nb) for j in range(mb) if plan[i][j] == "#"]

count = 0
for top in range(nd - nb + 1):
    for left in range(md - mb + 1):
        if all(desert[top + i][left + j] == "#" for i, j in cells):
            count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
