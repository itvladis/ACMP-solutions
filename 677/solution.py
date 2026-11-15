from fractions import Fraction

with open("input.txt") as f:
    k, n, m, d = map(int, f.read().split())

rest = 1 - Fraction(1, k) - Fraction(1, n) - Fraction(1, m)
answer = -1
if rest > 0:
    total = d / rest
    if total.denominator == 1:
        x = total.numerator
        if x % k == 0 and x % n == 0 and x % m == 0:
            answer = x

with open("output.txt", "w") as f:
    f.write(str(answer) + "\n")
