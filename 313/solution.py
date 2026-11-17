with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
last = {}
best = 0
for i in range(n):
    route = data[1 + i]
    if route in last:
        gap = i - last[route]
        if gap > best:
            best = gap
    last[route] = i

with open('output.txt', 'w') as f:
    f.write(str(best))
