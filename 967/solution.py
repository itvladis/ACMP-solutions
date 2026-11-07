def digit_sum(x, k):
    total = 0
    while x:
        total += x % k
        x //= k
    return total


data = list(map(int, open("input.txt").read().split()))
n, k1, k2 = data[:3]
b = sorted(digit_sum(a, k1) * digit_sum(a, k2) for a in data[3:3 + n])
open("output.txt", "w").write(" ".join(map(str, b)) + "\n")
