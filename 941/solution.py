with open('input.txt') as f:
    a, b = f.read().split()

with open('output.txt', 'w') as f:
    f.write(str(int(a, 3) + int(b, 3)))
