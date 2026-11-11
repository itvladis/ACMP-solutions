from math import sin, tan, pi

with open("input.txt") as f:
    n, a = map(int, f.read().split())

angle = pi / n
outer = a / (2 * sin(angle))
inner = a / (2 * tan(angle))

with open("output.txt", "w") as f:
    f.write("YES" if outer - inner < 1 else "NO")
