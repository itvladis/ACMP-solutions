def count(x):
    c = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            c += 1
            while x % p == 0:
                x //= p
        p += 1
    return c + (x > 1)


data = open("input.txt").read().split()
nums = list(map(int, data[1:1 + int(data[0])]))
best = min(nums, key=lambda x: (-count(x), x))
open("output.txt", "w").write(str(best))
