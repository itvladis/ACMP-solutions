with open("input.txt") as f:
    x, y = map(int, f.read().split())

p, q = 1, 0
r, s = 0, 1
for _ in range(x - 2):
    p, q, r, s = r, s, p + r, q + s

answer = None
for a in range(1, y + 1):
    rest = y - r * a
    if rest < 0:
        break
    if rest % s == 0 and rest // s < a:
        answer = (a, rest // s)
        break

with open("output.txt", "w") as f:
    f.write(f"{answer[0]} {answer[1]}\n")
