from collections import Counter

with open("input.txt") as f:
    tokens = f.read().split()

n, m = int(tokens[0]), int(tokens[1])
grid = Counter("".join(tokens[2:2 + n]))
words = Counter("".join(tokens[2 + n:2 + n + m]))

left = grid - words
with open("output.txt", "w") as f:
    f.write("".join(sorted(left.elements())) + "\n")
