def is_power(x):
    for k in range(2, 31):
        root = round(x ** (1 / k))
        for r in (root - 1, root, root + 1):
            if r > 1 and r ** k == x:
                return True
    return False


with open('input.txt') as f:
    data = list(map(int, f.read().split()))

numbers = data[1:data[0] + 1]

with open('output.txt', 'w') as f:
    f.write('\n'.join('YES' if is_power(x) else 'NO' for x in numbers))
