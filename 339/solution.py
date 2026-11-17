def leap(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def day_number(date):
    d, m, y = map(int, date.split('.'))
    months = [31, 29 if leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    p = y - 1
    days = p * 365 + p // 4 - p // 100 + p // 400
    return days + sum(months[:m - 1]) + d


with open('input.txt') as f:
    start, end = f.read().split()

with open('output.txt', 'w') as f:
    f.write(str(day_number(end) - day_number(start) + 1))
