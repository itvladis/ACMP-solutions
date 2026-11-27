with open('input.txt') as f:
    n = int(f.read())

p = 307
lines = ['YES'] + [f'{i} {i * i % p}' for i in range(n)]

with open('output.txt', 'w') as f:
    f.write('\n'.join(lines))
