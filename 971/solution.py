x, y = map(int, open("input.txt").read().split())
lim = 10 ** 9
if abs(x) == lim or abs(y) == lim:
    ans = "NO"
else:
    ans = f"YES\n{x + 1} {y}\n{x} {y + 1}\n{x - 1} {y - 1}"
open("output.txt", "w").write(ans)
