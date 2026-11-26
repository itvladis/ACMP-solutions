with open("input.txt") as f:
    source = list(f.readline().strip())
    target = f.readline().strip()

steps = []
for i in range(len(target)):
    if source[i] != target[i]:
        j = source.index(target[i], i)
        source[i:j + 1] = source[i:j + 1][::-1]
        steps.append(f"{i + 1} {j + 1}")

with open("output.txt", "w") as f:
    f.write("\n".join([str(len(steps))] + steps) + "\n")
