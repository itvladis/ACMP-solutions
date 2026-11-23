from itertools import combinations_with_replacement
from math import factorial, prod

with open("input.txt") as f:
    n = int(f.read())

if n == 1:
    count, smallest = 10, 0
else:
    count = 0
    smallest = None
    for digits in combinations_with_replacement(range(1, 10), n):
        if sum(digits) != prod(digits):
            continue
        ways = factorial(n)
        for d in set(digits):
            ways //= factorial(digits.count(d))
        count += ways
        number = int("".join(map(str, digits)))
        if smallest is None or number < smallest:
            smallest = number

with open("output.txt", "w") as f:
    f.write(f"{count} {smallest}")
