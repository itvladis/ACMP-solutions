with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n, k = data[0], data[1]
w, dw, s = data[2], data[3], data[4]
weekly = set(data[5:5 + dw])
dm = data[5 + dw]
holidays = set(data[6 + dw:6 + dw + dm])

total = 0
run = 0
for day in range(1, n + 1):
    weekday = (s - 1 + day - 1) % w + 1
    if weekday in weekly or day in holidays:
        run = 0
    else:
        run += 1
        if run >= k:
            total += 1

with open('output.txt', 'w') as f:
    f.write(str(total))
