with open('input.txt') as f:
    data = f.read().split()

n = int(data[0])
houses = data[1:n + 1]

with open('output.txt', 'w') as f:
    f.write(houses[n // 2])
