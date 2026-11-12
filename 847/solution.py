a, b = open("input.txt").read().split()
ok = sorted(a) == sorted(b) and all(x != y for x, y in zip(a, b))
open("output.txt", "w").write("YES" if ok else "NO")
