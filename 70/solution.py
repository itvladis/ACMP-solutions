with open('input.txt') as f:
    lines = f.read().split()

s = lines[0]
k = int(lines[1])

if k > 0:
    times = min(k, 1023 // len(s) + 1)
    ans = (s * times)[:1023]
else:
    k = -k
    if len(s) % k == 0 and s[:len(s) // k] * k == s:
        ans = s[:len(s) // k]
    else:
        ans = 'NO SOLUTION'

with open('output.txt', 'w') as f:
    f.write(ans)
