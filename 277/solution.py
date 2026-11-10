with open("input.txt") as f:
    a, b, c = map(int, f.read().split())

result = ""
for coef, var in ((a, ""), (b, "x"), (c, "y")):
    if coef == 0:
        continue
    sign = "-" if coef < 0 else ("+" if result else "")
    value = abs(coef)
    body = var if var and value == 1 else str(value) + var
    result += sign + body

with open("output.txt", "w") as f:
    f.write(result or "0")
