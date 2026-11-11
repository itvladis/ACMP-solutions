def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


with open("input.txt") as f:
    a, b = map(int, f.read().split())

best = -1
best_sum = -1
for n in range(a, b + 1):
    if is_prime(n):
        s = sum(map(int, str(n)))
        if s >= best_sum:
            best_sum = s
            best = n

with open("output.txt", "w") as f:
    f.write(str(best))
