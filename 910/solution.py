n, m = map(int, open("input.txt").read().split())
term = 1
total = 0
for k in range(1, n + 1):
    term = term * k * 2 % m
    total = (total + term) % m
open("output.txt", "w").write(str(total))
