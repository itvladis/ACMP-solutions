def digits(x):
    return sum(map(int, str(x)))


def smith(x):
    total = 0
    rest = x
    d = 2
    while d * d <= rest:
        while rest % d == 0:
            total += digits(d)
            rest //= d
        d += 1
    if rest == x:
        return False
    if rest > 1:
        total += digits(rest)
    return total == digits(x)


nums = map(int, open("input.txt").read().split())
open("output.txt", "w").write("".join("1" if smith(x) else "0" for x in nums))
