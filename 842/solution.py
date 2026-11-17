with open('input.txt') as f:
    n = int(f.read())

for p in (2, 5):
    while n % p == 0:
        n //= p

with open('output.txt', 'w') as f:
    f.write('YES' if n > 1 else 'NO')
