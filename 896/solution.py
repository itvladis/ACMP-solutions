from math import gcd

with open("input.txt") as f:
    m, n = map(int, f.read().split())

with open("output.txt", "w") as f:
    f.write(str(m + n - gcd(m, n)))
