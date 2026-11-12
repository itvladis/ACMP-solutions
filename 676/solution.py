n = int(open("input.txt").read())
win = [False] * (n + 1)
for i in range(1, n + 1):
    win[i] = any(i >= m and not win[i - m] for m in (1, 2, 1000))
open("output.txt", "w").write("1" if win[n] else "2")
