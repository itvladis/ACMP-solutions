with open("input.txt") as f:
    n = int(f.read())

factors = []
d = 2
while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n //= d
    d += 1 if d == 2 else 2
if n > 1:
    factors.append(n)

with open("output.txt", "w") as f:
    f.write("*".join(map(str, factors)))
