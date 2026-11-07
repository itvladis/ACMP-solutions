from math import isqrt

k = int(open("input.txt").read())
best = None
for h in range(1, isqrt(k) + 1):
    w = k // h
    score = w - h + k - h * w
    if best is None or score < best[0]:
        best = (score, h, w)
open("output.txt", "w").write(f"{best[1]} {best[2]}\n")
