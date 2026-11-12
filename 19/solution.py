def cell(s):
    return ord(s[0]) - ord('A'), int(s[1]) - 1


q, r, k = map(cell, open("input.txt").read().split())
hit = set()
for x in range(8):
    for y in range(8):
        dx, dy = x - q[0], y - q[1]
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):
            hit.add((x, y))
        if x == r[0] or y == r[1]:
            hit.add((x, y))
        if sorted((abs(x - k[0]), abs(y - k[1]))) == [1, 2]:
            hit.add((x, y))
hit -= {q, r, k}
open("output.txt", "w").write(str(len(hit)))
