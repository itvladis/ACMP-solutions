with open('input.txt') as f:
    big_r, r, h, b = map(int, f.read().split())

far = (r + h - b) ** 2 + r * r

with open('output.txt', 'w') as f:
    f.write('YES' if far <= big_r * big_r else 'NO')
