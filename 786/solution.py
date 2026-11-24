with open("input.txt") as f:
    n = int(f.read())

answer = 0
if n & (n - 1):
    power = 1
    while power * 2 < n:
        power *= 2
    answer = n - power

with open("output.txt", "w") as f:
    f.write(str(answer))
