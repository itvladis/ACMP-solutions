with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
sectors = data[1:1 + n]
a, b, k = data[1 + n:4 + n]

lo = (a - 1) // k
hi = (b - 1) // k

if hi - lo + 1 >= n:
    best = max(sectors)
else:
    best = 0
    for c in range(lo, hi + 1):
        best = max(best, sectors[c % n], sectors[-c % n])

with open('output.txt', 'w') as f:
    f.write(str(best))
