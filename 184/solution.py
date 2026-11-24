DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def moment(day_month, clock):
    day, month = map(int, day_month.strip(".").split("."))
    hours, minutes = map(int, clock.split(":"))
    return (sum(DAYS[:month - 1]) + day - 1) * 1440 + hours * 60 + minutes


def worked_before(t):
    day, minute = divmod(t, 1440)
    return day * 480 + min(max(minute - 600, 0), 480)


with open("input.txt") as f:
    tokens = f.read().split()

k = int(tokens[0])
moments = sorted(moment(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(k))

total = 0
for i in range(0, k, 2):
    total += worked_before(moments[i + 1] + 1) - worked_before(moments[i])

with open("output.txt", "w") as f:
    f.write(f"{total // 60}:{total % 60:02d}")
