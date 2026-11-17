with open('input.txt') as f:
    lines = f.read().split('\n')

n = int(lines[0])
lo, hi = 30.0, 4000.0
prev = float(lines[1].split()[0])
for line in lines[2:n + 1]:
    value, word = line.split()
    cur = float(value)
    if cur != prev:
        mid = (cur + prev) / 2
        towards_cur = word == 'closer'
        if (cur > prev) == towards_cur:
            lo = max(lo, mid)
        else:
            hi = min(hi, mid)
    prev = cur

with open('output.txt', 'w') as f:
    f.write(f'{lo} {hi}')
