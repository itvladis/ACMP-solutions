from math import acos, hypot, pi, sqrt

data = list(map(float, open("input.txt").read().split()))
xk, yk, xc, yc, r = data[:5]
d = hypot(xk - xc, yk - yc)
if d <= r:
    area = pi * r * r
else:
    tangent = sqrt(d * d - r * r)
    alpha = acos(r / d)
    area = r * tangent + r * r * (pi - alpha)
open("output.txt", "w").write(f"{area:.5f}\n")
