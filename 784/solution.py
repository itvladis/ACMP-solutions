with open("input.txt") as f:
    data = list(map(int, f.read().split()))

a, b = data[1], data[2]
while a != b:
    if a > b:
        a //= 2
    else:
        b //= 2

with open("output.txt", "w") as f:
    f.write(str(a))
