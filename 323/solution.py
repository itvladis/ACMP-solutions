def prime(x):
    return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))


n = int(open("input.txt").read())
p = 2
while not (prime(p) and prime(n - p)):
    p += 1
open("output.txt", "w").write(f"{p} {n - p}")
