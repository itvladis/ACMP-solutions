with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
prices = list(map(int, data[1:1 + n]))

total = 0
best = 0
for price in reversed(prices):
    best = max(best, price)
    total += best

with open("output.txt", "w") as f:
    f.write(str(total))
