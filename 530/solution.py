with open("input.txt") as f:
    tokens = f.read().split()

w, h = int(tokens[0]), int(tokens[1])
first = tokens[2:2 + h]
second = tokens[2 + h:2 + 2 * h]
op = "".join(tokens[2 + 2 * h:])

result = []
for a, b in zip(first, second):
    result.append("".join(op[int(x) * 2 + int(y)] for x, y in zip(a, b)))

with open("output.txt", "w") as f:
    f.write("\n".join(result))
