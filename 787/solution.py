with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]

value = a[:]
for step in range(n - 2, -1, -1):
    first_moves = step % 2 == 0
    pick = max if first_moves else min
    value = [pick(value[r], value[r + 1]) for r in range(step + 1)]

with open('output.txt', 'w') as f:
    f.write(str(value[0]))
