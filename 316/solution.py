n = int(open("input.txt").read())
s = n
while s + 7 * ((s + 99) // 100) > n:
    s -= 1
open("output.txt", "w").write(f"{s} {7 * ((s + 99) // 100)}")
