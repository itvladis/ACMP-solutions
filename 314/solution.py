with open('input.txt') as f:
    n, k = map(int, f.read().split())

order = sorted(str(i) for i in range(1, n + 1))

with open('output.txt', 'w') as f:
    f.write(str(order.index(str(k)) + 1))
