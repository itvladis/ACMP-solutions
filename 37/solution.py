from fractions import Fraction

with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
q = Fraction(data[1])
values = list(map(int, data[2:2 + 4 * n]))

ok = True
for i in range(n):
    x1, y1, x2, y2 = values[4 * i:4 * i + 4]
    if x2 * x2 + y2 * y2 > q * q * (x1 * x1 + y1 * y1):
        ok = False
        break

with open("output.txt", "w") as f:
    f.write("Yes" if ok else "No")
