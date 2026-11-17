with open('input.txt') as f:
    x = int(f.read())

count = 0
a = 1
while 4 * a <= x:
    b = a
    while a + 3 * b <= x:
        rest = x - a - b
        count += rest // 2 - b + 1
        b += 1
    a += 1

with open('output.txt', 'w') as f:
    f.write(str(count))
