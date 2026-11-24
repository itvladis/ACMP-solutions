with open("input.txt") as f:
    n = int(f.read())

pre = 0
twos = fives = 0
m = n
while m % 2 == 0:
    m //= 2
    twos += 1
while m % 5 == 0:
    m //= 5
    fives += 1
pre = max(twos, fives)

period = 1
value = 10 % m
while value != 1 % m:
    value = value * 10 % m
    period += 1

with open("output.txt", "w") as f:
    f.write(f"{pre} {period}")
