def knight(a, b):
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return {dx, dy} == {1, 2}


with open('input.txt') as f:
    first, second = f.read().replace(',', ' ').split()

a = (ord(first[0]) - ord('a'), int(first[1]) - 1)
b = (ord(second[0]) - ord('a'), int(second[1]) - 1)

if knight(a, b):
    answer = '1'
elif any(knight(a, (x, y)) and knight((x, y), b) for x in range(8) for y in range(8)):
    answer = '2'
else:
    answer = 'NO'

with open('output.txt', 'w') as f:
    f.write(answer)
