with open('input.txt') as f:
    n = int(f.read())

h = [1]
i2 = i3 = i5 = 0
while len(h) < n:
    nxt = min(h[i2] * 2, h[i3] * 3, h[i5] * 5)
    h.append(nxt)
    if nxt == h[i2] * 2:
        i2 += 1
    if nxt == h[i3] * 3:
        i3 += 1
    if nxt == h[i5] * 5:
        i5 += 1

with open('output.txt', 'w') as f:
    f.write(str(h[n - 1]))
