with open('input.txt') as f:
    lines = f.read().split()

h, m, s = map(int, lines[0].split(':'))
parts = list(map(int, lines[1].split(':')))
parts = [0] * (3 - len(parts)) + parts

total = h * 3600 + m * 60 + s + parts[0] * 3600 + parts[1] * 60 + parts[2]
days, rest = divmod(total, 86400)
result = f'{rest // 3600:02d}:{rest // 60 % 60:02d}:{rest % 60:02d}'
if days:
    result += f'+{days} days'

with open('output.txt', 'w') as f:
    f.write(result)
