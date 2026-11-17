with open('input.txt') as f:
    k, m, n = map(int, f.read().split())

if n <= k:
    answer = 2 * m
else:
    answer = (2 * n + k - 1) // k * m

with open('output.txt', 'w') as f:
    f.write(str(answer))
