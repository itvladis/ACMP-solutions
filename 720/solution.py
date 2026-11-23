from math import isqrt

with open("input.txt") as f:
    r_text, l_text = f.read().split()

if "." in r_text:
    whole, frac = r_text.split(".")
else:
    whole, frac = r_text, ""
frac = (frac + "0" * 9)[:9]
r = int(whole or "0") * 10 ** 9 + int(frac)
l = int(l_text)

limit = r * r // (l * l * 10 ** 18)
total = 0
i = 1
while i * i <= limit:
    total += isqrt(limit - i * i)
    i += 1

with open("output.txt", "w") as f:
    f.write(str(4 * total))
