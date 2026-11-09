digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as f:
    s = f.readline().rstrip("\r\n")

base = 2
for ch in s:
    pos = digits.find(ch)
    if pos == -1:
        base = -1
        break
    base = max(base, pos + 1)

if not s:
    base = -1

with open("output.txt", "w") as f:
    f.write(str(base))
