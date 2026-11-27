with open('input.txt') as f:
    data = f.read().split()

n, m, x = int(data[0]), int(data[1]), int(data[2])

count = [0] * m
for s in data[3:3 + n]:
    h = 0
    power = 1
    for ch in s:
        h = (h + int(ch) * power) % m
        power = power * x % m
    count[h] += 1

total = sum(c * (c - 1) // 2 for c in count)

with open('output.txt', 'w') as f:
    f.write(str(total))
