with open('input.txt') as f:
    m, n = map(int, f.read().split())

t = min(m, n // 2)
extra_boys = m - t
extra_girls = n - 2 * t

if t == 0:
    ans = 'B' * m + 'G' * n
elif extra_boys == 0:
    ans = 'BGG' * t + 'G' * extra_girls
elif extra_girls == 1:
    ans = 'BGG' * t + 'B' * extra_boys + 'G'
else:
    ans = 'BGG' * t + 'B' * extra_boys

with open('output.txt', 'w') as f:
    f.write(ans)
