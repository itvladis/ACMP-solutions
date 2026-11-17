with open('input.txt') as f:
    n, m = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write(str(pow(2, 2 ** n, m)))
