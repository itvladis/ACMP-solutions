with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:1 + n]

best = cur = 1
last = 0
for i in range(1, n):
    d = (a[i] > a[i - 1]) - (a[i] < a[i - 1])
    if d == 0:
        cur = 1
    elif last == -d:
        cur += 1
    else:
        cur = 2
    last = d
    best = max(best, cur)

with open('output.txt', 'w') as f:
    f.write(str(best))
