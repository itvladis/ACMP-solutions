w, h, n = map(int, open("input.txt").read().split())
lo, hi = 0, max(w, h) * n
while hi - lo > 1:
    mid = (lo + hi) // 2
    if (mid // w) * (mid // h) >= n:
        hi = mid
    else:
        lo = mid
open("output.txt", "w").write(str(hi))
