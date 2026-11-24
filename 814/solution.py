with open("input.txt") as f:
    x = int(f.read())

limit = max(x, 2)
prime = [True] * (limit + 1)
prime[0] = prime[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

count = 0
for p in range(2, x // 2 + 1):
    if prime[p] and prime[x - p]:
        count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
