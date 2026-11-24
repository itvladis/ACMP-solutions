with open("input.txt") as f:
    m, n, x, y = map(int, f.read().split())

lines = ["0"]
if (m, n) != (x, y) and (m + n) % 2 == (x + y) % 2:
    if abs(m - x) == abs(n - y):
        lines = ["1"]
    else:
        for i in range(1, 9):
            for j in range(1, 9):
                if abs(i - m) == abs(j - n) and abs(i - x) == abs(j - y):
                    lines = ["2", f"{i} {j}"]
                    break
            if len(lines) == 2:
                break

with open("output.txt", "w") as f:
    f.write("\n".join(lines))
