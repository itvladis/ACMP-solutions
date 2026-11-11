with open("input.txt") as f:
    l, r = map(int, f.read().split())

count = 0
for n in range(l, r + 1):
    product = 1
    for ch in str(n):
        product *= int(ch)
        if product == 0:
            break
    if product and n % product == 0:
        count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
