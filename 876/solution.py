from math import hypot

with open("input.txt") as f:
    a, b, r = map(float, f.read().split())

length = hypot(a, b)
x = r * a / length
y = r * b / length

with open("output.txt", "w") as f:
    f.write("%.12f\n%.12f %.12f\n" % (r * length, x, y))
