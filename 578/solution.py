with open('input.txt') as f:
    n = int(f.read())

digits = []
while n > 0:
    r = n % 3
    if r == 0:
        r = 3
    digits.append(str(r))
    n = (n - r) // 3

with open('output.txt', 'w') as f:
    f.write(''.join(reversed(digits)))
