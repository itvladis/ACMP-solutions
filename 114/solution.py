with open('input.txt') as f:
    n, k = map(int, f.read().split())

nonzero, zero = k - 1, 0
for _ in range(n - 1):
    nonzero, zero = (nonzero + zero) * (k - 1), nonzero

with open('output.txt', 'w') as f:
    f.write(str(nonzero + zero))
