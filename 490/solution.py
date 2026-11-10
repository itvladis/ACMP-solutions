MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def day_number(date):
    d, m, y = map(int, date.split("."))
    return (y - 93) * 365 + sum(MONTHS[:m - 1]) + d


with open("input.txt") as f:
    petya, vasya = f.read().split()

with open("output.txt", "w") as f:
    f.write(str(day_number(vasya) - day_number(petya)))
