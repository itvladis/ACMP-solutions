with open("input.txt") as f:
    n = int(f.read())

limit = 2000000
digit_sum = [0] * limit
count = 0
x = 0
length = 1
next_power = 10
while True:
    x += 1
    if x == next_power:
        length += 1
        next_power *= 10
    digit_sum[x] = digit_sum[x // 10] + x % 10
    if digit_sum[x] % length == 0:
        count += 1
        if count == n:
            break

with open("output.txt", "w") as f:
    f.write(str(x))
