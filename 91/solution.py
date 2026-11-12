n = int(open("input.txt").read())
a = [2, 3, 4, 7, 13]
taken = set(a)
b = []
cur = 0
for i in range(n):
    if i >= 5:
        a.append(b[i - 1] + b[i - 3])
        taken.add(a[-1])
    cur += 1
    while cur in taken:
        cur += 1
    b.append(cur)
open("output.txt", "w").write(f"{a[n - 1]}\n{b[n - 1]}")
