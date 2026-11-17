def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open('input.txt') as f:
    n = int(f.read())

while True:
    if is_prime(n):
        break
    if n < 10:
        n = 0
        break
    n = sum(map(int, str(n)))

with open('output.txt', 'w') as f:
    f.write(str(n))
