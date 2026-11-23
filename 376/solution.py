from datetime import date


def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


with open("input.txt") as f:
    bd, bm, d, m, y = map(int, f.read().split())

today = date(y, m, d)
year = y
while True:
    if bd == 29 and bm == 2 and not is_leap(year):
        year += 1
        continue
    birthday = date(year, bm, bd)
    if birthday >= today:
        break
    year += 1

with open("output.txt", "w") as f:
    f.write(str((birthday - today).days))
