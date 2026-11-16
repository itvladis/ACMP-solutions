with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
t = data[3 * n + 1]
rate = [0] * (max(t, 1001) + 2)
for i in range(n):
    l, r, v = data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]
    rate[l] += v
    rate[r] -= v

volume = 0
cur = 0
for moment in range(t):
    cur += rate[moment]
    volume = max(0, volume + cur)

with open('output.txt', 'w') as f:
    f.write(str(volume))
