from math import gcd, isqrt

with open('input.txt') as f:
    x = int(f.read())

target = x + 1
answer = (0, 0)
for d in range(isqrt(target), 0, -1):
    if target % d == 0:
        a, b = d + 1, target // d + 1
        if gcd(a, b) == 1:
            answer = (a, b)
            break

with open('output.txt', 'w') as f:
    f.write(f'{answer[0]} {answer[1]}')
