def factorize(x):
    result = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            result[d] = result.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


with open("input.txt") as f:
    n, m = map(int, f.read().split())

a = factorize(n)
b = factorize(m)
answer = sum(abs(a.get(p, 0) - b.get(p, 0)) for p in set(a) | set(b))

with open("output.txt", "w") as f:
    f.write(str(answer) + "\n")
