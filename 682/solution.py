with open('input.txt') as f:
    n = int(f.read())

first = 10 ** (n - 1)
last = 10 ** n - 1
count = last - first + 1
total = (first + last) * count // 2

with open('output.txt', 'w') as f:
    f.write(str(total))
