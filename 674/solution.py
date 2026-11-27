from functools import lru_cache


@lru_cache(maxsize=None)
def ways(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    return ways(n // 2) + ways((n + 1) // 2)


with open('input.txt') as f:
    n = int(f.read())

with open('output.txt', 'w') as f:
    f.write(str(ways(n)))
