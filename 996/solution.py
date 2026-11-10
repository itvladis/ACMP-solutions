with open("input.txt") as f:
    n = int(f.read())

seen = bytearray(3 * n + 10)
a = 1
seen[1] = 1
for i in range(2, n + 1):
    a += 3 if seen[i] else 2
    seen[a] = 1

with open("output.txt", "w") as f:
    f.write(str(a))
