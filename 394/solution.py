from math import gcd

with open("input.txt") as f:
    n, m = map(int, f.read().split())

with open("output.txt", "w") as f:
    f.write(str(n // gcd(n, m)))
