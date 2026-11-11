from fractions import Fraction

with open("input.txt") as f:
    t1, t2, s1, s2, s = map(int, f.read().split())

if s <= s1:
    time = Fraction(s * t1, s1)
elif s1 <= s2:
    time = None
else:
    step = s1 - s2
    k = (s - s1 + step - 1) // step
    time = k * (t1 + t2) + Fraction((s - k * step) * t1, s1)

with open("output.txt", "w") as f:
    if time is None:
        f.write("NO")
    else:
        cents = (time * 100 * 2 + 1) // 2
        f.write("%d.%02d" % (cents // 100, cents % 100))
