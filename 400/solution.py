with open('input.txt') as f:
    nums = list(map(int, f.read().split()))

p = sorted(tuple(sorted(nums[i:i + 2])) for i in range(0, 12, 2))

ok = p[0] == p[1] and p[2] == p[3] and p[4] == p[5]
if ok:
    a, b, c = p[0], p[2], p[4]
    ok = a[0] == b[0] and a[1] == c[0] and b[1] == c[1]

with open('output.txt', 'w') as f:
    f.write('POSSIBLE' if ok else 'IMPOSSIBLE')
