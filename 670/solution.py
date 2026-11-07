n = int(open("input.txt").read())
x = 0
while n:
    x += 1
    s = str(x)
    if len(set(s)) == len(s):
        n -= 1
open("output.txt", "w").write(str(x) + "\n")
