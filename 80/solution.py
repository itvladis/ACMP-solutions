import re

with open('input.txt') as f:
    s = f.readline().rstrip('\r\n')

m = re.fullmatch(r'(-?\d+)([-+*/])(-?\d+)=(-?\d+)', s)
if not m:
    res = 'ERROR'
else:
    a, op, b, c = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4))
    if op == '+':
        ok = a + b == c
    elif op == '-':
        ok = a - b == c
    elif op == '*':
        ok = a * b == c
    else:
        ok = b != 0 and b * c == a
    res = 'YES' if ok else 'NO'

with open('output.txt', 'w') as f:
    f.write(res)
