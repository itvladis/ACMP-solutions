lines = open("input.txt").read().split()
a, b = lines[0], lines[1]
m = len(b)
shifts = {b[i:] + b[:i] for i in range(m)}
count = sum(a[i:i + m] in shifts for i in range(len(a) - m + 1))
open("output.txt", "w").write(str(count))
