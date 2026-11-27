with open('input.txt') as f:
    data = f.read().split()

n, k = int(data[0]), int(data[1])
a = data[2:2 + n]

bad = []
for r in range(k):
    idx = list(range(r, n, k))
    ones = [i for i in idx if a[i] == '1']
    zeros = [i for i in idx if a[i] == '0']
    if ones and zeros:
        bad.append((ones, zeros))

if not bad:
    res = 'OK\n0'
elif len(bad) > 1:
    res = 'FAIL'
else:
    ones, zeros = bad[0]
    cand = []
    if len(ones) == 1:
        cand.append(ones[0])
    if len(zeros) == 1:
        cand.append(zeros[0])
    res = 'OK\n' + str(min(cand) + 1) if cand else 'FAIL'

with open('output.txt', 'w') as f:
    f.write(res)
