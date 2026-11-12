n, k = map(int, open("input.txt").readline().split())
c = sorted(map(int, open("input.txt").read().split()[2:2 + n]), reverse=True)
total = sum((i // k + 1) * x for i, x in enumerate(c))
open("output.txt", "w").write(str(total))
