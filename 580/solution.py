with open("input.txt") as f:
    a, b, c, r = map(int, f.read().split())

p = a + b + c
fits = 4 * r * r * p <= (p - 2 * a) * (p - 2 * b) * (p - 2 * c)

with open("output.txt", "w") as f:
    f.write("YES" if fits else "NO")
