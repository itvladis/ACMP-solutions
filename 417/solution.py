from datetime import date, timedelta

with open("input.txt") as f:
    k = int(f.read())

day = date(2008, 1, 1) + timedelta(days=k)
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with open("output.txt", "w") as f:
    f.write(f"{names[day.weekday()]}, {day.day:02d}.{day.month:02d}")
